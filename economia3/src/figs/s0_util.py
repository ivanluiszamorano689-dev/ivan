"""Ayudas para los diagramas de §0 y §4 del Paso a paso (prefijo s0_). No genera figuras por sí solo."""
import sys
import textwrap

sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403,E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon  # noqa: E402

DARK = {"blue": "#184f95", "orange": "#a8431b", "aqua": "#0f6e4c", "yellow": "#8a5d00",
        "violet": "#3a2d86", "red": "#a82b2a", "green": "#006100", "ink": C["ink"], "gray": C["ink2"]}
BG = {"blue": C["blue_bg"], "orange": C["orange_bg"], "aqua": C["aqua_bg"], "yellow": C["yellow_bg"],
      "violet": C["violet_bg"], "red": C["red_bg"], "green": C["green_bg"], "gray": C["gray_bg"], "white": "#ffffff"}
MID = {"blue": C["blue"], "orange": C["orange"], "aqua": C["aqua"], "yellow": C["yellow"], "violet": C["violet"],
       "red": C["red"], "green": C["green"], "gray": C["ink3"], "ink": C["ink"]}


def canvas(w, h, W=100.0):
    """Lienzo en coordenadas 0..W (x) y 0..H (y) con aspecto 1:1."""
    fig = plt.figure(figsize=(w, h))
    ax = fig.add_axes([0, 0, 1, 1])
    H = W * h / w
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax, H


def rbox(ax, x, y, w, h, color="blue", fill="bg", lw=1.3, r=1.4, ec=None, z=2, ls="-"):
    fc = {"bg": BG.get(color, "#ffffff"), "solid": MID.get(color, color), "white": "#ffffff"}.get(fill, fill)
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


def txt(ax, x, y, s, size=8.5, color=None, weight="normal", ha="center", va="center", n=None, ls=1.25,
        style="normal", z=5, **kw):
    return ax.text(x, y, wrap(s, n), fontsize=size, color=color or C["ink"], fontweight=weight, ha=ha, va=va,
                   linespacing=ls, fontstyle=style, zorder=z, **kw)


def arr(ax, p0, p1, color=None, lw=1.4, rad=0.0, ms=10, style="-|>", z=3, ls="-"):
    a = FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms, color=color or C["ink2"], lw=lw,
                        connectionstyle=f"arc3,rad={rad}", zorder=z, linestyle=ls, shrinkA=0, shrinkB=0)
    ax.add_patch(a)
    return a


def elbow(ax, p0, p1, color=None, lw=1.3, xm=None, z=3):
    """Conector en codo: horizontal hasta xm, vertical, horizontal hasta p1 (con flecha)."""
    x0, y0 = p0
    x1, y1 = p1
    xm = (x0 + x1) / 2 if xm is None else xm
    ax.plot([x0, xm, xm], [y0, y0, y1], color=color or C["ink2"], lw=lw, zorder=z, solid_capstyle="butt")
    arr(ax, (xm, y1), (x1, y1), color=color, lw=lw, z=z)


def diamond(ax, x, y, w, h, color="orange", fill="bg", lw=1.3, z=2):
    pts = [(x, y + h / 2), (x + w / 2, y), (x, y - h / 2), (x - w / 2, y)]
    fc = {"bg": BG.get(color, "#fff"), "white": "#fff"}.get(fill, fill)
    ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=MID.get(color, color), lw=lw, zorder=z))


def num_badge(ax, x, y, s, color="violet", r=1.9, size=8.5):
    from matplotlib.patches import Circle
    ax.add_patch(Circle((x, y), r, fc=MID.get(color, color), ec="white", lw=1.0, zorder=6))
    txt(ax, x, y, s, size=size, color="white", weight="bold", z=7)


def comma(v, d=2):
    return f"{v:.{d}f}".replace(".", ",")
