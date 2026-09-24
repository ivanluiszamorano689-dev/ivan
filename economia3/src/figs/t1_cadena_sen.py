"""Figura 1.2 — La cadena de Sen: bienes primarios → factores de conversión → capacidades → funcionamientos."""
from t1_util import *

fig, ax, H = canvas(6.9, 4.15)

# marco de la libertad (supracapacidad)
rbox(ax, 0.6, 13.2, 98.8, H - 13.8, "violet", fill="#fbfaff", lw=1.3, r=2.5, ls=(0, (5, 3)), z=1)
txt(ax, 2.6, H - 3.2, "LIBERTAD (supracapacidad)", size=8.2, color=DARK["violet"], weight="bold", ha="left")
txt(ax, 31.5, H - 3.2, "el marco que hace posible elegir (p. ej., el Estado garantiza el derecho a estudiar)",
    size=7.6, color=C["ink2"], ha="left", style="italic")

boxes = [
    ("gray", "Bienes primarios", "(recursos)", "ingreso, bienes\ny servicios", "lo que TENÉS",
     "Ej.: una beca, una\nescuela en el barrio"),
    ("orange", "Factores de", "conversión", "Personales: edad, género,\nsalud, discapacidad\n\nEntorno: físico, social,\nepidemiológico, acceso a\nservicios públicos",
     "cuánto RINDE", "Ej.: salud, transporte,\ntener que trabajar"),
    ("violet", "Capacidades", "(conjunto de capacidad)", "combinaciones de\nfuncionamientos entre\nlas que podés elegir", "el MENÚ",
     "Ej.: la posibilidad real\nde estudiar"),
    ("aqua", "Funcionamientos", "(logros)", "lo que efectivamente\nlográs ser o hacer", "el PLATO elegido",
     "Ej.: estudiar,\nrecibirse"),
]
bw, gap, x0 = 20.2, 4.9, 2.4
yb, yt = 17.0, H - 7.0
for i, (col, t1, t2, body, tag, ej) in enumerate(boxes):
    x = x0 + i * (bw + gap)
    rbox(ax, x, yb, bw, yt - yb, col, fill="white", lw=1.5, r=1.8)
    rbox(ax, x, yt - 8.2, bw, 8.2, col, fill="bg", lw=1.5, r=1.8)
    txt(ax, x + bw / 2, yt - 2.7, t1, size=8.8, color=DARK[col], weight="bold")
    txt(ax, x + bw / 2, yt - 5.8, t2, size=(8.8 if i == 1 else 7.4), color=DARK[col],
        weight=("bold" if i == 1 else "normal"))
    txt(ax, x + bw / 2, yt - 10.2, body, size=7.4, color=C["ink"], va="top", ls=1.25)
    pill(ax, x + bw / 2, yb + 8.4, tag, color=col, size=7.3, h=3.1, fill="solid", tcolor="white")
    txt(ax, x + bw / 2, yb + 3.4, ej, size=6.9, color=C["ink2"], style="italic", ls=1.2)

ya = (yb + yt) / 2 + 3
for i in range(3):
    xa = x0 + (i + 1) * bw + i * gap
    arr(ax, (xa + 0.4, ya), (xa + gap - 0.4, ya), color=C["ink2"], lw=1.8, ms=13)
txt(ax, x0 + 3 * bw + 2.5 * gap, ya - 5.0, "elección\n(agencia)", size=7.2, color=DARK["violet"], weight="bold")

# dónde mira cada enfoque
yq = 6.2
txt(ax, 25.0, yq + 5.2, "¿Dónde mira cada enfoque?", size=7.6, color=C["ink2"], weight="bold")
cx = [x0 + bw / 2 + i * (bw + gap) for i in range(4)]
notes = [("gray", "Rawls: reparte\nbienes primarios", "white"),
         ("orange", "acá se separan dos\npersonas con igual renta", "white"),
         ("violet", "SEN evalúa acá:\nlibertad real", "solid"),
         ("aqua", "bien-estar logrado\n(lo observable)", "white")]
for x, (col, s, fl) in zip(cx, notes):
    rbox(ax, x - bw / 2, yq - 3.3, bw, 6.6, col, fill=("solid" if fl == "solid" else "white"), lw=1.1, r=1.4)
    txt(ax, x, yq, s, size=7.0, color=("white" if fl == "solid" else DARK[col]), weight="bold", ls=1.15)
    arr(ax, (x, yq + 3.4), (x, yb - 0.3), color=MID[col], lw=1.1, ms=8)
save(fig, "t1_cadena_sen")
