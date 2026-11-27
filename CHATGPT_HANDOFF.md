# Mystic Forest content: handoff to ChatGPT

This document hands the Mystic Forest art-and-content work to ChatGPT. It explains the project, the rules, what exists today, how to make new sprites with image generation, how to improve the existing sprites, and how to get the work into the GitHub repo.

**For the owner:** start a ChatGPT conversation, attach this file, and also attach the repo as a ZIP (on GitHub: **Code → Download ZIP** for `pierceh2/MysticForest-Content`, branch `main`). Then say: "Read CHATGPT_HANDOFF.md and follow it. Here is my first job: …" and use a job template from section 10.

**For ChatGPT:** read this whole file first, then read `CLAUDE.md` from the repo ZIP. `CLAUDE.md` is the source of truth for every rule. If this file and `CLAUDE.md` ever disagree, follow `CLAUDE.md` and tell the owner about the difference.

## Current approved integration — November 27, 2026

The owner approved the Winter reskin pack for **December 1–February 28 at 10 Forest tokens**, plus ordinary seasonal acquisition for **Snowman 3/1, Winterberry Bush 3/1 and Frost Obelisk 8/4** (one-time unlock / per-placement tokens). The dates and economy no longer need approval. Winter is revision 3 with its window configured. Winter and the three objects remain disabled until native checks pass; the [release record and authorized activation patch](handoffs/winter-2026/README.md) specify that next step without repeat business approval.

This integration includes earlier approved PRs #3–#7: Ground atlases, Cow base/Autumn/Winter, Cherry Blossom base/Winter, and Gold/Silver/Bronze base sprites. All approved PNG bytes and the Classic Retro originals are preserved. Cherry and the veins are disabled catalog registrations; Ground, Cow and Snow Hare remain pilots. Familiars is still undecided, as the owner requested.

Use the [current seasonal-placement handoff](handoffs/seasonal-planting/SEASONAL_PLANTING_XCODE_HANDOFF.md) for the seven existing restricted objects and four Winter-only objects. Dates restrict purchases and every new placement while preserving ownership and saved forests. This needs native enforcement. Update the existing Settings → Future Features screen using the [current roadmap handoff](handoffs/rewards-collections/FUTURE_FEATURES_HANDOFF.md).

### Ground and Animals for Xcode

Dirt Patch and Dirt Rows have approved base, Autumn Leaves and Winter atlases. Cobblestone Circle has approved base art and joins neighboring stone cells; soil and stone retain their distinct boundaries. Ground gets its own type, Store and Inventory sections and saved cell-surface layer beneath existing trees, animals and landmarks. The planned **Terraforming** spell gates both menus and actions. Surface prices and spell acquisition remain pending. The [Ground handoff](pilots/ground/FOREST_OBJECT_TYPES_XCODE_HANDOFF.md) and [Debug contract](pilots/ground/OBJECT_TYPES.preview.json) cover placement, adjacency, persistence and legacy saves. Monthly floors remain visible independently of this gate.

Cow has approved base, Autumn Leaves and Winter sprites; Snow Hare has approved winter-only base art. Both belong to the future Animals type and separate Store/Inventory sections. **Familiars** remains undecided between a spell and achievement, with no earning condition or production economy set. Hide Animals actions while the gate is absent or unearned; preserve saved animals' rendering. See the [Cow handoff](pilots/animals/README.md) and [Winter object handoff](pilots/winter_objects/XCODE_HANDOFF.md). The current live catalog still supports only trees and landmarks.

---

Current inventory snapshot: 2026-11-27. Historical art-generation guidance later in this file remains reference material; consult the current catalog and coverage before new work.

---

## 1. The project in one minute

- "Mystic Forest" is a tab in the owner's iOS app. Daily focus time earns tokens; the owner spends tokens to unlock and place pixel-art **trees** (one tile) and **landmarks** (2x2 tiles) on a small isometric plot. Each day is drawn in one **art pack**.
- The app reads only two things from the public repo `pierceh2/MysticForest-Content` on branch `main`, through `raw.githubusercontent.com`:
  - `catalog.json`: every item and pack (names, descriptions, prices, seasons, tags, purchase windows, revisions).
  - `sprites/<pack>/<key>.png`: one PNG per item per pack.
- Changing those files and pushing to `main` changes the app (after the owner taps **Sync now**). Nothing else in the repo reaches the app.
- The owner has a dark-themed app, so the art is forest-toned and slightly darker than a bright cartoon.

## 2. What you (ChatGPT) do, and what you need

You make the **pixel art**, the **names** and the **descriptions**, package each job as a **delivery**, and (if you can) apply it to the repo.

| You need | How you get it |
| --- | --- |
| The rules | `CLAUDE.md` in the repo ZIP |
| The current catalog and sprites | `catalog.json` and `sprites/` in the repo ZIP. Online copies: `https://raw.githubusercontent.com/pierceh2/MysticForest-Content/main/catalog.json` and `.../main/sprites/<pack>/<key>.png` |
| A Python sandbox with Pillow | Your code tool. Run the repo's scripts there (section 7) |
| Image generation | Your image tool, for new or redrawn art (section 6) |
| A way to change the repo | Either write access to GitHub (a GitHub connection or coding agent that can commit), **or** hand the owner a ZIP to upload. See section 8 |

If your Python sandbox has no internet, work from the repo ZIP. Never guess what a file contains; open it.

## 3. The rules you must not break (short version of `CLAUDE.md`)

**Items** (in `catalog.json` under `trees` or `landmarks`):

| Field | Rule |
| --- | --- |
| `key` | `^[a-z][a-z0-9_]*$`, unique, **permanent**. Never rename, remove or reuse a key; saved forests and unlocks refer to it |
| `name` | Title case, up to 24 characters |
| `description` | One warm sentence, up to 120 characters, cosy fantasy-forest voice. No markdown, emoji, prices, tokens or game mechanics |
| `tokenPrice` | Required whole number. Tree: default store (unlock) price. Landmark: default plant price |
| `storePrice` / `plantPrice` | Optional. Only write them when they differ from the defaults: tree store = `tokenPrice`, tree plant = 1; landmark store = 8, landmark plant = `tokenPrice` |
| `startsUnlocked` | Trees only. `tokenPrice` 0 only when this is true |
| `footprint` | Landmarks only, always `[2, 2]` |
| `enabled` | `false` hides an item for staging or retirement (still drawn in saved forests). Never delete |
| `spriteRevision` | Starts at 1; +1 whenever the item's **default-pack** PNG changes |
| `season` | Optional season id, browsing only: `winter`, `spring`, `summer`, `autumn`, or a holiday id such as `halloween`, `thanksgiving`. **Never "fall"** |
| `tags` | Optional, up to 12 lowercase labels, browsing only. Never repeat the item's season in its tags |
| `window` | Optional `{ "start": "MM-DD", "end": "MM-DD" }`, inclusive, repeats yearly, may cross the new year. Outside it an unowned item is hidden from the Store. The specified seasonal keys also reject new placement even when owned; ownership and saved placements persist. See the current seasonal handoff. Never add `buyOnlyInSeason` to an item. A bad date makes the item never buyable, so check month lengths |

**Packs** (in `catalog.json` under `packs`): `key` (permanent, also the folder name), `name`, `description`, `kind` (`seasonal`/`holiday`), `season`, `window`, `tags`, `tokenPrice`, `enabled`, `revision` (+1 once per delivery whenever any of the pack's art changes; a new pack starts at 1), optional `ground` colours (`grassLight`, `grassDark`, `margin`, `soilLeft`, `soilRight`, as `#RRGGBB`). A pack may cover only some items; missing ones fall back to `default8bit`, which must have every enabled item.

**General:** no fields that `CLAUDE.md` does not list. Never change an existing price, window, `startsUnlocked`, footprint or key unless the owner asks in that job. Leave `biomes` out unless asked. Keep `catalog.json` valid UTF-8 JSON with two-space indentation, and keep its existing layout (insert text; don't reformat the file).

**Not yet in `CLAUDE.md`:** the owner has said that items earned from spells or achievements will be tagged exactly `secret` or `achievement` (never shown in the Store, no `storePrice`, `tokenPrice` 1 for such trees). `CLAUDE.md` and the validator don't document these tags yet, so ask the owner before using them.

## 4. Sprite format (every PNG)

| Item | Canvas |
| --- | --- |
| Tree (1 tile) | 32 wide x 48 tall |
| Landmark (2x2) | 64 wide x 96 tall |

- RGBA PNG. Every pixel fully transparent (alpha 0) or fully opaque (alpha 255). No anti-aliasing, blur, glow or gradients: the app scales with nearest-neighbour.
- Draw at 1x. Never export large; the app scales up.
- **Anchor:** the bottom-centre pixel of the PNG is the bottom corner of the item's footprint. The ground diamond is 32x16 for one tile (the bottom 16 rows of a tree canvas) or 64x32 for 2x2 (the bottom 32 rows of a landmark canvas). A tree's trunk foot sits at the centre of its diamond: **row 40** (8 rows above the bottom), centred between columns 15 and 16. A landmark's base sits inside its 64x32 diamond and reaches near the bottom row.
- Don't draw the ground tile. A shadow up to 2 rows under a tree's foot, or a few tiny leaves inside the tile, is fine.
- Nothing may touch the left, right or top edge.
- Style: 8-bit pixel art, 1-pixel dark outline (`#101b15`), light from the top left, at most 16 colours per sprite, each species recognisable by silhouette alone.
- **A pack reskin** keeps the same canvas, silhouette, footprint and foot position as the default sprite, with the theme added on top.

### The palette in use

Reusing these keeps new art consistent with the set (they are in `tools/make_sprites.py`, `tools/make_november.py` and `tools/make_thanksgiving_items.py`):

| Group | Colours |
| --- | --- |
| Outline, shadow | `#101b15`, `#1d2d22` |
| Trunk browns | `#80552f`, `#5d3d23`, `#3f2a1a` |
| Oak greens (light to dark) | `#7aa63f`, `#58903a`, `#40762f`, `#2d5c2b`, `#1f4426` |
| Pine blue-greens | `#4f8f62`, `#377249`, `#27583b`, `#1a4030`, `#112c22` |
| Birch yellow-greens, bark | `#b0c24f`, `#8cab40`, `#6c8f36`, `#527230`, `#3b5628`; bark `#dcd8c8`, `#aaa696`, `#2a2a28` |
| Willow pale greens | `#a3c077`, `#80a262`, `#648550`, `#4b6a40`, `#37522f` |
| Stone, slate roof | `#8c9289`, `#6f7770`, `#565e58`, `#3c443f`; roof `#5f8590`, `#486a75`, `#34515c` |
| Autumn oranges | `#e3a73c`, `#c97a2d`, `#a8532a`, `#823b27`, `#5c2a22` |
| Golds | `#f0cf5a`, `#d9ad45`, `#b88a36`, `#8f6a2d`, `#6a4d26` |
| Warm glow, cream | `#f4c85e`, `#c98a3a`; cream `#e8dcc0`, `#c4b594` |
| Water, lily | `#4a9aa3`, `#33788a`, `#245c72`, `#a9d9d8`; lily `#d98aa6` |
| Reds (maple, apples) | `#f2603a`, `#e0402f`, `#c42f2c`, `#9a2328`, `#6e1a22` |

## 5. Current content (2026-11-27)

The catalog contains **15 trees and 9 landmarks**, including disabled staging entries. The current pack table and item-by-pack grid are in [PACK_COVERAGE.md](PACK_COVERAGE.md). Refined art is the default under the existing permanent item keys; original Classic Retro sprites remain in `art-archive/classic-retro/` for the future separate pack.

| Pack | Window | Unlock tokens | Revision | Direct sprite coverage | Release state |
| --- | --- | ---: | ---: | --- | --- |
| Default 8-bit / Refined (`default8bit`) | Always | 0 | Item revisions | 24 of 24 | Existing default |
| Autumn Leaves (`fall`) | October 1–December 1 | 10 | 4 | 10 of 24 | Enabled |
| Thanksgiving Feast (`thanksgiving_feast`) | November 15–November 30 | 10 | 3 | 9 of 24 | Enabled |
| Winter (`winter`) | December 1–February 28 | 10 | 3 | 13 of 24 | Approved; disabled until native checks |

Missing overrides use the default sprite. Mineral veins and intrinsically winter-only base objects intentionally need no seasonal overrides. The Ground and Animal pilot sprites are counted separately from the runtime tree/landmark grid.

`tokenPrice` is the default tree unlock price (placement 1) and landmark placement cost (unlock 8). No item overrides storePrice or plantPrice. Winter, Snowman, Winterberry Bush and Frost Obelisk have approved prices. Cherry Blossom and vein tokenPrice values remain staging placeholders. Ground and Animal prices are unresolved.

The exact current purchase/new-placement windows are recorded in [the seasonal handoff](handoffs/seasonal-planting/SEASONAL_PLANTING_XCODE_HANDOFF.md). Apple Tree and Hay Bale Stack remain October 1–December 1 inclusive, so their approved Winter art covers the December 1 overlap. Harvest Table is November 15–November 30 only. Seasonal artwork does not widen an item's window.

### Remaining release and implementation work

- Verify Refined/default and Winter sprite scale in the native app. An older report described pack sprites appearing undersized; use full PNG canvases and check Day/World anchors instead of enlarging art to compensate. This content integration does not verify the reported app behavior.
- Complete native seasonal enforcement and visual checks, then apply the already-authorized Winter/three-object activation patch.
- Keep Familiars, Terraforming, Village, individual vein unlocks and Classic Retro pack availability separate from art-pack ownership. Their unresolved conditions are documented in Future Features.
- Cherry Blossom base/Winter art is approved; its release economy and availability remain pending. Autumn Cherry remains a separate visual decision.
- Keep pack keys permanent: `fall` remains the folder/key for season `autumn`.

Read and regenerate `PACK_COVERAGE.md` after content additions. Do not turn an intentionally excluded appearance into an accidental gap.

### Tools in the repo

| Script | What it does |
| --- | --- |
| `scripts/validate.py` | The repo validator. Must print `OK` before any commit |
| `tools/check_sprite.py` | Checks one PNG: `python3 tools/check_sprite.py path.png tree|landmark` |
| `tools/fit_sprite.py` | **Turns any picture (for example a generated image) into a valid sprite** (section 6) |
| `tools/recolour_sprite.py` | Lists or swaps a sprite's colours exactly (section 7, route C) |
| `tools/make_pack_coverage.py` | Regenerates `PACK_COVERAGE.md` (`--check` to test it is current) |
| `tools/make_sprites.py`, `make_harvest.py`, `make_november.py`, `make_thanksgiving_*.py` | The code that drew every existing sprite (pixel art from shapes and palettes). Useful as reference or to tweak an existing drawing. Never edit `make_sprites.py` |

## 6. Making new sprites with image generation

Image models make large, smooth, anti-aliased pictures. They cannot output a valid 32x48 hard-pixel sprite directly. The reliable way is: **generate a big clean picture, then convert it with `tools/fit_sprite.py`**, then look at it and fix.

### Step 1: generate the picture

Use this prompt template (fill in the brackets):

```text
Pixel art game sprite of [ONE OBJECT, e.g. "a sugar maple tree in full autumn colour"], for a cosy
fantasy forest game. Isometric three-quarter view from slightly above, the same angle for every
sprite. Chunky 8-bit style, large clear shapes, few colours, a 1-pixel dark outline around the whole
silhouette, light coming from the top left. [COLOURS AND DETAILS, e.g. "deep red and orange crown,
dark brown trunk"]. The whole object is visible and centred, standing upright, with its base at the
bottom. Plain flat solid magenta background (#FF00FF) filling the entire image. No ground, no grass,
no shadow, no text, no border, no other objects.
```

Tips:
- Ask for **one object per image**, square (for example 1024x1024).
- **Magenta background** keeps the cut-out clean. If the subject contains magenta or pink (for example lily flowers), ask for a flat lime-green background (`#00FF00`) instead and pass `--key "#00FF00"`.
- For a **tree**, describe a silhouette clearly different from the existing ones (see section 5). For a **2x2 landmark**, ask for "an isometric diorama-style object on a diamond-shaped base, wider than it is tall". The base should be a diamond seen from above at a 2:1 ratio.
- Generate 2 to 4 options and pick the one whose **silhouette** reads best when you imagine it 32 pixels wide.

### Step 2: convert it

```bash
# a new tree, colours picked from the picture (at most 16)
python3 tools/fit_sprite.py generated.png out/maple.png --kind tree --preview out/maple_8x.png

# the same, but limited to the set's palette, which keeps it consistent with the other sprites
python3 tools/fit_sprite.py generated.png out/maple.png --kind tree \
    --palette sprites/default8bit/oak.png sprites/fall/maple.png --preview out/maple_8x.png

# a 2x2 landmark
python3 tools/fit_sprite.py generated.png out/well.png --kind landmark --preview out/well_8x.png
```

What it does: removes the background (flood fill from the edges), trims the soft fringe, shrinks the subject into the drawn area (trees up to 28x38 with the foot on row 40; landmarks up to 60x64 with the base on row 94, next to the bottom edge), forces hard alpha, limits colours, adds the 1-pixel `#101b15` outline, and runs the sprite checks. It prints `OK …` or the exact problem. Run `python3 tools/fit_sprite.py --help` for every option (`--box`, `--colours`, `--key`, `--tolerance`, `--defringe`, `--no-outline`).

### Step 3: look at it, then fix

**Always look at the 8x preview** (nearest-neighbour on dark green) next to existing sprites before delivering. Check: is it recognisable at 1x? Is the foot or base where the others' are? Does the colour weight match the set? Common fixes:
- Too much detail or noise: regenerate with "simpler, bigger shapes, fewer colours", or pass `--colours 10`.
- Odd colours: add `--palette` with one or two existing sprites of a similar kind.
- Tiny details lost (faces, flames): edit those few pixels by hand in Python on the 32x48 result (draw exact pixels with `putpixel`), then re-run `tools/check_sprite.py`.
- Wrong proportions: change `--box` (for example `--box 24x38` for a slimmer tree).

If image generation keeps failing for an item, draw it in code instead, following the existing `tools/make_*.py` scripts, and keep that script in `tools/`.

## 7. Improving the existing sprites

There are three routes. Pick per item.

### Route A: redraw from a written brief (the list below)

Generate a fresh picture from the brief, convert with `fit_sprite.py` using **`--like` the existing sprite** so the new art fills the same area and sits on the same foot, and `--palette` with the existing sprite (or the palette groups in section 4) so colours stay in the family:

```bash
python3 tools/fit_sprite.py generated.png out/birch.png --kind tree \
    --like sprites/default8bit/birch.png --palette sprites/default8bit/birch.png --preview out/birch_8x.png
```

Suggested improvements, most valuable first (these are honest weak spots noted when each sprite was made):

| Priority | Item | Today | Suggested redraw |
| --- | --- | --- | --- |
| 1 | jack_o_lantern | The carved face is dense and merges into one band at 1x | Simpler face: two big triangle eyes and one wide grin, brighter yellow glow, darker body rim so the cuts pop |
| 1 | corn_stalks | Thick golden stalks read like wheat until you see the cobs | Fewer, greener-gold stalks with broad drooping leaves and two or three obvious cobs; tied with twine |
| 1 | harvest_table | Large pale cloth block; the food is small | Darker cream or plaid cloth, fewer but bigger dishes (one pie, one pumpkin, bread, two candles), maybe two short benches |
| 2 | birch | Crown looks like stacked blobs | Lighter, airier crown of small drooping leaf clusters, keep the white bark with black marks |
| 2 | larch | Reads a little like a layered Japanese pine | More irregular, drooping, gappy needle tufts, still clearly unlike the solid pine |
| 2 | maple | Crown is a stylised maple-leaf shape | Fuller, rounded crown with a pointed, lobed edge; keep the cool green (red in the fall pack) |
| 2 | scarecrow | Legs short and thin | Taller post, longer trousers, clearer straw hat silhouette |
| 3 | hay_bales | Layer edges a bit busy; fills the whole tile | Slightly smaller stack, cleaner bale edges, two clear twine bands per bale |
| 3 | pumpkin | Small on its tile | A little larger (about 22x16), stronger ribs |
| 3 | ginkgo | Small dark dashes where fans overlap | Cleaner fan-shaped clusters with fewer overlaps |
| 3 | apple_tree | Windfall apples sit near the tile edge | Move windfalls closer to the trunk |
| - | oak, pine, willow, shrine, pond | Read well | Leave unless the owner asks |

Pack sprites with known weak spots: `thanksgiving_feast/maple` is close to `fall/maple` (both red); `thanksgiving_feast/pumpkin` (a pile) is wider than the default pumpkin; the string lights on `thanksgiving_feast/oak` and `birch` are tiny at 1x.

### Route B: restyle from the existing sprite

1. Take the existing PNG (repo ZIP, or `https://raw.githubusercontent.com/pierceh2/MysticForest-Content/main/sprites/<pack>/<key>.png`).
2. Enlarge it 16x with **nearest-neighbour** on a magenta background so the image model sees clean blocks:
   ```python
   from PIL import Image
   s = Image.open("sprites/default8bit/birch.png").convert("RGBA")
   bg = Image.new("RGBA", s.size, (255, 0, 255, 255)); bg.alpha_composite(s)
   bg.resize((s.width * 16, s.height * 16), Image.NEAREST).save("birch_ref.png")
   ```
3. Give that image to the image tool as a reference: "Redraw this pixel-art sprite with the same silhouette, size, pose and base position, but [CHANGE]. Keep it pixel art with a dark outline, flat magenta background, no ground or shadow."
4. Convert with `fit_sprite.py --like <the original PNG>` (plus `--palette` if the colours should stay), then compare the 8x previews side by side.

This keeps the item recognisable, which matters for reskins and for redraws the owner only wants polished.

### Route C: recolour (best for seasonal pack reskins)

Many pack reskins are mostly a colour change (green leaves to orange, gold or snow-white). Recolouring keeps every pixel, the silhouette and the foot exactly:

```bash
python3 tools/recolour_sprite.py sprites/default8bit/oak.png --list          # see its colours
python3 tools/recolour_sprite.py sprites/default8bit/oak.png out/oak.png \
    --map "#7aa63f=#e8eef0" "#58903a=#c9d6dc" "#40762f=#9fb2bb" "#2d5c2b=#6f8794" "#1f4426=#4a5d68"
```

Then add small theme details by hand in Python (snow on top edges, lights, ornaments, a pumpkin at the foot), keeping inside 16 colours, and re-run `tools/check_sprite.py`.

### Revisions when you change art

- A redrawn **default-pack** PNG: that item's `spriteRevision` +1.
- Any changed PNG in another **existing pack**: that pack's `revision` +1, once per delivery.
- New items start at `spriteRevision` 1; a new pack starts at `revision` 1.

The app only re-downloads art when these numbers go up, so never skip this.

## 8. Getting the work into the repo

### The delivery folder

Every job becomes one folder, `deliveries/delivery-<yyyy-mm-dd>-<short-name>/`:

```text
README.md            What's in it / Placeholders / Weak spots / Decisions for the owner
changes.json         what to add or change in catalog.json
sprites/<pack>/<key>.png     every new or redrawn PNG, at its final path
```

`changes.json`:

```json
{
  "add": {
    "trees": [ { "key": "maple", "name": "Maple", "description": "…", "tokenPrice": 4, "startsUnlocked": false, "enabled": true, "tags": ["deciduous"] } ],
    "landmarks": [],
    "packs": []
  },
  "edit": {
    "trees": [ { "key": "birch", "description": "New text." } ],
    "landmarks": [],
    "packs": []
  },
  "retire": [],
  "spritesChanged": [ { "pack": "default8bit", "key": "maple" } ]
}
```

- `add` entries are complete (no `spriteRevision`; it is set when applying). `edit` entries hold the `key` plus only the changed fields. `retire` lists keys to disable. Leave out empty sections.
- `spritesChanged` lists **every** PNG in the delivery, and nothing else.
- Prices: use the owner's numbers; if none, placeholders 3 (tree), 4 (landmark), 10 (pack), listed in the README.
- See the existing folders in `deliveries/` for real examples.

### Applying a delivery (follow `CLAUDE.md` "Applying a delivery")

1. Check the delivery against `CLAUDE.md`. Stop and ask on any conflict.
2. Copy each listed PNG to the same path under `sprites/`.
3. Merge `changes.json` into `catalog.json` by inserting text in the file's existing style (look at how current entries are laid out). Append adds; change only the supplied fields for edits; set `"enabled": false` for retires.
4. Set revisions (section 7).
5. Run `python3 tools/make_pack_coverage.py`, and add a row to "Left out on purpose" in `PACK_COVERAGE.md` for any item deliberately skipped.
6. Run `python3 scripts/validate.py` until it prints `OK`. If it fails because of your delivery, fix the delivery, not the validator.
7. Commit (one commit per delivery) with a message like `Add maple tree (delivery 2026-11-20-maple)`, listing any placeholders, and push to `main`. Then confirm the GitHub Action "Validate content" passed.

### If you cannot commit to GitHub

Do steps 1 to 6 in your sandbox on the unzipped repo, then give the owner **one ZIP** containing the delivery folder plus every changed repo file at its repo path (`catalog.json`, `PACK_COVERAGE.md`, `sprites/...`, any new `tools/...`). Tell the owner exactly which files to upload and where (GitHub web: **Add file → Upload files**, keeping folder paths, commit to `main`), or that they can give the folder to their repo agent with: "Apply the delivery at deliveries/<name>/ following the 'Applying a delivery' section of CLAUDE.md."

### Never

- Edit `CLAUDE.md`, `scripts/validate.py` or `tools/make_sprites.py` (rule changes go to the owner).
- Delete or rename a key or pack, reuse a key, or change a footprint.
- Change an existing price, window or `startsUnlocked` unless asked in that job.
- Spell the season "fall".
- Deliver a sprite you have not looked at enlarged, or one that fails `check_sprite.py`.
- Upscale sprites to work around the app's display bug.
- Invent fields, footprint sizes, growth stages or item types. Stop and describe options instead.
- Push with validation failing.

## 9. How to report each job

```text
Applied: <delivery folder> (committed on main as <commit>, or "ZIP for the owner to upload")
Added / changed / retired: <keys>
Files: <catalog.json and the PNGs touched>
Revisions raised: <item or pack, old to new>
Placeholders to tune: <prices or windows the owner should set>
Coverage: <gaps and exclusions in PACK_COVERAGE.md after this job>
Sprite check: <what you looked at, what you fixed, check results>
Concerns: <weak spots, decisions the owner should make>
Next step for the owner: <for example "tap Sync now", or which files to upload>
```

## 10. Job templates for the owner

```text
Task: add tree
Key: <lowercase key>        Name: <name or "you choose">
Look: <shape, colours, mood>
Description: <text or "you write it">
Store price (unlock): <number or "placeholder">     Plant price: <number or "default">
Starts unlocked: <yes | no>     Window: <MM-DD to MM-DD, or "none">
Season / tags: <season id and tags, or "none" or "you choose">
```

```text
Task: add landmark
Key: <key>   Name: <name or "you choose">
Look: <what it looks like; it fills a 2x2 footprint>
Description: <text or "you write it">
Store price: <number or "default">     Plant price: <number or "placeholder">
Window: <MM-DD to MM-DD, or "none">     Season / tags: <…>
```

```text
Task: add pack
Pack key: <lowercase key>      Name: <name or "you choose">
Look: <theme, mood, colours>
Season id: <winter | spring | summer | autumn | a holiday id>
Window: <MM-DD to MM-DD, or "none">
Items to cover: <keys, or "all": read PACK_COVERAGE.md, cover the gaps, propose exclusions>
Token price: <number or "placeholder">     Ground colours: <#RRGGBB list or "you choose">
```

```text
Task: redraw <item key> [in pack <pack key>]
Route: <A brief | B restyle from existing | C recolour>
Notes: <what to change>
```

```text
Task: improve existing sprites
Items: <keys, or "the priority list in CHATGPT_HANDOFF.md section 7">
Notes: <anything specific>
```

```text
Task: rewrite text / set tags or season / set prices / set window / retire <keys>
Items: <keys>
Notes: <what to change>
```

```text
Task: review
Look at what exists and tell me what is weak or inconsistent. (No delivery needed.)
```

**Suggested first job:** "Task: improve existing sprites. Items: jack_o_lantern, corn_stalks, harvest_table. Route: A for each. One delivery." That tests the whole pipeline on the three weakest sprites.
