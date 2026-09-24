"""Utilidades comunes a los gráficos del TP3 (prefijo p3_)."""
import sys

sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403,E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

GRID = "#ebe9e3"


def coma(v, dec=3, signo=False):
    s = f"{v:+.{dec}f}" if signo else f"{v:.{dec}f}"
    return s.replace(".", ",").replace("-", "−")


def miles(v, dec=0):
    s = f"{v:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_coma(dec=2):
    return plt.FuncFormatter(lambda v, p: coma(v, dec))


def fmt_pct(dec=0, signo=False):
    def f(v, p):
        s = f"{v:+.{dec}f}" if signo else f"{v:.{dec}f}"
        return s.replace(".", ",").replace("-", "−") + " %"
    return plt.FuncFormatter(f)


def caja(ax, x, y, w, h, texto, fc="#ffffff", ec=None, lw=1.2, size=9, color=None, weight="normal",
         ls="-", r=0.08, zorder=2, ha="center"):
    """Caja redondeada centrada en (x, y) con texto."""
    p = FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                       fc=fc, ec=ec or C["ink2"], lw=lw, ls=ls, zorder=zorder)
    ax.add_patch(p)
    tx = x if ha == "center" else x - w / 2 + 0.12
    ax.text(tx, y, texto, ha=ha, va="center", fontsize=size, color=color or C["ink"], fontweight=weight,
            zorder=zorder + 1, linespacing=1.35)
    return p


def flecha(ax, x0, y0, x1, y1, color=None, lw=1.3, texto=None, tdx=0, tdy=0.12, size=8.5, tcolor=None,
           style="-|>", rad=0.0, weight="bold", ha="center", va="bottom"):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=style, color=color or C["ink2"], lw=lw, shrinkA=0, shrinkB=0,
                                mutation_scale=10, connectionstyle=f"arc3,rad={rad}"))
    if texto:
        ax.text((x0 + x1) / 2 + tdx, (y0 + y1) / 2 + tdy, texto, ha=ha, va=va, fontsize=size,
                color=tcolor or color or C["ink2"], fontweight=weight)


def lienzo(w, h, xmax=10, ymax=6):
    fig, ax = new_fig(w, h)
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, ymax)
    ax.axis("off")
    fig.subplots_adjust(left=0.005, right=0.995, top=0.995, bottom=0.005)
    return fig, ax
