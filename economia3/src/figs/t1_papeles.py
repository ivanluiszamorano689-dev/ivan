"""Figura 1.4 — Los dos papeles de la libertad en el desarrollo (Sen)."""
from t1_util import *

fig, ax, H = canvas(6.8, 2.55)

# caja central
cx, cw = 50, 25
rbox(ax, cx - cw / 2, 12.6, cw, 20.4, "violet", fill="solid", r=2.2)
txt(ax, cx, 28.6, "DESARROLLO", size=10, color="white", weight="bold")
txt(ax, cx, 22.4, "= expansión de las\nlibertades reales", size=8.6, color="white", weight="bold")
txt(ax, cx, 16.0, "fin primordial y\nmedio principal", size=7.4, color="#e4e0f7", style="italic")

sides = [
    (1.0, "violet", "Papel CONSTITUTIVO", "la libertad como FIN",
     "evitar el hambre · estar alfabetizado ·\nparticipar en la vida de la comunidad",
     "valor intrínseco: aunque no sumen\nun peso al PBI, ya son desarrollo"),
    (68.0, "orange", "Papel INSTRUMENTAL", "la libertad como MEDIO",
     "derechos y oportunidades que se\nrefuerzan entre sí: la libertad es el motor",
     "las 5 libertades instrumentales\n(Figura 1.5)"),
]
sw = 31.0
for x, col, t, sub, body, foot in sides:
    rbox(ax, x, 11.0, sw, H - 11.8, col, fill="bg", r=2.2)
    txt(ax, x + sw / 2, H - 3.7, t, size=9.2, color=DARK[col], weight="bold")
    txt(ax, x + sw / 2, H - 7.4, sub, size=8.2, color=DARK[col], style="italic")
    txt(ax, x + sw / 2, H - 10.3, body, size=7.3, color=C["ink"], va="top", ls=1.22)
    rbox(ax, x + 1.5, 12.3, sw - 3, 6.8, col, fill="white", lw=1.0, r=1.4)
    txt(ax, x + sw / 2, 15.7, foot, size=7.2, color=DARK[col], weight="bold", ls=1.18)

arr(ax, (1.0 + sw + 0.6, 22.8), (cx - cw / 2 - 0.6, 22.8), color=C["violet"], lw=2.2, ms=15)
arr(ax, (68.0 - 0.6, 22.8), (cx + cw / 2 + 0.6, 22.8), color=C["orange"], lw=2.2, ms=15)

# corolario
rbox(ax, 1.0, 0.4, 98, 9.2, "gray", fill="bg", lw=0, r=1.6)
txt(ax, 3.0, 7.3, "COROLARIO", size=7.2, color=C["ink2"], weight="bold", ha="left")
txt(ax, 16.5, 7.3, "el desarrollo exige eliminar las principales fuentes de privación de libertad:", size=7.8,
    color=C["ink"], weight="bold", ha="left")
txt(ax, 50, 3.3, "pobreza y tiranía  ·  escasez de oportunidades económicas y privaciones sociales sistemáticas  ·\n"
    "abandono de los servicios públicos  ·  intolerancia o exceso de intervención de los Estados represivos",
    size=7.4, color=C["ink2"], ls=1.28)
save(fig, "t1_papeles")
