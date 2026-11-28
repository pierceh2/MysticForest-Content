# Winter Wave 2 — approved supported release settings

Frostbloom Tree and Snow Lantern Circle have approved artwork, ordinary seasonal-store acquisition, dates and prices. Frostbloom is **3 tokens to unlock / 1 per placement**; Snow Lantern Circle is **8 / 4**. Both use **December 1–February 28 inclusive, annually**, for purchase and **every new placement, including when already owned**. No additional spell or achievement is required. Their intrinsic base art does not require Winter-pack ownership.

The [current release approval](../../handoffs/forest-release-2026/approval.json) supplies these later decisions; the original art approval is preserved. The [manifest](manifest.json) records current catalog windows and per-item approved economy. Both runtime entries remain disabled at spriteRevision 1 pending native checks. This commit changes no artwork. These business decisions need no repeat approval.

## Arctic Fox remains separate

Arctic Fox is an approved art pilot only at `pilots/animals/sprites/default8bit/arctic_fox.png`. The latest approval does not settle its dates, acquisition, prices or Familiars. December 1–February 28 remains a proposal for Fox, not an approved window. Preserve its null catalog entry and pending economy. Never map it to trees merely because its canvas is 32×48.

Keep all Animals behind the future Animal type and unresolved Familiars spell/achievement. Hide Store/Inventory sections and actions while the gate is missing, unknown or unearned; preserve saved animal rendering. Reindeer has earlier date-only approval and Snow Hare has earlier Winter dates, but their animal release conditions remain deferred.

## Native acceptance

1. Inspect the approved full canvases in Day and close/distant macro Forest with nearest-neighbor rendering and unchanged anchors. Check connected Frostbloom branches/buds and four readable candle windows in the lantern circle. Do not enlarge source files to compensate for app scaling.
2. Include both supported keys in the shared seasonal eligibility service at Store, Inventory, placement preview and final mutation. Evaluate actual local device date, valid window, enabled state, ownership, balance and footprint before any token/occupancy mutation. Owned objects, old plot dates, Chronoshift and selected appearance cannot bypass dates.
3. Exercise November 30, December 1, New Year, February 28, leap-day February 29 and March 1. February 29 is excluded. Recheck at midnight, time-zone changes and foreground return; reject atomically on any invalid or closed eligibility.
4. Preserve ownership and existing placements outside the window. Verify 2×2 occupancy for the Lantern Circle, full-canvas art across base/Winter/Christmas, missing overrides, offline reload and existing saved keys/positions.
5. After native checks pass, use the approved prices and dates without further business approval. Keep Animals out of supported-content activation. The older four-key Winter activation patch is unchanged; this handoff does not activate either new entry or merge content.

Port the updated [Future Features records](../../handoffs/rewards-collections/MysticForest-FutureFeatures.json) into the existing Settings tab by native ID or meaning. Mark these supported business decisions complete while showing native work as pending. Keep Fox/Familiars unresolved and preserve all unrelated roadmap rows.
