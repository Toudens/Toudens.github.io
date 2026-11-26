"""Render three teaching figures (Python, Pillow, Windows SimSun and Times New Roman)."""
from math import exp
from pathlib import Path
from random import Random
import os

from PIL import Image, ImageDraw, ImageFont, PngImagePlugin


PAPERS = Path(__file__).resolve().parents[2] / "content" / "papers"
FONTS = Path(os.environ["WINDIR"]) / "Fonts"
S = 3
PALETTES = {"": ("#333333", "#707070", "#202020", "#f1f1f1"),
            "-dark": ("#dddddd", "#ababab", "#ededed", "#292929")}


class Plate:
    def __init__(self, width, height, theme):
        self.theme = theme
        self.ink, self.rule, self.accent, self.wash = PALETTES[theme]
        self.im = Image.new("RGBA", (width*S, height*S), (0,0,0,0))
        self.d = ImageDraw.Draw(self.im)

    def label(self, x, baseline, text, size=14, color=None, center=True):
        groups = []
        for ch in text:
            face = "times.ttf" if ord(ch) < 128 or ch in "×−→" else "simsun.ttc"
            if not groups or groups[-1][0] != face:
                groups.append([face, ch])
            else:
                groups[-1][1] += ch
        runs = [(txt, ImageFont.truetype(str(FONTS / face), size*S)) for face, txt in groups]
        at = x*S - (sum(self.d.textlength(txt, font=f) for txt, f in runs)/2 if center else 0)
        for txt, f in runs:
            self.d.text((round(at), baseline*S), txt, font=f, fill=color or self.ink, anchor="ls")
            at += self.d.textlength(txt, font=f)

    def rect(self, x, y, w, h, color, outline=None, width=1):
        self.d.rectangle((x*S, y*S, (x+w)*S, (y+h)*S), fill=color,
                         outline=outline, width=round(width*S))

    def line(self, x, y, x2, y2, fill=None):
        self.d.line((x*S, y*S, x2*S, y2*S), fill=fill or self.rule, width=2)

    def arrow(self, x, y, x2):
        self.line(x, y, x2, y)
        self.d.polygon([(x2*S,y*S), ((x2-5)*S,(y-3)*S), ((x2-5)*S,(y+3)*S)],fill=self.rule)

    def save(self, article, filename):
        metadata = PngImagePlugin.PngInfo()
        metadata.add_text("Fonts", "Times New Roman; SimSun")
        p = PAPERS / article / filename
        self.im.save(p.with_stem(p.stem + self.theme), pnginfo=metadata, optimize=True)


def dit(theme):
    plate = Plate(372, 115, theme)
    grid = [1.9, -.7, .1, 1.]
    noise = [.5, -.2, .4, -.25]
    clean = [(v-.8*n)/.6 for v,n in zip(grid,noise)]
    next_grid = [.8*v+.6*n for v,n in zip(clean,noise)]
    assert abs(clean[0]-2.5) < 1e-9 and abs(next_grid[0]-2.3) < 1e-9
    for cx, values, label in zip((59,186,313), (grid,clean,next_grid),
                                 ("当前状态","清晰估计","下一状态")):
        x, y = cx-27, 29
        plate.label(cx,17,label,14)
        for j,v in enumerate(values):
            gray = round(174-50*v)
            plate.rect(x+27*(j%2),y+27*(j//2),27,27,(gray,gray,gray),plate.rule)
        plate.rect(x-1,y-1,29,29,None,plate.accent,1.7)
        plate.label(cx,104,f"{values[0]:.1f}",16,plate.accent)
    plate.arrow(102,56,142)
    plate.arrow(230,56,270)
    plate.save("DiT","patch-step-example.png")


SIDE=88


def scene(variant):
    # Two original, intentionally different layouts for the very same prompt.
    im = Image.new("RGB",(SIDE,SIDE),"#f4f1e8")
    d = ImageDraw.Draw(im)
    if variant == 0:
        bx, by, bw, bh = 5, 44, 43, 21
        cx, cy, cw, ch = 54, 28, 19, 32
    else:
        bx, by, bw, bh = 7, 35, 32, 26
        cx, cy, cw, ch = 47, 44, 26, 23
    d.line((2,71,85,71),fill="#c0b7a5",width=1)
    d.chord((bx,by-bh,bx+bw,by+bh),start=0,end=180,fill="#b43d36")
    d.ellipse((bx,by-3,bx+bw,by+3),fill="#eaa294",outline="#9f3832")
    d.rectangle((bx+bw//3, by+bh-1,bx+2*bw//3,by+bh+1),fill="#a63a33")
    d.ellipse((cx+cw-5,cy+3,cx+cw+8,cy+ch-6),outline="#255b80",width=3)
    d.rounded_rectangle((cx,cy,cx+cw,cy+ch),radius=3,fill="#326e98")
    d.ellipse((cx,cy-2,cx+cw,cy+3),fill="#a9c7cd",outline="#255b80")
    return [byte/127.5-1 for byte in im.tobytes()]


def noise(seed, count):
    rng=Random(seed)
    return [rng.gauss(0,1) for _ in range(count)]


def mix(a,b,t):
    return [(1-t)*x+t*y for x,y in zip(a,b)]


def euler(x,t,h,templates):
    # For the equal-prior two-image distribution, compute the conditional mean
    # velocity exactly. The sampler has no per-sample target image.
    scores=[-sum((v-t*y)**2 for v,y in zip(x,im))/(2*(1-t)**2) for im in templates]
    weights=[exp(s-max(scores)) for s in scores]
    p=weights[1]/sum(weights)
    mean=mix(*templates,p)
    return [v+h*(m-v)/(1-t) for v,m in zip(x,mean)], p


def sd3(theme):
    plate=Plate(396,213,theme)
    templates=[scene(0),scene(1)]
    eps=noise(100,len(templates[0]))
    train=[eps,mix(eps,templates[0],.25),templates[0]]
    start=noise(4,len(eps))
    mid, p0=euler(start,0,.5,templates)
    end, p1=euler(mid,.5,.5,templates)
    assert p0==.5
    print("Toy sampler P(second layout) at t=0.5:", p1)
    for title, y, frames, times in (
            ("训练",1,train,("0","0.25","1")),
            ("生成",111,(start,mid,end),("0","0.5","1"))):
        plate.label(23,y+42,title,14)
        for i,(values,t) in enumerate(zip(frames,times)):
            # Only the display clips to [-1,1]; computation uses unrounded values.
            im=Image.frombytes("RGB",(SIDE,SIDE),bytes(round(127.5*(1+max(-1,min(1,v)))) for v in values))
            x=58+119*i
            plate.im.paste(im.resize((75*S,75*S), Image.Resampling.NEAREST),(x*S,(y+2)*S))
            plate.label(x+37.5,y+95,"t = "+t,14)
    plate.save("SD3","rectified-flow-frames.png")


def joint(theme):
    plate=Plate(372,164,theme)
    for x,label,count in [(94,"图像位置","1024"),(278,"文本位置","154")]:
        plate.label(x,17,label+"  "+count)
        plate.label(x,40,"独立投影   Q, K, V",13,plate.rule)
        plate.line(x,49,x,62)
        plate.line(x,113,x,130)
        plate.d.polygon([(x*S,131*S),((x-3)*S,126*S),((x+3)*S,126*S)],fill=plate.rule)
        plate.label(x,152,label+"的输出",14)
    plate.rect(28,63,316,49,plate.wash)
    plate.label(186,84,"一次联合注意力",15,plate.accent)
    plate.label(186,103,"每个位置都可读取图像与文本",13)
    plate.save("SD3","joint-attention.png")


if __name__=="__main__":
    for theme in PALETTES:
        dit(theme)
        sd3(theme)
        joint(theme)
