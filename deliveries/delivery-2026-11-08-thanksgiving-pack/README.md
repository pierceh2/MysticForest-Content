# Delivery 2026-11-08-thanksgiving-pack

Delivery 2 of 3 for the Thanksgiving work. It adds the new `thanksgiving_feast` pack and the five reskins that work as single-tile items. The landmark reskins (hay bales and shrine) come in delivery 3.

**Apply `delivery-2026-11-08-thanksgiving-items` first.** This pack reskins `apple_tree`, which that delivery adds. (The November trees delivery should also be applied before either of these, but nothing here depends on it.)

## What's in it
**The pack**, `thanksgiving_feast` ("Thanksgiving Feast"): a holiday pack for the new season id `thanksgiving`, open 11-15 to 11-30, 10 tokens, with `autumn` in its tags so it shows when filtering by autumn. It has warm ground colours: honey-straw grass, deeper umber soil (grassLight `#A98240`, grassDark `#946E34`, margin `#775628`, soilLeft `#6A3A1E`, soilRight `#512C16`). I compared them against the current `fall` ground with the sprites on top, and the string lights, baskets and gold leaves all stay readable.

**Five reskins** in `sprites/thanksgiving_feast/`. The look is warm and cosy: honey and wine leaves, string lights, ribbons, and baskets and piles of harvest fruit at the foot.

| Key | Thanksgiving version |
| --- | --- |
| oak | Honey-gold crown (warmer and yellower than the fall pack's orange), two swags of string lights with glowing bulbs, a basket of apples at the foot |
| maple | Deep wine-red crown with gold flecks (darker than the fall pack's scarlet), a cream ribbon and bow round the trunk |
| apple_tree | Golden leaves with many more red apples, and a basket of apples at the foot |
| pumpkin | A pile of three pumpkins (orange, deep red-orange and cream) with a curling vine |
| scarecrow | A warm orange scarf, autumn leaves tucked in the hat band, and a small pumpkin at its foot |

All five PNGs passed `check_sprite.py` (32x48, hard alpha, nothing on the edges, foot in place, at most 16 colours; each uses between 11 and 15). I looked at each enlarged on dark green next to its default and fall versions, and on top of the new ground tile.

The drawing code is `tools/make_thanksgiving_pack.py`. It reuses the other `tools/make_*.py` scripts and regenerates all five PNGs.

## Placeholders
- **Window 11-15 to 11-30** is my suggestion (American Thanksgiving is the fourth Thursday of November, a moving date that a fixed range cannot follow). The owner did not give dates.
- **Ground colours** are my exact values; the owner approved the idea (warmer and redder than the fall pack) but not the hex numbers.
- The pack price (10) is the owner's. `buyOnlyInSeason` is left out so it keeps its default.

## Weak spots
- **Pumpkin:** the Thanksgiving pumpkin is a pile of three, so it fills more of the tile than the single default pumpkin. The foot is in the same place, but the silhouette is wider (about 28 px against 25).
- **Maple:** it is still a red maple, and sits close to the fall pack's maple. The darker wine colour, gold flecks and ribbon set it apart, but at 1x the difference is modest. The bow is small.
- **Oak lights:** the string lights are a few pixels each and read best at a larger size.
- **Coverage:** only five of the pack's items are in this delivery. The pack's art is incomplete until delivery 3 (hay bales and shrine), and nothing is drawn yet for the birch, willow, pine, pond, larch, ginkgo, corn stalks, jack-o'-lantern or harvest table. Those fall back to the default pack.

## Decisions for the owner
- **Pack key `thanksgiving_feast`.** You asked for a key distinct from the season id `thanksgiving`, so I chose `thanksgiving_feast`. Pack keys are permanent, so tell me before it is applied if you want a different one.
- **Season id and tags.** The pack's `season` is `thanksgiving`, and its tags are `autumn` (so it appears in the autumn filter), `harvest` and `cosy`. The season is not repeated in the tags.
- **Revision:** the pack is new, so the repo agent starts its `revision` at 1.
- **Which items:** I covered oak, maple, apple tree, pumpkin and scarecrow. I left the jack-o'-lantern alone (Halloween) and avoided Pilgrim and turkey imagery.
