# Cow pilot for Xcode

The cow is a stationary, one-cell animal. Use the permanent key `cow` and the proposed type `animal`. The base, Autumn Leaves and winter art are approved. The [Debug catalog proposal](COW.preview.json) maps all three sprites to this item. The live catalog supports trees and landmarks. Publish animal entries when the Swift content loader, save model and content validator support them.

## Familiars

Add separate Animals sections to Store and Inventory. Resolve a single **Familiars** unlock for both. Its source is a future decision between a spell and an achievement. Until an authoritative unlock exists and is earned, hide Animals and its items, including purchase and placement shortcuts. Use Debug fixtures to test both states.

After the unlock, apply ordinary purchase eligibility in Store and show owned animals in Inventory. Cow purchase and placement prices are undecided. Learning Terraforming controls Ground. Use the active, owned art pack to select the cow’s appearance. Familiars remains the prerequisite for both Animals menus.

## Placement and artwork

Draw the cow with nearest-neighbor sampling on its native 32 × 48 canvas. Use the existing one-cell isometric foreground projection and depth order. Its bottom-center canvas anchor aligns with the front tip of the cell and the hooves sit near the middle of the tile. The cow may stand over a cell surface where available. Its placement occupies one foreground cell.

Persist one `cow` placement per cow using the save model's ordinary animal identity and coordinates. Resolve its appearance from the saved day's effective, owned pack, with the approved base as fallback. Use `sprites/fall/cow.png` for Autumn Leaves and `sprites/winter/cow.png` for the winter fixture. The Winter pack has an approved December 1–February 28 window and 10-token price; it remains disabled until its native checks pass. Preserve existing placements and historical rendering when building the menu eligibility checks.

## Debug acceptance

1. Open a pre-animal save. With Familiars unavailable or unearned, confirm both menus hide Animals even if a fixture owns the cow or a seasonal pack. A Terraforming-only fixture should produce the same result.
2. Enable Familiars alone. Verify unowned and owned cows follow normal Store and Inventory eligibility. Confirm the Ground category still follows its own gate.
3. Place a cow beside a tree on a free cell. Save, reopen offline and inspect that date in Day and World. Check depth sorting, the hoof anchor and stable placement over the monthly floor or an available surface.
4. Keep the saved cow key and coordinates fixed. Exercise the base, Autumn Leaves and winter appearances in the Debug pack fixture. Confirm a missing override or unowned seasonal pack falls back to base, each appearance aligns at the same hoof position in Day and World, and seasonal pack ownership alone keeps both Animals menus hidden.

## Snow Hare shares the future Animal category

The approved snowy-base Hare is preserved at `sprites/default8bit/snow_hare.png` in this pilot directory. It shares the unresolved Familiars gate, but its planned purchases and every new placement are limited to December 1–February 28 inclusive. Neither Cow nor Hare has approved production prices or a live animal catalog entry. See [the Winter object manifest](../winter_objects/manifest.json) for Hare's exact sprite and native checks. Familiars may remain pending while ordinary seasonal Winter items are verified.

## Arctic Fox approved base pilot

Arctic Fox now has approved base art at `sprites/default8bit/arctic_fox.png` in this pilot folder. It shares the future Animals model and unresolved Familiars gate. Its prices, acquisition and exact dates remain undecided; December 1–February 28 is only a proposal. There is no runtime animal catalog entry. See the [Winter Wave 2 manifest](../winter_objects_wave2/manifest.json) and [handoff](../winter_objects_wave2/XCODE_HANDOFF.md).

## Approved Christmas Animal artwork

Christmas Fox and Hare skins are approved at `sprites/christmas/arctic_fox.png` and `sprites/christmas/snow_hare.png`. `sprites/christmas/cow.png` is a byte-identical copy of the approved Winter Cow because appearance fallback goes to base, not Winter. `sprites/default8bit/reindeer.png` is a new approved one-cell Animal pilot with intrinsic Christmas art. Reindeer is not a tree or live catalog entry, and owning the Christmas pack does not grant any animal or Familiars.

Reindeer purchase and every-new-placement dates are approved as December 15–30 inclusive, closing December 31 at 00:00 local time. Acquisition and prices remain unset; Familiars and native Animals support remain required. Snow Hare keeps its approved December 1–February 28 rule; Fox retains its pending base dates. All Animals still depend on native Animal support and unresolved Familiars. Preserve ownership and old animal rendering outside windows or while menus are hidden. See the [Christmas approval](../../handoffs/christmas-2026/approval.json) and [Xcode calendar/gate handoff](../../handoffs/christmas-2026/XCODE_HANDOFF.md).
