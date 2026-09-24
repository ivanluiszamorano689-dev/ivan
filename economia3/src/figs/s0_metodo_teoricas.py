"""§4 · Diagrama de flujo del método para las preguntas teóricas de opción múltiple."""
from s0_util import *

fig, ax, H = canvas(6.6, 3.3)

# ---- fila superior: los cuatro pasos de análisis
steps = [
    ("1", "Ubicá el tema", "¿Sen, PPA, índices, Solow? Anotá «Tema X.Y» y el concepto clave."),
    ("2", "Definición exacta", "Recitá la de la cátedra, no «lo que suena bien»."),
    ("3", "Palabras trampa", "siempre · suficiente · garantiza · exclusivamente · endógena · todas"),
    ("4", "Descartá", "Cada opción contra la definición: ✗ si exagera, invierte o contradice."),
]
top_h = 13.0
y_top = H - 1.2 - top_h
gap = 3.6
bw = (100 - 2.0 - gap * 3) / 4
for i, (n, t, d) in enumerate(steps):
    x = 1.0 + i * (bw + gap)
    rbox(ax, x, y_top, bw, top_h, "violet", fill="bg", lw=1.2)
    num_badge(ax, x + 2.6, y_top + top_h - 2.6, n, "violet", r=1.7, size=8)
    txt(ax, x + 5.0, y_top + top_h - 2.6, t, size=8.2, weight="bold", color=DARK["violet"], ha="left")
    txt(ax, x + 1.6, y_top + top_h - 5.4, d, size=6.9, ha="left", va="top", n=26, ls=1.2)
    if i < 3:
        arr(ax, (x + bw + 0.4, y_top + top_h / 2), (x + bw + gap - 0.4, y_top + top_h / 2), color=C["violet"])

# ---- decisión
dx = 15.0
dw, dh = 25.0, 13.5
x4 = 1.0 + 3 * (bw + gap) + bw / 2
yr = y_top - 3.0
dy = yr - 2.6 - (5 * 4.9 + 4 * 1.05) / 2
ax.plot([x4, x4, dx, dx], [y_top - 0.3, yr, yr, dy + dh / 2 + 1.2], color=C["ink2"], lw=1.3, zorder=2)
arr(ax, (dx, dy + dh / 2 + 1.3), (dx, dy + dh / 2 + 0.05), color=C["ink2"])
diamond(ax, dx, dy, dw, dh, "orange", fill="bg", lw=1.3)
txt(ax, dx, dy, "¿Cuántas\nquedan\nen pie?", size=7.8, weight="bold", color=DARK["orange"], ls=1.1)

outs = [
    ("green", "Queda 1", "5 · Elegila: +10."),
    ("violet", "Ninguna o varias", "Todas fallan → «Ninguna»; varias ciertas → «Todas» (si existe)."),
    ("blue", "Quedan 2", "6 · Arriesgá: valor esperado +2,5."),
    ("yellow", "Quedan 3", "Valor esperado 0: arriesgá sólo si una te convence más."),
    ("red", "Quedan 4 o 5", "Dejá en blanco: arriesgar vale −1,25 o −2."),
]
ox = 33.0
ow = 100 - 1.0 - ox
oh = 4.9
og = 1.05
ytop_out = yr - 2.6
for i, (col, t, d) in enumerate(outs):
    y = ytop_out - (i + 1) * oh - i * og
    rbox(ax, ox, y, ow, oh, col, fill="bg", lw=1.1, r=1.0)
    txt(ax, ox + 1.4, y + oh / 2, t, size=7.7, weight="bold", color=DARK[col], ha="left")
    txt(ax, ox + 17.0, y + oh / 2, d, size=7.3, ha="left")
    elbow(ax, (dx + dw / 2, dy), (ox - 0.2, y + oh / 2), color=MID[col], lw=1.1, xm=ox - 3.5)
save(fig, "s0_metodo_teoricas")
