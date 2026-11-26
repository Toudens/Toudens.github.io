"""Render the two FM examples at 2x their 372px article display width.

Chinese uses SimSun; Latin letters and numbers use Times New Roman. Both
themes have an identical transparent canvas, so the article controls its size.
Every color is neutral gray; solid/dashed lines and filled/open markers carry
the distinctions even when the figure is printed without color.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np


OUTPUT = Path(__file__).resolve().parents[2] / "content/papers/FlowMatching"
LATIN_PATH = Path("C:/Windows/Fonts/times.ttf")
CHINESE_PATH = Path("C:/Windows/Fonts/simsun.ttc")
assert LATIN_PATH.exists() and CHINESE_PATH.exists()
LATIN = FontProperties(fname=str(LATIN_PATH), size=9.2)
CHINESE = FontProperties(fname=str(CHINESE_PATH), size=9.2)
THEMES = {
    "light": {
        "ink": "#383838", "muted": "#737373", "primary": "#505050",
        "grid": "#dadada", "axis": "#999999",
    },
    "dark": {
        "ink": "#d0d0d0", "muted": "#a2a2a2", "primary": "#c0c0c0",
        "grid": "#464646", "axis": "#7b7b7b",
    },
}

plt.rcParams.update({
    "font.family": "Times New Roman", "font.size": 9.2,
    "axes.unicode_minus": False, "figure.facecolor": "none",
    "axes.facecolor": "none", "savefig.facecolor": "none",
})


def canvas(title, limits, ticks, colors):
    fig, ax = plt.subplots(figsize=(3.72, 2.66), dpi=200)
    fig.subplots_adjust(left=0.145, right=0.95, bottom=0.18, top=0.82)
    fig.text(0.145, 0.94, title, fontproperties=CHINESE,
             color=colors["ink"], va="center")
    ax.set_xlim(-0.035, 1.035)
    ax.set_ylim(*limits)
    ax.set_xticks([0, 0.5, 1], ["0", "0.5", "1"])
    ax.set_yticks(ticks, [f"{value:g}" for value in ticks])
    ax.set_xlabel("t", fontproperties=LATIN, color=colors["ink"], labelpad=2)
    ax.set_ylabel("x", fontproperties=LATIN, color=colors["ink"], labelpad=4)
    ax.grid(color=colors["grid"], linewidth=0.45, zorder=0)
    ax.set_axisbelow(True)
    for side in ["top", "right"]:
        ax.spines[side].set_visible(False)
    for side in ["left", "bottom"]:
        ax.spines[side].set_color(colors["axis"])
        ax.spines[side].set_linewidth(0.55)
    ax.tick_params(colors=colors["muted"], length=2.5, width=0.55, pad=3)
    for item in ax.get_xticklabels() + ax.get_yticklabels():
        item.set_fontproperties(LATIN)
    return fig, ax


def label(ax, text, point, offset, color, arrow=False, align="left"):
    return ax.annotate(
        text, xy=point, xytext=offset, textcoords="offset points",
        fontproperties=LATIN, color=color, ha=align, va="center",
        arrowprops={"arrowstyle": "-", "color": color, "lw": 0.55,
                    "shrinkA": 3, "shrinkB": 3} if arrow else None,
        zorder=5,
    )


def save(fig, stem, theme, description):
    suffix = "-dark" if theme == "dark" else ""
    fig.savefig(OUTPUT / f"{stem}{suffix}.png", transparent=True,
                metadata={"Description": description})
    plt.close(fig)


def training_figure(theme):
    colors = THEMES[theme]
    fig, ax = canvas("同一中点，不同速度", (-0.2, 3.35),
                     [0, 1, 1.5, 2, 3], colors)
    t = np.linspace(0, 1, 101)
    ax.plot(t, 3 * t, color=colors["primary"], lw=0.95, zorder=3)
    ax.plot(t, 1 + t, color=colors["muted"], lw=0.8,
            linestyle=(0, (3, 2.5)), zorder=2)
    ax.plot([0, 1], [0, 3], "o", color=colors["primary"], ms=2.7, zorder=4)
    ax.plot([0, 1], [1, 2], "o", color=colors["muted"], ms=3.1,
            mfc="none", mew=0.65, zorder=4)
    ax.plot(0.5, 1.5, "o", color=colors["ink"], ms=3.1, zorder=5)
    label(ax, "A: u = 3", (0.76, 2.28), (-28, 23), colors["primary"])
    label(ax, "B: u = 1", (0.10, 1.85), (0, 0), colors["muted"])
    label(ax, "(0.5, 1.5)", (0.5, 1.5), (16, -29),
          colors["ink"], arrow=True)
    save(fig, "fm-example-training", theme,
         "Article example: A x=3t; B x=1+t; both pass (0.5,1.5). "
         "Neutral grayscale with solid/filled A and dashed/open B. "
         "SimSun Chinese and Times New Roman Latin; transparent 744x532 PNG.")


def generation_figure(theme):
    colors = THEMES[theme]
    fig, ax = canvas("两次欧拉更新", (-1.25, 1.85),
                     [-1, 0, 0.5, 1.5], colors)
    fig.text(0.95, 0.94, "h = 0.5", fontproperties=LATIN,
             color=colors["muted"], ha="right", va="center")
    times = np.array([0.0, 0.5, 1.0])
    states = np.array([-1.0, 0.5, 1.5])
    ax.plot(times, states, color=colors["primary"], lw=0.95,
            marker="o", markersize=3, zorder=3)
    label(ax, "v = 3", (0.2, -0.4), (-3, 20), colors["primary"])
    label(ax, "v = 2", (0.76, 1.02), (-9, 19), colors["primary"])
    label(ax, "(0.5, 0.5)", (0.5, 0.5), (9, -18), colors["ink"])
    save(fig, "fm-example-euler", theme,
         "Article example: Euler (t,x)=(0,-1),(0.5,0.5),(1,1.5); "
         "velocities 3 and 2. Neutral grayscale, transparent 744x532 PNG.")
    np.testing.assert_allclose(np.diff(states) / np.diff(times), [3, 2])


if __name__ == "__main__":
    assert 0.5 * 0 + 0.5 * 3 == 0.5 * 1 + 0.5 * 2 == 1.5
    for theme in THEMES:
        training_figure(theme)
        generation_figure(theme)
