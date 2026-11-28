# Pack coverage

A running record of which items each art pack reskins. **Use it before planning a new pack**: the grid shows which trees and landmarks already have a version in each pack, which are gaps, and which were left out on purpose. A pack only needs to cover some items; anything it lacks falls back to the default pack.

The two tables below are **generated** from `catalog.json` and the `sprites/` folders by `tools/make_pack_coverage.py`. Do not edit them by hand. Run the script after every delivery that adds an item, a pack or a reskin. The "Left out on purpose" table is the one part kept by hand.

## Packs

<!-- packs:start -->
| Pack | Name | Kind | Season | Window | Price | Revision | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `default8bit` | Default 8-bit | default | - | always | 0 | - | - |
| `fall` | Autumn Leaves | seasonal | autumn | 10-01 to 12-01 | 10 | 4 | cosy, leaves |
| `thanksgiving_feast` | Thanksgiving Feast | holiday | thanksgiving | 11-15 to 11-30 | 10 | 3 | autumn, harvest, cosy |
| `winter` | Winter | seasonal | winter | 12-01 to 02-28 | 10 | 3 | snow, frost, cosy |

<!-- packs:end -->

## Coverage by item

`yes` means the pack has its own sprite for the item. `-` means a gap: nothing yet, so the default sprite shows. `excluded` means it was left out on purpose (see the table after the grid).

<!-- coverage:start -->
| Item | Type | Season | `default8bit` | `fall` | `thanksgiving_feast` | `winter` |
| --- | --- | --- | --- | --- | --- | --- |
| `oak` (Oak) | tree | - | yes | yes | yes | yes |
| `pine` (Pine) | tree | - | yes | yes | - | yes |
| `birch` (Birch) | tree | - | yes | yes | yes | yes |
| `willow` (Willow) | tree | - | yes | yes | - | yes |
| `pumpkin` (Pumpkin) | tree | autumn | yes | excluded | yes | excluded |
| `jack_o_lantern` (Jack-o'-Lantern) | tree | autumn | yes | excluded | excluded | excluded |
| `scarecrow` (Scarecrow) | tree | autumn | yes | excluded | yes | excluded |
| `larch` (Larch) | tree | - | yes | yes | - | yes |
| `maple` (Maple) | tree | - | yes | yes | yes | yes |
| `ginkgo` (Ginkgo) | tree | - | yes | yes | - | yes |
| `apple_tree` (Apple Tree) | tree | - | yes | - | yes | yes |
| `corn_stalks` (Corn Stalks) | tree | autumn | yes | excluded | - | excluded |
| `snowman` (Snowman (retired)) | tree | winter | yes | excluded | excluded | excluded |
| `winterberry_bush` (Winterberry Bush (retired)) | tree | winter | yes | excluded | excluded | excluded |
| `cherry_blossom` (Cherry Blossom Tree (retired)) | tree | - | yes | - | - | yes |
| `frostbloom_tree` (Frostbloom Tree (retired)) | tree | winter | yes | excluded | excluded | excluded |
| `shrine` (Shrine) | landmark | - | yes | yes | yes | yes |
| `pond` (Lily Pond) | landmark | - | yes | yes | yes | yes |
| `hay_bales` (Hay Bale Stack) | landmark | autumn | yes | excluded | yes | yes |
| `harvest_table` (Harvest Table) | landmark | thanksgiving | yes | excluded | excluded | excluded |
| `village_hut` (Village Hut (retired)) | landmark | - | yes | yes | - | yes |
| `frost_obelisk` (Frost Obelisk (retired)) | landmark | winter | yes | excluded | excluded | excluded |
| `gold_vein` (Gold Vein (retired)) | landmark | - | yes | excluded | excluded | excluded |
| `silver_vein` (Silver Vein (retired)) | landmark | - | yes | excluded | excluded | excluded |
| `bronze_vein` (Bronze Vein (retired)) | landmark | - | yes | excluded | excluded | excluded |
| `snow_lantern_circle` (Snow Lantern Circle (retired)) | landmark | winter | yes | excluded | excluded | excluded |
| **Reskinned** | | | 26 of 26 | 10 of 26 | 9 of 26 | 13 of 26 |
| **Left out on purpose** | | | 0 | 14 | 10 | 13 |
| **Gaps** | | | 0 | 2 | 7 | 0 |

<!-- coverage:end -->

## Left out on purpose

Add a row here when an item should not get a reskin in a pack, with the reason, so it is not mistaken for a gap. One row per item.

<!-- excluded:start -->
| Pack | Item | Reason |
| --- | --- | --- |
| `fall` | `pumpkin` | Already autumn-themed in the default pack. |
| `fall` | `jack_o_lantern` | Already autumn-themed in the default pack. |
| `fall` | `scarecrow` | Already autumn-themed in the default pack. |
| `fall` | `hay_bales` | Already autumn-themed in the default pack. |
| `fall` | `corn_stalks` | Already autumn-themed (dry golden stalks) in the default pack. |
| `fall` | `harvest_table` | A Thanksgiving item; its default sprite is already the autumn look. |
| `thanksgiving_feast` | `jack_o_lantern` | A Halloween item, not Thanksgiving. |
| `thanksgiving_feast` | `harvest_table` | Thanksgiving-only; its default sprite is already the Thanksgiving look. |
| `winter` | `pumpkin` | Approved purchase-and-new-placement window is October 1-November 30; no Winter appearance. |
| `winter` | `jack_o_lantern` | Approved purchase-and-new-placement window is October 1-October 31; no Winter appearance. |
| `winter` | `scarecrow` | Approved purchase-and-new-placement window is October 1-November 30; no Winter appearance. |
| `winter` | `corn_stalks` | Approved purchase-and-new-placement window is November 15-November 30; no Winter appearance. |
| `winter` | `harvest_table` | Thanksgiving-only new placement, November 15-November 30; excluded by the owner's latest instruction. |
| `fall` | `snowman` | Intrinsically winter base art; this winter-only object uses its default appearance and needs no separate seasonal override. |
| `fall` | `winterberry_bush` | Intrinsically winter base art; this winter-only object uses its default appearance and needs no separate seasonal override. |
| `fall` | `frost_obelisk` | Intrinsically winter base art; this winter-only object uses its default appearance and needs no separate seasonal override. |
| `thanksgiving_feast` | `snowman` | Intrinsically winter base art; this winter-only object uses its default appearance and needs no separate seasonal override. |
| `thanksgiving_feast` | `winterberry_bush` | Intrinsically winter base art; this winter-only object uses its default appearance and needs no separate seasonal override. |
| `thanksgiving_feast` | `frost_obelisk` | Intrinsically winter base art; this winter-only object uses its default appearance and needs no separate seasonal override. |
| `winter` | `snowman` | Intrinsically winter base art; this winter-only object uses its default appearance and needs no separate seasonal override. |
| `winter` | `winterberry_bush` | Intrinsically winter base art; this winter-only object uses its default appearance and needs no separate seasonal override. |
| `winter` | `frost_obelisk` | Intrinsically winter base art; this winter-only object uses its default appearance and needs no separate seasonal override. |
| `fall` | `gold_vein` | Mineral veins intentionally use the approved base appearance in every pack. |
| `fall` | `silver_vein` | Mineral veins intentionally use the approved base appearance in every pack. |
| `fall` | `bronze_vein` | Mineral veins intentionally use the approved base appearance in every pack. |
| `thanksgiving_feast` | `gold_vein` | Mineral veins intentionally use the approved base appearance in every pack. |
| `thanksgiving_feast` | `silver_vein` | Mineral veins intentionally use the approved base appearance in every pack. |
| `thanksgiving_feast` | `bronze_vein` | Mineral veins intentionally use the approved base appearance in every pack. |
| `winter` | `gold_vein` | Mineral veins intentionally use the approved base appearance in every pack. |
| `winter` | `silver_vein` | Mineral veins intentionally use the approved base appearance in every pack. |
| `winter` | `bronze_vein` | Mineral veins intentionally use the approved base appearance in every pack. |
| `fall` | `frostbloom_tree` | Intrinsic snowy base artwork supplies this appearance; release dates and acquisition remain pending on the disabled entry. |
| `fall` | `snow_lantern_circle` | Intrinsic snowy base artwork supplies this appearance; release dates and acquisition remain pending on the disabled entry. |
| `thanksgiving_feast` | `frostbloom_tree` | Intrinsic snowy base artwork supplies this appearance; release dates and acquisition remain pending on the disabled entry. |
| `thanksgiving_feast` | `snow_lantern_circle` | Intrinsic snowy base artwork supplies this appearance; release dates and acquisition remain pending on the disabled entry. |
| `winter` | `frostbloom_tree` | Intrinsic snowy base artwork supplies this appearance; release dates and acquisition remain pending on the disabled entry. |
| `winter` | `snow_lantern_circle` | Intrinsic snowy base artwork supplies this appearance; release dates and acquisition remain pending on the disabled entry. |
<!-- excluded:end -->

## How to use this when planning a pack

1. Open the grid and read the column of the closest existing pack, and the row of any item you are adding.
2. Decide per item: reskin it, or add it to the exclusions with a reason (for example the item is already themed for the season).
3. After the delivery is applied, run `python3 tools/make_pack_coverage.py` and commit the result.
4. When you add a new item, check its row: every pack column that shows `-` is a pack you may want to reskin it for. Say so in the delivery README.

## Winter release status

Winter revision **3** includes the approved Cherry Blossom override alongside the 12 previously staged sprites. Its **December 1–February 28** inclusive window and **10-token** unlock price are owner-approved. It remains disabled until the native visual and pack checks pass. See the [approved release and activation patch](handoffs/winter-2026/README.md); no repeat approval of these business decisions is required.

Apple Tree and Hay Bale Stack retain October 1–December 1 purchase and new-placement windows. Their Winter overrides cover December 1 without extending availability. Harvest Table remains November 15–November 30 and has no Winter override. Existing ownership and saved placements are retained on all dates.

The generated grid calls any disabled entry “retired.” Village Hut, Cherry Blossom, the three veins and the new winter-only objects are staged entries awaiting their distinct release conditions, not deleted content.

## Approved winter-only objects

Snowman, Winterberry Bush and Frost Obelisk have approved default sprites and disabled catalog entries at spriteRevision 1. Their approved unlock/placement prices are respectively **3/1, 3/1 and 8/4 Forest tokens**. They are ordinary seasonal purchases, December 1–February 28 inclusive, with the same limits on every new placement. Native verification precedes activation. They do not require the Winter pack and need no seasonal overrides.

Snow Hare uses `pilots/animals/sprites/default8bit/snow_hare.png`; it remains outside the runtime coverage grid. Its art and winter-only direction are approved, but Familiars, Animal support and animal economy remain pending.

## Approved pilot coverage

These files are included in the repository but are not live catalog entries. Seasonal pack ownership changes appearance only; it does not grant Terraforming or Familiars.

| Pilot item | Base | Autumn Leaves | Winter | Production condition |
| --- | --- | --- | --- | --- |
| Cow | Approved | Approved | Approved | Animals type; unresolved Familiars and economy |
| Snow Hare | Approved snowy base | Base fallback | Base fallback | Animals type; unresolved Familiars and economy; winter-only placement |
| Arctic Fox | Approved snowy base | Base fallback | Base fallback | Animals type; unresolved Familiars, economy and exact dates |
| Dirt Patch | Approved atlas | Approved atlas | Approved atlas | Ground type; future Terraforming; economy |
| Dirt Rows | Approved atlas | Approved atlas | Approved atlas | Ground type; future Terraforming; economy |
| Cobblestone Circle | Approved atlas | Base fallback | Base fallback | Same Ground prerequisites; seasonal artwork deferred |

The [Ground handoff](pilots/ground/FOREST_OBJECT_TYPES_XCODE_HANDOFF.md) covers all 16 edge masks and placement under existing objects. The [Cow handoff](pilots/animals/README.md) covers stable identity and all three appearances. Cherry Blossom's Autumn and Thanksgiving columns remain actual gaps; Autumn art still needs its separate visual approval.

## Approved Winter Wave 2 staging

Frostbloom Tree and Snow Lantern Circle add two approved base sprites and disabled catalog entries. Their prices are repository placeholders and their purchase/placement windows are not configured. Arctic Fox is an approved 32×48 Animals pilot outside the runtime matrix. See the [manifest](pilots/winter_objects_wave2/manifest.json) and [Xcode handoff](pilots/winter_objects_wave2/XCODE_HANDOFF.md). No pack art or revision changes in this delivery.
