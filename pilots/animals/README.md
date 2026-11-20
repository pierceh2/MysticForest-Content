# Cow pilot for Xcode

The cow is a stationary, one-cell animal. Use the permanent key `cow` and the proposed type `animal`. The base art is approved. The [Debug catalog proposal](COW.preview.json) pairs the item with its sprite. The live catalog supports trees and landmarks. Publish animal entries when the Swift content loader, save model and content validator support them.

## Familiars

Add separate Animals sections to Store and Inventory. Resolve a single **Familiars** unlock for both. Its source is a future decision between a spell and an achievement. Until an authoritative unlock exists and is earned, hide Animals and its items, including purchase and placement shortcuts. Use Debug fixtures to test both states.

After the unlock, apply ordinary purchase eligibility in Store and show owned animals in Inventory. Cow purchase and placement prices are undecided. Learning Terraforming controls Ground. Owning an art pack can select a cow appearance once that override exists. Neither grants access to Animals.

## Placement and artwork

Draw the cow with nearest-neighbor sampling on its native 32 × 48 canvas. Use the existing one-cell isometric foreground projection and depth order. Its bottom-center canvas anchor aligns with the front tip of the cell and the hooves sit near the middle of the tile. The cow may stand over a cell surface where available. Its placement occupies one foreground cell.

Persist one `cow` placement per cow using the save model's ordinary animal identity and coordinates. Resolve its appearance from the saved day's effective, owned pack, with the approved base as fallback. Only the base PNG is staged. Preserve existing placements and historical rendering when building the menu eligibility checks.

## Debug acceptance

1. Open a pre-animal save. With Familiars unavailable or unearned, confirm both menus hide Animals even if a fixture owns the cow or a seasonal pack. A Terraforming-only fixture should produce the same result.
2. Enable Familiars alone. Verify unowned and owned cows follow normal Store and Inventory eligibility. Confirm the Ground category still follows its own gate.
3. Place a cow beside a tree on a free cell. Save, reopen offline and inspect that date in Day and World. Check depth sorting, the hoof anchor and stable placement over the monthly floor or an available surface. With a seasonal pack active and no override available, the base cow should draw.
