# Approved winter-only objects: Xcode integration

## Status and scope

The owner approved the Snowman, Winterberry Bush, Snow Hare and Frost Obelisk artwork and requested publication to main. These four native PNGs are final approved art for this pass. More art generation is optional; begin app integration and visual verification now.

Three supported-class objects have disabled entries in `catalog.json`. Snow Hare is an animal pilot because the current runtime catalog accepts only trees and landmarks. All four have one base appearance; Winter reskin-pack ownership is not required. [The manifest](manifest.json) records exact paths, hashes, dimensions, approved art and unresolved release decisions. It is project metadata, not an alternate runtime decoder input.

| Key | Class / footprint | Published sprite | Runtime state |
| --- | --- | --- | --- |
| `snowman` | Tree slot / 1×1 | `sprites/default8bit/snowman.png` | Registered, disabled, spriteRevision 1 |
| `winterberry_bush` | Tree slot / 1×1 | `sprites/default8bit/winterberry_bush.png` | Registered, disabled, spriteRevision 1 |
| `frost_obelisk` | Landmark / 2×2 | `sprites/default8bit/frost_obelisk.png` | Registered, disabled, spriteRevision 1 |
| `snow_hare` | Future Animal / 1×1 | `pilots/animals/sprites/default8bit/snow_hare.png` | Pilot only; no live catalog entry |

The three new catalog entries use `season: winter` and `window: {start: 12-01, end: 02-28}`. Their disabled state prevents this art publication from enabling sales. They must remain disabled until the owner settles release decisions and native placement checks are verified. Preserve every existing key, price, footprint, pack configuration and historical saved object.

## Price placeholders, not final approval

`CHATGPT_HANDOFF.md` section 8 supplies staging defaults when no prices were given. These values make valid disabled entries without treating art approval as approval of the economy:

| Object | Staged tokenPrice | Effective one-time store unlock | Effective per-placement cost |
| --- | ---: | ---: | ---: |
| Snowman | 3 | 3 tokens | 1 token |
| Winterberry Bush | 3 | 3 tokens | 1 token |
| Frost Obelisk | 4 | 8 tokens | 4 tokens |
| Snow Hare | Not set | Not set | Not set |

Tree store price defaults to tokenPrice and planting to 1. Landmark store price defaults to 8 and planting to tokenPrice. No explicit storePrice/plantPrice overrides are added. Final economy and any item-specific acquisition requirements remain unapproved. Snow Hare additionally requires Familiars; whether that is a spell or achievement and how it is earned remain open.

## First Xcode pass: integrate approved work

1. Sync the latest content and verify Refined/default and approved Winter reskins with the existing item keys. Respect the current item and pack revisions. Verify full PNG canvases, nearest-neighbor rendering, correct contact points, layering and consistent Day/macro Forest scale. Use development fixtures for disabled content; do not enable production content for a visual test.
2. Implement or verify the seasonal purchase/new-placement rules below in both the UI and final mutation. Existing ownership and saved placements must survive all dates and pack changes.
3. Integrate or verify the approved `ForestGroundKit/` handoff in the canonical Xcode package. Keep the 6×6 plot and its 36 placement cells. The monthly surfaces should remain quiet, avoid a checkerboard, and join coherently across daily plots in the macro spiral. Verify exposed soil faces and two-, three- and four-plot joins with the Apple toolchain.
4. Update the existing Settings → Future Features screen with the prepared Animals/Familiars, Ground/Terraforming, Village, vein/reward and seasonal-placement roadmap subjects. Reuse matching entries instead of creating duplicate unlock subjects. Informational roadmap entries do not activate content or grant entitlements.
5. Add the new three supported-class objects to development fixtures for art/anchor checks. Add Hare to an animal fixture only after the new animal type can decode, persist and render it. Report simulator evidence and remaining gaps.

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

Extend this policy to the four winter-only keys with **December 1–February 28 inclusive**. The exact proposed endpoint excludes February 29. The three disabled catalog entries carry the purchase window; native code must enforce the new-placement restriction, including owned items. The future animal path must enforce the same rule for Hare. Retain ownership and continue rendering all previously saved placements after a window closes. This newer owner-directed policy supersedes historical handoff text saying owned seasonal objects are always plantable.

Verify boundary dates, year wrapping, owned-item placement, stale UI across midnight, no currency/cell mutation on rejection, saved-object rendering and pack independence. Keep all four winter-only objects unavailable to players until the relevant paths pass.

## Animals and Ground remain separate classes

**Animals:** implement a dedicated type ID and catalog/model path, Store and Inventory sections, foreground placement, persistence and rendering. `animal` / `animals` are proposed identifiers, not fields to insert into the current version-1 content catalog. Familiars gates the category. While the gate is unavailable, undecided or unearned, hide its sections and actions; keep saved animals renderable. A Debug entitlement can support development without granting a production unlock. Cow remains coordinated with its separate draft; this delivery adds only Hare to the pilot path.

**Ground:** retain the separate Ground type and sections planned with the existing ground pilot. Terraforming is the future spell gate. Ground surfaces render beneath existing trees, animals and landmarks, use compatible adjacent-edge joins, and require their own saved occupancy rather than consuming the foreground slot. No further ground artwork is generated or activated in this delivery.

## Release decisions still needed

- Confirm or replace the three staged price schedules; set Snow Hare pricing.
- Decide whether Snowman, Winterberry Bush and Frost Obelisk are ordinary seasonal purchases or need an additional unlock.
- Define Familiars as a spell or achievement, with a stable requirement ID and earning criteria.
- Separately decide whether to activate the existing Winter reskin pack for December 1–February 28 at its current 10-token price. It is still disabled with no configured window; this delivery does not change it.
- Complete native verification before enabling the new objects. Village, veins, Cherry Blossom, Classic Retro and Ground retain their separate unresolved release decisions.

## Optional later art

Frostbloom Tree, Snow Lantern Circle and Arctic Fox can be generated after this integration pass. Autumn Cherry Blossom remains a separate visual decision. Village House and additional ground surfaces remain later work. None is a prerequisite for the approved work above.
