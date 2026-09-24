"""Figura 1.1 — Renta per cápita y esperanza de vida: relación positiva, débil y que se aplana (esquemático)."""
import sys; sys.path.insert(0, "../lib")
from econ_style import *

x = np.linspace(0.02, 10, 400)
f = lambda v: 1.0 + 3.0 * (1 - np.exp(-v / 1.9))           # forma cóncava que se aplana
fig, ax = new_fig(6.2, 3.1)
ax.fill_between(x, f(x) - 0.55, f(x) + 0.55, color=C["gray_bg"], lw=0, zorder=1)
ax.plot(x, f(x), color=C["blue"], lw=LW, zorder=3)
econ_axes(ax, "PBI per cápita", "Esperanza de vida", xlim=(0, 10.4), ylim=(0.5, 5.0))
label_curve(ax, 10, f(10), "relación promedio", C["blue"], dx=0, dy=-11, ha="right", size=8.5)
ax.text(10.2, 1.0, "franja gris: mucha dispersión alrededor\ndel promedio (la relación es débil)",
        fontsize=7.8, color=C["ink2"], ha="right", va="center")
# tramos
ax.annotate("tramo empinado:\ncada peso extra rinde mucho", (0.75, f(0.75)), xytext=(0.35, 4.55), fontsize=8,
            color=C["ink2"], ha="left", va="center", arrowprops=dict(arrowstyle="-", color=C["ink3"], lw=0.8))
ax.annotate("tramo plano: más renta,\ncasi la misma vida", (5.8, f(5.8) + 0.02), xytext=(4.3, 4.72), fontsize=8,
            color=C["ink2"], ha="left", va="center", arrowprops=dict(arrowstyle="-", color=C["ink3"], lw=0.8))
# casos de Sen (posiciones ilustrativas)
SL = (1.45, 3.3)
AF = (6.9, 2.7)
ax.plot([SL[0], AF[0] + 0.02], [SL[1], SL[1]], ls=(0, (2, 2)), lw=0.9, color=C["aqua"], zorder=2)
arrow(ax, AF[0], SL[1], AF[0], AF[1] + 0.12, C["orange"], lw=1.2)
ax.text(AF[0] + 0.2, (SL[1] + AF[1]) / 2 + 0.03, "más renta que en Sri Lanka,\npero menos chances\nde llegar a adulto",
        fontsize=7.6, color=C["ink2"], ha="left", va="center")
pts = {"Sri Lanka": (SL[0], SL[1], C["aqua"], (0, 7), "center"),
       "Sudáfrica: más rica que Sri Lanka, pero vive menos": (3.4, 1.75, C["orange"], (7, -3), "left"),
       "Afroamericanos (EE.UU.)": (AF[0], AF[1], C["orange"], (-6, -4), "right"),
       "Blancos (EE.UU.)": (8.3, 4.0, C["ink2"], (0, 7), "center")}
for name, (px, py, col, (dx, dy), ha) in pts.items():
    point(ax, px, py, col)
    ax.annotate(name, (px, py), xytext=(dx, dy), textcoords="offset points", ha=ha, fontsize=8.3,
                fontweight="bold", color=C["ink"], va="bottom" if dy > 0 else "top")
save(fig, "t1_renta_vida")
