# Approved Forest release settings

The owner approved the recommended settings for exactly six supported runtime entries. These business decisions are complete; native verification and owner-managed merges remain separate.

| Content | Annual inclusive purchase window | Unlock tokens | Placement tokens | Acquisition |
| --- | --- | ---: | ---: | --- |
| Christmas appearance pack | December 15–30 | 10 once | — | Ordinary seasonal pack purchase |
| Present Pile | December 15–30 | 8 | 4 | Ordinary seasonal store purchase |
| Santa Chimney | December 15–30 | 8 | 4 | Ordinary seasonal store purchase |
| Santa Sleigh | December 15–30 | 8 | 4 | Ordinary seasonal store purchase |
| Frostbloom Tree | December 1–February 28 | 3 | 1 | Ordinary seasonal store purchase |
| Snow Lantern Circle | December 1–February 28 | 8 | 4 | Ordinary seasonal store purchase |

The five objects obey the same dates for **every new placement, including already-owned objects**. Christmas automatic appearance uses December 15–30, closing December 31 at 00:00 local time. Winter ends February 28; February 29 is excluded. Use actual local device date, preserve ownership and saved placements, and reject an ineligible final mutation before changing tokens or occupancy. No extra spell/achievement is required for these five ordinary store objects, and their base artwork does not require an appearance pack.

**All six entries remain disabled pending native verification.** No art, art revision, numeric price or existing enabled flag changes in this metadata update. Frostbloom and Snow Lantern gain their approved catalog windows. The earlier held Christmas date edits are included in the same commit. Their numeric prices were already staged and are now approved.

Animals remain deferred: no Animals collection, economy, acquisition grant or Familiars implementation is approved here. Arctic Fox does not acquire an approved date window. Reindeer keeps its earlier December 15–30 date-only approval, and Snow Hare keeps its earlier Winter dates; both still have unresolved animal release conditions. Keep Animal menus/actions hidden while Familiars is missing, unknown or unearned, and retain saved animal rendering.

The [structured approval](approval.json) is authoritative for this scope. Historical artwork and date-only receipts remain unchanged; this record supplies later business decisions. The [Christmas Xcode handoff](../christmas-2026/XCODE_HANDOFF.md), [Winter Wave 2 handoff](../../pilots/winter_objects_wave2/XCODE_HANDOFF.md) and [shared seasonal contract](../seasonal-planting/SEASONAL_PLANTING_XCODE_HANDOFF.md) define native acceptance.

PR15 remains stacked on unmerged PR14. Merge the dependency first, then retarget PR15 to main and rerun checks. This content commit does not merge either PR or activate production. Once native checks pass, use these approved business decisions without asking the owner to approve the same dates or prices again.
