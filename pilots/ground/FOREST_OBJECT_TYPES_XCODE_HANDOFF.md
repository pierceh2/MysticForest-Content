# Mystic Forest · Animals and Ground

**Dirt Patch and Dirt Rows are approved for staging** in their base, Autumn Leaves and winter appearances. Give Animals and Ground their own type identities and their own sections in both Inventory and Store. A player must be able to put dirt beneath a tree that is already planted, change that dirt to rows, and remove the dirt while the tree stays in place.

## Item identities and screens

| Design class | Proposed type ID | Proposed catalog array | Inventory | Store |
| --- | --- | --- | --- | --- |
| Animal | `animal` | `animals` | Owned animals and their existing placement actions | Eligible animal unlocks |
| Ground | `ground` | `groundTiles` | Owned surfaces with a cell-editing action | Eligible ground unlocks |

The current content contract supports `trees` and `landmarks`. The Swift app target is needed to confirm the actual enum names, persisted discriminators, ownership keys, section order and Store filters. Match its conventions. If existing catalog arrays imply the item type, do the same for the new arrays. `groundTiles` distinguishes purchasable items from a pack’s existing `ground` color overrides.

Keep `dirt_patch` and `dirt_rows` as separate, stable item keys. Each covers one logical cell and has a set of 32 × 16 isometric top-face variants. All adjacency masks and seasonal appearances of an item resolve through that single identity and entitlement. Reserve the Animal section for its own content. The next art pilot is a one-cell standing cow. Review its base pose beside a planted tree before starting the autumn and winter reskins. Implement and verify the two new catalog types in a Debug fixture first. Extend the iOS decoder, inventory and store models, save readers, and content validator before releasing new arrays in the downloadable catalog.

## Terraforming and Ground visibility

Terraforming is a planned spell. Until the player has learned it, hide Ground and its items in both Store and Inventory. The same rule gates purchase and placement entry points, including search results or shortcuts if the app has them. Use the spell model’s learned state once available. A missing definition, unresolved state or older save with no spell entitlement takes the locked path. Do not grant Terraforming during migration or introduce a player-facing spell in this phase.

Learning Terraforming reveals the Ground category. Apply ordinary item ownership and price checks after that. Autumn Leaves or winter pack ownership can change a surface’s appearance only. Render previously placed surfaces and the twelve monthly base floors independently of this gate. The separate Animals category follows its own eligibility rules.

## Place and edit ground beneath existing objects

- Store the surface for each local cell on its saved day, independently of foreground placements. An optional sparse list of `(x, y, itemKey)` records is sufficient for a 6 × 6 plot. An absent list on an older day means all 36 cells show their normal monthly or pack ground.
- In the Ground inventory section, select a surface and enter ground-edit mode. Convert the tap to a board cell using the existing inverse isometric projection. Give the selected ground cell priority over the sprite covering it, even on a mature tree or within a 2 × 2 landmark. Keep the normal tree/landmark selection behavior outside ground editing.
- Applying, replacing or clearing a surface changes only that one surface record. Preserve the tree’s identity, placement, growth state and ownership. A 2 × 2 landmark can cover four independently editable ground cells. Removing a foreground object later reveals the surface below it. Selecting the same surface twice should produce one saved edit and at most one applicable charge.
- Use the existing ownership and transaction model once the economy is decided. Record the selected surface and any required token deduction atomically. For the editing fixture, simulate Terraforming learned and grant both surfaces. Test the locked fixture with those same owned items as well. Store prices, placement cost, per-cell consumption and how Terraforming is learned are open decisions.

## Draw, join and persist

Paint the resolved monthly or seasonal plot top, then its purchased cell surfaces, then contact shadows and the existing depth-sorted foreground objects. Use identical cell projections in Day and at each day’s offset in World. Clearing dirt reveals the appropriate monthly top. Zooming and reskinning change appearance without changing a cell’s saved key.

The fixture includes neutral, Autumn Leaves (`fall`), and winter (`winter`) atlases for the same two item keys. The neutral files are `surfaces/dirt_patch.png` and `surfaces/dirt_rows.png`. Seasonal files use the corresponding `surfaces/fall/` and `surfaces/winter/` folders. Use the selected day’s effective pack, then the neutral atlas if needed. The pack’s ownership and availability follow the existing selection rules.

Read `surfaces/atlas.json`. Both items share the `soil` merge group, so touching patch and rows share a continuous soil edge. In grid coordinates the edge bits are −u = 1, +u = 2, −v = 4, +v = 8. The +u axis projects down-right and +v down-left. Furrows run along +u with two bands per cell. They continue into neighboring rows and end where they meet plain dirt. Derive adjacency from the four edge-sharing cells on **that saved day**. Recompute the edited cell and its four cardinal neighbors after applying, replacing or clearing dirt. A diagonal touch and a neighboring day in the World spiral each keep their own boundaries. Persist surface IDs and coordinates. Derive the atlas frame again after loading. Preserve the existing rules for which historical days are editable. Unknown or offline art can fall back to the monthly surface while retaining the saved cell key.

## Xcode acceptance

1. Open a pre-change save with a mature tree, a 2 × 2 landmark and earlier dates. Confirm the existing inventory, store ownership and placements still load. With Terraforming absent or unlearned, verify Ground is hidden in both screens and its items cannot be purchased or placed, including with a seasonal pack and owned dirt. Verify old saved surfaces still render. In a second fixture, mark Terraforming learned and confirm that both screens show eligible Ground items. Verify Animals and the monthly floor work in both spell states.
2. Place Dirt Patch beneath the tree, switch to Dirt Rows, reopen the app offline, and inspect the same date in Day and World. Clear the surface. Compare the tree’s placement and stored identity before and after. Repeat on one cell under the landmark and check its other three cells.
3. Check a single tile, straight row, 2 × 2 block, L shape, diagonal-only pair and a row touching plain dirt. Replace a middle cell, then remove it. Check the neighbors redraw, furrows align, and adjoining days keep their own land. Verify dates with no purchased surface still use the monthly ground.
4. Confirm normal item selection still targets the foreground, Ground mode targets the underlying cell, and a repeated edit or insufficient balance leaves state and token balance consistent.

## Prompt for Xcode Codex

> Read the Mystic Forest object-types handoff and the dirt atlas metadata. Inspect the app’s current item-type, save, Inventory, Store and placement models. Add typed Animals and Ground sections to both screens, preserving old saves and item keys. Gate all Ground options in both screens on the future Terraforming learned state. Exercise missing, unlearned and learned states in Debug. Preserve saved ground rendering and existing monthly floors. Keep implementing the spell as a future task. Implement Dirt Patch and Dirt Rows in the Debug fixture using a separate per-day cell surface layer. Make applying, replacing and clearing soil work beneath an already-planted tree and individual cells of a 2 × 2 landmark. Render the same surfaces below objects in Day and World, with adjacency from the atlas metadata. Exercise the acceptance cases above and return before/after screenshots of the same mature tree. Record build and test results and any compatibility work needed before publishing the catalog schema.
