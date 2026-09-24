"""Ayudas para los diagramas del Tema 1 (prefijo t1_). No genera figuras por sí solo."""
import sys
import textwrap

sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403,E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle  # noqa: E402

DARK = {"blue": "#184f95", "orange": "#a8431b", "aqua": "#0f6e4c", "yellow": "#8a5d00",
        "violet": "#3a2d86", "red": "#a82b2a", "green": "#006100", "ink": C["ink"], "gray": C["ink2"]}
BG = {"blue": C["blue_bg"], "orange": C["orange_bg"], "aqua": C["aqua_bg"], "yellow": C["yellow_bg"],
      "violet": C["violet_bg"], "red": C["red_bg"], "green": C["green_bg"], "gray": C["gray_bg"], "white": "#ffffff"}
MID = {"blue": C["blue"], "orange": C["orange"], "aqua": C["aqua"], "yellow": C["yellow"], "violet": C["violet"],
       "red": C["red"], "green": C["green"], "gray": C["ink3"], "ink": C["ink"]}


def canvas(w, h, W=100.0):
    """Lienzo para diagramas: coordenadas 0..W en x y 0..H en y, con aspecto 1:1."""
    fig = plt.figure(figsize=(w, h))
    ax = fig.add_axes([0, 0, 1, 1])
    H = W * h / w
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax, H


def rbox(ax, x, y, w, h, color="blue", fill=None, lw=1.4, r=1.6, ec=None, z=2, ls="-"):
    """Caja redondeada. fill: 'bg' (fondo claro del color), 'solid', 'white' o un hex."""
    fc = {"bg": BG.get(color, "#ffffff"), "solid": MID.get(color, color), "white": "#ffffff", None: BG.get(color, "#fff")}.get(fill, fill)
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc,
                       ec=ec if ec is not None else MID.get(color, color), lw=lw, zorder=z, ls=ls)
    ax.add_patch(p)
    return p


def wrap(s, n):
    if n is None:
        return s
    out = []
    for par in s.split("\n"):
        out.extend(textwrap.wrap(par, n) or [""])
    return "\n".join(out)


def txt(ax, x, y, s, size=8.5, color=None, weight="normal", ha="center", va="center", n=None, ls=1.28,
        style="normal", z=5, **kw):
    return ax.text(x, y, wrap(s, n), fontsize=size, color=color or C["ink"], fontweight=weight, ha=ha, va=va,
                   linespacing=ls, fontstyle=style, zorder=z, **kw)


def arr(ax, p0, p1, color=None, lw=1.6, rad=0.0, ms=11, style="-|>", z=3, ls="-", shrinkA=0, shrinkB=0):
    a = FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms, color=color or C["ink2"], lw=lw,
                        connectionstyle=f"arc3,rad={rad}", zorder=z, linestyle=ls, shrinkA=shrinkA, shrinkB=shrinkB)
    ax.add_patch(a)
    return a


def pill(ax, x, y, s, color="violet", size=7.6, pad_x=1.2, h=3.0, fill="bg", weight="bold", tcolor=None, w=None):
    """Etiqueta redondeada centrada en (x, y). El ancho se estima por cantidad de caracteres."""
    unit_pt = ax.figure.get_figwidth() * 72 / ax.get_xlim()[1]
    width = w if w is not None else len(s) * size * 0.56 / unit_pt + 2 * pad_x
    rbox(ax, x - width / 2, y - h / 2, width, h, color, fill=fill, lw=1.0, r=h / 2)
    txt(ax, x, y, s, size=size, color=tcolor or DARK.get(color, C["ink"]), weight=weight)
    return width
