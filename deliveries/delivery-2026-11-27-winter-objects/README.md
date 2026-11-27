# Approved winter-only objects

The owner approved all four native sprites in the review array and requested publication to main.

## Applied content

- New disabled tree entries: `snowman`, `winterberry_bush`.
- New disabled 2×2 landmark entry: `frost_obelisk`.
- Each new runtime entry starts at spriteRevision 1, has its approved `default8bit` PNG, and carries the December 1–February 28 purchase window and winter season label.
- Snow Hare is approved at `pilots/animals/sprites/default8bit/snow_hare.png`, outside the live version-1 catalog until Animals support exists.
- [Structured manifest](../../pilots/winter_objects/manifest.json), [Xcode handoff](../../pilots/winter_objects/XCODE_HANDOFF.md), and pack coverage document all four objects and their remaining dependencies.

`changes.json` contains only the three supported runtime entries and the three PNGs copied into this delivery's `sprites/` folder. The applying step sets their initial spriteRevision to 1. Hare is tracked in the separate pilot manifest; do not add an unsupported animals collection to catalog.json.

## Placeholders and owner decisions

The repository handoff section 8 supplies new-item placeholders: tree tokenPrice 3, landmark tokenPrice 4. Therefore Snowman and Winterberry Bush each use a 3-token store unlock with the existing 1-token planting default. Frost Obelisk uses the existing 8-token store default and a 4-token placement cost. These are disabled staging values, not final approved economy. Hare prices remain unset.

Final prices, extra item unlocks if desired, and the Familiars spell/achievement definition remain decisions for the owner. The proposed winter window governs both purchase and new placement, including owned items; this needs native enforcement before activation. Ownership and previously saved placements persist.

## Coverage and revisions

Each object has one intrinsically snowy base appearance. No Winter reskin-pack ownership is required. The three registered objects are intentionally excluded from separate Autumn, Thanksgiving and Winter override production; absent overrides use the base PNG. Hare is outside the generated tree/landmark grid.

Existing items, prices, revisions, windows, pack enablement and pack revisions are unchanged. Winter remains disabled at revision 2, priced at 10 tokens, with no configured window. This delivery enables no new object or pack.

## Validation and limits

The approved sprite hashes are recorded in the manifest. All four use hard-alpha RGBA, appropriate 32×48 or 64×96 canvases, at most 16 opaque colors, valid contact rows and no clipped top/side edges. The Hare is checked against the one-cell canvas format, not treated as a runtime tree.

Run `python3 scripts/validate.py`, `python3 tools/make_pack_coverage.py --check` and individual `tools/check_sprite.py` checks before committing. In-app Day/Forest placement, scale, occlusion, cache refresh, seasonal gating and Animals support still need Xcode verification. No artwork is redrawn or resized in this publication.
