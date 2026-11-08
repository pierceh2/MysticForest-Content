# Delivery 2026-11-08-harvest

## What's in it
Four new autumn items, all in the default pack (`sprites/default8bit/`), so no pack `revision` changes.

| Key | Name | Type | Look |
| --- | --- | --- | --- |
| pumpkin | Pumpkin | tree | Classic ribbed orange pumpkin with a brown stem and a green vine leaf. |
| jack_o_lantern | Jack-o'-Lantern | tree | The same pumpkin, carved with triangle eyes, a nose and a toothy mouth, glowing yellow inside. |
| scarecrow | Scarecrow | tree | Straw hat, stitched burlap face, plaid shirt on a crossbar, patched trousers, straw poking out. |
| hay_bales | Hay Bale Stack | landmark (2x2) | Five rectangular bales in three layers (two, two crosswise, one on top), tied with twine. |

Every PNG passed `check_sprite.py` (right size, hard alpha, nothing on the edges, foot or base in place, at most 16 colours). I also looked at each one enlarged 8x on dark green, next to the oak, birch, shrine and pond.

The drawing code is `tools/make_harvest.py`. It reuses the helpers in `tools/make_sprites.py` and regenerates the four PNGs.

## Placeholders
- Prices: tree unlock 4 each, landmark 4 per placement, as requested. These are the owner's numbers; nothing is guessed.
- No windows or pack prices (no new pack).

## Weak spots
- **The pumpkins are small.** A pumpkin sits low on the tile (about 25 px wide, 15 px tall), so it will look much smaller than a tree. That is true to life, but it may feel sparse next to the oak.
- **The jack-o'-lantern's face is dense.** The dark rim round each cut makes the eyes and mouth merge into one band at 1x. It reads as a jack-o'-lantern, but it is the weakest of the four.
- **The scarecrow's legs are short and thin.** Fine at tile size, but it could be redrawn taller.
- **The hay stack is busy.** Five bales with edges and twine read as a stack, but the right-hand layer edges are a little cluttered. It also fills almost the whole 2x2 tile.
- **Only the default pack.** No autumn-pack versions of these are included; none are needed unless you want them.

## Decisions for the owner
- **Plant cost cannot be set.** You asked for "4 token unlock, 1 token plant" on the three trees, and "8 token unlock, 4 token plant" on the hay stack. An item has only one `tokenPrice`. For a **tree** it is the one-time unlock, so I set it to **4**; the 1-token planting cost has no field. For a **landmark** it is paid **each time it is placed**, so I set it to **4** (the plant cost); the **8-token unlock has no field**. If planting costs are set app-wide, the trees are fine as they are. If you want a separate unlock price for landmarks or per-item plant costs, that needs a new field, which I did not invent. Tell me how you want to handle it.
- **Season and tags.** You asked for tags `fall` on all four. Seasons are never spelled "fall", and the season is not repeated in `tags`, so every item has `"season": "autumn"` and the tags are only the others: `halloween` and `pumpkin` (pumpkin, jack-o'-lantern), `halloween` (scarecrow), `harvest` (hay stack).
- **Keys and names.** `jack_o_lantern` for the key (letters, digits and underscores only). The hay stack's key is `hay_bales` and its name is "Hay Bale Stack".
- **Descriptions** are mine, one sentence each, in the same voice as the existing ones.
