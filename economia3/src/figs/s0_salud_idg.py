"""§4 · P3 d: el índice de salud reproductiva es un LOGRO (más alto = mejor);
el IDG final mide DESIGUALDAD (más bajo = mejor). Datos: P3 (TMM, TNA) y P6/P7 (IDG publicados en el examen)."""
from s0_util import *

fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.0, 2.45), gridspec_kw=dict(hspace=1.1, height_ratios=[1, 1.2]))

def line(ax, xlim, ticks, dec):
    ax.set_xlim(*xlim)
    ax.set_ylim(-0.6, 0.9)
    for s in ("left", "top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_position(("data", 0))
    ax.spines["bottom"].set_color(C["ink3"])
    ax.set_yticks([])
    ax.set_xticks(ticks)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: comma(v, dec)))
    ax.tick_params(axis="x", labelsize=7.4, colors=C["ink3"], pad=2)

# --- índice de salud reproductiva (logro)
line(a1, (0, 0.06), [0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06], 2)
for v, n, col, dy in [(0.0281, "Namibia 0,0281", "blue", 1), (0.0464, "Honduras 0,0464", "orange", 1)]:
    a1.plot([v], [0], "o", ms=8, color=C[col], mec="white", mew=1.5, zorder=4)
    a1.annotate(n, (v, 0), xytext=(0, 9), textcoords="offset points", ha="center", va="bottom", fontsize=8,
                fontweight="bold", color=DARK[col])
arrow(a1, 0.001, 0.55, 0.009, 0.55, color=C["green"], lw=1.4)
a1.text(0.0095, 0.55, "mejor", ha="left", va="center", fontsize=7.8, color=DARK["green"], fontweight="bold")
a1.set_title(r"Índice de salud reproductiva $\sqrt{10/\mathrm{TMM}\cdot 1/\mathrm{TNA}}$ — es un LOGRO: más alto, mejor",
             fontsize=8.4, pad=4)

# --- IDG final (desigualdad)
line(a2, (0, 0.6), [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6], 1)
a2.set_ylim(-0.6, 1.25)
for v, n, col, dy in [(0.268, "Barbados 0,268", "blue", 9), (0.335, "Jamaica 0,335", "orange", 23),
                      (0.454, "Guyana 0,454", "aqua", 9)]:
    a2.plot([v], [0], "o", ms=8, color=C[col], mec="white", mew=1.5, zorder=4)
    if dy > 10:
        a2.plot([v, v], [0.12, 0.62], color=C[col], lw=0.8, zorder=3)
    a2.annotate(n, (v, 0), xytext=(0, dy), textcoords="offset points",
                ha="center", va="bottom", fontsize=8, fontweight="bold", color=DARK[col])
arrow(a2, 0.11, 0.55, 0.01, 0.55, color=C["green"], lw=1.4)
a2.text(0.115, 0.55, "mejor", ha="left", va="center", fontsize=7.8, color=DARK["green"], fontweight="bold")
a2.set_title("IDG final (P6 y P7) — mide DESIGUALDAD: más bajo, mejor (0 = igualdad)", fontsize=8.4, pad=4)
save(fig, "s0_salud_idg")
