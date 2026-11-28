# Mystic Forest Content

This repository stores the catalog and sprites used by the Mystic Forest tab of ChronosKeep. The app reads `catalog.json` and `sprites/` from `main`; pilot and handoff files support native development and do not activate features by themselves. Read [CLAUDE.md](CLAUDE.md) and [CHATGPT_HANDOFF.md](CHATGPT_HANDOFF.md) before changes.

## Current approved integration

The approved Ground, Cow, Cherry Blossom base/Winter and Gold/Silver/Bronze work is consolidated with the existing Refined and Winter artwork. Approved PNG bytes and Classic Retro originals are preserved. [PACK_COVERAGE.md](PACK_COVERAGE.md) tracks current runtime and pilot coverage.

Winter's **December 1–February 28** window and **10-token** price are approved. Snowman and Winterberry Bush are ordinary seasonal purchases at **3 tokens to unlock / 1 to place**; Frost Obelisk is **8 / 4**. Their business decisions are complete. The [Winter release handoff](handoffs/winter-2026/README.md) includes the authorized activation patch to apply after native checks; these entries are still disabled today.

## Native handoffs

- [Seasonal purchase and new-placement rules](handoffs/seasonal-planting/SEASONAL_PLANTING_XCODE_HANDOFF.md)
- [Settings → Future Features / rewards and collections](handoffs/rewards-collections/FUTURE_FEATURES_HANDOFF.md)
- [Animals and Ground types; Terraforming; soil beneath existing objects](pilots/ground/FOREST_OBJECT_TYPES_XCODE_HANDOFF.md)
- [Cow and Familiars](pilots/animals/README.md)
- [Winter objects and Snow Hare](pilots/winter_objects/XCODE_HANDOFF.md)
- [Mineral vein unlocks](docs/mineral-veins/README.md)

Cherry Blossom remains a disabled tree with its existing 3-token staging price; final economy, unlock and availability are undecided. Base and Winter art are approved. Autumn art remains a separate approval. Veins remain disabled with independent future spell/achievement conditions and the existing 4-token landmark placement placeholders. Animal and Ground catalog types require native and validator support before publication.

## Validation

Run `python3 scripts/validate.py` and `python3 tools/make_pack_coverage.py --check` before publication. Run `python3 pilots/ground/verify.py` for the Ground atlases. Content validation does not replace the required native build, date-rule tests and Day/World visual check.

## Approved Winter Wave 2

The approved original Frostbloom Tree and Snow Lantern Circle are staged as disabled catalog entries; Arctic Fox is a separate Animals pilot. Frostbloom and Snow Lantern Circle now have approved ordinary seasonal-store prices of 3/1 and 8/4 and December 1–February 28 windows, pending native checks. Arctic Fox release conditions remain deferred. The [Wave 2 handoff](pilots/winter_objects_wave2/XCODE_HANDOFF.md) records these boundaries and the native visual checks. This batch does not change the earlier Winter release approval or add Christmas artwork.

## Approved Christmas artwork

The approved Christmas art is staged in a disabled pack plus three disabled holiday landmarks and four Animal pilot files. See the [Christmas approval and calendar handoff](handoffs/christmas-2026/README.md). December 15–30 inclusive is now approved for Christmas dates. The pack price of 10 and each monument's 8 unlock / 4 placement through ordinary seasonal acquisition are approved. The pack and three monuments stay disabled until native checks pass; Animals remain deferred. This draft depends on unmerged PR14; merge the dependency first, then retarget and recheck. Existing artwork, windows, ownership rules and earlier Winter activation approval are preserved.

See the [scoped release approval](handoffs/forest-release-2026/README.md) for the six supported keys. This metadata commit publishes the formerly held dates and current business decisions through existing draft PR15 without activating or merging content.
