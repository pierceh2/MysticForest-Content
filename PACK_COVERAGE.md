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
| `winter` | Winter | seasonal | winter | always | 10 | 3 | snow, frost, cosy |

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
| `cherry_blossom` (Cherry Blossom Tree (retired)) | tree | - | yes | - | - | yes |
| `shrine` (Shrine) | landmark | - | yes | yes | yes | yes |
| `pond` (Lily Pond) | landmark | - | yes | yes | yes | yes |
| `hay_bales` (Hay Bale Stack) | landmark | autumn | yes | excluded | yes | yes |
| `harvest_table` (Harvest Table) | landmark | thanksgiving | yes | excluded | excluded | excluded |
| `village_hut` (Village Hut (retired)) | landmark | - | yes | yes | - | yes |
| **Reskinned** | | | 18 of 18 | 10 of 18 | 9 of 18 | 13 of 18 |
| **Left out on purpose** | | | 0 | 6 | 2 | 5 |
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
<!-- excluded:end -->

## How to use this when planning a pack

1. Open the grid and read the column of the closest existing pack, and the row of any item you are adding.
2. Decide per item: reskin it, or add it to the exclusions with a reason (for example the item is already themed for the season).
3. After the delivery is applied, run `python3 tools/make_pack_coverage.py` and commit the result.
4. When you add a new item, check its row: every pack column that shows `-` is a pack you may want to reskin it for. Say so in the delivery README.

## Winter release status

The approved core Winter artwork is published with pack revision 2. This Cherry Blossom draft advances Winter to revision 3 for its approved additional override. `winter` remains disabled and has no configured purchase/appearance window. The generated Packs table shows `always` for an unset window; it does not indicate that this disabled pack is available in the Store.

Apple Tree and Hay Bale Stack preserve their October 1-December 1 purchase and approved new-placement windows, inclusive. Their Winter overrides cover the December 1 overlap if the Winter season is configured to begin December 1. The artwork does not extend either item's availability.

The seasonal placement restrictions require native app enforcement. Existing saved objects and ownership are retained. Village Hut remains disabled behind its proposed Village achievement. Cherry Blossom, Cow and the ground pilots remain coordinated with their separate draft work and are not activated by this delivery.
