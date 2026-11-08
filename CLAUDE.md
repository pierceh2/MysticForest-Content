# Mystic Forest content repo: rules for any agent working here

The Mystic Forest tab of my iOS app reads this repo (read-only) from raw.githubusercontent.com on `main` and caches it. Nothing in the app is changed by editing here except what is described in this file. Read this file fully before every task.

## Layout
- `catalog.json`: every tree and landmark.
- `sprites/<pack>/<key>.png`: one PNG per item. The only pack right now is `default8bit`.
- `scripts/validate.py`: run `python3 scripts/validate.py` before every commit. Never commit while it reports a problem.
- `tools/make_sprites.py`: draws sprites in code. Optional for new items.

## catalog.json
Top level: `version` (always 1), `packs`, `trees`, `landmarks`, and optional `biomes`.

Tree: `{ "key", "name", "description", "tokenPrice", "startsUnlocked", "enabled", "spriteRevision" }`

Landmark: `{ "key", "name", "description", "tokenPrice", "footprint", "enabled", "spriteRevision" }`

| Field | Rules |
| --- | --- |
| `key` | Lowercase letters, digits and underscores, starting with a letter (`^[a-z][a-z0-9_]*$`). Unique across trees and landmarks. Permanent: saved forests on my phone refer to it. |
| `name` | Short display name, up to 24 characters. |
| `description` | One sentence, up to 120 characters. Warm and plain, no markdown. |
| `tokenPrice` | Whole number of Forest tokens, never coins. A tree's price is a one-time unlock (0 only when `startsUnlocked` is true). A landmark's price is paid each time one is placed (at least 1). |
| `startsUnlocked` | Trees only. True means owned from the start. |
| `footprint` | Landmarks only. `[width, height]` in tiles. Only `[2, 2]` is supported right now. Ask me before using another size. |
| `enabled` | False hides the item from the inventory, but old forests still draw it. |
| `spriteRevision` | Whole number starting at 1. Increase it by 1 whenever the item's PNG changes, because the app only re-downloads art when this changes. |

Rules:
- Never delete an item, rename a key, or reuse a key. To retire an item set `"enabled": false` and keep its PNG.
- Never change a `footprint` once published.
- Do not add fields that are not listed here. The app ignores unknown fields, so an extra field does nothing and only confuses the file. Growth stages and coin prices are left out on purpose.
- Prices are placeholders that I tune. Do not change a price unless I ask.
- Keep the file valid UTF-8 JSON with a two-space indent.

### Packs in catalog.json

`packs` is a list. The first entry is always the default pack, as it is now. Other packs are seasonal or holiday looks. A day is drawn in one pack. The app falls back to the default pack's sprite for any item a pack doesn't have, so a pack may cover only some items.

| Field | Rules |
| --- | --- |
| `key` | Lowercase letters, digits and underscores (`^[a-z][a-z0-9_]*$`). Unique among packs. **Permanent**, like item keys. It is also the folder name `sprites/<key>/`. |
| `name` | Display name, up to 24 characters. |
| `description` | One warm sentence, up to 120 characters. Optional. |
| `kind` | Optional text such as `seasonal` or `holiday`. For information only. |
| `season` | Optional season id matching `^[a-z][a-z0-9_]*$`. Use `winter`, `spring`, `summer` or `autumn` for the natural seasons, and a holiday's own id (`halloween`, `christmas`) for a holiday. Never use "fall". |
| `window` | Optional `{ "start": "MM-DD", "end": "MM-DD" }`, the yearly range in which the pack can be bought and is worn on its own. It may run over the new year. |
| `tokenPrice` | Whole number of Forest tokens to unlock it once. Much larger than a tree. A placeholder I tune. |
| `buyOnlyInSeason` | Optional, default `true`. When true the pack can only be bought while its window is open. Once bought it stays owned for good. |
| `enabled` | False hides it from the shop. Days already in it still draw it. |
| `revision` | Whole number, default 0. **Increase it by 1 whenever any of the pack's art changes**, because the app only downloads a pack's sprites again when this goes up. (An item's own `spriteRevision` still covers changes to the default pack's sprite.) |
| `ground` | Optional colours `{ "grassLight", "grassDark", "margin", "soilLeft", "soilRight" }` as `#RRGGBB`. They replace the month's ground colours for days in this pack. Any left out keep the month's. |

Rules for packs:
- Never delete a pack, rename its key, or reuse a key. To retire one set `"enabled": false` and keep its folder.
- Pack art uses exactly the same sprite format as the default pack (sizes, anchor, transparency, hard pixels). A reskinned item must keep its silhouette's footprint and foot position so it sits on the ground the same way.
- A non-default pack folder may be missing sprites. The **default pack must still have a sprite for every enabled item**.
- A window written wrongly (not `MM-DD`) means the pack never opens, so check every window.
- Do not add a pack, or change a pack's price, window or colours, unless asked.

## Words

- **Season**: an app-wide named look, with an id and a name. Ids are lowercase letters, digits and underscores (`^[a-z][a-z0-9_]*$`). The four natural seasons are `winter`, `spring`, `summer` and `autumn` (always spelled **autumn**, not "fall"). Holidays and events are more ids, such as `halloween` and `christmas`. A season is not a date range.
- **Window**: a pack's yearly date range, `{ "start": "MM-DD", "end": "MM-DD" }`. It may run over the new year (`"12-01"` to `"02-28"`). The pack can be bought, and is worn on its own, while its window is open.
- **Pack**: a set of sprites that is the Forest's art for one season. A pack's key is its folder name and is permanent. The key does not have to match the season id (a pack called `fall` can be the art for the season `autumn`).

### Monthly ground colours (optional)

`biomes` is an optional list that overrides the app's built-in ground colours for a month: `{ "month": 1-12, "key", "name", "grassLight", "grassDark", "margin", "soilLeft", "soilRight" }`, colours as `#RRGGBB`. Every field except `month` is optional. **Leave `biomes` out unless I ask**: the app's built-in colours blend smoothly round the year and are what I want unless I say otherwise.

## Sprite format (every PNG)
| Item | Canvas size in pixels |
| --- | --- |
| Tree | 32 wide x 48 tall |
| 2x2 landmark | 64 wide x 96 tall |

- RGBA PNG. Every pixel is either fully transparent (alpha 0) or fully opaque (alpha 255). No anti-aliasing, blur, gradients, glow or semi-transparent pixels, because the app scales the art with nearest-neighbour.
- Draw at 1x. Never upscale or export large; the app does the scaling.
- Anchor rule: the bottom-centre pixel of the PNG is the bottom corner of the item's footprint on the ground. The ground tile is a 2:1 diamond, 32x16 pixels for one tile (64x32 for a 2x2), so the diamond fills the bottom 16 rows of a tree canvas, or the bottom 32 rows of a landmark canvas. A tree's trunk foot goes at the centre of that diamond: 8 pixels above the bottom edge, horizontally centred. A landmark's base sits inside its 64x32 diamond.
- Do not draw the ground tile into the sprite. A soft shadow of up to 2 rows right under a tree's foot is fine.
- Nothing may touch the left, right or top edge of the canvas.
- Style: 8-bit pixel art, a 1-pixel dark outline, light from the top left, at most 16 colours per sprite. Forest greens and browns, slightly darker than a bright cartoon (the app has a dark theme). Each species must be recognisable by silhouette alone at this size.
- Extra art packs are more folders beside `default8bit`; a pack that lacks an item falls back to `default8bit`.

## Workflow for any change
1. Read this file.
2. Make the change.
3. If a PNG changed, bump that item's `spriteRevision`.
4. Run `python3 scripts/validate.py` until it prints OK.
5. Commit with a clear message and push to `main`.
6. Confirm the GitHub Action passes.
7. Report what changed.

Ask me first if a request would break any rule above.