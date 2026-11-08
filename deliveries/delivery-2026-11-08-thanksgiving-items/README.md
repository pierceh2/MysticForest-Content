# Delivery 2026-11-08-thanksgiving-items

Delivery 1 of 3 for the Thanksgiving work (revised: prices and season updated after the owner confirmed them). It adds three new default-pack items. The `thanksgiving` pack itself (its entry, window, price, ground colours and the reskins) comes in the next deliveries, and will reskin these items too.

## What's in it
| Key | Name | Type | Look |
| --- | --- | --- | --- |
| apple_tree | Apple Tree | tree | A short, rounded, gnarled tree with a green crown dotted with red apples, and two windfall apples at the foot |
| corn_stalks | Corn Stalks | tree | A tied bundle of five dry golden stalks with tassels, three corn cobs (green husks, golden kernels) and long drooping blades |
| harvest_table | Harvest Table | landmark (2x2) | A long table with a cream cloth and a deep-green runner, two candles, a bowl of apples, a small pumpkin, two pies and a loaf of bread, with a few fallen leaves around it |

All three PNGs passed `check_sprite.py` (right size, hard alpha, nothing on the edges, foot or base in place, at most 16 colours: 13, 10 and 15). I looked at each enlarged on dark green next to the oak, scarecrow, shrine and hay bales, and redrew the corn and the table several times:
- The first corn drew its stalks near the foot by mistake, then the stalks were too close together so the outline filled the gaps; the blades were single dotted pixels and the check script caught a blade touching the left edge. All fixed.
- The first table had a heavy dark bench that dominated it, a red runner that blended into the red apples, tiny candles and a crowd of items in one spot. The bench is gone, the runner is deep green, and the items are spread around the table.

The drawing code is `tools/make_thanksgiving_items.py`. It reuses `tools/make_sprites.py` and the palette in `tools/make_november.py`.

## Placeholders
- **Tree prices are the owner's:** `tokenPrice` 4 for each new regular tree (apple tree and corn stalks). With the default store and plant prices, each costs 4 to unlock and 1 to plant.
- **The landmark's price is a guess:** `tokenPrice` 4 for the harvest table (the standard landmark placeholder), so it costs 8 to unlock and 4 to place under the defaults. No `storePrice` or `plantPrice` is written.

## Weak spots
- **Corn Stalks:** stylised. The thick golden stalks dominate, so at 1x it can read a little like wheat until you see the cobs.
- **Harvest Table:** the items are small and the cloth is a big pale block, so it reads best at a larger size. It is also lower and smaller than the shrine and hay bales.
- **Apple Tree:** the two windfall apples sit just outside the foot's diamond, near its right edge.

## Decisions for the owner
- **Season and tags.** The harvest table is Thanksgiving-only, so it has `"season": "thanksgiving"` (the owner's new season id), and `autumn` is in its tags so it still shows when filtering by autumn: `["harvest", "autumn"]`. `thanksgiving` is not repeated in its tags. The corn stalks are a general harvest item, so they keep `"season": "autumn"` with tags `["harvest", "thanksgiving"]`; tell me if you would rather file them under `thanksgiving`. The apple tree is a regular year-round tree, with no season and tags `["fruit", "harvest"]`. All tags are my choices.
- **Key naming.** `apple_tree` for the apple tree's key, since keys are permanent.
- **Descriptions** are mine, one sentence each, in the voice of the existing ones.
- **No pack in this delivery.** No `revision` changes are needed. The three new items start at `spriteRevision` 1.
