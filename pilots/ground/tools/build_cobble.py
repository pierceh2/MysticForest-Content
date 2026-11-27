"""Produce the native four-neighbour Cobblestone Circle atlas. Requires Pillow."""
import math
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageColor

ATLAS = Path(__file__).resolve().parents[1] / "surfaces/cobblestone_circle.png"

# Each bit joins one logical board side, before isometric projection.
SIDES = ((-1, 0, 1), (1, 0, 2), (0, -1, 4), (0, 1, 8))
PALETTE = {
    "mortar": "#626355",
    "joints": "#4e544e",
    "soilDark": "#756246",
    "soil": "#876f52",
    "soilLight": "#997f5d",
    "shadow": "#6b736c",
    "sage": "#8c9584",
    "slate": "#818e92",
    "warm": "#a19a88",
    "coolLight": "#adb2a5",
    "cream": "#bfbbab",
    "fieldA": "#7d8376",
    "fieldB": "#888b7f",
    "fieldC": "#90958a",
}
RGBA = {name: ImageColor.getrgb(hex_color) + (255,) for name, hex_color in PALETTE.items()}
EMPTY = (0, 0, 0, 0)
# Curated bed of fieldstones. The staggered points repeat at integer cell
# translations so the texture phase is independent of all neighbour masks.
SITES = (
    (.100, .093, 0), (.414, .148, 2), (.782, .078, 1),
    (.231, .407, 1), (.573, .455, 0), (.936, .384, 1),
    (.086, .747, 2), (.440, .798, 0), (.752, .743, 1),
)
COPIES = tuple((x + u, y + v, tone) for x, y, tone in SITES
               for u in (-1, 0, 1) for v in (-1, 0, 1))

@dataclass(frozen=True)
class Stone:
    u: float
    v: float
    tu: float
    tv: float
    half_length: float
    half_width: float
    tone: str

def curb_stones(mask):
    stones = []
    # Replace each exposed rounded corner by a pair of oblong setts as
    # soon as the adjoining side opens. Corners never rely on a diagonal bit.
    face = ("slate", "sage", "warm", "slate", "warm", "sage", "slate", "warm")
    for i, (su, sv) in enumerate(((-1, -1), (1, -1), (1, 1), (-1, 1))):
        closed_u = not mask & (1 if su == -1 else 2)
        closed_v = not mask & (4 if sv == -1 else 8)
        if closed_u and closed_v:
            for j, angle in enumerate((math.pi / 8, 3 * math.pi / 8)):
                nu, nv = su * math.cos(angle), sv * math.sin(angle)
                stones.append(Stone(.5 + .35*nu, .5 + .35*nv, -nv, nu,
                                    .134, .100, face[2*i+j]))
        elif closed_u:
            for j, t in enumerate((.125, .375)):
                stones.append(Stone(.5 + .35*su, .5 + t*sv,
                                    0, 1, .120, .100, face[2*i+j]))
        elif closed_v:
            for j, t in enumerate((.125, .375)):
                stones.append(Stone(.5 + t*su, .5 + .35*sv,
                                    1, 0, .120, .100, face[2*i+j]))
    return stones

def exposed_distance(u, v, mask):
    # Signed distance to the exterior of a rounded square extended across all
    # joined sides. Only pairs of *exposed* sides can create rounded corners.
    lo_u, hi_u = (-2 if mask & 1 else .035), (3 if mask & 2 else .965)
    lo_v, hi_v = (-2 if mask & 4 else .035), (3 if mask & 8 else .965)
    rad = .465
    a = abs(u-(lo_u+hi_u)/2) - (hi_u-lo_u)/2 + rad
    b = abs(v-(lo_v+hi_v)/2) - (hi_v-lo_v)/2 + rad
    return rad - math.hypot(max(a,0), max(b,0)) - min(max(a,b),0)

def paved_field(u, v):
    # Boundary distance in the periodic Voronoi bed supplies one continuous
    # mortar lattice across internal edges. Bevel tone depends on which way
    # the nearest edge faces the upper-left light.
    distances = sorted(((u-x)**2+(v-y)**2, x, y, tone) for x,y,tone in COPIES)
    ds, x, y, tone = distances[0]
    borders=[]
    for dt, xx, yy, _ in distances[1:6]:
        length=math.hypot(xx-x, yy-y)
        borders.append(((dt-ds)/(2*length), (xx-x)/length, (yy-y)/length))
    borders.sort()
    d, nx, ny = borders[0]
    # Soften vertices; broad stone centers stay in the narrow value range.
    d -= max(0., .035-(borders[1][0]-d)) * .30
    if d < .012:
        return "mortar"
    facing = -.90*nx - .35*ny
    if d < .047 and facing > .12:
        return ("sage","warm","coolLight")[tone]
    if d < .040 and facing < -.12:
        return "shadow"
    return ("fieldA","fieldB","fieldC")[tone]

def color_at(u, v, mask, stones):
    edge = exposed_distance(u,v,mask)
    if edge < 0:
        return EMPTY
    # Any shared side opens the circle into a bed of laid fieldstones.
    key=paved_field(u,v)
    if edge < .180:
        key="joints" if edge < .145 else "mortar"
    for s in stones:
        du, dv = u-s.u, v-s.v
        along=(du*s.tu+dv*s.tv)/s.half_length
        across=(-du*s.tv+dv*s.tu)/s.half_width
        # A softly squared cobble with a cool bottom edge and one lit plane.
        if abs(along)**2.65 + abs(across)**2.65 < 1:
            nu=along*s.tu-across*s.tv
            nv=along*s.tv+across*s.tu
            light = -.90*nu - .35*nv
            if light > .47:
                key = "cream" if s.tone=="warm" else "coolLight"
            elif light < -.50:
                key = "shadow"
            else:
                key = s.tone
            break
    return RGBA[key]

# The eight-to-ten-pixel-deep standalone ellipse has nine deliberately
# spaced setts. A hand-hinted one-pixel joint reads more clearly than sampling
# tiny arcs. All other masks use extended side geometry and continuous paving.
RING = (
    (12,2,"sage", ("..hbbb.",".hbbbbs","..ssdd.")),
    (18,3,"warm", (".hbb..","hbbbb.","..sssd")),
    (22,5,"slate",(".hbb.","hbbbs",".sssd")),
    (22,8,"sage", (".hhb.","hbbbs","bssd.")),
    (17,10,"warm",("..hhbb",".hbbbs","bsssd.")),
    (11,11,"slate",(".hhbbb","hbbbbs",".sssd.")),
    (6,9,"sage",  (".hhbb.","hbbbbs","..sssd")),
    (4,6,"slate", ("..hhbb",".hbbbs","..sssd")),
    (7,4,"warm",  ("..hhbb",".hbbbs","bsssd.")),
)

def single_circle():
    tile=Image.new("RGBA",(32,16))
    for y in range(2,14):
        for x in range(4,28):
            radius=((x-15.5)/11.1)**2+((y-7.6)/5.)**2
            if radius>1:
                continue
            key="soil" if radius<.60 else "soilDark"
            if (x,y) in {(11,7),(12,7),(18,9)}:
                key="soilLight"
            tile.putpixel((x,y),RGBA[key])
    for x,y,tone,rows in RING:
        shades={"h":RGBA["cream" if tone=="warm" else "coolLight"],
                "b":RGBA[tone],"s":RGBA["shadow"],"d":RGBA["joints"]}
        for iy,row in enumerate(rows):
            for ix,value in enumerate(row):
                if value!=".":
                    tile.putpixel((x+ix,y+iy),shades[value])
    return tile

def frame(mask):
    if mask==0:
        return single_circle()
    tile=Image.new("RGBA",(32,16))
    stones=curb_stones(mask)
    for y in range(16):
        for x in range(32):
            across=(x+.5-16)/32
            down=(y+.5)/16
            u, v=down+across, down-across
            if 0<=u<1 and 0<=v<1:
                tile.putpixel((x,y), color_at(u,v,mask,stones))
    return tile

def build():
    atlas=Image.new("RGBA",(128,64))
    for mask in range(16):
        atlas.paste(frame(mask),((mask%4)*32,(mask//4)*16))
    ATLAS.parent.mkdir(parents=True,exist_ok=True)
    atlas.save(ATLAS,optimize=True)
    return atlas

if __name__=="__main__":
    build()
