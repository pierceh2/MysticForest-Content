# Winter Wave 2 — approved artwork, pending release

Use the [manifest](manifest.json) for the approved Frostbloom Tree, Snow Lantern Circle and Arctic Fox file hashes, dimensions and staging fields. The owner approved their artwork. This handoff does not activate them, set final economy, approve exact dates or create an Animals runtime class.

## Catalog and native model

Frostbloom Tree is a disabled `trees` entry at 32×48 and one foreground cell. Snow Lantern Circle is a disabled `landmarks` entry at 64×96 and a 2×2 footprint. Both start at spriteRevision 1. Their default PNGs already provide winter appearances, independent of Winter-pack ownership. Catalog tokenPrice 3 and 4 are the documented repository placeholders; final prices and acquisition remain open.

Leave both disabled until prices, acquisition and purchase/new-placement windows are approved, then verify the resulting behavior before release. The proposed December 1–February 28 window is not configured in their catalog entries. Do not infer year-round permission from this staging omission. The earlier Winter/Snowman/Winterberry/Frost Obelisk four-key activation approval remains separate and unchanged.

Arctic Fox stays at `pilots/animals/sprites/default8bit/arctic_fox.png`. It uses the proposed `animal` type and Animals Store/Inventory sections, one foreground cell and the normal bottom-center canvas anchor. Do not map it to `trees` merely because its PNG is 32×48. Implement decoding, persistence, occupancy and rendering through the native animal model before registering live animal content.

## Familiars and saved forests

Familiars remains a future spell or achievement with no stable identifier or earning condition selected. Hide Animals sections and all purchase/placement actions while it is missing, unavailable or unearned. Art-pack ownership does not grant the category or the animal. Continue rendering already-saved animals independently of menu visibility. Arctic Fox prices, acquisition and exact date window remain unset.

## Visual and release checks

1. Inspect all three approved native canvases in Day and close/distant macro Forest views with nearest-neighbor sampling. Preserve the full canvas and bottom-center anchor. Tree/animal feet end at row 40; the snow-lantern base ends at row 94.
2. Check that Frostbloom's branch structure stays connected, its blue-white buds remain visible, all four amber lantern windows read clearly, and the Fox's ears, muzzle, paws and tail remain recognizable. Do not enlarge sprite files to compensate for any app scale bug.
3. Verify the same saved keys and coordinates across eligible appearance packs, missing overrides, offline reload and date changes. Future Christmas reskins may change appearance only, without granting ownership or altering placement eligibility.
4. After the owner settles exact release dates, add the configured window and share the authoritative purchase/new-placement check across Store, Inventory, preview and final mutation. Exercise owned and unowned cases, boundaries, year wrapping, midnight rollover and leap day according to the chosen dates. Reject atomically before spending tokens or changing occupancy.
5. Keep previous ownership and saved placements after a seasonal window closes. Ground surfaces may remain beneath foreground objects; its Terraforming gate is separate from Familiars.

## Settings → Future Features

Port the updated [roadmap records](../../handoffs/rewards-collections/MysticForest-FutureFeatures.json) into the existing Settings tab by matching existing IDs or meaning. Update Familiars for Arctic Fox and add the Frostbloom/Snow Lantern subject once. Keep technical fields out of player-facing copy and preserve unrelated roadmap entries. Artwork approval does not mean native implementation is complete.
