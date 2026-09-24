"""Figura 1.5 — Las cinco libertades instrumentales: se refuerzan entre sí y expanden la libertad general."""
from t1_util import *
import math

fig, ax, H = canvas(6.8, 4.1)
cx, cy = 50, H / 2 + 0.3
nodes = [
    ("blue", "1 · Libertades políticas", "votar, criticar, elegir gobernantes,\nprensa libre, derecho a peticionar"),
    ("orange", "2 · Servicios económicos", "ingresos, crédito, precios relativos,\nintercambio, funcionamiento de mercados"),
    ("aqua", "3 · Oportunidades sociales", "educación y sanidad: escuelas,\nhospitales, clínicas, alfabetización"),
    ("yellow", "4 · Garantías de transparencia", "información pública, rendición de\ncuentas, controles, anticorrupción"),
    ("violet", "5 · Seguridad protectora", "red de protección: mecanismos fijos\n(desempleo, indigentes) y ad hoc\n(hambrunas, empleo de emergencia)"),
]
angles = [90, 90 - 72, 90 - 144, 90 - 216, 90 - 288]
rx, ry = 34.0, 20.5
bw, bh = 31.0, 12.4
pos = []
for a in angles:
    t = math.radians(a)
    pos.append((cx + rx * math.cos(t), cy + ry * math.sin(t)))

# líneas de refuerzo mutuo (todas con todas)
for i in range(5):
    for j in range(i + 1, 5):
        (x1, y1), (x2, y2) = pos[i], pos[j]
        ax.plot([x1, x2], [y1, y2], color=C["ink3"], lw=0.8, ls=(0, (2, 2.5)), zorder=1)

# centro
ax.add_patch(Circle((cx, cy), 9.2, fc=C["violet_bg"], ec=C["violet"], lw=1.6, zorder=3))
txt(ax, cx, cy + 1.6, "Libertad general", size=8.4, color=DARK["violet"], weight="bold")
txt(ax, cx, cy - 2.2, "capacidades de\nlas personas", size=7.4, color=DARK["violet"])

for (x, y), (col, t, body) in zip(pos, nodes):
    hh = bh + (2.4 if body.count("\n") == 2 else 0)
    rbox(ax, x - bw / 2, y - hh / 2, bw, hh, col, fill="white", lw=1.5, r=1.6, z=4)
    rbox(ax, x - bw / 2, y + hh / 2 - 4.2, bw, 4.2, col, fill="bg", lw=1.5, r=1.6, z=4)
    txt(ax, x, y + hh / 2 - 2.1, t, size=8.0, color=DARK[col], weight="bold")
    txt(ax, x, y - 2.0, body, size=6.9, color=C["ink"], ls=1.2)
    # flecha al centro
    dx, dy = cx - x, cy - y
    d = math.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    p0 = (x + ux * 9.5, y + uy * 7.0)
    p1 = (cx - ux * 9.8, cy - uy * 9.8)
    arr(ax, p0, p1, color=MID[col], lw=1.6, ms=11, z=2)

txt(ax, 99, 3.0, "líneas punteadas: cada libertad refuerza a las otras", size=7.0, color=C["ink3"],
    ha="right", style="italic")
save(fig, "t1_rueda")
