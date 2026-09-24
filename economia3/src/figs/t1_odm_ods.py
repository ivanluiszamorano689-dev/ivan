"""Figura 1.6 — Línea de tiempo: de los ODM (2000-2015) a los ODS (2015-2030)."""
from t1_util import *

fig, ax, H = canvas(6.8, 2.85)
X = lambda yr: 5.0 + (yr - 1990) * 2.25          # 1990 -> 5 ; 2030 -> 95
ya = 22.0                                        # eje del tiempo

ax.plot([X(1989), X(2031.5)], [ya, ya], color=C["ink2"], lw=1.4, zorder=2)
arr(ax, (X(2031), ya), (X(2032.2), ya), color=C["ink2"], lw=1.4, ms=10)
for yr in [1990, 2000, 2015, 2030]:
    ax.plot([X(yr)], [ya], "o", ms=7, color="white", mec=C["ink"], mew=1.6, zorder=4)
    txt(ax, X(yr), ya - 3.2, str(yr), size=8.6, weight="bold")

# barras de cada agenda
for (a, b, col, t1, t2) in [(2000, 2015, "blue", "ODM · Objetivos del Milenio",
                             "8 objetivos · 21 metas · 60 indicadores"),
                            (2015, 2030, "aqua", "ODS · Agenda 2030",
                             "17 objetivos · 169 metas · 230 indicadores")]:
    rbox(ax, X(a) + 0.6, ya + 2.2, X(b) - X(a) - 1.2, 9.0, col, fill="solid", lw=0, r=1.4)
    txt(ax, (X(a) + X(b)) / 2, ya + 8.4, t1, size=8.2, color="white", weight="bold")
    txt(ax, (X(a) + X(b)) / 2, ya + 4.6, t2, size=7.6, color="white")

# hitos
txt(ax, X(2000), ya + 15.6, "Declaración del Milenio\n189 países", size=7.5, color=DARK["blue"], weight="bold")
txt(ax, X(2015), ya + 15.6, "Agenda 2030\n193 Estados", size=7.5, color=DARK["aqua"], weight="bold")
txt(ax, X(1990) + 0.2, ya + 6.6, "año base\nde las metas", size=7.2, color=C["ink2"], style="italic")

# meta ODM 1 (1990 -> 2015)
yb = ya - 7.2
ax.plot([X(1990), X(1990), X(2015), X(2015)], [ya - 5.2, yb, yb, ya - 5.2], color=C["blue"], lw=1.1, zorder=1)
txt(ax, (X(1990) + X(2015)) / 2, yb - 2.3, "ODM 1: reducir a la mitad la pobreza extrema (< 1 dólar diario) y el hambre entre 1990 y 2015",
    size=7.2, color=DARK["blue"])

# rasgos
rbox(ax, X(2000) - 17, 0.6, 40, 8.2, "blue", fill="bg", lw=1.0, r=1.4)
txt(ax, X(2000) + 3, 4.7, "foco social (pobreza, hambre, salud, educación)\npaíses en desarrollo · objetivos por separado",
    size=7.1, color=C["ink"])
rbox(ax, 53.5, 0.6, 45.5, 8.2, "aqua", fill="bg", lw=1.0, r=1.4)
txt(ax, 76.25, 4.7, "universales · indivisibles · sostenibles · ambiciosos\n3 dimensiones: económica, social y ambiental",
    size=7.1, color=C["ink"])
txt(ax, X(2030) + 0.5, ya + 15.6, "“nadie es\ndejado atrás”", size=7.5, color=DARK["aqua"], style="italic")
save(fig, "t1_odm_ods")
