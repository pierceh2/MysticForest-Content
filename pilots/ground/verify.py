"""Validate shipped atlas bytes, pack-equivalent shapes and four-way seams. Requires Pillow."""
from pathlib import Path
from math import floor
import json
from PIL import Image
ROOT=Path(__file__).resolve().parent
DATA=ROOT/'surfaces'
M=json.loads((DATA/'atlas.json').read_text())
assert M['connectionMask']['bits']=={'minusU':1,'plusU':2,'minusV':4,'plusV':8}
assert M['geometry']['screenStepU']==[16,8] and M['geometry']['screenStepV']==[-16,8]
groups = M['mergeGroupByItem']
fixture = json.loads((ROOT / 'OBJECT_TYPES.preview.json').read_text())
items = {item['key']: item['mergeGroup'] for item in fixture['debugItems']}
assert groups == items == {'dirt_patch': 'soil', 'dirt_rows': 'soil', 'cobblestone_circle': 'stone'}
assert set(M['itemKeys']) == set(items)
assert M['formatVersion'] == 2 and M['image']['tileSize'] == [32, 16]
assert all(set(case['ownedGroundItems']) == set(items) for case in fixture['debugSpellFixtures'])
ASSETS={}
for pack,entry in M['packAssets'].items():
    ASSETS[pack]={}
    for key,file in entry['atlases'].items():
        img=Image.open(DATA/file)
        assert img.mode=='RGBA' and img.size==(128,64)
        frames=[img.crop((32*(i%4),16*(i//4),32*(i%4)+32,16*(i//4)+16)) for i in range(16)]
        ASSETS[pack][key]=frames
        for frame in frames:
            colors=frame.getcolors(512)
            assert {c[-1] for count,c in colors}=={0,255} and len(colors)<=17
            assert all(c==(0,0,0,0) for count,c in colors if c[-1]==0)
assert set(ASSETS)=={'default8bit','winter','fall'}
base = ASSETS['default8bit']
assert set(base) == set(items)
soil_keys = {key for key, group in groups.items() if group == 'soil'}
assert all(set(ASSETS[pack]) == soil_keys for pack in ('fall', 'winter'))
ref=base['dirt_patch']
for pack, items in ASSETS.items():
    for key,frames in items.items():
        if groups[key] != 'soil':
            continue
        for m,frame in enumerate(frames):
            assert frame.getchannel('A').tobytes()==ref[m].getchannel('A').tobytes()
        assert len({f.getchannel('A').tobytes() for f in frames})==16
        if key=='dirt_rows':
            assert all(a.tobytes()!=b.tobytes() for a,b in zip(frames,items['dirt_patch']))
        if pack!='default8bit':
            assert all(a.tobytes()!=b.tobytes() for a,b in zip(frames,ASSETS['default8bit'][key]))

DIFFS=((-1,0,1),(1,0,2),(0,-1,4),(0,1,8))
def mask_for(layout, u, v):
    """Derive one frame index from this saved day's surface keys."""
    group = groups.get(layout.get((u, v)))
    if group is None or not (0 <= u < 6 and 0 <= v < 6):
        return 0
    mask = 0
    for du, dv, bit in DIFFS:
        x, y = u + du, v + dv
        if 0 <= x < 6 and 0 <= y < 6 and groups.get(layout.get((x, y))) == group:
            mask |= bit
    return mask

def uv(x,y):
    return (y+.5)/16+(x+.5)/32,(y+.5)/16-(x+.5)/32

def atlas_position(u,v):
    return (-16+16*(u-v),8*(u+v))

def fill(frame,x,y):
    return frame.getpixel((x,y))

# A fully joined tile must tessellate exactly. Any tile edit relative to a
# full-mask frame must lie close to a genuinely exposed side. Each mask must
# remove grass-space and rim on its own side without altering the furrow phase.
for pack,types in ASSETS.items():
    for key,frames in types.items():
        if groups[key] != 'soil':
            continue
        assert sum(n for n,c in frames[15].getcolors(512) if c[3])==256
        for mask,frame in enumerate(frames):
            for y in range(16):
                for x in range(32):
                    u,v=uv(x-16,y)
                    within=0<=u<1 and 0<=v<1
                    baseline=fill(frames[15],x,y)
                    observed=fill(frame,x,y)
                    assert bool(baseline[3])==within
                    if not within:
                        assert observed[3]==0
                        continue
                    nonjoining=[d for bit,d in [(1,u),(2,1-u),(4,v),(8,1-v)] if not mask&bit]
                    if min(nonjoining,default=1)>.125:
                        assert observed==baseline, (pack,key,mask,x,y)
                    if min(nonjoining,default=1)<.025:
                        assert observed[3]==0
assert len(set(ref[0].getchannel('A').tobytes()) - {0,255})==0

layouts=[
 {(0,0),(1,0),(0,1),(1,1)},
 {(0,0),(1,0),(0,1)},
 {(0,0),(1,0),(2,0)},
 {(0,0),(1,1)}
]
for cells in layouts:
    day = dict.fromkeys(cells, 'dirt_patch')
    lookup={p:mask_for(day,*p) for p in cells}
    if cells=={(0,0),(1,1)}:
        assert set(lookup.values())=={0}
    for x in range(-64,64):
        for y in range(-4,64):
            u,v=uv(x,y);owner=(floor(u),floor(v))
            # Independently composite the projected tiles and ensure every
            # opaque pixel has exactly one owner. A shared edge with no exposed
            # side in its vicinity must draw the fully joined tile's color.
            seen=[]
            for p,m in lookup.items():
                left,top=atlas_position(*p);a,b=x-left,y-top
                if 0<=a<32 and 0<=b<16 and fill(ref[m],a,b)[3]:
                    seen.append(p)
            assert len(seen)<=1 and all(p==owner for p in seen)
            if owner in cells:
                fu,fv=u-owner[0],v-owner[1]
                edge=[d for (du,dv,_),d in zip(DIFFS,[fu,1-fu,fv,1-fv]) if (owner[0]+du,owner[1]+dv) not in cells]
                if min(edge,default=1)>.125:
                    assert seen==[owner]
# A perpendicular transect of the fully tilled tile must encounter two
# separate bands of deep furrow soil, repeated at a half-cell in v.
for pack,items in ASSETS.items():
    frame=items['dirt_rows'][15];deep=frame.getpixel((16,0))[:3]
    colors=[c[:3] for n,c in frame.getcolors(512) if c[3]]
    deep=min(colors,key=lambda c:sum(c))
    coords=[uv(x-16,y) for y in range(16) for x in range(32) if frame.getpixel((x,y))[:3]==deep]
    assert all(min(v%.5,.5-v%.5)<.10 for u,v in coords)
    assert any(0<v<.12 for u,v in coords) and any(.49<v<.62 for u,v in coords)
# Stone uses a rounded ring in the isolated frame. Its connected side faces
# meet at the same texels as its fully paved courtyard.
stone_key = 'cobblestone_circle'
stone = base[stone_key]
assert len({frame.tobytes() for frame in stone}) == 16
for mask, frame in enumerate(stone):
    day = {(2, 2): stone_key}
    day.update({(2 + du, 2 + dv): stone_key for du, dv, bit in DIFFS if mask & bit})
    assert mask_for(day, 2, 2) == mask
    for y in range(16):
        for x in range(32):
            u, v = uv(x - 16, y)
            pixel = frame.getpixel((x, y))
            if not (0 <= u < 1 and 0 <= v < 1):
                assert pixel[3] == 0
                continue
            if mask == 15:
                assert pixel[3] == 255
            for bit, normal, tangent in ((1, u, v), (2, 1-u, v), (4, v, u), (8, 1-v, u)):
                if mask & bit and normal < .07 and .37 < tangent < .63:
                    assert pixel[3] == 255 and pixel == stone[15].getpixel((x, y))

for cells in [*layouts, {(0, 0)}, {(1, 0), (1, 1), (1, 2)}]:
    day = dict.fromkeys(cells, stone_key)
    occupied = set()
    for (u, v) in day:
        frame = stone[mask_for(day, u, v)]
        left, top = atlas_position(u, v)
        for y in range(16):
            for x in range(32):
                if frame.getpixel((x, y))[3]:
                    point = (left + x, top + y)
                    assert point not in occupied
                    a, b = uv(*point)
                    assert (floor(a), floor(b)) == (u, v)
                    occupied.add(point)
    assert occupied

# Coordinate boundaries and material boundaries must both be honored when
# a cell changes under foreground objects. Unknown surface keys stay isolated.
day = {(0, 0): stone_key, (1, 0): stone_key, (2, 0): 'dirt_patch',
       (3, 0): 'dirt_rows', (4, 0): 'unknown', (-1, 0): stone_key}
assert [mask_for(day, u, 0) for u in range(5)] == [2, 1, 2, 1, 0]
day[1, 0] = 'dirt_rows'
assert [mask_for(day, u, 0) for u in range(4)] == [0, 2, 3, 1]
del day[2, 0]
assert [mask_for(day, u, 0) for u in range(4)] == [0, 0, 0, 0]
assert mask_for({(5, 5): stone_key, (6, 5): stone_key, (5, 6): stone_key}, 5, 5) == 0
print('PASS: 112 frames in seven hard-alpha atlases; six soil atlases and one base stone atlas')
print('PASS: all 16 masks, projected footprint and nearest-neighbor seam colors')
print('PASS: 2x2, L, line and diagonal-only layouts; tilled phase and mixed-material mask identity')
