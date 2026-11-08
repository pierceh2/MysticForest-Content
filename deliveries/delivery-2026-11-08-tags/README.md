# Delivery 2026-11-08-tags

## What's in it
Browsing tags for every existing item and for the `fall` pack. No art changes, no new items, no text, price or footprint changes.

| Key | Tags |
| --- | --- |
| oak | deciduous, classic |
| pine | evergreen, conifer |
| birch | deciduous, slender |
| willow | deciduous, waterside |
| shrine | stone, mossy |
| pond | water, waterside |
| fall (pack) | cosy, leaves |

There is no `sprites/` folder and no `spritesChanged`, so no revision numbers should change.

## Placeholders
None.

## Weak spots
- The tag words are my choices; the labels are only for browsing and change no rule. Easy to swap.
- The edits use an `edit.packs` section (for the `fall` pack). The sprite-agent prompt only shows `edit.trees` as an example, but the repo's rules say `edit` entries cover any `add`-able section.

## Decisions for the owner
- **No `season` on any existing item.** Oak, pine, birch, willow, shrine and pond are year-round, so none "clearly belongs to a season". Giving them one (for example `autumn` on the oak) would file them under that season in the app. I left it out on purpose. If you want, say which items belong to which season.
- **The pack's `season` stays `autumn`.** It is already set; I did not repeat it in the pack's tags, as the rules say.
- **Tag choices.** I used plant type (deciduous, evergreen, conifer), look (classic, slender, mossy, stone, leaves), setting (waterside, water) and mood (cosy). Tell me if you want a different set, such as holiday-style tags.
