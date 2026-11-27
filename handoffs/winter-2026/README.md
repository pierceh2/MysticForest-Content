# Approved Winter release and content integration

The owner approved these decisions on **November 27, 2026**. This integration includes the approved Ground, Cow, Cherry Blossom and three mineral-vein work from PRs #3–#7, alongside the Winter art and winter-only objects already published. The exact source heads are recorded in [approval.json](approval.json).

## Settled release decisions

| Content | Dates, inclusive every year | One-time unlock | Per placement | Acquisition |
| --- | --- | ---: | ---: | --- |
| Winter reskin pack | December 1–February 28 | 10 Forest tokens | — | Ordinary seasonal pack purchase |
| Snowman | December 1–February 28 | 3 Forest tokens | 1 token | Ordinary seasonal item purchase |
| Winterberry Bush | December 1–February 28 | 3 Forest tokens | 1 token | Ordinary seasonal item purchase |
| Frost Obelisk | December 1–February 28 | 8 Forest tokens | 4 tokens | Ordinary seasonal item purchase |

The three objects use their snowy default sprites and do not require the Winter pack. Their purchase and every new placement use the actual local date, including when already owned. The exact February 28 endpoint excludes February 29. Retain ownership and saved placements when a window closes.

Winter is now revision **3** because the approved Winter Cherry Blossom override is included. Its catalog window is configured and its price is approved. Winter and these three objects remain disabled until the native checks below pass. This is a technical activation condition; **no further approval of the dates, prices or ordinary acquisition is required**.

## Authorized activation after native verification

1. Read the current app source and confirm the native target and installed-app compatibility. Content-only changes cannot establish placement enforcement or update an older installed app's code.
2. Verify Refined/default and Winter rendering on the full native canvases in Day and macro Forest, including anchors, nearest-neighbor sampling, ground contact, shadows and depth sorting. Use Debug fixtures for disabled content.
3. Implement or verify the [seasonal rules](../seasonal-planting/SEASONAL_PLANTING_XCODE_HANDOFF.md) in Store, Inventory, previews and the final purchase/add-instance action. Test endpoints, year wrapping, February 29, owned items, historical plots and UI left open across midnight. Rejection must preserve currency and occupancy; saved objects must keep rendering.
4. Verify the approved price table, Winter pack entitlement/selection, missing-override fallback and independence of winter-only base objects from pack ownership. Record the tested app revision, build/test results and Day/World screenshots. Confirm supported app versions receive the enforcement before shared-main activation.
5. Apply [activation.changes.json](activation.changes.json) by stable keys to the latest catalog, after checking [approval.json](approval.json). It changes only the four `enabled` flags. Preserve current prices, windows, revisions, unrelated records and pending entitlement gates. An activation-only edit does not change artwork revisions.
6. Run `python3 scripts/validate.py` and `python3 tools/make_pack_coverage.py --check` (regenerate coverage if the enabled-state labels changed), publish the checked content change, and confirm CI. The owner's authorization covers this activation once its technical prerequisites pass.

No native app build or simulator verification was performed by this content integration. The content repository contains no ChronosKeep Swift target. Its JSON and PNG checks are not evidence of in-app behavior.

## Earlier approved work included

| Scope | Included work | Runtime release state |
| --- | --- | --- |
| Ground, PR #3 | Dirt Patch and Dirt Rows: base, Autumn Leaves, Winter; Cobblestone Circle: base | Pilot only. Future Terraforming spell, new type support and economy remain pending. |
| Cow, PR #4 | Base, Autumn Leaves and Winter | Animal pilot. Familiars kind/condition and animal economy remain pending. Snow Hare is preserved alongside Cow. |
| Cherry Blossom, PR #5 | Base and approved Winter override | Disabled tree. Existing 3-token placeholder and unresolved unlock/availability are preserved. Autumn appearance needs separate art approval. |
| Gold Vein, PR #6 | Approved crystalline base | Disabled 2×2 landmark. Future individual spell/achievement condition and final economy remain pending. |
| Silver and Bronze Veins, PR #7 | Approved base sprites | Same individual unlock requirement as Gold. All veins intentionally use base art across packs. |

The rollup keeps all existing catalog entries, pricing, footprints, existing seasonal dates, approved Winter artwork, Snow Hare and Classic Retro originals. It adds no live `animals` or `groundTiles` arrays. The proposed models stay in pilot files until the native app and validator support them.

## Other decisions kept pending

Familiars may remain undecided. Hide Animals options while its entitlement is undefined or unearned; do not let art-pack ownership bypass it. Ground uses the separate future Terraforming spell and must render underneath existing foreground objects. Village Hut awaits its Village achievement. Veins await their own unlock conditions. Classic Retro pack availability remains undecided. These gates do not hold up verification of the ordinary seasonal Winter purchases above.

The existing Settings → Future Features screen should receive the current [handoff entries](../rewards-collections/FUTURE_FEATURES_HANDOFF.md). Reuse matching subjects rather than duplicating them. Informational entries never grant unlocks or activate content.

Historical delivery READMEs describe decisions at the time each delivery was prepared. This release record and the current catalog supersede older claims that the Winter date, its price, or the three supported objects' acquisition are awaiting approval. PRs #8 and #10 are older documentation drafts and are not merged by this integration.
