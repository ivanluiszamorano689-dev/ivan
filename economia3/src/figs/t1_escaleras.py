"""Figura 1.8 — Dos escaleras para clasificar países: ingreso (Banco Mundial) y desarrollo humano (PNUD). Esquemático."""
from t1_util import *
from matplotlib.colors import to_rgb


def mix(hex_color, t):
    r, g, b = to_rgb(hex_color)
    return (1 - t + t * r, 1 - t + t * g, 1 - t + t * b)


fig, ax, H = canvas(6.8, 3.05)
BW, SH, Y0 = 38.0, 5.4, 13.0
ladders = [
    (3.0, "blue", "BANCO MUNDIAL · por ingreso", "INB per cápita, método Atlas: criterio puramente monetario",
     ["Ingreso bajo", "Ingreso mediano bajo", "Ingreso mediano alto", "Ingreso alto"],
     ["", "", "", ""], "umbrales en US$ que se actualizan cada año"),
    (57.0, "violet", "PNUD · por desarrollo humano", "IDH: incorpora salud y educación además del ingreso",
     ["DH bajo", "DH medio", "DH alto", "DH muy alto"],
     ["< 0,550", "0,550 – 0,699", "0,700 – 0,799", "≥ 0,800"], "cortes del IDH (se ven en el Tema 2)"),
]
for x, col, title, sub, steps, cuts, note in ladders:
    txt(ax, x, Y0 + 4 * SH + 6.3, title, size=8.8, color=DARK[col], weight="bold", ha="left")
    txt(ax, x, Y0 + 4 * SH + 2.6, sub, size=7.1, color=C["ink2"], ha="left")
    for i, (s, c) in enumerate(zip(steps, cuts)):
        t = 0.16 + 0.25 * i
        yy = Y0 + i * SH
        ax.add_patch(FancyBboxPatch((x, yy), BW, SH - 0.7, boxstyle="round,pad=0,rounding_size=1.0",
                                    fc=mix(MID[col], t), ec="none", zorder=2))
        tc = "white" if t > 0.55 else DARK[col]
        ym = yy + (SH - 0.7) / 2
        txt(ax, x + 1.6, ym, s, size=7.9, color=tc, weight="bold", ha="left")
        if c:
            txt(ax, x + 17.5, ym, c, size=7.5, color=tc, ha="left")
    txt(ax, x, Y0 - 2.4, note, size=7.0, color=C["ink3"], ha="left", style="italic")

# país X: sube por ingreso, no se mueve por DH
lx, rx = 3.0, 57.0
ym = lambda i: Y0 + i * SH + (SH - 0.7) / 2
xm = lx + BW - 3.0
arr(ax, (xm, ym(1) + 0.9), (xm, ym(2) - 1.0), color=C["orange"], lw=1.6, ms=10, z=6)
point(ax, xm, ym(1), C["orange"])
point(ax, xm, ym(2), C["orange"])
txt(ax, lx + BW + 1.5, ym(1.5), "País X:\nsube por\ningreso…", size=7.4, color=DARK["orange"], weight="bold",
    ha="left")
xr = rx + BW - 3.0
point(ax, xr, ym(1), C["orange"])
txt(ax, rx + BW + 1.5, ym(1), "…y sigue\nen DH medio", size=7.4, color=DARK["orange"], weight="bold", ha="left")

rbox(ax, 3.0, 0.3, 94, 7.2, "gray", fill="bg", lw=0, r=1.2)
txt(ax, 50, 3.9, "Aparte, la ONU define los PAÍSES MENOS ADELANTADOS: ingreso bajo + debilidad de capital humano\n"
    "+ vulnerabilidad económica y ambiental", size=7.3, color=C["ink"])
save(fig, "t1_escaleras")
