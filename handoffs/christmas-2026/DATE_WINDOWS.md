# Mystic Forest — purchase, placement and appearance dates

## Audit result

The start dates, inclusive end dates and out-of-season behavior are recorded. They are not all at the same release stage. The owner's latest message approves the Christmas artwork; it does not explicitly approve the proposed Christmas dates, prices or the separate Winter Wave 2 release settings.

This audit uses the existing Christmas planning JSON and register, main `1d7b0fe0af5df0f9469e3dfd3ab83b9b7b793dc6`, and the approved Winter Wave 2 draft at `99ad32feac650a009e13a0bacf2039fc514c4c57`. The Christmas publication workflow may stage the recorded proposals in disabled catalog entries. A draft catalog entry is not an enabled app feature or a verified native date check.

## Christmas dates

| Content | Purchase window | New placement / appearance window | Last included day and following day | Recorded state |
| --- | --- | --- | --- | --- |
| Christmas appearance pack | December 1–December 25 | Automatic Christmas appearance: December 1–December 25. Base-object placement follows that object's own rule. | December 25 included; automatic Christmas eligibility closes on December 26. | Exact proposal recorded in `Christmas-Content-Proposal.json`; proposed disabled pack catalog entry. Dates and price remain unapproved. |
| Present Pile | December 1–December 25 | Every new placement: December 1–December 25, including when already owned. | December 25 included; new purchase and placement unavailable on December 26. | Exact proposal and supported candidate landmark `window` recorded. |
| Santa Chimney | December 1–December 25 | Every new placement: December 1–December 25, including when already owned. | December 25 included; new purchase and placement unavailable on December 26. | Exact proposal and supported candidate landmark `window` recorded. |
| Santa Sleigh | December 1–December 25 | Every new placement: December 1–December 25, including when already owned. | December 25 included; new purchase and placement unavailable on December 26. | Exact proposal and supported candidate landmark `window` recorded. |
| Reindeer | December 1–December 25, proposed | Every new placement: December 1–December 25, proposed. | December 25 included in the proposal; December 26 outside it. | Animal pilot only. Exact proposed window recorded; Familiars, acquisition and economy remain unresolved. No runtime Animals catalog support is claimed. |

The three monuments and Reindeer have intrinsic Christmas default artwork. They do not require ownership of the Christmas appearance pack. Reindeer still requires the future Animals/Familiars path.

## Base-object dates preserved by Christmas reskins

| Content | Purchase and every-new-placement window | End behavior | Recorded state |
| --- | --- | --- | --- |
| Snowman, Winterberry Bush, Frost Obelisk | December 1–February 28 | February 28 included; March 1 outside. February 29 is also outside in a leap year. | Dates and supported-object economy already approved; windows configured in disabled catalog entries pending native checks/activation. |
| Snow Hare | December 1–February 28 | Same inclusive winter endpoint and leap-day rule. | Dates approved and recorded in animal-pilot handoffs; Familiars, animal economy and native support pending. |
| Frostbloom Tree, Snow Lantern Circle, Arctic Fox | December 1–February 28, proposed | Proposed February 28 endpoint. | Exact proposal recorded in the register and Winter Wave 2 manifest. Frostbloom and Lantern have **no configured catalog window** in PR #14; Fox is pilot-only. Release dates and economics remain undecided. |
| Oak, Pine, Birch, Willow, Larch, Maple, Ginkgo; Shrine and Lily Pond | No seasonal date restriction | Ordinary ownership, enabled-state, price and footprint rules continue throughout the year. | No item `window` in the catalog. A Christmas skin does not make these Christmas-only items. |
| Village Hut | No seasonal date restriction configured | Future Village unlock and enabled-state rules still apply. | Staged disabled; pending Village achievement access. Owning an art pack does not unlock the hut. |
| Cherry Blossom | No seasonal date restriction configured | Does not imply production availability. | Staged disabled; its separate release/acquisition status remains unchanged. |
| Cow | No seasonal date restriction established by this Christmas work | Does not imply production availability. | Animal pilot; Familiars and economy pending. Christmas reuses its Winter appearance. |

## Existing autumn and Thanksgiving exceptions

These values are already approved and configured; the Christmas work preserves them.

| Content | Purchase and every-new-placement window | First unavailable date after closing |
| --- | --- | --- |
| Apple Tree, Hay Bale Stack | October 1–December 1 | December 2 |
| Harvest Table, Corn Stalks | November 15–November 30 | December 1 |
| Pumpkin, Scarecrow | October 1–November 30 | December 1 |
| Jack-o'-Lantern | October 1–October 31 | November 1 |

Apple and Hay have explicit Winter-compatible copies in Christmas coverage for the December 1 overlap and saved rendering. Those files do not extend their planting period. The base-item window takes precedence over the active appearance pack for purchase and every new placement.

## Calendar and saved-forest behavior

- All recorded windows repeat every year and include both endpoints. Use the device's actual local calendar date. December-to-February ranges wrap across New Year.
- A closing date remains eligible for that entire local calendar day. The following local midnight closes eligibility. Refresh UI on date rollover and foreground return; recheck the final purchase/add-instance mutation before changing tokens or occupancy.
- Ownership and already-saved placements persist after the window closes. Existing forests continue to render their saved objects, locations and pack selections. Closing a season does not delete or hide placed objects.
- Owning an item does not bypass a restricted new-placement window. Historical plot dates, Chronoshift appearances and selected art packs do not replace the actual eligibility date.
- Proposed automatic selection: eligible owned/enabled Christmas takes priority during December 1–25; from December 26, resolve eligible owned Winter, otherwise the existing default/monthly appearance. Preserve existing saved-day, manual and Chronoshift behavior. This is a native resolver requirement, not a promise that older app builds already implement it.
- The current runtime schema supports an item `window` with `start` and `end`; it has no separate supported item planting-window flag. Native eligibility logic must apply it to every restricted new-placement route. Do not put planning-only fields such as `restrictEveryNewPlacement`, `inclusive` or `approved` inside runtime catalog windows.
- Missing or malformed windows for restricted keys must fail closed. Catalog validation checks date shape and real month/day values; it does not verify the iOS Store, Inventory or final placement behavior.

## Evidence

Primary recorded sources: `ChristmasPlanning/Christmas-Content-Proposal.json` (`packProposal`, `newObjectProposals`, `preservedSeasonalWindows`, `futureFeaturesRows`); `Mystic-Forest-Object-Register.json`; the Winter Wave 2 `manifest.json` (`availabilityProposal`, `catalogWindow`); and `handoffs/seasonal-planting/SEASONAL_PLANTING_XCODE_HANDOFF.md`.

Repository rules and the audited catalog are available at the [PR #14 commit](https://github.com/pierceh2/MysticForest-Content/tree/99ad32feac650a009e13a0bacf2039fc514c4c57). Native application enforcement was not verified in this audit.
