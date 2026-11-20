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
ref=ASSETS['default8bit']['dirt_patch']
for pack, items in ASSETS.items():
    for key,frames in items.items():
        for m,frame in enumerate(frames):
            assert frame.getchannel('A').tobytes()==ref[m].getchannel('A').tobytes()
        assert len({f.getchannel('A').tobytes() for f in frames})==16
        if key=='dirt_rows':
            assert all(a.tobytes()!=b.tobytes() for a,b in zip(frames,items['dirt_patch']))
        if pack!='default8bit':
            assert all(a.tobytes()!=b.tobytes() for a,b in zip(frames,ASSETS['default8bit'][key]))

DIFFS=((-1,0,1),(1,0,2),(0,-1,4),(0,1,8))
def mask_for(layout,u,v):
    return sum(bit for du,dv,bit in DIFFS if (u+du,v+dv) in layout)

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
    lookup={p:mask_for(cells,*p) for p in cells}
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
print('PASS: six 128x64 hard-alpha atlases, 96 frames; neutral and both seasonal families')
print('PASS: all 16 masks, projected footprint and nearest-neighbor seam colors')
print('PASS: 2x2, L, line and diagonal-only layouts; tilled phase and mixed-material mask identity')
