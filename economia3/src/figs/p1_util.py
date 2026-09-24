"""Ayudas para los diagramas del bloque p1 (formulario + TP1).

Diagramas de cajas y flechas dibujados con matplotlib en coordenadas de datos
(0..W, 0..H) para que el texto quede siempre dentro de su caja.
"""
import sys

sys.path.insert(0, "../lib")
from econ_style import C, np, plt  # noqa: E402,F401
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon  # noqa: E402

# Colores fijos de las cinco libertades instrumentales (los mismos que las tarjetas del HTML)
LIB = {
    "pol": (C["blue"], C["blue_bg"], "#184f95", "Libertades políticas"),
    "eco": (C["orange"], C["orange_bg"], "#a8431b", "Servicios económicos"),
    "soc": (C["aqua"], C["aqua_bg"], "#0f6e4c", "Oportunidades sociales"),
    "tra": (C["violet"], C["violet_bg"], "#3a2d86", "Garantías de transparencia"),
    "seg": (C["yellow"], C["yellow_bg"], "#8a5d00", "Seguridad protectora"),
}


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
        ha="center", va="center", r=1.6, pad_x=1.4, title=None, title_color=None, title_size=None, ls="-",
        linespacing=1.3, z=2):
    """Caja redondeada con esquina inferior izquierda en (x, y). Si hay title, va arriba en negrita."""
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec or C["ink2"],
                       lw=lw, ls=ls, zorder=z)
    ax.add_patch(p)
    cx = x + w / 2 if ha == "center" else x + pad_x
    if title:
        ax.text(cx, y + h - 1.0, title, ha=ha, va="top", fontsize=title_size or size + 0.6, fontweight="bold",
                color=title_color or color or C["ink"], zorder=z + 1, linespacing=linespacing)
    if text:
        ty = y + h / 2 if va == "center" else y + h - 1.0
        ax.text(cx, ty, text, ha=ha, va=va, fontsize=size, color=color or C["ink"], fontweight=weight,
                zorder=z + 1, linespacing=linespacing)
    return p


def arr(ax, x0, y0, x1, y1, color=None, lw=1.4, style="-|>", ms=10, ls="-", rad=0.0, z=1):
    a = FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style, mutation_scale=ms, color=color or C["ink2"],
                        lw=lw, ls=ls, shrinkA=0, shrinkB=0, zorder=z,
                        connectionstyle=f"arc3,rad={rad}")
    ax.add_patch(a)
    return a


def diamond(ax, cx, cy, w, h, text, fc="white", ec=None, size=8.2, lw=1.2):
    pts = [(cx - w / 2, cy), (cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2)]
    ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=ec or C["ink2"], lw=lw, zorder=2))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=size, color=C["ink"], zorder=3, linespacing=1.25)
