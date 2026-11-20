# Mystic Forest rewards and collections

**Destination**  Settings → Future Features in the ChronosKeep iOS app  
**Content snapshot**  November 20, 2026 · [MysticForest-Content main at 61c05b2](https://github.com/pierceh2/MysticForest-Content/tree/61c05b2879af875de35f049e9e0258458b4c5177)  
**Companion file**  [Nine roadmap entries with player-facing copy and decision history](MysticForest-FutureFeatures.json)

The Village Hut and Refined default rollout have merged. Five draft content PRs hold the remaining approved objects. The existing iOS Settings view and its backing data live outside the accessible content repository. The nine entries below are ready for the app-side port. Adding this handoff to the content repo alone does not populate the tab.

| Settings entry | What exists | Proposed unlock | Still to decide |
| --- | --- | --- | --- |
| Terraforming | Dirt Patch, Dirt Rows and Cobblestone Circle in the draft ground pilot. [PR 3](https://github.com/pierceh2/MysticForest-Content/pull/3) | Learning the future Terraforming spell opens Ground in Store and Inventory and allows ground purchases and placement beneath trees. | Spell criteria and how individual surfaces are acquired afterward. |
| Familiars | Cow with base, autumn and winter art in the draft animal pilot. [PR 4](https://github.com/pierceh2/MysticForest-Content/pull/4) | Familiars opens Animals in Store and Inventory. | Spell or achievement, its criteria, and how players acquire the cow afterward. |
| Village Hut | Disabled 2×2 landmark on main with base, autumn and winter art. [PR 1](https://github.com/pierceh2/MysticForest-Content/pull/1) | Village achievement proposed. Eligible owned seasonal packs supply reskins once the player has access to the hut. | Achievement criteria and identifier. Does it award the hut or reveal it for purchase? |
| Gold Vein | Approved year-round landmark, disabled in its draft. [PR 6](https://github.com/pierceh2/MysticForest-Content/pull/6) | A spell or achievement for Gold Vein. | Name, type, criteria and whether it awards the vein or opens a purchase. |
| Silver Vein | Approved year-round landmark, disabled in its draft. [PR 7](https://github.com/pierceh2/MysticForest-Content/pull/7) | A spell or achievement for Silver Vein. | Name, type, criteria and whether it awards the vein or opens a purchase. |
| Bronze Vein | Approved year-round landmark, disabled in its draft. [PR 7](https://github.com/pierceh2/MysticForest-Content/pull/7) | A spell or achievement for Bronze Vein. | Name, type, criteria and whether it awards the vein or opens a purchase. |
| Cherry Blossom Tree | Approved base tree, disabled in draft. Autumn and winter art await approval. [PR 5](https://github.com/pierceh2/MysticForest-Content/pull/5) | Open. | How the tree enters the collection. The draft placement cost does not establish its unlock. |
| Classic Retro Collection | All 34 original sprite files are archived on main. Refined is the default. [PR 2](https://github.com/pierceh2/MysticForest-Content/pull/2) | Separate appearance pack proposed. Unlock open. | Availability, timing and how pack selection works alongside seasonal appearances. |
| Winter Art Pack | Disabled pack on main with a 10-token catalog value. Hut artwork has merged. Cow artwork is in PR 4. [Catalog](https://github.com/pierceh2/MysticForest-Content/blob/61c05b2879af875de35f049e9e0258458b4c5177/catalog.json) | Open. | Release window and actual acquisition method. The catalog price alone does not establish a live purchase. |

## Port into the existing Settings tab

1. Open the iOS app target and follow Settings → Future Features to its current list, model and localization source. Reuse its navigation, grouping, ordering and status conventions.
2. Match existing rows by native ID or meaning. Update each matching feature in place and add each missing row once. Use the companion file’s `title` and `playerSummary` for display and translate using the app’s existing approach. `handoffKey` identifies a record across handoffs. Preserve existing native IDs and reconcile compound rows without duplicating their content.
3. Keep technical state, PR numbers, pricing placeholders and open design questions in the handoff. Show the roadmap rows even to players who have yet to earn the corresponding future unlock. Make this an informational Settings change only.
4. Build the app and open the existing tab on a simulator. Verify all nine subjects are represented once, unrelated roadmap entries still appear, and reopening the tab preserves the same list. Check that visiting Settings has no effect on inventory, purchases, achievements, spells or saved placements. Include a screenshot and the build or test result in the app PR.

## Boundaries for future rewards work

- Ground and Animals need separate Store and Inventory sections. When those category gates are implemented, a missing or unearned gate keeps their controls hidden. Continue rendering previously saved forest placements. A player can place eligible Ground underneath an existing tree.
- Keep object access, individual ownership, placement cost and seasonal artwork selection separate. Buying an appearance pack alone should never grant the hut or cow. Use one base appearance for each ore across seasons.
- Monthly 6×6 ground appearances follow the calendar. Autumn Leaves and Thanksgiving Feast already have catalog acquisition rules. Other surfaces, houses, fair monuments and random theme collections stay in the design backlog. No specific meditation unlock has been selected for these nine entries.
