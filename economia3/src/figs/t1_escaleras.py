"""Figura 1.8 — Dos escaleras para clasificar países: ingreso (Banco Mundial) y desarrollo humano (PNUD). Esquemático."""
from t1_util import *
from matplotlib.colors import to_rgb


def mix(hex_color, t):
    r, g, b = to_rgb(hex_color)
    return (1 - t + t * r, 1 - t + t * g, 1 - t + t * b)


fig, ax, H = canvas(6.8, 3.55)
ladders = [
    (3.0, "blue", "BANCO MUNDIAL · por ingreso", "INB per cápita (método Atlas) · criterio monetario",
     ["Ingreso bajo", "Ingreso mediano bajo", "Ingreso mediano alto", "Ingreso alto"],
     ["", "", "", ""], "umbrales en US$: se actualizan cada año"),
    (58.0, "violet", "PNUD · por desarrollo humano", "IDH: salud + educación + ingreso",
     ["DH bajo", "DH medio", "DH alto", "DH muy alto"],
     ["< 0,550", "0,550 – 0,699", "0,700 – 0,799", "≥ 0,800"], "cortes fijos (se ven en el Tema 2)"),
]
sw, sh, y0 = 11.0, 6.4, 12.0
for x, col, title, sub, steps, cuts, note in ladders:
    txt(ax, x, H - 2.6, title, size=8.8, color=DARK[col], weight="bold", ha="left")
    txt(ax, x, H - 6.2, sub, size=7.3, color=C["ink2"], ha="left")
    for i, (s, c) in enumerate(zip(steps, cuts)):
        t = 0.18 + 0.24 * i
        yy = y0 + i * sh
        w = 23 + i * sw * 0.0
        xs = x + i * 3.2
        ww = 36 - i * 3.2 + 3.2 * 0
        ax.add_patch(FancyBboxPatch((xs, yy), 36 - i * 3.2 * 0, sh - 0.7, boxstyle="round,pad=0,rounding_size=1.0",
                                    fc=mix(MID[col], t), ec="none", zorder=2))
        tc = "white" if t > 0.55 else DARK[col]
        txt(ax, xs + 1.6, yy + (sh - 0.7) / 2, s, size=7.9, color=tc, weight="bold", ha="left")
        if c:
            txt(ax, xs + 34.4, yy + (sh - 0.7) / 2, c, size=7.6, color=tc, ha="right")
    txt(ax, x, y0 - 2.6, note, size=7.0, color=C["ink3"], ha="left", style="italic")

# país que sube en una escalera y no en la otra
lx, rx = 3.0, 58.0
yA0, yA1 = y0 + 1 * sh + (sh - 0.7) / 2, y0 + 2 * sh + (sh - 0.7) / 2
xm = lx + 36 + 2.5
point(ax, xm, yA0, C["orange"])
point(ax, xm, yA1, C["orange"])
arr(ax, (xm, yA0 + 1.2), (xm, yA1 - 1.3), color=C["orange"], lw=1.6, ms=10)
txt(ax, xm + 2.0, (yA0 + yA1) / 2, "País X\ncrece su\ningreso…", size=7.3, color=DARK["orange"],
    weight="bold", ha="left")
yB = y0 + 1 * sh + (sh - 0.7) / 2
xr = rx + 3.2 + 36 + 2.5
point(ax, xr, yB, C["orange"])
txt(ax, xr + 2.0, yB + 0.2, "…y sigue\nen DH\nmedio", size=7.3, color=DARK["orange"], weight="bold", ha="left")

rbox(ax, 3.0, 0.4, 94, 5.4, "gray", fill="bg", lw=0, r=1.2)
txt(ax, 50, 3.1, "Aparte, la ONU define los PAÍSES MENOS ADELANTADOS: ingreso bajo + debilidad de capital humano + "
    "vulnerabilidad económica y ambiental", size=7.1, color=C["ink"])
save(fig, "t1_escaleras")
