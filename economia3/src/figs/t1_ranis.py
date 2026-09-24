"""Figura 1.9 — Los dos encadenamientos de Ranis y Stewart entre crecimiento económico (CE) y desarrollo humano (DH)."""
from t1_util import *

fig, ax, H = canvas(6.8, 3.55)
cy = H / 2

# nodos
for x, col, t1, t2 in [(1.0, "blue", "Crecimiento", "económico (CE)"), (79.0, "violet", "Desarrollo", "humano (DH)")]:
    rbox(ax, x, cy - 7.5, 20, 15, col, fill="solid", r=2.4)
    txt(ax, x + 10, cy + 1.8, t1, size=9.4, color="white", weight="bold")
    txt(ax, x + 10, cy - 2.2, t2, size=8.4, color="white", weight="bold")

# cadena A (arriba) y B (abajo)
chains = [
    ("blue", "CADENA A · CE → DH", "¿cuánto del crecimiento se vuelve desarrollo humano?",
     ["ingreso de los hogares y su distribución (pobreza)",
      "gasto de los hogares en alimentos, salud y educación",
      "gasto público social: cuánto se recauda y qué parte va a DH",
      "organizaciones comunitarias y ONG"], cy + 3.0),
    ("violet", "CADENA B · DH → CE", "¿cuánto del desarrollo humano vuelve como crecimiento?",
     ["personas más sanas y educadas: más productivas",
      "más capacidad de adoptar tecnología e innovar",
      "más y mejor inversión",
      "mejor distribución del ingreso y exportaciones más complejas"], 1.0),
]
bx, bw, bh = 25.0, 50.0, 21.2
for col, title, q, items, y in chains:
    rbox(ax, bx, y, bw, bh, col, fill="bg", lw=1.3, r=1.8)
    txt(ax, bx + 2, y + bh - 2.6, title, size=8.2, color=DARK[col], weight="bold", ha="left")
    txt(ax, bx + 2, y + bh - 6.0, q, size=7.2, color=C["ink2"], ha="left", style="italic")
    yy = y + bh - 9.4
    for it in items:
        ax.plot([bx + 2.8], [yy], "o", ms=2.8, color=MID[col], zorder=5)
        txt(ax, bx + 4.2, yy, it, size=7.2, color=C["ink"], ha="left")
        yy -= 3.0

# flechas del círculo
yA = cy + 3.0 + bh / 2
yB = 1.0 + bh / 2
arr(ax, (11, cy + 7.8), (bx - 0.6, yA), color=C["blue"], lw=2.0, ms=14, rad=-0.35)
arr(ax, (bx + bw + 0.6, yA), (89, cy + 7.8), color=C["blue"], lw=2.0, ms=14, rad=-0.35)
arr(ax, (89, cy - 7.8), (bx + bw + 0.6, yB), color=C["violet"], lw=2.0, ms=14, rad=-0.35)
arr(ax, (bx - 0.6, yB), (11, cy - 7.8), color=C["violet"], lw=2.0, ms=14, rad=-0.35)
save(fig, "t1_ranis")
