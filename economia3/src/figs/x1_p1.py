"""Parciales resueltos · P1 (1er parcial 08/10/2022, Tema A).
Figura P1.1 — Solow en tasas: CA = 0,65/k^(4/7) y CD = 0,13 -> 0,085 (k* 16,72 -> 35,17).
Figura P1.2 — PBI de Argensur a TCm y a PPA frente al de Norte Unidos.
Correr desde figs/:  python3 x1_p1.py
"""
import sys; sys.path.insert(0, "../lib")
from econ_style import *


def coma(v, d=2):
    return f"{v:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


# ---------------------------------------------------------------- Figura P1.1
sA, a = 0.65, 3 / 7
cd0, cd1 = 0.13, 0.085
k0 = (sA / cd0) ** (1 / (1 - a))
k1 = (sA / cd1) ** (1 / (1 - a))
CA = lambda k: sA / k ** (1 - a)

k = np.linspace(1.2, 46, 500)
fig, ax = new_fig(6.2, 3.5)
ax.plot(k, CA(k), color=C["orange"], lw=LW)
ax.plot([0, 46], [cd0, cd0], color=C["aqua"], lw=LW)
ax.plot([0, 46], [cd1, cd1], color=C["aqua"], lw=LW, ls="--")
econ_axes(ax, r"$k$", r"$\gamma_k$", xlim=(0, 46), ylim=(0, 0.36))
label_curve(ax, 46, cd0, r"$CD = n+\delta = 0{,}13$", C["aqua"], dx=4)
label_curve(ax, 46, cd1, r"$CD' = 0{,}04+0{,}045 = 0{,}085$", C["aqua"], dx=4)
label_curve(ax, 7.2, CA(7.2), r"$CA = \dfrac{sA}{k^{1-\alpha}} = \dfrac{0{,}65}{k^{4/7}}$", C["orange"], dx=10,
            dy=12, size=10)
vguide(ax, k0, cd0, r"$k^*=16{,}72$")
vguide(ax, k1, cd1, r"$k^{*\prime}=35{,}17$")
point(ax, k0, cd0, C["ink"], "A", dx=5, dy=5)
point(ax, k1, cd1, C["ink"], "B", dx=5, dy=5)
# desplazamiento de la CD
arrow(ax, 40.5, cd0 - 0.004, 40.5, cd1 + 0.006, C["ink2"])
ax.text(41.2, (cd0 + cd1) / 2, r"$\delta$ a la mitad", fontsize=8.6, color=C["ink2"], va="center")
# tasa positiva en k*=16,72 tras el cambio
arrow(ax, k0 - 1.2, cd1 + 0.004, k0 - 1.2, cd0 - 0.004, C["ink"], both=True, lw=1.1)
ax.text(k0 - 2.0, (cd0 + cd1) / 2, r"$\gamma_k>0$", fontsize=9, ha="right", va="center", color=C["ink"])
arrow(ax, k0 + 1.5, 0.018, k1 - 1.5, 0.018, C["ink2"])
ax.text((k0 + k1) / 2, 0.024, "transición hacia el nuevo EE", fontsize=8.4, ha="center", va="bottom",
        color=C["ink2"])
save(fig, "x1_p1_solow_tasas")

# ---------------------------------------------------------------- Figura P1.2
labels = ["Norte Unidos", "Argensur a PPA\n(700.000 / 30,4348)", "Argensur a TC de mercado\n(700.000 / 40)"]
vals = [92000, 23000, 17500]
cols = [C["blue"], C["orange"], C["orange"]]
fig, ax = new_fig(6.2, 2.45)
y = np.array([2, 1, 0])
bars = ax.barh(y, vals, height=0.56, color=cols, zorder=3)
bars[2].set_hatch("////")
bars[2].set_facecolor("white")
bars[2].set_edgecolor(C["orange"])
bars[2].set_linewidth(1.4)
for yi, v in zip(y, vals):
    ax.text(v + 1500, yi, "US$ " + coma(v, 0), va="center", ha="left", fontsize=9, fontweight="bold",
            color=C["ink"])
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=8.6)
ax.set_xlim(0, 118000)
ax.set_xticks([0, 20000, 40000, 60000, 80000, 100000])
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: coma(v, 0)))
ax.grid(axis="x", color="#ebe9e3", lw=0.8)
ax.set_axisbelow(True)
ax.spines["left"].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.set_xlabel("PBI en dólares (2021)", fontsize=8.6, color=C["ink2"])
# brechas
ax.text(103500, 1.0, "NU / Argensur\n= 4 veces", fontsize=8.4, ha="center", va="center", color=C["ink"])
ax.text(103500, 0.0, "NU / Argensur\n= 5,26 veces", fontsize=8.4, ha="center", va="center", color=C["ink"])
save(fig, "x1_p1_ppa")
