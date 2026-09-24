"""§0 · Índice visual: qué tipo de ejercicio apareció en qué parcial y con cuántos puntos."""
from s0_util import *

cols = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9"]
dates = ["08/10/22", "2023", "s/f", "20/9/24", "28/9/24", "28/9/24", "28/9/24", "2025", "27/9/25"]
kind = ["T+P", "P+T", "P", "T", "T", "P", "P", "P", "T"]
# (sección, color, tipo, {columna: puntos})
rows = [
    ("§1", "aqua", "Solow sin tecnología", {0: 20, 1: 15}),
    ("§1", "aqua", "Harrod-Domar", {1: 5}),
    ("§1", "aqua", "Solow con tecnología", {5: 20, 6: 20, 7: 25}),
    ("§2", "blue", "TC de mercado y PPA", {0: 20, 1: 20}),
    ("§2", "blue", "Tasas de crecimiento", {5: 20, 6: 20}),
    ("§2", "blue", "Índice Big Mac", {7: 15}),
    ("§3", "orange", "IDH, IDH-D y pérdida", {1: 20, 2: 14, 5: 20, 6: 20, 7: 14}),
    ("§4", "violet", "Casos e interpretación", {2: 6, 7: 6}),
    ("§4", "violet", "Teóricas (4 × 10 ptos)", {0: 40, 1: 40, 3: 40, 4: 40, 8: 40}),
]

fig, ax = new_fig(6.8, 3.7)
ax.set_xlim(-5.0, 9.45)
ax.set_ylim(len(rows) - 0.45, -1.75)
ax.axis("off")

# bandas de sección y rótulos de fila
sec_rows = {}
for i, (sec, col, name, pts) in enumerate(rows):
    sec_rows.setdefault(sec, []).append(i)
    if i % 2 == 0:
        ax.add_patch(plt.Rectangle((-0.5, i - 0.5), 9.0, 1.0, fc="#f7f6f2", ec="none", zorder=0))
    ax.text(-0.62, i, name, ha="right", va="center", fontsize=8.3, color=C["ink"])
    for j, v in pts.items():
        r = 5.5 + 9.5 * (v / 40) ** 0.5
        ax.plot([j], [i], "o", ms=r * 1.55, color=MID[col], mec="white", mew=1.2, zorder=3,
                alpha=0.95)
        ax.text(j, i, str(v), ha="center", va="center", fontsize=7.4 if v < 40 else 7.8, color="white",
                fontweight="bold", zorder=4)
    ax.text(8.95, i, f"{len(pts)}×", ha="left", va="center", fontsize=8.4, color=C["ink2"], fontweight="bold")

for sec, idx in sec_rows.items():
    col = rows[idx[0]][1]
    y0, y1 = min(idx) - 0.42, max(idx) + 0.42
    ax.add_patch(plt.Rectangle((-4.25, y0), 0.14, y1 - y0, fc=MID[col], ec="none", zorder=2))
    ax.text(-4.95, (y0 + y1) / 2, sec, ha="left", va="center", fontsize=8.8, color=DARK[col],
            fontweight="bold")

# encabezados de columna
for j, (c, d, k) in enumerate(zip(cols, dates, kind)):
    ax.text(j, -1.42, c, ha="center", va="center", fontsize=8.6, color=C["ink"], fontweight="bold")
    ax.text(j, -1.0, d, ha="center", va="center", fontsize=6.1, color=C["ink2"])
    ax.text(j, -0.7, k, ha="center", va="center", fontsize=6.6, color=C["ink3"], fontweight="bold")
ax.text(8.95, -1.0, "veces", ha="left", va="center", fontsize=7.2, color=C["ink3"])
ax.text(-4.95, -1.0, "T = teórica · P = práctica\nnúmero = puntos en juego", ha="left", va="center",
        fontsize=6.8, color=C["ink3"], linespacing=1.3)
ax.plot([-0.5, 8.5], [-0.5, -0.5], color=C["rule"], lw=0.8, zorder=1)
save(fig, "s0_mapa")
