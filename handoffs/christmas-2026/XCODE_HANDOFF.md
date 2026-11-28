# Christmas artwork and calendar handoff for Xcode

The owner approved all Christmas artwork. The approved 25 native PNG bytes are frozen in [approval.json](approval.json). Christmas dates are now approved as December 15–30 inclusive, recorded in [date-decision.json](date-decision.json). The owner also approved the pack at 10 tokens once and each monument at 8 tokens to unlock / 4 per placement through ordinary seasonal purchases. The [scoped release approval](../forest-release-2026/approval.json) completes these supported business decisions. Keep entries disabled until native verification passes; Animals remain deferred. Do not include Christmas in the earlier authorized four-key Winter activation patch.

## Dependency and content model

This content draft is stacked on open, unmerged PR14 (`feature/winter-wave2-approved-art`, head `99ad32feac650a009e13a0bacf2039fc514c4c57`). Frostbloom and Snow Lantern Circle base keys come from that branch, as does the Fox base pilot. Merge PR14 first, retarget the Christmas draft to main, refresh dependencies and rerun checks before merging Christmas. Do not duplicate registrations or rename keys.

Christmas uses eighteen tree/landmark overrides. Present Pile, Santa Chimney and Santa Sleigh are new disabled 2×2 landmarks in default8bit, each at spriteRevision 1. The Christmas pack starts at revision 1. Existing item revisions and all earlier pack revisions remain unchanged. Seven Winter overrides are copied exactly into Christmas because the resolver falls back to default8bit, not Winter. Four Animal sprites remain under pilots/animals; do not add an unsupported animals collection or disguise animals as trees.

## Purchase, planting and end dates

The approved Christmas window is December 15 through December 30, inclusive and annual. It opens at 00:00 local time on December 15 and closes at 00:00 local time on December 31. December 30 is included in full. Christmas pack purchase remains seasonal (`buyOnlyInSeason: true`); its approved automatic appearance window is the same. Present Pile, Santa Chimney and Santa Sleigh use that approved window for purchase and **every new placement**, including owned objects. Their intrinsic Christmas art does not require the appearance pack. Reindeer has the same approved window in pilot metadata, with no price or live catalog entry.

All new runtime entries remain disabled. Their approved catalog tokenPrice values stay unchanged: pack 10, monuments 4 each (effective 8-token unlock and 4-token placement). Release-settings approval is complete for the pack and three supported monuments. No extra unlock is required for these ordinary seasonal-store objects. Reindeer/other animal prices, acquisition and Familiars remain pending, and no production activation occurs in this commit.

Use the **actual local device date at the time of the final action**. An old plot's saved date, selected pack, manual skin or a previously open menu must not bypass eligibility. Implement the approved rules through one authoritative eligibility service shared by Store, Inventory, preview and mutation. Check enabled state, valid current window, category gate, item ownership, balance and free footprint before changing any token, item or occupancy state. Recheck after midnight or app resume. Reject failures atomically. A malformed required window must fail closed.

Preserve permanent ownership and existing saved placements when the window closes. Continue rendering old Christmas scenes even while new purchases and placements are unavailable. Unowned objects should be hidden outside their purchase window; owned unavailable objects follow the native inventory convention with planting disabled and a clear seasonal date. Do not erase old objects, refund or charge tokens on calendar rollover.

## Existing windows and base access remain authoritative

- Apple Tree and Hay Bale Stack remain October 1–December 1 inclusive. There is no eligibility overlap with Christmas December 15–30. Their unchanged Christmas copies support saved/manual rendering and never extend purchase or new-placement eligibility past December 1.
- Pumpkin and Scarecrow remain October 1–November 30; Jack-o'-Lantern October 1–31; Corn Stalks and Harvest Table November 15–30. Their Christmas override exclusions do not remove old placements.
- Snowman, Winterberry Bush, Frost Obelisk and Snow Hare keep the approved December 1–February 28 window. February 29 is outside it. Snow Hare still requires Animals/Familiars support and unresolved acquisition/economy.
- Frostbloom Tree and Snow Lantern Circle now have approved December 1–February 28 purchase/every-new-placement windows and ordinary seasonal-store prices of 3/1 and 8/4. They stay disabled pending native checks. Arctic Fox remains a separate deferred Animal pilot; its dates/acquisition/economy are not approved here.
- Cherry Blossom, Village Hut and the veins retain their existing unresolved acquisition gates and disabled state. Christmas pack ownership never grants these objects or earns their gates.

## Animals and Familiars

Keep Cow, Fox, Hare and Reindeer in the future Animal type with separate Store and Inventory sections, one-cell foreground occupancy, persistence and rendering. Familiars remains undecided between a spell and achievement, with no stable earning condition. Missing, unknown or unearned gates hide both sections and all purchase/placement entry points; preserve rendering of already-saved animals. Reindeer is an intrinsic holiday base, independent of Christmas-pack ownership. None of these pilot files creates a production entitlement. Ground may sit beneath foreground animals; Terraforming is a separate gate.

## Appearance, scale and quiet ground

Verify the native resolver before release. The native resolver should select eligible owned+enabled Christmas over eligible Winter during the approved December 15–30 holiday window, then eligible Winter or existing default/monthly appearance from December 31. The date decision does not authorize a change to established manual/saved-day behavior. Preserve established manual/Chronoshift, saved-day and offline behavior; record the verified behavior rather than silently changing it. Every object retains its own purchase/placement constraints regardless of appearance.

Use full 32×48 tree/animal and 64×96 landmark canvases, nearest-neighbor rendering, existing anchors and 2:1 isometric projection. Do not upscale source PNGs to compensate for a display bug. Preserve quiet monthly ground and macro-forest edge continuity; this delivery adds no biome or ground-color changes. The new landmarks need 2×2 atomic occupancy checks before spending tokens.

## Native acceptance before any activation

1. Inspect Day and close/distant macro Forest views with the same keys and positions across base, Winter and Christmas. Verify scale, ground contact, depth order, missing-override fallback, cache revisions, old saves and offline reload.
2. Inspect Pine lights/gifts, connected snowy branches, Frostbloom buds, lantern candles, all monument silhouettes and complete sleigh runners. At 32×48 the Hare eye is less distinct, and Reindeer eye/bell details simplify; review the actual native pixels. Source concepts do not prove native fidelity.
3. Exercise December 14 (Christmas closed), December 15 (open), December 30 (open through the full local day) and December 31 (closed from 00:00). Also exercise November 30, December 1–2, January dates, February 28, leap-day February 29 and March 1 under each base object's unchanged rule. Include owned/unowned, enabled/disabled, missing gates, stale menus, historical plots, midnight rollover, app resume and offline state.
4. Verify blocked 2×2 placement and every failed eligibility check leaves balances, ownership, occupancy and saved placements unchanged. Existing placements still render after close dates and while class menus are hidden.
5. Update the existing Settings → Future Features tab from the repository roadmap by stable ID or meaning. Show approved artwork separately from pending native implementation/release; never grant content by opening Settings. Preserve unrelated roadmap rows and avoid duplicate tabs.

Record build/simulator evidence before claiming app verification. Repository validation, image-format checks and art approval alone do not establish native integration or calendar enforcement.

The [complete date audit](DATE_WINDOWS.md) and [structured audit](date-audit.json) cover all 31 recorded subjects. They record the approved Christmas dates and newly approved Frostbloom/Snow Lantern settings, preserving unrelated approval states. Supported prices/acquisition are now approved by the current release record. Native activation and all Animal release conditions remain pending.
