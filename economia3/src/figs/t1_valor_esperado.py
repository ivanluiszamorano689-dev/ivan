"""Figura 0.2 — Valor esperado de contestar al azar en la teórica (+10 / −5)."""
import sys; sys.path.insert(0, "../lib")
from econ_style import *

opts = [5, 4, 3, 2]
ev = [10 / k - 5 * (k - 1) / k for k in opts]          # -2, -1.25, 0, +2.5
cols = [C["red"] if v < -1e-9 else (C["green"] if v > 1e-9 else C["ink3"]) for v in ev]
lab = ["−2", "−1,25", "0", "+2,5"]

fig, ax = new_fig(3.5, 2.75)
x = np.arange(len(opts))
ax.bar(x, [v if abs(v) > 1e-9 else 0.06 for v in ev], width=0.58, color=cols, zorder=3)
ax.axhline(0, color=C["ink2"], lw=1.0, zorder=4)
for xi, v, t in zip(x, ev, lab):
    off = 0.25 if v >= 0 else -0.25
    ax.text(xi, v + off, t, ha="center", va="bottom" if v >= 0 else "top", fontsize=9.5, fontweight="bold",
            color=C["ink"])
ax.set_xticks(x)
ax.set_xticklabels([f"{k} opciones\np = 1/{k}" for k in opts], fontsize=8)
ax.set_ylim(-3.1, 3.5)
ax.set_yticks([-2, -1, 0, 1, 2, 3])
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:+.0f}".replace("+0", "0").replace("-", "−")))
data_axes(ax, "", "puntos esperados por pregunta")
ax.set_xlabel("opciones que siguen en pie cuando elegís al azar", fontsize=8.3, color=C["ink2"])
ax.text(2.02, 1.9, "conviene", ha="center", fontsize=8, color=C["green"], fontweight="bold")
ax.text(0.5, 1.2, "no conviene", ha="center", fontsize=8, color=C["red"], fontweight="bold")
save(fig, "t1_valor_esperado")
