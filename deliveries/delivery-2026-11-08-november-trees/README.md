# Delivery 2026-11-08-november-trees

## What's in it
Three new trees, each with a regular green-season sprite in the default pack and an autumn reskin in the existing `fall` pack. Six PNGs in total.

| Key | Name | Default pack | `fall` pack |
| --- | --- | --- | --- |
| larch | Larch | Pointed fresh-green conifer of soft, drooping needle layers with open space between them and the trunk showing through, so it differs from the solid, hard-tiered pine | Gold, amber and rust needles, a few fallen needles at the base |
| maple | Maple | Cool deep-green crown shaped like a maple leaf, five pointed lobes | Strong scarlet red with a few orange flecks in the light, and a few red and amber leaves at the base |
| ginkgo | Ginkgo | Lime-green crown of overlapping fans on a straight trunk | Lemon yellow, with a heavier scatter of fallen yellow leaves, since a ginkgo drops its leaves all at once |

Every PNG passed `check_sprite.py` (32x48, hard alpha, nothing on the edges, foot at the same place as the oak, at most 16 colours; each uses 9 or 10). I also looked at all six enlarged 8x on dark green, next to the oak, pine and birch and their fall versions. The larch, maple and ginkgo were each redrawn at least twice. After the owner's review the fall maple was made redder, and the larch (default and fall) was redrawn twice: first filled out, then reworked into spaced layers because a larch has more room between its branches. The other three PNGs are unchanged by those revisions.

The reskins keep the exact silhouette, canvas and foot position of the default sprites, and add only the autumn colours and a few fallen leaves inside the tile.

The drawing code is `tools/make_november.py`. It reuses the helpers in `tools/make_sprites.py` and regenerates all six PNGs.

## Placeholders
- None. Prices are as requested: `tokenPrice` 4 for each tree. The store price and plant price are left to their defaults (store price = `tokenPrice` = 4, plant price = 1), so no `storePrice` or `plantPrice` is written.

## Weak spots
- **Larch:** redrawn after review so there is open vertical space between the layers of needles, as on a real larch. The layers are fairly flat and regular, so at 1x it can look a little like a layered Japanese pine.
- **Maple:** the leaf-shaped crown is iconic and readable, but it is stylised and slightly smaller than the oak's crown. It looks more like a leaf on a trunk than a real tree.
- **Ginkgo:** a few small dark dashes show where fans overlap. They add some texture, but at 1x they can look like gaps.
- **Pack coverage:** the `fall` pack now covers six default items plus these three new ones. Items that are already autumn-themed in the default pack (the pumpkins, scarecrow and hay bales) have no reskin, and need none.

## Decisions for the owner
- **No `season` on any of the three.** They are regular year-round trees in the default pack, so none "clearly belongs to a season". Their autumn look comes from the `fall` pack. If you want any of them filed under the autumn season in the app, tell me.
- **Tags:** `larch` gets `conifer`; `maple` and `ginkgo` get `deciduous` (matching the oak, birch and willow). They are my choices and easy to change.
- **Descriptions** are mine, one sentence each, in the voice of the existing ones. The ginkgo's "drops every leaf in a single night" is a nod to how ginkgos really behave.
- **Pack revision:** these deliveries add PNGs to the existing `fall` pack, so its `revision` should go up once for the delivery. The three new items start at `spriteRevision` 1. Neither is set by me.
- **Thanksgiving pack:** not included. We can plan it next. Note that a pack's window may close and hand back to another pack.
