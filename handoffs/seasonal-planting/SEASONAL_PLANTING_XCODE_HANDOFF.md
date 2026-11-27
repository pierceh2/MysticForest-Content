# Mystic Forest: seasonal purchase and new placement

Updated November 27, 2026. This is the current native implementation requirement for **seven existing seasonal keys and four Winter-only keys**. It supersedes the older five-key handoff and general statements that every owned seasonal object is plantable all year.

The content repository supplies the catalog, approved sprites and handoffs. It does not implement the iOS Store, Inventory, placement mutation or simulator target. Do not report this behavior as complete until verified in the native project.

## Approved windows

Use the device's actual local calendar date and inclusive recurring month/day windows. Resolve supported objects' current `window` from the synced catalog; the table records the owner's approved values. The Snow Hare window must be carried into the future supported animal model when that model is implemented.

| Object | Permanent key | Class | Purchase and new-placement window |
| --- | --- | --- | --- |
| Pumpkin | `pumpkin` | Tree | October 1–November 30 |
| Jack-o'-Lantern | `jack_o_lantern` | Tree | October 1–October 31 |
| Corn Stalks | `corn_stalks` | Tree | November 15–November 30 |
| Scarecrow | `scarecrow` | Tree | October 1–November 30 |
| Apple Tree | `apple_tree` | Tree | October 1–December 1 |
| Harvest Table | `harvest_table` | Landmark, 2×2 | November 15–November 30 |
| Hay Bale Stack | `hay_bales` | Landmark, 2×2 | October 1–December 1 |
| Snowman | `snowman` | Tree slot | December 1–February 28 |
| Winterberry Bush | `winterberry_bush` | Tree slot | December 1–February 28 |
| Frost Obelisk | `frost_obelisk` | Landmark, 2×2 | December 1–February 28 |
| Snow Hare | `snow_hare` | Future Animal | December 1–February 28 |

Year wrapping is required: December and January are within a December–February window. **February 29 is outside the approved window.** Do not silently extend it to the last day of February. The Hay Bale Stack and Apple Tree retain their individual approved December 1 endpoint; a related item's or pack's window does not replace it.

## Approved Winter release and economics

| Content | Acquisition | One-time purchase | Each new placement | Activation condition |
| --- | --- | ---: | ---: | --- |
| Winter appearance pack | Ordinary seasonal pack purchase, December 1–February 28 | 10 Forest tokens | Not applicable | Native art, pack-resolution, cache and saved-forest verification |
| Snowman | Ordinary seasonal item purchase, December 1–February 28 | 3 tokens | 1 token | Native visual and seasonal purchase/new-placement verification |
| Winterberry Bush | Ordinary seasonal item purchase, December 1–February 28 | 3 tokens | 1 token | Native visual and seasonal purchase/new-placement verification |
| Frost Obelisk | Ordinary seasonal item purchase, December 1–February 28 | 8 tokens | 4 tokens | Native visual and seasonal purchase/new-placement verification |
| Snow Hare | Familiars access remains unresolved; Winter window approved | Undecided | Undecided | Animal support, Familiars definition and acquisition decisions, plus native checks |

The first four rows' dates, acquisition and prices are approved. Their disabled state is a deployment gate while the listed native checks remain unverified; it is not a request for another owner decision. After successful checks, carry out the authorized activation procedure in the current Winter handoff and run the repository checks. Do not enable Snow Hare or the separate Cow/Familiars pilot as part of that activation.

The three supported Winter objects use base sprites and do not require the Winter appearance pack. Pack ownership grants appearances, not object ownership or an exemption from object placement windows. An owned pack stays owned under the existing pack contract.

## Shared native eligibility

1. Reuse one local-date provider and one inclusive month/day evaluator for seasonal purchase and new-placement eligibility. A range whose start is later than its end wraps through New Year. Use calendar components, not elapsed seconds or a historical plot's date.
2. Apply the seasonal check to all eleven keys above even when already owned. Native support, enabled state, access gates, ownership, available currency and footprint rules remain separate prerequisites. Missing or invalid window data for a restricted key makes new purchase/placement unavailable until valid data is restored.
3. Drive Store, Inventory actions and placement previews from the same result. Show owned out-of-season items through the app's normal disabled-action treatment with their availability dates. Preserve the category visibility rules for unresolved/unearned Familiars and Terraforming.
4. Recheck in every authoritative purchase or add-instance operation immediately before changing tokens, inventory or saved placements. A stale screen, date rollover or concurrent request must not bypass the restriction. Reject a 2×2 landmark before reserving any of its four cells. A rejected action must leave balances and the full saved occupancy unchanged.
5. Refresh date-sensitive UI on local midnight, foreground return and relevant catalog changes. Keep the action-level check authoritative even if the UI has not refreshed.

Current content schema has no supported per-item planting-window flag. Reuse existing catalog windows and keep the restricted key set together in native eligibility logic. Do not add unsupported runtime JSON fields to simulate enforcement. When an animal schema is supported, route Snow Hare through the same eligibility service and its independent Familiars prerequisite.

Appearance context does not replace eligibility time. A saved historical date, Chronoshift appearance choice, owned seasonal pack, Winter reskin on another object or selected macro-forest plot must not allow an out-of-season new placement.

## Preserve existing forests

Ownership persists when a window closes and the owned item becomes eligible again when its window reopens. Loading, syncing, restoring and rendering an existing saved placement are distinct from creating a new instance. Preserve saved keys, locations, footprints, balances and pack selections. Do not delete or hide existing trees, landmarks or animals when their purchase season ends.

Use Debug saved-state fixtures for historical art review. They may restore already saved scenes containing disabled or out-of-season objects without changing production entitlements. They must not expose an unrestricted production purchase or add-instance route.

## Required Xcode verification

- Exercise every restricted key on the day before its window, the first day, the final day and the following day. Both endpoints pass the seasonal check; both outside dates fail. Other prerequisites must be satisfied through an appropriate test fixture.
- Explicitly cover Jack-o'-Lantern on October 31/November 1; Pumpkin, Scarecrow, Corn Stalks and Harvest Table on November 30/December 1; Apple Tree and Hay Bale Stack on December 1/December 2.
- Cover each Winter key on November 30/December 1, December 31/January 1, February 28/March 1, and February 28/February 29/March 1 in a leap year. February 29 must fail.
- Repeat with already owned items, all supported new-instance entry points, historical plots and appearance overrides. Leave an eligible placement screen open across the closing midnight and confirm rejection at commit. Repeat after backgrounding/foregrounding.
- Confirm rejected purchases and placements spend no tokens, add no inventory, reserve no cells and write no partial placement. Include a 2×2 landmark and missing/invalid window fixtures.
- Reopen, sync and restore saved forests outside the objects' windows. Confirm all existing objects still render, ownership persists, and ordinary year-round content follows its existing rules.
- Verify Winter sprites at native scale in Day and macro Forest views: intact canvases, nearest-neighbor rendering, correct feet/bases, consistent scale, layering, missing-override fallback, cache revision refresh and retained saved-day appearance behavior.
- Keep Snow Hare's production path unavailable while Familiars is undecided. Test its date eligibility in an explicit development fixture without granting live access.

Record the app commit/build, tested dates, simulator captures, check results and any remaining failures. Passing content validation alone does not establish native behavior. The approved Winter pack and three supported objects can proceed through authorized activation after their relevant checks pass; other unresolved unlocks remain pending.

## Related handoffs

- [Winter objects and activation status](../../pilots/winter_objects/XCODE_HANDOFF.md)
- [Settings → Future Features](../rewards-collections/FUTURE_FEATURES_HANDOFF.md)
- [Runtime catalog](../../catalog.json)
