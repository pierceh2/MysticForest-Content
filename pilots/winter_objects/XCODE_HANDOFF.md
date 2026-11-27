# Approved winter-only objects: Xcode integration

## Status and scope

The owner approved the Snowman, Winterberry Bush, Snow Hare and Frost Obelisk artwork and requested publication to main. These four native PNGs are final approved art for this pass. More art generation is optional; begin app integration and visual verification now.

Three supported-class objects have disabled entries in `catalog.json`. Snow Hare is an animal pilot because the current runtime catalog accepts only trees and landmarks. All four have one base appearance; Winter reskin-pack ownership is not required. [The manifest](manifest.json) records exact paths, hashes, dimensions, approved art and current release decisions. It is project metadata, not an alternate runtime decoder input.

| Key | Class / footprint | Published sprite | Runtime state |
| --- | --- | --- | --- |
| `snowman` | Tree slot / 1×1 | `sprites/default8bit/snowman.png` | Registered, disabled, spriteRevision 1 |
| `winterberry_bush` | Tree slot / 1×1 | `sprites/default8bit/winterberry_bush.png` | Registered, disabled, spriteRevision 1 |
| `frost_obelisk` | Landmark / 2×2 | `sprites/default8bit/frost_obelisk.png` | Registered, disabled, spriteRevision 1 |
| `snow_hare` | Future Animal / 1×1 | `pilots/animals/sprites/default8bit/snow_hare.png` | Pilot only; no live catalog entry |

The three catalog entries use `season: winter` and `window: {start: 12-01, end: 02-28}`. The owner has approved these dates, prices and ordinary seasonal acquisition. They remain disabled until native visual and seasonal-placement checks pass. Then apply the [authorized activation patch](../../handoffs/winter-2026/activation.changes.json) under the [approved release handoff](../../handoffs/winter-2026/README.md), without asking again about the settled business decisions. Preserve every existing key, price, footprint and historical saved object.

## Approved economy and acquisition

On November 27, 2026, the owner accepted the recommended prices and ordinary seasonal purchase route. The original staging values are now approved for the three supported-class objects:

| Object | Catalog tokenPrice | Approved one-time store unlock | Approved per-placement cost |
| --- | ---: | ---: | ---: |
| Snowman | 3 | 3 tokens | 1 token |
| Winterberry Bush | 3 | 3 tokens | 1 token |
| Frost Obelisk | 4 | 8 tokens | 4 tokens |
| Snow Hare | Not set | Not set | Not set |

Tree store price defaults to tokenPrice and planting to 1. Landmark store price defaults to 8 and planting to tokenPrice. No explicit storePrice/plantPrice overrides are needed. Snowman, Winterberry Bush and Frost Obelisk need no additional spell, achievement or art-pack unlock. The Winter reskin pack itself is approved at 10 tokens for December 1–February 28 and now has that configured window, at revision 3. Snow Hare pricing remains unset; Familiars may remain pending, including whether it is a spell or achievement and how it is earned.

## First Xcode pass: integrate approved work

1. Sync the latest content and verify Refined/default and approved Winter reskins with the existing item keys. Respect the current item and pack revisions. Verify full PNG canvases, nearest-neighbor rendering, correct contact points, layering and consistent Day/macro Forest scale. Use development fixtures for disabled content; do not enable production content for a visual test.
2. Implement or verify the seasonal purchase/new-placement rules below in both the UI and final mutation. Existing ownership and saved placements must survive all dates and pack changes.
3. Integrate or verify the approved `ForestGroundKit/` handoff in the canonical Xcode package. Keep the 6×6 plot and its 36 placement cells. The monthly surfaces should remain quiet, avoid a checkerboard, and join coherently across daily plots in the macro spiral. Verify exposed soil faces and two-, three- and four-plot joins with the Apple toolchain.
4. Update the existing Settings → Future Features screen with the prepared Animals/Familiars, Ground/Terraforming, Village, vein/reward and seasonal-placement roadmap subjects. Reuse matching entries instead of creating duplicate unlock subjects. Informational roadmap entries do not activate content or grant entitlements.
5. Add the three supported-class objects to development fixtures for art/anchor checks. Add Hare to an animal fixture only after the new animal type can decode, persist and render it. Report simulator evidence and remaining gaps. Once the release checks pass and compatible app builds will receive the content, apply the four authorized enabled edits and confirm content CI. Animal, Ground and other unresolved unlocks remain separate.

The app checkout is not part of this content publication. Native implementation, simulator builds and in-app behavior have not been verified in this session.

## Seasonal new-placement policy

Use the actual local device date, inclusive recurring month-day windows and year-boundary wrapping. The same eligibility must drive Store, Inventory and placement previews. Recheck in the authoritative purchase/add-instance action immediately before spending tokens or changing occupancy. A 2×2 landmark must not reserve any of its cells on rejection. An old saved date, a changed art pack, existing ownership or a screen left open across midnight must not bypass the rule.

| Existing seasonal key | Purchase and new-placement window |
| --- | --- |
| `pumpkin` | October 1–November 30 |
| `jack_o_lantern` | October 1–October 31 |
| `corn_stalks` | November 15–November 30 |
| `scarecrow` | October 1–November 30 |
| `apple_tree` | October 1–December 1 |
| `harvest_table` | November 15–November 30 |
| `hay_bales` | October 1–December 1 |

Extend this policy to the four winter-only keys with **December 1–February 28 inclusive**. The approved endpoint excludes February 29. The three disabled catalog entries carry the purchase window; native code must enforce the new-placement restriction, including owned items. The future animal path must enforce the same rule for Hare. Retain ownership and continue rendering all previously saved placements after a window closes. See the [current standalone seasonal handoff](../../handoffs/seasonal-planting/SEASONAL_PLANTING_XCODE_HANDOFF.md).

Verify boundary dates, year wrapping, owned-item placement, stale UI across midnight, no currency/cell mutation on rejection, saved-object rendering and pack independence. Keep all four winter-only objects unavailable to players until the relevant paths pass.

## Animals and Ground remain separate classes

**Animals:** implement a dedicated type ID and catalog/model path, Store and Inventory sections, foreground placement, persistence and rendering. `animal` / `animals` are proposed identifiers, not fields to insert into the current version-1 content catalog. Familiars gates the category. While the gate is unavailable, undecided or unearned, hide its sections and actions; keep saved animals renderable. A Debug entitlement can support development without granting a production unlock. Cow base/Autumn/Winter and Snow Hare base art are now included together under `pilots/animals/`; both retain unresolved production economy and Familiars conditions.

**Ground:** retain the separate Ground type and sections planned with the existing ground pilot. Terraforming is the future spell gate. Ground surfaces render beneath existing trees, animals and landmarks, use compatible adjacent-edge joins, and require their own saved occupancy rather than consuming the foreground slot. No further ground artwork is generated or activated in this delivery.

## Remaining decisions and technical conditions

- Snowman, Winterberry Bush and Frost Obelisk prices, dates and ordinary seasonal purchase route are approved. Apply their authorized activation only after native checks.
- Set Snow Hare and Cow production pricing in a later decision; neither has a live animal catalog entry.
- Define Familiars as a spell or achievement, with a stable requirement ID and earning criteria.
- Winter pack activation for December 1–February 28 at 10 tokens is approved after native verification. It is configured but still disabled pending that check.
- Village, veins, Cherry Blossom, Classic Retro and Ground retain their separate unresolved release decisions. Their approved artwork is preserved; they do not block the ordinary seasonal Winter activation.

## Optional later art

Frostbloom Tree, Snow Lantern Circle and Arctic Fox can be generated after this integration pass. Autumn Cherry Blossom remains a separate visual decision. Village House and additional ground surfaces remain later work. None is a prerequisite for the approved work above.
