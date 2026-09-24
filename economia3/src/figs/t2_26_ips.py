"""Tema 2.6: valores del Índice de Progreso Social 2024 (datos del manual)."""
from t2_util import *

ips = [("Noruega", 1, 91.95), ("Dinamarca", 2, 91.65), ("Chile", 36, 79.49), ("Uruguay", 38, 79.26),
       ("Argentina", 41, 76.85), ("Brasil", 55, 72.35)]
fig, ax = new_fig(6.2, 1.95)
ys = np.arange(len(ips))[::-1]
cols = [C["blue"] if n == "Argentina" else C["ink3"] for n, _, _ in ips]
bars = ax.barh(ys, [v for _, _, v in ips], color=cols, height=0.6)
for b, (n, r, v) in zip(bars, ips):
    yy = b.get_y() + b.get_height() / 2
    ax.annotate(fmt(v, 2), (v, yy), xytext=(4, 0), textcoords="offset points", va="center", fontsize=8.2,
                fontweight="bold" if n == "Argentina" else "normal")
    ax.annotate(f"{r}°", (0, yy), xytext=(5, 0), textcoords="offset points", va="center", fontsize=7.8,
                color="white", fontweight="bold")
ax.set_yticks(ys)
ax.set_yticklabels([n for n, _, _ in ips], fontsize=8.8)
ax.set_xlim(0, 100)
ax.set_xticks([0, 25, 50, 75, 100])
clean_hbar(ax, "IPS 2024 (escala 0 a 100) · el número en la barra es el puesto en el ranking")
ax.xaxis.label.set_size(8.2)
save(fig, "t2_ips_valores")
