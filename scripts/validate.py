import json
import os
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SPRITES = ROOT / "sprites"
FIELDS = {
    "trees": {"key", "name", "description", "tokenPrice", "startsUnlocked", "enabled", "spriteRevision"},
    "landmarks": {"key", "name", "description", "tokenPrice", "footprint", "enabled", "spriteRevision"},
}
errors = []

def error(message):
    errors.append(message)

def previous_catalog():
    revision = "HEAD~1"
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if event_path and Path(event_path).is_file():
        try:
            revision = json.loads(Path(event_path).read_text()).get("pull_request", {}).get("base", {}).get("sha", revision)
        except (OSError, ValueError):
            pass
    result = subprocess.run(["git", "show", f"{revision}:catalog.json"], cwd=ROOT, capture_output=True, text=True)
    try:
        return json.loads(result.stdout) if result.returncode == 0 else None
    except ValueError:
        return None

def main():
    try:
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"catalog.json: {exc}", file=sys.stderr)
        return 1
    if not isinstance(catalog, dict):
        print("catalog.json: top level must be an object", file=sys.stderr)
        return 1
    if set(catalog) != {"version", "packs", "trees", "landmarks"}:
        error("catalog.json: top level must contain only version, packs, trees and landmarks")
    if type(catalog.get("version")) is not int or catalog["version"] != 1:
        error("catalog.json: version must be 1")
    packs = catalog.get("packs")
    pack_keys = set()
    if not isinstance(packs, list):
        error("catalog.json: packs must be a list")
        packs = []
    for index, pack in enumerate(packs):
        if not isinstance(pack, dict) or set(pack) != {"key", "name"} or not all(isinstance(pack.get(field), str) and pack[field].strip() for field in ("key", "name")):
            error(f"packs[{index}]: must contain non-empty string key and name only")
        elif pack["key"] in pack_keys:
            error(f"packs[{index}]: duplicate key {pack['key']}")
        else:
            pack_keys.add(pack["key"])
    if "default8bit" not in pack_keys:
        error("catalog.json: packs must include default8bit")
    items = {}
    for collection, fields in FIELDS.items():
        entries = catalog.get(collection)
        if not isinstance(entries, list):
            error(f"catalog.json: {collection} must be a list")
            continue
        for index, item in enumerate(entries):
            label = f"{collection}[{index}]"
            if not isinstance(item, dict):
                error(f"{label}: item must be an object")
                continue
            if set(item) != fields:
                error(f"{label}: fields do not match the {collection[:-1]} schema")
            key = item.get("key")
            if not isinstance(key, str) or not re.fullmatch(r"[a-z][a-z0-9_]*", key):
                error(f"{label}: key must match [a-z][a-z0-9_]*")
                key = f"invalid_{collection}_{index}"
            if key in items:
                error(f"{label}: duplicate key {key}")
            items[key] = (collection, item)
            for field, limit in (("name", 24), ("description", 120)):
                value = item.get(field)
                if not isinstance(value, str) or not value.strip() or len(value) > limit:
                    error(f"{key}: {field} must be a non-empty string of at most {limit} characters")
            description = item.get("description")
            if isinstance(description, str) and description.strip():
                if description[-1] not in ".!?" or any(char in description[:-1] for char in ".!?") or re.search(r"[#*_`\[\]\\\n]", description):
                    error(f"{key}: description must be one plain-text sentence")
            price = item.get("tokenPrice")
            if type(price) is not int or price < (0 if collection == "trees" else 1):
                error(f"{key}: tokenPrice must be a whole number and valid for this item type")
            if collection == "trees":
                unlocked = item.get("startsUnlocked")
                if type(unlocked) is not bool:
                    error(f"{key}: startsUnlocked must be a boolean")
                elif type(price) is int and (price == 0) != unlocked:
                    error(f"{key}: tokenPrice must be 0 exactly when startsUnlocked is true")
            elif item.get("footprint") != [2, 2]:
                error(f"{key}: footprint must be [2, 2]")
            if type(item.get("enabled")) is not bool:
                error(f"{key}: enabled must be a boolean")
            if type(item.get("spriteRevision")) is not int or item["spriteRevision"] < 1:
                error(f"{key}: spriteRevision must be a whole number starting at 1")
            if item.get("enabled") is True and not (SPRITES / "default8bit" / f"{key}.png").is_file():
                error(f"enabled item {key}: missing sprites/default8bit/{key}.png")

    for path in SPRITES.rglob("*.png") if SPRITES.exists() else []:
        relative = path.relative_to(SPRITES)
        if len(relative.parts) != 2 or path.stem not in items:
            error(f"unreferenced sprite: {path.relative_to(ROOT)}")
            continue
        if relative.parts[0] not in pack_keys:
            error(f"{path.relative_to(ROOT)}: pack is not listed in catalog.json")
        expected = (32, 48) if items[path.stem][0] == "trees" else (64, 96)
        try:
            with Image.open(path) as image:
                if image.format != "PNG" or image.mode != "RGBA":
                    error(f"{path.relative_to(ROOT)}: must be an RGBA PNG")
                    continue
                if image.size != expected:
                    error(f"{path.relative_to(ROOT)}: expected {expected[0]}x{expected[1]}, got {image.width}x{image.height}")
                alpha = image.getchannel("A")
                values = set(alpha.getdata())
                if not values or values == {0}:
                    error(f"{path.relative_to(ROOT)}: image must not be fully transparent")
                if not values.issubset({0, 255}):
                    error(f"{path.relative_to(ROOT)}: alpha values must be only 0 or 255")
                if any(alpha.getpixel((x, 0)) == 255 for x in range(image.width)):
                    error(f"{path.relative_to(ROOT)}: opaque pixel touches top edge")
                if any(alpha.getpixel((x, y)) == 255 for x in (0, image.width - 1) for y in range(image.height)):
                    error(f"{path.relative_to(ROOT)}: opaque pixel touches left or right edge")
        except OSError as exc:
            error(f"{path.relative_to(ROOT)}: cannot read PNG ({exc})")
    earlier = previous_catalog()
    if isinstance(earlier, dict):
        old_items = {item.get("key"): item for kind in FIELDS for item in earlier.get(kind, []) if isinstance(item, dict)}
        for key, old in old_items.items():
            if key not in items:
                error(f"catalog.json: previously published key {key} was removed")
            elif "footprint" in old and items[key][1].get("footprint") != old["footprint"]:
                error(f"catalog.json: footprint for {key} changed")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())