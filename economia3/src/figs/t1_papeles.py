"""Figura 1.4 — Los dos papeles de la libertad en el desarrollo (Sen)."""
from t1_util import *

fig, ax, H = canvas(6.8, 3.35)

# caja central
cx, cw = 50, 25
rbox(ax, cx - cw / 2, 19.5, cw, 20, "violet", fill="solid", r=2.2)
txt(ax, cx, 35.2, "DESARROLLO", size=10, color="white", weight="bold")
txt(ax, cx, 29.0, "= expansión de las\nlibertades reales", size=8.6, color="white", weight="bold")
txt(ax, cx, 22.6, "fin primordial y\nmedio principal", size=7.4, color="#e4e0f7", style="italic")

sides = [
    (1.0, "violet", "Papel CONSTITUTIVO", "la libertad como FIN",
     "Las libertades fundamentales SON\nel desarrollo: evitar el hambre,\nestar alfabetizado, participar en\nla vida de la comunidad.",
     "valor intrínseco: aunque no sumen\nun peso al PBI, ya son desarrollo"),
    (68.0, "orange", "Papel INSTRUMENTAL", "la libertad como MEDIO",
     "Derechos y oportunidades de distinto\ntipo se refuerzan entre sí y\nexpanden la libertad general:\nla libertad es el motor.",
     "las 5 libertades instrumentales\n(Figura 1.5)"),
]
sw = 31.0
for x, col, t, sub, body, foot in sides:
    rbox(ax, x, 13.0, sw, H - 14.0, col, fill="bg", r=2.2)
    txt(ax, x + sw / 2, H - 4.2, t, size=9.2, color=DARK[col], weight="bold")
    txt(ax, x + sw / 2, H - 8.2, sub, size=8.2, color=DARK[col], style="italic")
    txt(ax, x + sw / 2, H - 11.2, body, size=7.5, color=C["ink"], va="top", ls=1.25)
    rbox(ax, x + 1.5, 14.6, sw - 3, 7.4, col, fill="white", lw=1.0, r=1.4)
    txt(ax, x + sw / 2, 18.3, foot, size=7.2, color=DARK[col], weight="bold", ls=1.2)

arr(ax, (1.0 + sw + 0.6, 29.5), (cx - cw / 2 - 0.6, 29.5), color=C["violet"], lw=2.2, ms=15)
arr(ax, (68.0 - 0.6, 29.5), (cx + cw / 2 + 0.6, 29.5), color=C["orange"], lw=2.2, ms=15)

# corolario
rbox(ax, 1.0, 0.8, 98, 10.0, "gray", fill="bg", lw=0, r=1.6)
txt(ax, 3.0, 8.2, "COROLARIO", size=7.2, color=C["ink2"], weight="bold", ha="left")
txt(ax, 16.5, 8.2, "el desarrollo exige eliminar las principales fuentes de privación de libertad:", size=7.8,
    color=C["ink"], weight="bold", ha="left")
txt(ax, 50, 3.8, "pobreza y tiranía  ·  escasez de oportunidades económicas y privaciones sociales sistemáticas  ·\n"
    "abandono de los servicios públicos  ·  intolerancia o exceso de intervención de los Estados represivos",
    size=7.4, color=C["ink2"], ls=1.3)
save(fig, "t1_papeles")
