# Approved Christmas artwork and dates — disabled staging

The owner approved all Christmas artwork, then explicitly selected **December 15–30 inclusive** for the Christmas pack and Christmas-only items. The [date decision](date-decision.json) records that instruction. The historical [artwork approval](approval.json) preserves all 25 native hashes and remains unchanged. **Dates, artwork, supported-object prices and ordinary seasonal acquisition are approved. Native verification and activation remain pending. Animals remain deferred.**

This draft depends on the still-unmerged [Winter Wave 2 PR #14](https://github.com/pierceh2/MysticForest-Content/pull/14), at `99ad32feac650a009e13a0bacf2039fc514c4c57`. Merge that dependency first, then retarget this draft to main and rerun checks. Neither PR is merged by this handoff.

## Included content

Christmas has eighteen runtime overrides: eleven festive tree/landmark skins and seven exact Winter copies. Missing pack artwork falls back to default8bit, so the seven copies are explicit. Present Pile, Santa Chimney and Santa Sleigh have intrinsic Christmas default art and do not require appearance-pack ownership. Four additional files remain Animal pilots: Christmas Fox/Hare, the Winter Cow copy and the Reindeer base.

The selected Pine uses multicolored lights, tinsel and three small gifts; Oak uses gold tinsel; Birch has a silver-blue treatment. The Pine gifts remain part of its one-cell skin, distinct from the two-by-two Present Pile. All source/provenance hashes remain in the immutable approval record. No image or art revision changes in this date update.

## Approved dates, prices and acquisition

| Content | Approved annual inclusive window | Economy | State |
| --- | --- | --- | --- |
| Christmas appearance pack | December 15–30 for purchase and automatic appearance | 10 Forest tokens once | Disabled until native verification |
| Present Pile, Santa Chimney, Santa Sleigh | December 15–30 for purchase and every new placement, including owned objects | 8 unlock / 4 placement Forest tokens each | Disabled until native verification |
| Reindeer | December 15–30 for purchase and every new placement, including owned objects | Unset | Animal pilot; Familiars, acquisition, economy and native support pending |

The window opens at **00:00 local time on December 15** and closes at **00:00 local time on December 31**. December 30 is included in full. Ownership and saved placements persist. Use actual local device date at the final mutation, independently of the plot's date or appearance.

Christmas skins preserve the base object's eligibility. Apple Tree and Hay Bales still end December 1, so they have **no purchase/new-placement overlap with Christmas**. Their unchanged Christmas copies support saved/manual rendering only. Harvest Table remains November 15–30. Winter and its approved winter-only objects retain December 1–February 28; Frostbloom and Snow Lantern Circle now have approved ordinary Winter-store release settings in [the scoped approval](../forest-release-2026/approval.json); Arctic Fox retains pending animal release conditions.

The [release configuration](release-configuration.json) records approved dates, prices and ordinary seasonal acquisition for the pack and three supported monuments, while keeping Animal release settings deferred. All four supported Christmas entries remain disabled; Reindeer remains outside the runtime catalog. The current [date audit](DATE_WINDOWS.md), [structured audit](date-audit.json), [Xcode handoff](XCODE_HANDOFF.md) and [delivery](../../deliveries/delivery-2026-11-28-christmas/README.md) agree on these dates. No date approval is inferred for unrelated content.

The [current release approval](../forest-release-2026/approval.json) supersedes pending supported-business fields in earlier art/date-only receipts. Those historical receipts remain unchanged. No repeat approval is needed for these supported dates, prices or acquisition methods. Native acceptance and owner-managed merges remain separate.
