"""Ayudas comunes para los gráficos del TP4 (prefijo p4).

Correr los scripts desde figs/:  cd figs && python3 p4_b_solow.py
"""
import sys

sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403
from econ_style import C, LW, np, plt  # noqa: F401
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch  # noqa: E402


def dec(v, nd=None):
    """Número con coma decimal (sin separador de miles)."""
    if nd is None:
        s = f"{v:g}"
    else:
        s = f"{v:.{nd}f}"
    return s.replace(".", ",")


def mdec(v, nd=3):
    """Número con coma decimal para usar dentro de mathtext ($...$)."""
    return f"{v:.{nd}f}".replace(".", "{,}")


def comma_fmt(nd=None, pct=False):
    def f(v, p):
        if pct:
            return (f"{v:.{nd or 0}f}".replace(".", ",") + " %")
        return dec(v, nd)
    return plt.FuncFormatter(f)


def bracket(ax, x, y0, y1, text, color, side="right", dx=5, size=8.4, weight="bold", tcolor=None):
    """Flecha doble vertical entre y0 e y1 en x, con rótulo al costado."""
    ax.annotate("", xy=(x, y1), xytext=(x, y0),
                arrowprops=dict(arrowstyle="<|-|>", color=color, lw=1.3, shrinkA=0, shrinkB=0, mutation_scale=8))
    if text:
        ax.annotate(text, (x, (y0 + y1) / 2), xytext=(dx if side == "right" else -dx, 0),
                    textcoords="offset points", ha="left" if side == "right" else "right", va="center",
                    fontsize=size, color=tcolor or C["ink"], fontweight=weight)


def ktick(ax, x, text, y0=None, dy=-4, size=8.4, color=None, weight="normal", ha="center"):
    """Rótulo sobre el eje horizontal en x (sin línea)."""
    y0 = ax.get_ylim()[0] if y0 is None else y0
    ax.annotate(text, (x, y0), xytext=(0, dy), textcoords="offset points", ha=ha, va="top", fontsize=size,
                color=color or C["ink"], fontweight=weight)


def vline(ax, x, y, color=None, y0=None, lw=0.9):
    y0 = ax.get_ylim()[0] if y0 is None else y0
    ax.plot([x, x], [y0, y], ls=(0, (3, 3)), lw=lw, color=color or C["ink3"])


def canvas(w, h, W=100, H=None):
    """Figura sin ejes con coordenadas 0..W x 0..H (H proporcional si no se da)."""
    H = H if H is not None else W * h / w
    fig = plt.figure(figsize=(w, h))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    return fig, ax, W, H


def box(ax, x, y, w, h, text="", fc="white", ec=None, lw=1.3, size=8.6, color=None, weight="normal",
        r=1.6, title=None, title_color=None, title_size=None, ls="-", linespacing=1.3, z=2, ha="center",
        pad_x=1.6):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec or C["ink2"],
                       lw=lw, ls=ls, zorder=z)
    ax.add_patch(p)
    cx = x + w / 2 if ha == "center" else x + pad_x
    if title:
        ax.text(cx, y + h - 1.2, title, ha=ha, va="top", fontsize=title_size or size + 0.6, fontweight="bold",
                color=title_color or color or C["ink"], zorder=z + 1, linespacing=linespacing)
        if text:
            ax.text(cx, y + (h - 1.2 - (title_size or size + 0.6) * 0.33) / 2, text, ha=ha, va="center",
                    fontsize=size, color=color or C["ink"], fontweight=weight, zorder=z + 1,
                    linespacing=linespacing)
    elif text:
        ax.text(cx, y + h / 2, text, ha=ha, va="center", fontsize=size, color=color or C["ink"],
                fontweight=weight, zorder=z + 1, linespacing=linespacing)
    return p


def arr(ax, x0, y0, x1, y1, color=None, lw=1.4, style="-|>", ms=10, ls="-", rad=0.0, z=1):
    a = FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style, mutation_scale=ms, color=color or C["ink2"],
                        lw=lw, ls=ls, shrinkA=0, shrinkB=0, zorder=z, connectionstyle=f"arc3,rad={rad}")
    ax.add_patch(a)
    return a


def panel_title(ax, text, size=9, pad=10):
    ax.set_title(text, fontsize=size, pad=pad, loc="left", fontweight="bold", color=C["ink"])


import os as _os
from econ_style import save as _save_svg  # noqa: E402


def save(fig, name):
    """Guarda el SVG (figs/out/<name>.svg). Con P4PNG=<dir> guarda además un PNG de control."""
    d = _os.environ.get("P4PNG")
    if d:
        fig.savefig(_os.path.join(d, name + ".png"), dpi=110)
    return _save_svg(fig, name)
