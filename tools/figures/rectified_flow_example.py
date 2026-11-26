"""Render the RF teacher/reflow example for a 372px article column.

Chinese uses SimSun; Latin letters and numbers use Times New Roman. Light and
dark images share a transparent 744x572 canvas and exact time coordinates.
All pixels are neutral grayscale; line patterns and filled/open markers
distinguish the teacher, second round, and first-round Euler approximation.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.lines import Line2D
import numpy as np


OUTPUT = Path(__file__).resolve().parents[2] / "content/papers/RectifiedFlow"
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


def label(ax, text, point, offset, color):
    ax.annotate(
        text, xy=point, xytext=offset, textcoords="offset points",
        fontproperties=LATIN, color=color, va="center",
        arrowprops={"arrowstyle": "-", "color": color, "lw": 0.55,
                    "shrinkA": 3, "shrinkB": 3}, zorder=5,
    )


def draw(theme):
    colors = THEMES[theme]
    fig, ax = plt.subplots(figsize=(3.72, 2.86), dpi=200)
    fig.subplots_adjust(left=0.145, right=0.95, bottom=0.17, top=0.76)
    fig.text(0.145, 0.96, "老师轨迹与重新配对", fontproperties=CHINESE,
             color=colors["ink"], va="center")
    ax.set_xlim(-0.035, 1.035)
    ax.set_ylim(0.8, 3.3)
    ax.set_xticks([0, 0.5, 1], ["0", "0.5", "1"])
    ax.set_yticks([1, 2, 3], ["1", "2", "3"])
    ax.set_xlabel("t", fontproperties=LATIN, color=colors["ink"], labelpad=2)
    ax.set_ylabel("Z", fontproperties=LATIN, color=colors["ink"], labelpad=5)
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

    t = np.linspace(0, 1, 401)
    teacher = 2 * t + np.sqrt((1 - t) ** 2 + t**2)
    second_round = 1 + 2 * t
    first_step = 1 + t
    ax.plot(t, teacher, color=colors["ink"], lw=0.8, zorder=3)
    ax.plot(t, second_round, color=colors["primary"], lw=1.0,
            linestyle=(0, (4, 2)), zorder=2)
    ax.plot(t, first_step, color=colors["muted"], lw=0.8,
            linestyle=(0, (1, 2.5)), zorder=2)
    middle = 1 + 1 / np.sqrt(2)
    ax.plot([0, 1], [1, 3], "o", color=colors["ink"], ms=3, zorder=4)
    ax.plot(1, 2, "s", color=colors["muted"], ms=3.1,
            mfc="none", mew=0.65, zorder=4)
    ax.plot(0.5, middle, "o", color=colors["ink"], ms=2.8, zorder=4)
    ax.plot(0.5, 2, "o", color=colors["primary"], ms=3.1,
            mfc="none", mew=0.65, zorder=4)
    label(ax, "1.71", (0.5, middle), (17, -22), colors["ink"])
    label(ax, "2", (0.5, 2), (-18, 21), colors["primary"])

    handles = [
        Line2D([0], [0], color=colors["ink"], lw=0.8),
        Line2D([0], [0], color=colors["primary"], lw=1.0,
               linestyle=(0, (4, 2))),
        Line2D([0], [0], color=colors["muted"], lw=0.8,
               linestyle=(0, (1, 2.5))),
    ]
    fig.legend(handles, ["老师轨迹", "第二轮", "第一轮一步"],
               loc="upper left", bbox_to_anchor=(0.125, 0.905), ncol=3,
               frameon=False, prop=CHINESE, labelcolor=colors["ink"],
               handlelength=1.15, handletextpad=0.4, columnspacing=0.8,
               borderaxespad=0)
    suffix = "-dark" if theme == "dark" else ""
    fig.savefig(OUTPUT / f"rf-example-reflow{suffix}.png", transparent=True,
                metadata={"Description":
                    "Article example: teacher Z=2t+sqrt((1-t)^2+t^2), "
                    "round 2 Z=1+2t, first-round one-step Euler Z=1+t. "
                    "Neutral grayscale: teacher solid/filled, second round "
                    "dashed/open, Euler dotted/open square. Transparent "
                    "744x572 PNG; SimSun and Times New Roman."})
    plt.close(fig)
    np.testing.assert_allclose(teacher[[0, 200, 400]], [1, middle, 3])
    np.testing.assert_allclose(second_round[[0, 200, 400]], [1, 2, 3])
    np.testing.assert_allclose(first_step[[0, 400]], [1, 2])


if __name__ == "__main__":
    for theme in THEMES:
        draw(theme)
