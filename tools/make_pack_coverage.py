"""Regenerates the tables in PACK_COVERAGE.md from catalog.json and the sprites/ folders.

Run from anywhere: python3 tools/make_pack_coverage.py          (rewrite the generated tables)
                   python3 tools/make_pack_coverage.py --check  (exit 1 if the file is out of date)

The two generated blocks sit between <!-- packs:start/end --> and <!-- coverage:start/end -->.
The "Left out on purpose" table in the same file is written by hand and read by this script:
a row is `| pack key | item key | reason |`. Pure standard library.
"""
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DOC = os.path.join(ROOT, "PACK_COVERAGE.md")

TEMPLATE = """# Pack coverage

A running record of which items each art pack reskins. **Use it before planning a new pack**: the grid shows which trees and landmarks already have a version in each pack, which are gaps, and which were left out on purpose. A pack only needs to cover some items; anything it lacks falls back to the default pack.

The two tables below are **generated** from `catalog.json` and the `sprites/` folders by `tools/make_pack_coverage.py`. Do not edit them by hand. Run the script after every delivery that adds an item, a pack or a reskin. The "Left out on purpose" table is the one part kept by hand.

## Packs

<!-- packs:start -->
<!-- packs:end -->

## Coverage by item

`yes` means the pack has its own sprite for the item. `-` means a gap: nothing yet, so the default sprite shows. `excluded` means it was left out on purpose (see the table after the grid).

<!-- coverage:start -->
<!-- coverage:end -->

## Left out on purpose

Add a row here when an item should not get a reskin in a pack, with the reason, so it is not mistaken for a gap. One row per item.

<!-- excluded:start -->
| Pack | Item | Reason |
| --- | --- | --- |
<!-- excluded:end -->

## How to use this when planning a pack

1. Open the grid and read the column of the closest existing pack, and the row of any item you are adding.
2. Decide per item: reskin it, or add it to the exclusions with a reason (for example the item is already themed for the season).
3. After the delivery is applied, run `python3 tools/make_pack_coverage.py` and commit the result.
4. When you add a new item, check its row: every pack column that shows `-` is a pack you may want to reskin it for. Say so in the delivery README.
"""


def load():
    with open(os.path.join(ROOT, "catalog.json"), encoding="utf-8") as f:
        return json.load(f)


def sprite_exists(pack, key):
    return os.path.isfile(os.path.join(ROOT, "sprites", pack, key + ".png"))


def block(text, name):
    m = re.search(r"<!-- %s:start -->\n(.*?)<!-- %s:end -->" % (name, name), text, re.S)
    if not m:
        sys.exit("PACK_COVERAGE.md is missing the %s block markers" % name)
    return m


def replace(text, name, body):
    m = block(text, name)
    return text[: m.start(1)] + body + text[m.end(1):]


def exclusions(text):
    rows = {}
    for line in block(text, "excluded").group(1).splitlines():
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0].lower() not in ("pack", "") and not set(cells[0]) <= set("-: "):
            rows[(cells[0], cells[1])] = cells[2]
    return rows


def window(p):
    w = p.get("window")
    return "%s to %s" % (w["start"], w["end"]) if w else "always"


def generate(text):
    cat = load()
    packs = cat["packs"]
    items = [("tree", t) for t in cat["trees"]] + [("landmark", t) for t in cat["landmarks"]]
    excluded = exclusions(text)
    keys = [p["key"] for p in packs]

    head = "| Pack | Name | Kind | Season | Window | Price | Revision | Tags |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n"
    rows = []
    for p in packs:
        rows.append("| `%s` | %s | %s | %s | %s | %s | %s | %s |" % (
            p["key"], p["name"], p.get("kind", "default" if p is packs[0] else ""), p.get("season", "-"),
            window(p), p.get("tokenPrice", "-"), p.get("revision", "-"), ", ".join(p.get("tags", [])) or "-"))
    packs_md = head + "\n".join(rows) + "\n\n"

    header = "| Item | Type | Season | " + " | ".join("`%s`" % k for k in keys) + " |\n"
    header += "| --- | --- | --- | " + " | ".join("---" for _ in keys) + " |\n"
    body, gaps = [], {k: 0 for k in keys[1:]}
    done = {k: 0 for k in keys[1:]}
    left = {k: 0 for k in keys[1:]}
    for kind, t in items:
        cells = []
        for k in keys:
            if sprite_exists(k, t["key"]):
                cells.append("yes")
                if k != keys[0]:
                    done[k] += 1
            elif (k, t["key"]) in excluded:
                cells.append("excluded")
                left[k] += 1
            else:
                cells.append("-")
                if k != keys[0]:
                    gaps[k] += 1
        name = t["name"] + ("" if t.get("enabled", True) else " (retired)")
        body.append("| `%s` %s | %s | %s | %s |" % (t["key"], "(%s)" % name, kind, t.get("season", "-"), " | ".join(cells)))
    total = len(items)
    summary = "| **Reskinned** | | | " + " | ".join("%d of %d" % (total, total) if k == keys[0] else "%d of %d" % (done[k], total) for k in keys) + " |\n"
    summary += "| **Left out on purpose** | | | " + " | ".join("0" if k == keys[0] else str(left[k]) for k in keys) + " |\n"
    summary += "| **Gaps** | | | " + " | ".join("0" if k == keys[0] else str(gaps[k]) for k in keys) + " |\n"
    coverage_md = header + "\n".join(body) + "\n" + summary + "\n"
    return packs_md, coverage_md


def main():
    text = open(DOC, encoding="utf-8").read() if os.path.exists(DOC) else TEMPLATE
    packs_md, coverage_md = generate(text)
    new = replace(replace(text, "packs", packs_md), "coverage", coverage_md)
    if "--check" in sys.argv:
        if new != text:
            sys.exit("PACK_COVERAGE.md is out of date: run python3 tools/make_pack_coverage.py")
        print("PACK_COVERAGE.md is up to date")
        return
    with open(DOC, "w", encoding="utf-8") as f:
        f.write(new)
    print("wrote PACK_COVERAGE.md")


if __name__ == "__main__":
    main()
