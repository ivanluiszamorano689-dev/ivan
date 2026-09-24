"""Ayudas para los gráficos y diagramas del Tema 2 (prefijo t2_).

No genera nada por sí solo: lo importan los scripts t2_*.py.
"""
import sys

sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403,E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402


def fmt(v, d=0):
    """Número con coma decimal y punto de miles: fmt(1234.5, 1) -> '1.234,5'."""
    s = f"{v:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def comma_axis(ax, axis="y", d=2):
    f = plt.FuncFormatter(lambda v, p: fmt(v, d))
    (ax.yaxis if axis == "y" else ax.xaxis).set_major_formatter(f)


def canvas(w, h):
    """Lienzo para diagramas: unidades = pulgadas, sin ejes."""
    fig, ax = plt.subplots(figsize=(w, h))
    fig.subplots_adjust(0, 0, 1, 1)
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.axis("off")
    return fig, ax


def rbox(ax, x, y, w, h, fc="white", ec=None, lw=1.3, r=0.08, ls="-", z=2):
    """Caja redondeada con esquina inferior izquierda en (x, y)."""
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc,
                       ec=ec or C["ink3"], lw=lw, ls=ls, zorder=z)
    ax.add_patch(p)
    return p


def txt(ax, x, y, s, size=9, color=None, weight="normal", ha="center", va="center", z=4, **kw):
    return ax.text(x, y, s, fontsize=size, color=color or C["ink"], fontweight=weight, ha=ha, va=va,
                   zorder=z, **kw)


def arr(ax, x0, y0, x1, y1, color=None, lw=1.3, style="-|>", rad=0.0, ms=10, z=3):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), zorder=z,
                arrowprops=dict(arrowstyle=style, color=color or C["ink2"], lw=lw, shrinkA=0, shrinkB=0,
                                mutation_scale=ms, connectionstyle=f"arc3,rad={rad}"))


def hbar_labels(ax, bars, labels, dx=4, color=None, size=8.5, inside=False):
    for b, lab in zip(bars, labels):
        w = b.get_width()
        y = b.get_y() + b.get_height() / 2
        if inside:
            ax.annotate(lab, (w, y), xytext=(-dx, 0), textcoords="offset points", ha="right", va="center",
                        fontsize=size, color="white", fontweight="bold")
        else:
            ax.annotate(lab, (w, y), xytext=(dx if w >= 0 else -dx, 0), textcoords="offset points",
                        ha="left" if w >= 0 else "right", va="center", fontsize=size, color=color or C["ink"])


def clean_hbar(ax, xlabel=""):
    """Barras horizontales: sin eje y visible, grilla vertical tenue."""
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color="#ebe9e3", lw=0.8)
    ax.set_axisbelow(True)
    ax.set_xlabel(xlabel)
