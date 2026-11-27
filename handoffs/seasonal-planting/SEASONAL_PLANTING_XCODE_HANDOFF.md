# Seasonal planting for five Mystic Forest items

Approved November 27, 2026.

## Required behavior

Pumpkin, Jack-o'-Lantern, Corn Stalks, Scarecrow and Apple Tree may be purchased and newly planted only during their individual catalog windows. Ownership persists between seasons. An owned item becomes eligible for planting again when its window reopens, subject to the app's ordinary placement rules.

| Item | Permanent key | Approved inclusive window |
| --- | --- | --- |
| Pumpkin | `pumpkin` | October 1–November 30 |
| Jack-o'-Lantern | `jack_o_lantern` | October 1–October 31 |
| Corn Stalks | `corn_stalks` | November 15–November 30 |
| Scarecrow | `scarecrow` | October 1–November 30 |
| Apple Tree | `apple_tree` | October 1–December 1 |

These dates are published in [catalog.json at the approved date change](https://github.com/pierceh2/MysticForest-Content/blob/cc0c78a50628a7ed93dad3ac113fdc5848bfc5ce/catalog.json). Resolve each item's current `window` from the synced catalog at runtime. This table records the approval snapshot.

## App integration

Use the same local-date provider and inclusive month/day evaluator as the Store purchase check. In the current content contract that means the device's actual local calendar date. Keep the restricted keys together in the shared planting eligibility logic. Reuse the current item, window and ownership models.

Evaluate the window for these five keys even when the item is already owned. Pack ownership, the rendered season, viewing a historical plot, and cosmetic Chronoshift selection supply appearance context. They do not substitute for the Store date used by this planting check.

Call the shared eligibility check from Inventory plant controls, placement previews, and every supported action that adds a new placed instance. Recheck immediately before committing the placement and spending its tokens, so a stale screen or a midnight rollover cannot complete an out-of-season planting. Return a clear out-of-season result before modifying balances or placements. Missing or invalid window data for a restricted key makes new planting unavailable until valid catalog data is restored.

For an owned item outside its window, show its seasonal availability through the app's existing disabled-action or locked-item treatment. Display the item's dates, for example “Plantable October 1–November 30.” Refresh eligibility on local date changes and when the app returns to the foreground.

Keep already saved trees in the forest and render them when their plots are opened. Loading, syncing, restoring or displaying an existing placement is distinct from adding a new instance. Route existing art regression scenes through the Debug saved-state restoration path. Their historical catalog snapshots provide art references. Use current production catalog dates for new planting eligibility checks.

## Verification in Xcode

- For each restricted key, check an owned item on the day before its window, its first day, its last day and the following day. Planting must fail outside the window and pass the seasonal check on both endpoints.
- Include Jack-o'-Lantern on October 31 and November 1, Pumpkin, Scarecrow and Corn Stalks on November 30 and December 1, and Apple Tree on December 1 and December 2.
- Attempt each supported placement action while the owned item is out of season. Confirm the authoritative placement operation rejects it before tokens or saved placements change.
- Open a placement screen while eligible, advance the injected clock to the next local date outside the window and attempt confirmation. Repeat after backgrounding and reopening the app.
- Reopen and sync a saved forest containing these items outside their windows. Confirm its existing objects still render and their ownership remains recorded.
- Verify ordinary year-round tree placement and the existing behavior of other objects. Exercise a historical plot and an appearance override while the actual Store date is outside the restricted item's window.
- Show the in-season and out-of-season Inventory and placement states in the simulator and report the app build and test results.

## Integration status

The purchase dates are on the content repository's main branch. The new planting restriction requires a native app change. The accessible content repository contains the catalog and sprites, while the iOS placement implementation and app target are in the ChronosKeep app repository.

This handoff is the approved implementation requirement. App implementation, build and simulator verification are pending. The current content catalog has no supported planting-window flag. Implement the shared app check using the existing item windows and these five approved keys.
