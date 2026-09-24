"""§4 · Árbol de decisión para clasificar casos según las cinco libertades instrumentales de Sen
(criterio del manual, Tema 1.3) aplicado a los tres casos de Yemen (P8 · Ej.3 c, 2025)."""
from s0_util import *

fig, ax, H = canvas(6.7, 2.95)

rows = [
    ("Quién gobierna y cómo: elecciones, crítica, prensa, reclamo público, justicia",
     "Libertades políticas", "Guerra civil entre rebeldes y gobierno"),
    ("Ingresos, crédito, financiamiento, precios, mercados, intercambio",
     "Servicios económicos", None),
    ("Acceso a salud o educación: escuelas, hospitales, vacunación",
     "Oportunidades sociales", "20 % de los niños nunca vacunados"),
    ("Información ocultada, corrupción, conflicto de intereses, rendición de cuentas",
     "Garantías de transparencia", None),
    ("Red de protección: ayuda de emergencia (ad hoc) o prestaciones fijas por ley",
     "Seguridad protectora", "Inundación: Ibrahim y su hijo lo perdieron todo"),
]

top = H - 4.6
rh = 6.6
rg = 1.25
cx0, cw = 24.5, 33.0      # condiciones
lx0, lw = 62.0, 17.5      # libertades
tx0, tw = 83.0, 16.5      # casos de Yemen

# raíz
ry0 = top - 5 * rh - 4 * rg
rbox(ax, 0.8, ry0, 18.5, top - ry0, "violet", fill="solid", lw=0, r=1.6)
txt(ax, 10.05, top - 4.2, "Leé el caso y preguntá:", size=7.3, color="white", n=14)
txt(ax, 10.05, (top + ry0) / 2, "¿Qué institución falla o funciona?", size=8.6, color="white",
    weight="bold", n=13)
txt(ax, 10.05, ry0 + 3.2, "(no «de qué tema habla»)", size=6.6, color="#e4e0f7", n=16)

# encabezados de columna
txt(ax, cx0 + cw / 2, top + 2.4, "si el núcleo del caso es…", size=7.2, color=C["ink3"], style="italic")
txt(ax, lx0 + lw / 2, top + 2.4, "…es la libertad", size=7.2, color=C["ink3"], style="italic")
txt(ax, tx0 + tw / 2, top + 2.4, "Yemen (P8 · Ej.3 c)", size=7.2, color=DARK["orange"], weight="bold")

for i, (cond, lib, caso) in enumerate(rows):
    y = top - (i + 1) * rh - i * rg
    ym = y + rh / 2
    rbox(ax, cx0, y, cw, rh, "gray", fill="white", lw=1.0, r=1.0, ec=C["rule"])
    txt(ax, cx0 + 1.3, ym, cond, size=6.9, ha="left", n=44, ls=1.15)
    elbow(ax, (19.3, (top + ry0) / 2), (cx0 - 0.2, ym), color=C["violet"], lw=1.0, xm=21.6)
    rbox(ax, lx0, y, lw, rh, "violet", fill="bg" if caso else "white", lw=1.2 if caso else 0.9,
         ec=None if caso else C["violet"])
    txt(ax, lx0 + lw / 2, ym, lib, size=7.4, weight="bold", color=DARK["violet"], n=15, ls=1.1)
    arr(ax, (cx0 + cw + 0.3, ym), (lx0 - 0.3, ym), color=C["ink3"], lw=1.1)
    if caso:
        rbox(ax, tx0, y + 0.5, tw, rh - 1.0, "orange", fill="bg", lw=1.0, r=1.0)
        txt(ax, tx0 + tw / 2, ym, caso, size=6.5, n=21, ls=1.1)
        arr(ax, (tx0 - 0.3, ym), (lx0 + lw + 0.3, ym), color=C["orange"], lw=1.2)
save(fig, "s0_arbol_sen")
