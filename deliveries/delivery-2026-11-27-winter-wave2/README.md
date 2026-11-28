# Approved Winter Wave 2 artwork

The owner approved the original icy-blossom Frostbloom Tree, Snow Lantern Circle and Arctic Fox. This delivery preserves the three approved PNG files byte-for-byte. The supported tree and landmark are registered disabled; Arctic Fox is an Animals pilot outside the runtime catalog.

| Object | Runtime or pilot path | Canvas / footprint | State |
| --- | --- | --- | --- |
| Frostbloom Tree | `sprites/default8bit/frostbloom_tree.png` | 32×48 / 1×1 | Disabled tree registration, spriteRevision 1 |
| Snow Lantern Circle | `sprites/default8bit/snow_lantern_circle.png` | 64×96 / 2×2 | Disabled landmark registration, spriteRevision 1 |
| Arctic Fox | `pilots/animals/sprites/default8bit/arctic_fox.png` | 32×48 / 1×1 | Animal pilot; no live catalog entry |

`changes.json` contains only the two supported catalog additions and their PNGs in this delivery. The third approved PNG is installed directly in the Animals pilot folder and recorded in the [Wave 2 manifest](../../pilots/winter_objects_wave2/manifest.json); it is not a tree or landmark delivery entry.

## Placeholders and remaining decisions

- Frostbloom tokenPrice 3 is the repository-standard tree placeholder (effective unlock 3, placement 1).
- Snow Lantern Circle tokenPrice 4 is the repository-standard landmark placeholder (effective unlock 8, placement 4).
- These are not final approved prices or acquisition methods. Arctic Fox has no price assigned.
- December 1–February 28 is a proposal for purchase and every new placement. The new catalog windows are deliberately unset until approved, and both entries remain disabled. An unset window is not a year-round release decision.
- Familiars is still undecided between a spell and achievement. Its identifier and earning conditions remain unset.

## Preservation and checks

No existing item, price, window, key, enabled state or pack revision changes. All prior sprite bytes, including Classic Retro, remain unchanged. No Christmas artwork is included. Winter remains revision 3 with its existing approved release settings. These new entries are excluded from the earlier four-key activation patch.

The three sprites pass native canvas, hard-alpha, palette, edge and ground-contact checks. The original Frostbloom has pointed blue-white icy buds; preserve that selection when making later reskins. Format checks do not verify native app appearance. Use the [Xcode handoff](../../pilots/winter_objects_wave2/XCODE_HANDOFF.md) for Day/World review, future release decisions and Familiars integration.

Existing Autumn Leaves and Thanksgiving packs intentionally use these objects' base art if an old saved placement is rendered there; no new seasonal overrides are required for this winter base-art delivery. Their winter appearances are already in the default sprites, so the Winter pack also falls back intentionally. Arctic Fox is counted separately as an animal pilot.
