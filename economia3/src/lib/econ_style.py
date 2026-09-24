"""Estilo común para todos los gráficos (matplotlib -> SVG).

Uso típico en un script de figs/:

    import sys; sys.path.insert(0, "../lib")
    from econ_style import *
    fig, ax = new_fig(w=6.2, h=3.6)
    ax.plot(k, f(k), color=C["blue"], lw=LW)
    econ_axes(ax, xlabel=r"$k$", ylabel=r"$y$")
    save(fig, "solow_basico")        # -> figs/out/solow_basico.svg

Reglas (ver COMPONENTES.md):
  * Colores en orden fijo: blue, orange, aqua (los tres primeros son seguros
    para daltonismo en cualquier combinación). Más de 3 series: agregar
    estilo de línea / marcador como segunda codificación.
  * Líneas de 2 px (LW), grilla ausente o muy tenue, ejes como flechas.
  * Etiquetas directas sobre las curvas (label_curve) en lugar de leyendas
    cuando hay <= 4 series. Texto siempre en tinta, nunca del color de la serie
    salvo el rótulo corto pegado a la curva.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
import numpy as np  # noqa: E402

_FONTS = Path(__file__).resolve().parent.parent / "assets" / "fonts"
for f in _FONTS.glob("Inter-*.ttf"):
    font_manager.fontManager.addfont(str(f))

OUT = Path(__file__).resolve().parent.parent / "figs" / "out"
OUT.mkdir(parents=True, exist_ok=True)

C = {
    "blue": "#2a78d6", "orange": "#eb6834", "aqua": "#1baf7a", "yellow": "#eda100",
    "magenta": "#e87ba4", "green": "#008300", "violet": "#4a3aa7", "red": "#e34948",
    "ink": "#1d1d1b", "ink2": "#52514e", "ink3": "#7a7974", "rule": "#d9d7d0",
    "blue_bg": "#eef5fd", "orange_bg": "#fdf1ea", "aqua_bg": "#e8f7f0", "violet_bg": "#f1effb",
    "red_bg": "#fdeeee", "yellow_bg": "#fdf6e2", "green_bg": "#e9f5e9", "gray_bg": "#f0efec",
}
SERIES = [C["blue"], C["orange"], C["aqua"], C["yellow"], C["magenta"], C["green"], C["violet"], C["red"]]
LW = 2.0

plt.rcParams.update({
    "font.family": "Inter",
    "font.size": 9.5,
    "mathtext.fontset": "cm",
    "axes.edgecolor": C["ink2"],
    "axes.labelcolor": C["ink"],
    "axes.linewidth": 0.9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titlesize": 10.5,
    "axes.titleweight": "bold",
    "axes.titlelocation": "left",
    "axes.titlepad": 10,
    "xtick.color": C["ink2"],
    "ytick.color": C["ink2"],
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "legend.frameon": False,
    "legend.fontsize": 8.5,
    "svg.fonttype": "path",
    "figure.dpi": 100,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.06,
    "lines.solid_capstyle": "round",
})


def new_fig(w=6.2, h=3.6, ncols=1, nrows=1, **kw):
    fig, ax = plt.subplots(nrows, ncols, figsize=(w, h), **kw)
    return fig, ax


def econ_axes(ax, xlabel="", ylabel="", xlim=None, ylim=None, ticks=False):
    """Ejes 'de pizarrón': solo los dos ejes con flecha, sin ticks numéricos
    (salvo ticks=True). Rótulos al final de cada eje."""
    if xlim:
        ax.set_xlim(*xlim)
    if ylim:
        ax.set_ylim(*ylim)
    ax.spines["left"].set_position(("data", ax.get_xlim()[0]))
    ax.spines["bottom"].set_position(("data", ax.get_ylim()[0]))
    ax.plot(1, ax.get_ylim()[0], ">", transform=ax.get_yaxis_transform(), clip_on=False, color=C["ink2"], ms=5)
    ax.plot(ax.get_xlim()[0], 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color=C["ink2"], ms=5)
    if not ticks:
        ax.set_xticks([])
        ax.set_yticks([])
    ax.set_xlabel(xlabel, loc="right", fontsize=10.5)
    ax.set_ylabel(ylabel, loc="top", rotation=0, fontsize=10.5, labelpad=-4)
    ax.yaxis.set_label_coords(-0.01, 1.02)
    return ax


def data_axes(ax, xlabel="", ylabel="", grid=True):
    """Ejes para datos reales (con ticks y grilla horizontal tenue)."""
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if grid:
        ax.grid(axis="y", color="#ebe9e3", lw=0.8)
        ax.set_axisbelow(True)
    return ax


def label_curve(ax, x, y, text, color, dx=0, dy=0, ha="left", va="center", size=9.5, weight="bold"):
    ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points", color=color,
                ha=ha, va=va, fontsize=size, fontweight=weight)


def vguide(ax, x, y, label=None, color=None, y0=None, size=9.5, dy=-12):
    """Línea guía punteada desde el eje x hasta (x, y) con rótulo en el eje."""
    y0 = ax.get_ylim()[0] if y0 is None else y0
    ax.plot([x, x], [y0, y], ls=(0, (3, 3)), lw=0.9, color=color or C["ink3"])
    if label:
        ax.annotate(label, (x, y0), xytext=(0, dy), textcoords="offset points", ha="center", va="top",
                    fontsize=size, color=C["ink"])


def hguide(ax, x, y, label=None, color=None, x0=None, size=9.5, dx=-6):
    x0 = ax.get_xlim()[0] if x0 is None else x0
    ax.plot([x0, x], [y, y], ls=(0, (3, 3)), lw=0.9, color=color or C["ink3"])
    if label:
        ax.annotate(label, (x0, y), xytext=(dx, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=size, color=C["ink"])


def point(ax, x, y, color=None, label=None, dx=6, dy=6, ha="left", size=9):
    ax.plot([x], [y], "o", ms=6.5, color=color or C["ink"], mec="white", mew=1.6, zorder=5)
    if label:
        ax.annotate(label, (x, y), xytext=(dx, dy), textcoords="offset points", ha=ha, fontsize=size,
                    color=C["ink"], fontweight="bold")


def arrow(ax, x0, y0, x1, y1, color=None, lw=1.4, both=False):
    style = "<|-|>" if both else "-|>"
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=style, color=color or C["ink2"], lw=lw, shrinkA=0, shrinkB=0,
                                mutation_scale=9))


def save(fig, name):
    path = OUT / f"{name}.svg"
    fig.savefig(path, format="svg", metadata={"Date": None})
    plt.close(fig)
    return path
