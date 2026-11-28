# Approved Christmas art delivery

This delivery adds the owner-approved Christmas artwork without production activation. It is stacked on open draft PR14 so the Frostbloom and Snow Lantern Circle base keys already exist. The [approval receipt](../../handoffs/christmas-2026/approval.json) covers all 25 frozen native PNGs.

## Contents and supported changes

- New disabled `christmas` pack at revision 1 with eighteen runtime overrides: eleven generated festive skins and seven byte-identical Winter copies.
- Three disabled 2×2 landmarks at spriteRevision 1: `present_pile`, `santa_chimney`, `santa_sleigh`, with intrinsic holiday base sprites.
- Four Animal pilot files installed separately: Christmas Fox/Hare, copied Winter Cow, and base Reindeer. These do not appear in changes.json or the runtime tree/landmark grid.
- Updated coverage, Xcode calendar/class-gate handoff, per-asset approval/provenance and existing Settings → Future Features records.

`changes.json` lists exactly the 21 runtime PNGs duplicated under this delivery's sprites folder. The four Animal files are recorded in the approval receipt and live only in the Animals pilot folder. No earlier native PNG or catalog entry is replaced, renamed or deleted.

## Placeholder dates and prices

The Christmas pack carries the proposed inclusive annual window December 1–25, tokenPrice 10 and buyOnlyInSeason true. Each new monument carries the same proposed window and tokenPrice 4, using the existing defaults of 8 tokens to unlock and 4 per placement. **These are documented staging placeholders; final release settings are not approved. All four runtime additions remain disabled.** Reindeer has no production price or catalog entry; its December 1–25 dates remain a pilot proposal.

When those release decisions are settled, the monument/Reindeer window must restrict purchase and every new placement, including owned objects, through the native final mutation check. The candidate close is December 26 at 00:00 local time. Ownership and old placements persist. A Christmas skin never extends an underlying object's window, grants it or bypasses Familiars/Village. Existing approved Winter dates/economy and PR14's pending Wave 2 conditions remain unchanged.

## Coverage and native limits

Christmas directly covers 18 of the branch's 29 runtime items. Eleven deliberate exclusions use default art: five unavailable harvest/Halloween objects, three base-only veins, and the three intrinsic Christmas monuments. All other old pack coverage is preserved; new monuments intentionally use default art in those packs. Animal coverage remains separate.

The selected Pine is v3 with mixed lights, tinsel and three gifts; Oak and Birch use their approved v2 treatments. Native format checks and exact hashes pass without repainting. Fine Pine light/tinsel detail reduces to colored pixels, the Hare eye is less distinct and the Reindeer eye/bell simplify at native resolution. Native Day/World fidelity, calendar enforcement, class gates and cache behavior remain unverified. See the [Xcode handoff](../../handoffs/christmas-2026/XCODE_HANDOFF.md).

Merge PR14 first, then retarget this draft to main and rerun checks. The owner handles merges. This delivery does not activate Christmas or alter the authorized Winter activation patch.
