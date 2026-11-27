# Mystic Forest: Settings → Future Features

Updated November 27, 2026 with the owner's Winter economy, acquisition and publication approvals.

This is the current source handoff for the existing ChronosKeep **Settings → Future Features** tab. The [companion JSON](MysticForest-FutureFeatures.json) contains eleven subjects: the nine stable records from the earlier rewards handoff, plus Winter Objects and Seasonal Placement. Its keys identify handoff records, not app model IDs. Neither file is a runtime catalog schema, unlock implementation or evidence that the native Settings tab has changed.

## Current decisions and remaining work

| Settings subject | Approved content or decision | Remaining work |
| --- | --- | --- |
| Terraforming | Dirt Patch and Dirt Rows each have base, autumn and winter art; Cobblestone Circle has base art. Ground is a separate category and surface layer beneath foreground objects. | Implement the future Terraforming spell, its earning criteria, Ground type, Store/Inventory sections, persistence and joins. Individual surface acquisition and prices remain undecided. |
| Familiars | Cow has approved base, autumn and winter art. Snow Hare has approved base art and a December 1–February 28 purchase/new-placement window. | Choose spell or achievement, stable requirement ID and criteria. Implement Animals as a separate type and sections. Cow/Hare acquisition and prices remain undecided. |
| Village Hut | Disabled 2×2 landmark with base, autumn and winter art. A Village achievement is proposed. | Define achievement ID and criteria, and whether it grants the hut or reveals a purchase. |
| Gold Vein | Approved base-only 2×2 landmark, staged disabled. Uses its base appearance across packs. | Define its own spell or achievement, criteria and grant-versus-purchase behavior. |
| Silver Vein | Approved base-only 2×2 landmark, staged disabled. Uses its base appearance across packs. | Define its own spell or achievement, criteria and grant-versus-purchase behavior. |
| Bronze Vein | Approved base-only 2×2 landmark, staged disabled. Uses its base appearance across packs. | Define its own spell or achievement, criteria and grant-versus-purchase behavior. |
| Cherry Blossom Tree | Base and Winter art are approved; the tree is staged disabled. | Decide acquisition/unlock and availability. Autumn artwork is not approved. The staged token value does not settle these decisions. |
| Classic Retro Collection | All 34 original sprite files remain archived. Refined is the standard appearance. A separate Classic Retro appearance pack is planned. | Decide unlock and availability, then define its selection alongside seasonal appearances. |
| Winter Art Pack | **10 Forest tokens; December 1–February 28 inclusive; ordinary seasonal pack purchase.** Approval is complete. Ownership persists. The pack remains disabled pending native visual verification. | Verify art, cache revisions, pack resolution and existing saved forests in the app, then activate under the existing approval. No repeat economy or date approval is required. |
| Winter Forest Objects | Snowman and Winterberry Bush: **3 tokens to unlock, 1 per placement**. Frost Obelisk: **8 to unlock, 4 per placement**. Ordinary seasonal purchases, **December 1–February 28 inclusive**, with no extra achievement/spell requirement. | Keep these three disabled until native visual and seasonal purchase/new-placement checks pass, then activate under the existing approval. Snow Hare remains separately behind undecided Familiars access and economics. |
| Seasonal Placement | Seven existing seasonal objects and four Winter objects may be purchased and newly placed only in their individual windows, including when owned. | Implement and verify the shared native check at Store, Inventory, preview and final mutation. Preserve ownership and all previously saved placements. |

The exact Winter endpoint is February 28; February 29 is outside the approved window. See the [current seasonal planting handoff](../seasonal-planting/SEASONAL_PLANTING_XCODE_HANDOFF.md) for all eleven keys and date-boundary acceptance checks.

## Port into the existing Settings tab

1. Locate the app's existing Future Features view, backing model, localization and status conventions. Match rows by existing native ID or meaning; update matching rows and add each missing subject once. Preserve unrelated entries and their native IDs. A combined existing row may represent multiple handoff subjects without duplication.
2. Use `title` and `playerSummary` as display copy. Map `handoffKey` to an existing or newly assigned native ID through the app's established mechanism. Keep technical metadata, source paths, staging prices, approval history and unresolved design questions out of player-facing copy.
3. Map the native status from the actual implementation. Content approval or presence in this repository does not mean the feature is available in the app. Keep the informational roadmap visible even when players have not earned a future unlock; visiting it must not grant anything.
4. Build and inspect the existing tab in a simulator. Verify all eleven subjects are represented once, prior unrelated entries remain, localization and scrolling work, and opening/reopening Settings does not change inventory, balances, ownership, spells, achievements or placements. Record the build, simulator evidence and any remaining gaps in the app handoff.

## Boundaries for implementation

- Ground and Animals need distinct type IDs, Store and Inventory sections, persistence and placement handling. `ground`/`groundTiles` and `animal`/`animals` are proposals to reconcile with the native model, not fields to insert into the current version-1 catalog without support.
- A missing, undefined or unearned category gate keeps its player-facing sections and actions hidden. Continue to render existing saved objects. Debug fixtures may exercise approved content without granting production entitlements.
- Terraforming governs purchased ground surfaces. It does not hide the monthly base floor. Ground can sit beneath existing trees and landmarks, has separate surface occupancy, and joins compatible neighbors within the same saved daily plot.
- Keep object access, ownership, placement cost and appearance-pack ownership separate. Buying Winter does not grant a hut, animal or vein, and does not bypass a seasonal object's planting window. The four Winter-only objects have one base appearance and do not require the Winter reskin pack.
- Retain each vein's independent future unlock. No specific meditation reward has been selected. Additional water surfaces, houses, fair monuments and random themed collections remain backlog work.

## Repository references

- [Runtime catalog](../../catalog.json) and [pack coverage](../../PACK_COVERAGE.md)
- [Ground type and placement handoff](../../pilots/ground/FOREST_OBJECT_TYPES_XCODE_HANDOFF.md)
- [Cow and Animals pilot](../../pilots/animals/README.md)
- [Winter objects and native checks](../../pilots/winter_objects/XCODE_HANDOFF.md)
- [Mineral vein unlock handoff](../../docs/mineral-veins/README.md)

This file supersedes the older nine-subject snapshot as guidance for the current approvals. It does not alter the remote state of older draft PRs. Native app implementation and simulator verification remain unverified until performed in the ChronosKeep app project.
