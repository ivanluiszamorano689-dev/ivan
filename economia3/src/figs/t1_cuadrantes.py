"""Figura 1.10 — Las cuatro combinaciones de Ranis y Stewart (esquemático)."""
from t1_util import *

fig, ax, H = canvas(5.0, 3.2)
x0, y0, S = 13.0, 12.0, 43.0          # origen y ancho de cada cuadrante (unidades del lienzo)
h = 25.5                              # alto de cada cuadrante
quads = [
    (0, 1, "yellow", "Desequilibrio a favor del DH", "DH alto con CE débil:\nbuena base humana que\ntodavía no rinde crecimiento"),
    (1, 1, "green", "Círculo virtuoso", "CE y DH se empujan\nmutuamente: las dos\ncadenas son fuertes"),
    (0, 0, "red", "Círculo vicioso", "CE y DH bajos: las dos\ncadenas débiles, uno\nfrena al otro"),
    (1, 0, "orange", "Desequilibrio a favor del CE", "crece el producto pero\nel DH no acompaña: ese\ncrecimiento no se sostiene"),
]
for i, j, col, t, body in quads:
    x, y = x0 + i * S, y0 + j * h
    rbox(ax, x + 0.5, y + 0.5, S - 1, h - 1, col, fill="bg", lw=1.2, r=1.6)
    txt(ax, x + S / 2, y + h - 4.0, t, size=8.0, color=DARK[col], weight="bold")
    txt(ax, x + S / 2, y + h / 2 + 0.6, body, size=7.3, color=C["ink"], ls=1.22)

# ejes
arr(ax, (x0, y0 - 1.5), (x0 + 2 * S + 2, y0 - 1.5), color=C["ink2"], lw=1.3, ms=10)
arr(ax, (x0 - 1.5, y0), (x0 - 1.5, y0 + 2 * h + 2), color=C["ink2"], lw=1.3, ms=10)
txt(ax, x0 + 2 * S + 2, y0 - 9.0, "crecimiento económico (CE)", size=8.0, color=C["ink"], ha="right")
txt(ax, x0 + S / 2, y0 - 5.0, "débil", size=7.4, color=C["ink3"])
txt(ax, x0 + 1.5 * S, y0 - 5.0, "fuerte", size=7.4, color=C["ink3"])
txt(ax, x0 - 3.0, y0 + 2 * h + 2.0, "DH", size=8.0, color=C["ink"], ha="right", va="top", weight="bold")
txt(ax, x0 - 3.0, y0 + h / 2, "débil", size=7.4, color=C["ink3"], ha="right")
txt(ax, x0 - 3.0, y0 + 1.5 * h, "fuerte", size=7.4, color=C["ink3"], ha="right")

# transiciones típicas
arr(ax, (x0 + S - 6, y0 + h + 5.6), (x0 + S + 6, y0 + h + 5.6), color=C["green"], lw=2.4, ms=15, z=6)
arr(ax, (x0 + S + 6, y0 + 5.6), (x0 + S - 6, y0 + 5.6), color=C["red"], lw=2.4, ms=15, z=6)
kw = dict(size=6.9, weight="bold", z=7, bbox=dict(fc="white", ec="none", pad=1.0, alpha=0.95))
txt(ax, x0 + S, y0 + h + 2.4, "tiende a pasar al virtuoso", color=C["green"], **kw)
txt(ax, x0 + S, y0 + 2.4, "tiende a caer en el vicioso", color=C["red"], **kw)
save(fig, "t1_cuadrantes")
