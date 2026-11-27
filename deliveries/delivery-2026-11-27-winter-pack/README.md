# Approved Winter artwork

The owner approved the labeled Winter review array on November 27, 2026. This delivery adds the eleven approved Winter appearances whose item keys already exist on the production catalog. The trees use the revised winter direction: bare deciduous branches, a bare Larch, evergreen Pine needles, and substantial settled snow. Shrine and Lily Pond retain their existing isometric structures.

## Contents

| Keys | Format |
| --- | --- |
| `oak`, `pine`, `birch`, `willow`, `larch`, `maple`, `ginkgo`, `apple_tree` | 32×48 RGBA tree PNGs |
| `shrine`, `pond`, `hay_bales` | 64×96 RGBA landmark PNGs |

Each PNG appears in `sprites/winter/` inside this delivery and at its corresponding repository runtime path. The delivered bytes match the approved native review candidates. PNGs use hard transparency and at most sixteen opaque colors. The source review arrays distinguished enlarged design concepts from the actual native sprite exports.

## Catalog and pack status

- Pack key: `winter`.
- Classification: `kind: seasonal`, `season: winter`.
- Descriptive tags: `snow`, `frost`, `cosy`.
- Applied pack revision: **1 → 2**, once for this art delivery.
- Current token price remains **10**.
- `enabled` remains **false**, and no pack window has been added. Pack activation and its calendar window are separate release decisions.
- Item keys, prices, purchase windows, footprints, unlock settings and default-art sprite revisions are preserved.

`changes.json` is the delivery input and deliberately contains no revision number. Applying this delivery to the original base commit raises the Winter revision once. The repository catalog accompanying this delivery already contains revision 2; do not reapply the delivery or raise the revision again for these same bytes.

## Seasonal availability

Apple Tree and Hay Bale Stack keep their October 1–December 1 purchase and approved new-placement windows, inclusive. Their Winter appearances cover the December 1 overlap if Winter is configured to begin on December 1. The art does not extend their placement eligibility.

Pumpkin, Jack-o'-Lantern, Scarecrow, Corn Stalks and Harvest Table intentionally have no Winter override. Their approved placement windows close before Winter. Harvest Table is limited to Thanksgiving, November 15–30. The handoff's restricted set includes these five keys plus Apple Tree and Hay Bale Stack; the iOS app must enforce their windows in both selection controls and final placement mutations, including the landmark paths. Already-saved placements and ownership persist.

These native placement rules are app work. Content PNGs and browsing tags cannot enforce them by themselves.

## Coverage and coordinated work

Winter now has its own sprite for **12 of the 17 current catalog items**, including the existing Village Hut appearance. The other five are intentional exclusions, giving **zero unexplained gaps** for the current catalog.

The existing Village Hut PNG is preserved byte-for-byte and the item remains disabled pending the Village achievement flow. Approved Winter Cherry Blossom artwork is coordinated with the base item's draft PR #5. Cow and the two soil atlases remain in their existing Animals and Ground pilot work in PRs #4 and #3. Those keys and feature gates are not activated by this delivery. Gold, Silver and Bronze veins remain base-only as the owner requested.

## Review observations

The selected Apple Tree preserves its reference's 38-pixel occupied height and row-43 baseline with a narrower bare branching framework. Willow and Maple use small width allowances inside the original canvas to preserve their full heights. Ginkgo and Pond each occupy one fewer vertical row than their references while preserving their baselines. The Shrine's palette retains its gold interior detail and teal roof. These are the native candidates shown in the approved array.

## Verification

Before release, run:

```sh
python3 tools/make_pack_coverage.py --check
python3 scripts/validate.py
```

The eleven PNGs were also individually checked with the repository's `tools/check_sprite.py`, and hashes were compared with the approved review manifest. Native iOS Day/World rendering, content-cache refresh and seasonal placement enforcement still require verification in the app.

## Reference

- Base main commit: `cc0c78a50628a7ed93dad3ac113fdc5848bfc5ce`.
- Base tree: `62fcb188b6f4e657cd3da9a429ea4a82ec2158f6`.
- Approval: the owner accepted the full labeled Winter review array with “Ok those are good!” before this delivery was prepared.
- New price or calendar placeholders introduced: **none**. The Winter pack's activation and window remain unset.
