# Mystic Forest — approved release dates and economy

## Current approval

The owner approved the four recommendation rows covering Christmas pricing and the supported Winter Wave 2 objects, and approved keeping Animals deferred. The selected artwork was already approved. The supported settings below now require no repeat business approval.

This decision supersedes the prior local publication hold and earlier pending-price/date statements for these six supported keys. Historical approval receipts remain evidence of their original state. Use the separate final publication receipt to identify the actual PR #15 head, checks and merge state; this audit does not claim a remote mutation on its own.

## Approved supported content

| Content | Purchase window | New placement / automatic appearance | One-time unlock | Each new placement | Acquisition |
| --- | --- | --- | ---: | ---: | --- |
| Christmas appearance pack | December 15–30 | Automatic appearance: December 15–30; base-object placement follows its own rules | 10 tokens | Not applicable | Ordinary seasonal appearance-pack purchase |
| Present Pile | December 15–30 | Every new placement: December 15–30 | 8 tokens | 4 tokens | Ordinary seasonal Store purchase |
| Santa Chimney | December 15–30 | Every new placement: December 15–30 | 8 tokens | 4 tokens | Ordinary seasonal Store purchase |
| Santa Sleigh | December 15–30 | Every new placement: December 15–30 | 8 tokens | 4 tokens | Ordinary seasonal Store purchase |
| Frostbloom Tree | December 1–February 28 | Every new placement: December 1–February 28 | 3 tokens | 1 token | Ordinary seasonal Store purchase |
| Snow Lantern Circle | December 1–February 28 | Every new placement: December 1–February 28 | 8 tokens | 4 tokens | Ordinary seasonal Store purchase |

All prices use Forest tokens. No additional spell or achievement is required for these supported objects. The base objects do not require ownership of the Winter or Christmas appearance pack. Pack ownership grants appearances and does not grant the underlying objects.

All six entries remain **disabled pending native verification** in the current staging work. Business approval does not mean the iOS checks have passed or that production has been enabled. Frostbloom and Snow Lantern Circle now need their approved `12-01` through `02-28` windows in the catalog and inclusion in the shared seasonal purchase/new-placement policy.

## Calendar boundaries and persistence

All windows repeat annually and include both endpoints. Use the actual local device date, with a final check before changing tokens, inventory or occupancy. Already owning an object does not bypass its new-placement window.

| Date | Christmas date eligibility |
| --- | --- |
| December 14 | Outside |
| December 15 | Inside, first day |
| December 26 | Inside; catches the obsolete December 25 cutoff |
| December 30 | Inside through the full local day |
| December 31 | Outside from 00:00 local time |

The winter window wraps across New Year. November 30 is outside; December 1, December 31, January 1 and February 28 are inside. February 29 and March 1 are outside. The February 28 endpoint is unchanged and must not expand silently in leap years.

Ownership and existing saved placements persist after closing. Rendering or restoring an existing placement is not a new purchase or add-instance operation. Preserve saved positions, pack selections and historical day appearances. Stale UI, selected historical dates, Chronoshift appearance choices and timezone changes must not bypass the final current-date check.

Within December 15–30, verify eligible owned/enabled Christmas automatic priority over Winter. Before December 15 and beginning December 31, resolve eligible owned Winter, otherwise the existing default/monthly appearance. The Forest catalog is the authoritative date source; other rooms' Christmas dates do not change.

## Animals remain deferred

| Animal | Date status | Still unresolved |
| --- | --- | --- |
| Reindeer | December 15–30 is already approved for purchase and every new placement | Familiars, acquisition, prices and native Animals release |
| Snow Hare | December 1–February 28 is previously approved | Familiars, acquisition, prices and native Animals release |
| Arctic Fox | December 1–February 28 remains a proposal, not an approved window | Exact window, Familiars, acquisition, prices and native Animals release |
| Cow | No new date restriction assigned by this approval | Familiars, acquisition, prices and native Animals release |

No animal price or acquisition route is approved by the four recommendation rows. Do not assign Arctic Fox the approved Frostbloom/Lantern window merely because they originated in the same artwork group. Reindeer remains an animal pilot with no current runtime catalog entry. Approved animal artwork and date plans do not activate Familiars or the Animals category.

## Previously approved settings remain unchanged

- Winter appearance pack: December 1–February 28, 10 tokens once, ordinary seasonal purchase.
- Snowman and Winterberry Bush: December 1–February 28, 3 tokens to unlock and 1 per placement.
- Frost Obelisk: December 1–February 28, 8 tokens to unlock and 4 per placement.
- Apple Tree and Hay Bale Stack: October 1–December 1. Their Christmas-folder copies support saved or permitted manual rendering; Christmas begins after their placement window closes.
- Harvest Table and Corn Stalks: November 15–30; Pumpkin and Scarecrow: October 1–November 30; Jack-o'-Lantern: October 1–31.
- Ordinary year-round object rules and the separate Village, Terraforming, Classic Retro and vein-unlock backlog remain unchanged.

## Native verification and staging

Verify Day and macro-Forest art, scale, anchors, pixel sampling, cache revision handling, pack ownership/priority/fallback, saved scenes, shared Store/Inventory/final mutation eligibility, midnight/timezone refresh and atomic 2×2 placement. Use Debug fixtures to test disabled content; passing content-repository checks is not evidence of native behavior.

The current update stages approved settings on the authorized feature branch and draft PR workflow. It does not merge to main or turn on production entries before the native gates pass. Existing Winter Wave 1 activation authorization remains intact and does not need new price/date approval.
