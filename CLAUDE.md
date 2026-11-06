# Mystic Forest content repo: rules for any agent working here

The Mystic Forest tab of my iOS app reads this repo (read-only) from raw.githubusercontent.com on `main` and caches it. Nothing in the app is changed by editing here except what is described in this file. Read this file fully before every task.

## Layout
- `catalog.json`: every tree and landmark.
- `sprites/<pack>/<key>.png`: one PNG per item. The only pack right now is `default8bit`.
- `scripts/validate.py`: run `python3 scripts/validate.py` before every commit. Never commit while it reports a problem.
- `tools/make_sprites.py`: draws sprites in code. Optional for new items.

## catalog.json
Top level: `version` (always 1), `packs`, `trees`, `landmarks`.

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
- Later, not now: monthly ground tiles `sprites/<pack>/ground/<biome>.png` (32x16). Extra art packs are more folders beside `default8bit`; a pack that lacks an item falls back to `default8bit`.

## Workflow for any change
1. Read this file.
2. Make the change.
3. If a PNG changed, bump that item's `spriteRevision`.
4. Run `python3 scripts/validate.py` until it prints OK.
5. Commit with a clear message and push to `main`.
6. Confirm the GitHub Action passes.
7. Report what changed.

Ask me first if a request would break any rule above.