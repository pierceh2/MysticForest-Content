# Christmas artwork and calendar handoff for Xcode

The owner approved all Christmas artwork. The approved 25 native PNG bytes are frozen in [approval.json](approval.json). Christmas release dates, prices and acquisition are still proposals. The disabled entries carry documented placeholder settings in [release-configuration.json](release-configuration.json); keep them disabled until decisions and native verification are complete. Do not include Christmas in the earlier authorized four-key Winter activation patch.

## Dependency and content model

This content draft is stacked on open, unmerged PR14 (`feature/winter-wave2-approved-art`, head `99ad32feac650a009e13a0bacf2039fc514c4c57`). Frostbloom and Snow Lantern Circle base keys come from that branch, as does the Fox base pilot. Merge PR14 first, retarget the Christmas draft to main, refresh dependencies and rerun checks before merging Christmas. Do not duplicate registrations or rename keys.

Christmas uses eighteen tree/landmark overrides. Present Pile, Santa Chimney and Santa Sleigh are new disabled 2×2 landmarks in default8bit, each at spriteRevision 1. The Christmas pack starts at revision 1. Existing item revisions and all earlier pack revisions remain unchanged. Seven Winter overrides are copied exactly into Christmas because the resolver falls back to default8bit, not Winter. Four Animal sprites remain under pilots/animals; do not add an unsupported animals collection or disguise animals as trees.

## Purchase, planting and end dates

The recorded Christmas proposal is December 1 through December 25, inclusive and annual. It opens at 00:00 local time on December 1 and closes at 00:00 local time on December 26. Christmas pack purchase is seasonal (`buyOnlyInSeason: true`); its candidate automatic appearance window is the same. The three intrinsic Christmas monuments have that same proposed window for purchase and **every new placement**, including owned objects. Their default Christmas art does not require owning the appearance pack. Reindeer has the same proposed window in pilot metadata, with no price or live catalog entry.

All new runtime entries remain disabled. Their catalog tokenPrice values are standard placeholders: pack 10, monuments 4 each (effective 8-token unlock and 4-token placement). `artworkApproved: true` does not mean `releaseSettingsApproved: true`. Do not activate or finalize prices/dates from the art approval alone.

Use the **actual local device date at the time of the final action**. An old plot's saved date, selected pack, manual skin or a previously open menu must not bypass eligibility. Once release rules are approved, share one authoritative eligibility service across Store, Inventory, preview and mutation. Check enabled state, valid current window, category gate, item ownership, balance and free footprint before changing any token, item or occupancy state. Recheck after midnight or app resume. Reject failures atomically. A malformed required window must fail closed.

Preserve permanent ownership and existing saved placements when the window closes. Continue rendering old Christmas scenes even while new purchases and placements are unavailable. Unowned objects should be hidden outside their purchase window; owned unavailable objects follow the native inventory convention with planting disabled and a clear seasonal date. Do not erase old objects, refund or charge tokens on calendar rollover.

## Existing windows and base access remain authoritative

- Apple Tree and Hay Bale Stack remain October 1–December 1 inclusive. Their Christmas Winter-copy appearances cover the December 1 overlap and rendering of saved scenes; they do not permit new placement on December 2.
- Pumpkin and Scarecrow remain October 1–November 30; Jack-o'-Lantern October 1–31; Corn Stalks and Harvest Table November 15–30. Their Christmas override exclusions do not remove old placements.
- Snowman, Winterberry Bush, Frost Obelisk and Snow Hare keep the approved December 1–February 28 window. February 29 is outside it. Snow Hare still requires Animals/Familiars support and unresolved acquisition/economy.
- Frostbloom, Snow Lantern Circle and Arctic Fox keep PR14's pending base release dates and acquisition; December 1–February 28 remains a proposal, not a configured runtime window for the two catalog entries.
- Cherry Blossom, Village Hut and the veins retain their existing unresolved acquisition gates and disabled state. Christmas pack ownership never grants these objects or earns their gates.

## Animals and Familiars

Keep Cow, Fox, Hare and Reindeer in the future Animal type with separate Store and Inventory sections, one-cell foreground occupancy, persistence and rendering. Familiars remains undecided between a spell and achievement, with no stable earning condition. Missing, unknown or unearned gates hide both sections and all purchase/placement entry points; preserve rendering of already-saved animals. Reindeer is an intrinsic holiday base, independent of Christmas-pack ownership. None of these pilot files creates a production entitlement. Ground may sit beneath foreground animals; Terraforming is a separate gate.

## Appearance, scale and quiet ground

Verify the native resolver before release. The proposed automatic order is an eligible owned+enabled Christmas pack over eligible Winter during the holiday, then eligible Winter or existing default/monthly appearance after Christmas. Preserve established manual/Chronoshift, saved-day and offline behavior; record the verified behavior rather than silently changing it. Every object retains its own purchase/placement constraints regardless of appearance.

Use full 32×48 tree/animal and 64×96 landmark canvases, nearest-neighbor rendering, existing anchors and 2:1 isometric projection. Do not upscale source PNGs to compensate for a display bug. Preserve quiet monthly ground and macro-forest edge continuity; this delivery adds no biome or ground-color changes. The new landmarks need 2×2 atomic occupancy checks before spending tokens.

## Native acceptance before any activation

1. Inspect Day and close/distant macro Forest views with the same keys and positions across base, Winter and Christmas. Verify scale, ground contact, depth order, missing-override fallback, cache revisions, old saves and offline reload.
2. Inspect Pine lights/gifts, connected snowy branches, Frostbloom buds, lantern candles, all monument silhouettes and complete sleigh runners. At 32×48 the Hare eye is less distinct, and Reindeer eye/bell details simplify; review the actual native pixels. Source concepts do not prove native fidelity.
3. Exercise November 30, December 1, December 25, December 26, January dates, February 28, leap-day February 29 and March 1 under each base object's own rule. Include owned/unowned, enabled/disabled, missing gates, stale menus, historical plots, midnight rollover, app resume and offline state.
4. Verify blocked 2×2 placement and every failed eligibility check leaves balances, ownership, occupancy and saved placements unchanged. Existing placements still render after close dates and while class menus are hidden.
5. Update the existing Settings → Future Features tab from the repository roadmap by stable ID or meaning. Show approved artwork separately from pending native implementation/release; never grant content by opening Settings. Preserve unrelated roadmap rows and avoid duplicate tabs.

Record build/simulator evidence before claiming app verification. Repository validation, image-format checks and art approval alone do not establish native integration or calendar enforcement.

The [complete date audit](DATE_WINDOWS.md) and [structured audit](date-audit.json) preserve all 31 recorded subjects and their approval states. The audit describes the pre-publication snapshot; the supported Christmas proposals are now configured in the disabled entries described above.
