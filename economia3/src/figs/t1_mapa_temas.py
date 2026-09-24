"""Figura 0.1 — Mapa de los tres temas del primer parcial."""
from t1_util import *

fig, ax, H = canvas(6.8, 3.75)

cols = [
    ("violet", "TEMA 1", "Desarrollo y libertad", "¿Qué es desarrollarse?",
     ["Crecimiento ≠ desarrollo", "Enfoque de capacidades (Sen)", "La libertad: fin y medio",
      "Las 5 libertades instrumentales", "De los ODM a los ODS", "Rasgos del subdesarrollo", "CE y DH (Ranis-Stewart)"], "TP1"),
    ("blue", "TEMA 2", "Indicadores del bienestar", "¿Cómo se mide?",
     ["PBI, PBN, nominal y real", "TC de mercado vs PPA", "Índice Big Mac", "Tasas de crecimiento",
      "IDH: salud · educación · ingreso", "IDH-D e IDG", "Índice de Progreso Social"], "TP2 · TP3"),
    ("aqua", "TEMA 3", "Crecimiento económico", "¿Cómo se crece?",
     ["Hechos del crecimiento", "Harrod-Domar", "Solow-Swan: k*, y*, estática", "Regla de oro",
      "Solow con progreso técnico", "Contabilidad y convergencia", "Romer: crecimiento endógeno"], "TP4"),
]
bw, gap, x0 = 29.5, 5.25, 0.5
top, bot = H - 1.0, 11.5
for i, (col, kick, title, q, items, tp) in enumerate(cols):
    x = x0 + i * (bw + gap)
    rbox(ax, x, bot, bw, top - bot, col, fill="white", lw=1.6, r=2.2)
    # banda de encabezado
    rbox(ax, x, top - 10.2, bw, 10.2, col, fill="solid", lw=1.6, r=2.2)
    ax.add_patch(plt.Rectangle((x + 0.05, top - 10.2), bw - 0.1, 3, fc=MID[col], ec="none", zorder=2))
    txt(ax, x + 2, top - 2.6, kick, size=7.4, color="white", weight="bold", ha="left")
    txt(ax, x + 2, top - 6.6, title, size=9.6, color="white", weight="bold", ha="left")
    txt(ax, x + bw / 2, top - 13.4, q, size=9.2, color=DARK[col], weight="bold", style="italic")
    yy = top - 17.8
    for it in items:
        bullet = not it.startswith("   ")
        if bullet:
            ax.plot([x + 2.4], [yy], "o", ms=3.2, color=MID[col], zorder=5)
        txt(ax, x + 3.9, yy, it.strip(), size=7.9, color=C["ink"], ha="left")
        yy -= 3.15
    pill(ax, x + bw / 2, bot + 2.7, "Práctica: " + tp, color=col, size=7.4, h=3.2)

# flechas entre temas
for i in range(2):
    xa = x0 + (i + 1) * bw + i * gap + 0.6
    arr(ax, (xa, (top + bot) / 2 + 6), (xa + gap - 1.2, (top + bot) / 2 + 6), color=C["ink2"], lw=2.0, ms=14)

# flecha de vuelta (Tema 4)
xl = x0 + bw / 2
xr = x0 + 2 * (bw + gap) + bw / 2
yb = 5.0
ax.plot([xr, xr, xl, xl], [bot, yb, yb, bot - 0.4], color=C["ink3"], lw=1.4, ls=(0, (4, 3)), zorder=1)
arr(ax, (xl, yb + 0.1), (xl, bot - 0.1), color=C["ink3"], lw=1.4, ms=12)
rbox(ax, 50 - 31, yb - 2.3, 62, 4.6, "gray", fill="white", lw=0, r=1)
txt(ax, 50, yb, "Tema 4 (y 1.6 de este manual): ¿el crecimiento se traduce en desarrollo humano?", size=7.8,
    color=C["ink2"], style="italic")
save(fig, "t1_mapa_temas")
