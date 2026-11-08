# Delivery 2026-11-08-item-windows

## What's in it
Adds a purchase `window` to seven existing items, so they can be bought only on certain dates each year. No art, price, season, tag or revision changes.

| Window | Items |
| --- | --- |
| Thanksgiving, 11-15 to 11-30 | corn_stalks, apple_tree, harvest_table |
| Fall, 10-01 to 12-01 | hay_bales, jack_o_lantern, pumpkin, scarecrow |

Each `edit` entry has only the `key` and the new `window` field (`{ "start": "MM-DD", "end": "MM-DD" }`, zero-padded, both ends inclusive, repeating every year). `buyOnlyInSeason` is not added; it defaults to true. There is no `sprites/` folder and no `spritesChanged`, so no `spriteRevision` or pack `revision` changes.

Per the owner's spec from the Xcode agent: outside its window an unowned item is hidden from the Store; items already owned stay owned, stay in the Inventory and can be planted all year; the window is checked against the device's local date. A window the app cannot read makes the item never buyable, so every date here was checked (month 01 to 12, day valid for the month).

## Blocked until the validator accepts it
`CLAUDE.md` and `scripts/validate.py` do not yet allow `window` on a tree or landmark (only on a pack), so the validator fails on this change ("fields do not match the tree schema"). **Do not apply this delivery until the repo agent has added an optional item `window` to `CLAUDE.md` and the validator.**

## Placeholders
None. The dates are the owner's.

## Weak spots
- The item windows duplicate the dates of the `fall` and `thanksgiving_feast` packs. If a pack's window changes later, the items' windows will not change with it.
- `apple_tree` is a regular tree with no season, so only its window marks it as a Thanksgiving item.

## Decisions for the owner
- Season is unchanged on every item, as instructed (`corn_stalks` stays `autumn`, `harvest_table` stays `thanksgiving`, `apple_tree` has none).
