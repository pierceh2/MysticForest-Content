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
PACK_FIELDS = {
    "key", "name", "description", "kind", "season", "tokenPrice",
    "buyOnlyInSeason", "enabled", "revision", "ground",
}
GROUND_FIELDS = {"grassLight", "grassDark", "margin", "soilLeft", "soilRight"}
BIOME_FIELDS = {"month", "key", "name", *GROUND_FIELDS}
KEY_PATTERN = re.compile(r"[a-z][a-z0-9_]*")
COLOR_PATTERN = re.compile(r"#[0-9A-Fa-f]{6}")
SEASON_DATE_PATTERN = re.compile(r"(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])")
DAYS_IN_MONTH = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # February allows 29
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
    if set(catalog) - {"version", "packs", "trees", "landmarks", "biomes"} or not {"version", "packs", "trees", "landmarks"}.issubset(catalog):
        error("catalog.json: top level must contain version, packs, trees and landmarks, and may contain biomes")
    if type(catalog.get("version")) is not int or catalog["version"] != 1:
        error("catalog.json: version must be 1")
    packs = catalog.get("packs")
    pack_keys = set()
    if not isinstance(packs, list):
        error("catalog.json: packs must be a list")
        packs = []
    elif not packs:
        error("catalog.json: packs must start with default8bit")
    for index, pack in enumerate(packs):
        label = f"packs[{index}]"
        if not isinstance(pack, dict):
            error(f"{label}: pack must be an object")
            continue
        if set(pack) - PACK_FIELDS or not {"key", "name", "tokenPrice"}.issubset(pack):
            error(f"{label}: fields do not match the pack schema")
        key = pack.get("key")
        if not isinstance(key, str) or not KEY_PATTERN.fullmatch(key):
            error(f"{label}: key must match [a-z][a-z0-9_]*")
        elif key in pack_keys:
            error(f"{label}: duplicate key {key}")
        else:
            pack_keys.add(key)
        if index == 0 and key != "default8bit":
            error("catalog.json: the first pack must have key default8bit")
        name = pack.get("name")
        if not isinstance(name, str) or not name.strip() or len(name) > 24:
            error(f"{label}: name must be 1 to 24 characters")
        description = pack.get("description")
        if "description" in pack and (not isinstance(description, str) or len(description) > 120):
            error(f"{label}: description must be at most 120 characters")
        if "kind" in pack and not isinstance(pack["kind"], str):
            error(f"{label}: kind must be text")
        price = pack.get("tokenPrice")
        if type(price) is not int or price < 0:
            error(f"{label}: tokenPrice must be a whole number of at least 0")
        revision = pack.get("revision", 0)
        if type(revision) is not int or revision < 0:
            error(f"{label}: revision must be a whole number of at least 0")
        for field in ("enabled", "buyOnlyInSeason"):
            if field in pack and type(pack[field]) is not bool:
                error(f"{label}: {field} must be a boolean")
        if "season" in pack:
            season = pack["season"]
            if not isinstance(season, dict) or set(season) != {"start", "end"}:
                error(f"{label}: season must contain start and end")
            else:
                for field in ("start", "end"):
                    value = season[field]
                    if (
                        not isinstance(value, str)
                        or not SEASON_DATE_PATTERN.fullmatch(value)
                        or int(value[3:]) > DAYS_IN_MONTH[int(value[:2]) - 1]
                    ):
                        error(f"{label}: season {field} must be a real MM-DD date")
        ground = pack.get("ground")
        if "ground" in pack:
            if not isinstance(ground, dict) or set(ground) - GROUND_FIELDS:
                error(f"{label}: ground must contain only supported colour fields")
            else:
                for field, value in ground.items():
                    if not isinstance(value, str) or not COLOR_PATTERN.fullmatch(value):
                        error(f"{label}: ground {field} must be a #RRGGBB colour")

    earlier = previous_catalog()
    if isinstance(earlier, dict):
        old_packs = earlier.get("packs", [])
        if isinstance(old_packs, list):
            current_pack_keys = {
                pack["key"] for pack in packs
                if isinstance(pack, dict) and isinstance(pack.get("key"), str)
            }
            for pack in old_packs:
                if isinstance(pack, dict) and isinstance(pack.get("key"), str) and pack["key"] not in current_pack_keys:
                    error(f"catalog.json: previously published pack key {pack['key']} was removed")

    biomes = catalog.get("biomes")
    if "biomes" in catalog:
        if not isinstance(biomes, list):
            error("catalog.json: biomes must be a list")
        else:
            biome_months = set()
            for index, biome in enumerate(biomes):
                label = f"biomes[{index}]"
                if not isinstance(biome, dict):
                    error(f"{label}: biome must be an object")
                    continue
                if set(biome) - BIOME_FIELDS or "month" not in biome:
                    error(f"{label}: fields do not match the biome schema")
                month = biome.get("month")
                if type(month) is not int or not 1 <= month <= 12:
                    error(f"{label}: month must be a whole number from 1 to 12")
                elif month in biome_months:
                    error(f"{label}: month {month} is repeated")
                else:
                    biome_months.add(month)
                for field in GROUND_FIELDS & biome.keys():
                    value = biome[field]
                    if not isinstance(value, str) or not COLOR_PATTERN.fullmatch(value):
                        error(f"{label}: {field} must be a #RRGGBB colour")

    if not packs or not isinstance(packs[0], dict) or packs[0].get("key") != "default8bit":
        error("catalog.json: packs must be a list whose first entry has key default8bit")
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
            if not isinstance(key, str) or not KEY_PATTERN.fullmatch(key):
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

    if SPRITES.exists():
        for directory in SPRITES.iterdir():
            if directory.is_dir() and directory.name not in pack_keys:
                error(f"{directory.relative_to(ROOT)}: pack is not listed in catalog.json")
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