# Approved Christmas art delivery

This delivery adds the owner-approved Christmas artwork without production activation. It is stacked on open draft PR14 so the Frostbloom and Snow Lantern Circle base keys already exist. The [approval receipt](../../handoffs/christmas-2026/approval.json) covers all 25 frozen native PNGs.

## Contents and supported changes

- New disabled `christmas` pack at revision 1 with eighteen runtime overrides: eleven generated festive skins and seven byte-identical Winter copies.
- Three disabled 2×2 landmarks at spriteRevision 1: `present_pile`, `santa_chimney`, `santa_sleigh`, with intrinsic holiday base sprites.
- Four Animal pilot files installed separately: Christmas Fox/Hare, copied Winter Cow, and base Reindeer. These do not appear in changes.json or the runtime tree/landmark grid.
- Updated coverage, Xcode calendar/class-gate handoff, per-asset approval/provenance and existing Settings → Future Features records.

`changes.json` lists exactly the 21 runtime PNGs duplicated under this delivery's sprites folder. The four Animal files are recorded in the approval receipt and live only in the Animals pilot folder. No earlier native PNG or catalog entry is replaced, renamed or deleted.

## Approved supported release settings

The Christmas pack carries the owner-approved inclusive annual window December 15–30. The approved pack price is 10 Forest tokens once and buyOnlyInSeason stays true. Each monument carries the same approved window and owner-approved tokenPrice 4, using the existing defaults of 8 tokens to unlock and 4 per placement. **Dates, art, prices and ordinary seasonal acquisition are approved for these supported entries. All four remain disabled pending native verification.** Reindeer has the same approved December 15–30 window in pilot metadata, with no production price or live catalog entry.

The approved monument/Reindeer window must restrict purchase and every new placement, including owned objects, through the native final mutation check before release. It opens December 15 at 00:00 local time, includes all of December 30 and closes December 31 at 00:00 local time. Ownership and old placements persist. A Christmas skin never extends an underlying object's window, grants it or bypasses Familiars/Village. Existing Winter settings remain unchanged. The later scoped approval completes Frostbloom/Lantern Winter dates and ordinary seasonal prices, while Arctic Fox remains deferred.

## Coverage and native limits

Christmas directly covers 18 of the branch's 29 runtime items. Eleven deliberate exclusions use default art: five unavailable harvest/Halloween objects, three base-only veins, and the three intrinsic Christmas monuments. All other old pack coverage is preserved; new monuments intentionally use default art in those packs. Animal coverage remains separate.

The selected Pine is v3 with mixed lights, tinsel and three gifts; Oak and Birch use their approved v2 treatments. Native format checks and exact hashes pass without repainting. Fine Pine light/tinsel detail reduces to colored pixels, the Hare eye is less distinct and the Reindeer eye/bell simplify at native resolution. Native Day/World fidelity, calendar enforcement, class gates and cache behavior remain unverified. See the [Xcode handoff](../../handoffs/christmas-2026/XCODE_HANDOFF.md).

Merge PR14 first, then retarget this draft to main and rerun checks. The owner handles merges. This delivery does not activate Christmas or alter the authorized Winter activation patch.

The [Christmas date decision](../../handoffs/christmas-2026/date-decision.json) supersedes the original December 1–25 proposal. Apple Tree and Hay Bales still end December 1; their unchanged Christmas copies support saved/manual rendering, with no seasonal eligibility overlap. The [later scoped release approval](../../handoffs/forest-release-2026/approval.json) also approves the supported prices/acquisition and adds Frostbloom/Snow Lantern winter windows through a separate metadata-only delivery. No PNG, art revision, numeric price or enabled flag changes in that update.
