# Approved Christmas artwork — disabled staging

The owner approved all Christmas artwork on November 28, 2026. The [approval record](approval.json) identifies every one of the 25 approved native PNGs and preserves its SHA-256. Artwork approval is complete. **Exact release dates, acquisition and prices remain proposals; no production activation is authorized.**

This draft is based on the still-unmerged [Winter Wave 2 PR #14](https://github.com/pierceh2/MysticForest-Content/pull/14), at `99ad32feac650a009e13a0bacf2039fc514c4c57`. Merge that dependency first, then retarget this draft to main and rerun checks. No part of this handoff merges either PR.

## Included content

Christmas has eighteen runtime overrides: eleven new festive tree/landmark skins and seven exact Winter copies. Missing pack artwork falls back to default8bit, so the seven copies are explicit. Three new monuments have intrinsic Christmas default art: Present Pile, Santa Chimney and Santa Sleigh. The monument pack is not an ownership requirement. Four additional files remain Animal pilots: Christmas Fox and Hare skins, the exact Winter Cow copy, and the Reindeer base.

The selected Pine uses multicolored lights, tinsel and three small gifts; Oak uses gold tinsel; Birch uses a silver-blue treatment. The small Pine gifts belong to its one-cell skin and remain distinct from the two-by-two Present Pile. The approved source bundle is `Mystic-Forest-Christmas-Art-Review.zip`; its hash and all source-concept/prompt references are retained in approval.json. Source concepts are provenance artifacts, not runtime sprites.

## Dates and prices recorded for later release

| Content | Recorded candidate window | Candidate economy | Current state |
| --- | --- | --- | --- |
| Christmas appearance pack | December 1–25 inclusive for purchases and automatic appearance | 10 Forest tokens once | Disabled; dates/price are placeholders |
| Present Pile, Santa Chimney, Santa Sleigh | December 1–25 inclusive for purchase and every new placement | 8 unlock / 4 placement tokens each | Disabled; dates/economy are placeholders |
| Reindeer | December 1–25 inclusive, proposed for purchase and every new placement | Unset | Animal pilot; Familiars and release settings pending |

The candidate holiday closes at **00:00 local time on December 26**. Ownership and saved placements persist. Christmas skins do not extend base-object windows: Apple Tree and Hay Bales retain their December 1 endpoint, Harvest Table remains November 15–30, and the approved Winter objects retain December 1–February 28. Frostbloom, Snow Lantern Circle and Arctic Fox still have pending base release settings under PR14.

The supported catalog contains the proposed windows and standard placeholder prices while all four new runtime entries remain disabled. Reindeer has no runtime catalog entry. The [structured release record](release-configuration.json) distinguishes configured placeholders from approved decisions. A calendar field alone does not implement placement restrictions in the app.

Use the [Xcode handoff](XCODE_HANDOFF.md) for gates, final mutation checks, appearance priority and native acceptance. Use the [delivery](../../deliveries/delivery-2026-11-28-christmas/README.md) for the exact catalog and sprite changes.

The [complete date audit](DATE_WINDOWS.md) and [structured audit](date-audit.json) preserve all 31 recorded subjects and their approval states. The audit describes the pre-publication snapshot; the supported Christmas proposals are now configured in the disabled entries described above.
