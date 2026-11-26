"""Render the DDIM and CFG worked examples as paired light/dark PNGs."""

import math
import os
from functools import cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, PngImagePlugin


PAPERS = Path(__file__).resolve().parents[2] / "content" / "papers"
FONTS = Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts"
W, H, SCALE = 372, 149, 4
STAGES = (41, 180, 315)
PALETTES = {
    "": ("#333333", "#656565", "#bcbcbc"),
    "-dark": ("#dddddd", "#b8b8b8", "#626262"),
}


@cache
def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size * SCALE)


def scaled(points):
    return [(x * SCALE, y * SCALE) for x, y in points]


def dotted(draw, nodes, color):
    travelled = 0
    dash = True
    for a, b in zip(nodes, nodes[1:]):
        length = math.dist(a, b)
        if length == 0:
            continue
        offset = 0
        while offset < length:
            goal = 4 if dash else 3
            advance = min(goal - travelled, length - offset)
            if dash:
                pts = [tuple(a[i] + (b[i] - a[i]) * r / length for i in range(2))
                       for r in (offset, offset + advance)]
                draw.line(scaled(pts), color, width=4)
            offset += advance
            travelled += advance
            if travelled >= goal - 1e-8:
                dash = not dash
                travelled = 0


def diagram(article, name, values, comparison, variant):
    for suffix, (accent, muted, faint) in PALETTES.items():
        image = Image.new("RGBA", (W * SCALE, H * SCALE))
        draw = ImageDraw.Draw(image)

        def label(x, y, text, color, face="simsun.ttc", size=14, anchor="mm"):
            draw.text((x * SCALE, y * SCALE), text, font=font(face, size),
                      fill=color, anchor=anchor)

        def point(x, y, color, hollow=False):
            r = 2.85
            draw.ellipse(scaled([(x - r, y - r), (x + r, y + r)]),
                         fill=(0, 0, 0, 0) if hollow else color,
                         outline=color, width=5)

        def y(value):
            origin, ratio = (104, 330) if variant == "ddim" else (98, 330)
            return origin - ratio * (value - values[0])

        points = list(zip(STAGES, map(y, values)))
        reference = (STAGES[2 if variant == "ddim" else 1], y(comparison))
        dotted(draw, [points[0], reference], muted)
        if variant == "ddim":
            label(126, 91, "直接一步", muted)
            label(236, 25, "两步采样", accent)
            label(324, 16, f"{comparison:.2f}", muted, "times.ttf", anchor="lm")
            label(325, 43, f"{values[2]:.2f}", accent, "times.ttf", anchor="lm")
            label(180, 34, f"{values[1]:.2f}", accent, "times.ttf")
        else:
            label(177, 49, f"{values[1]:.2f}", accent, "times.ttf")
            label(325, 31, f"{values[2]:.3f}", accent, "times.ttf", anchor="lm")
            label(190, 84, f"{comparison:.3f}", muted, "times.ttf", anchor="lm")
            label(254, 64, "加强引导", accent)
            label(115, 103, "普通条件", muted)

        draw.line(scaled(points), accent, width=7, joint="curve")
        point(*reference, muted, hollow=True)
        for x, v in points:
            point(x, v, accent)
        label(31 if variant == "ddim" else 38, 87 if variant == "ddim" else 80,
              f"{values[0]:.2f}", accent, "times.ttf")

        for x, operator, stage in zip(STAGES, ("t", "s" if variant == "ddim" else "r", "0"),
                                      ("较高噪声", "较低噪声", "清晰端")):
            draw.line(scaled([(x, 112), (x, 117)]), faint, width=4)
            label(x - 11, 132, stage, muted, size=13)
            label(x + (24 if stage != "清晰端" else 18), 132, operator, muted,
                  "timesi.ttf" if operator.isalpha() else "times.ttf", size=14)

        metadata = PngImagePlugin.PngInfo()
        metadata.add_text("Fonts", "Times New Roman; SimSun")
        image.save(PAPERS / article / (name + suffix + ".png"), pnginfo=metadata, optimize=True)


def ddim_step(state, a_now, b_now, a_next, b_next, epsilon):
    return a_next * (state - b_now * epsilon) / a_now + b_next * epsilon


def guided(empty, conditioned):
    return empty + 2 * (conditioned - empty)


def main():
    ddim_middle = ddim_step(0.76, 0.6, 0.8, 0.8, 0.6, 0.20)
    ddim_end = ddim_step(ddim_middle, 0.8, 0.6, 1, 0, 0.24)
    ddim_direct = ddim_step(0.76, 0.6, 0.8, 1, 0, 0.20)
    diagram("DDIM", "DDIM-jump-example", (0.76, ddim_middle, ddim_end), ddim_direct, "ddim")

    cfg_middle = ddim_step(0.58, 0.6, 0.8, 0.8, 0.6, guided(0.40, 0.30))
    cfg_end = ddim_step(cfg_middle, 0.8, 0.6, 1, 0, guided(0.20, 0.15))
    cfg_cond = ddim_step(0.58, 0.6, 0.8, 0.8, 0.6, 0.30)
    diagram("CFG", "CFG-guidance-example", (0.58, cfg_middle, cfg_end), cfg_cond, "cfg")


if __name__ == "__main__":
    main()
