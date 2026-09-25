import sys; sys.path.insert(0, "../lib")
from econ_style import *

# Datos reales: Índice Big Mac julio 2024 (Parcial 2025, Ej. 2) + país X (E2 de este anexo)
paises = ["Azerbaiyán", "Bahrein", "Emiratos Árabes", "Australia", "País X (E2)"]
valores = [-36.4, -21.4, -13.8, -11.0, 31.98]

colors = [C["blue"] if v < 0 else C["orange"] for v in valores]

fig, ax = new_fig(6.3, 3.7)
ypos = np.arange(len(paises))
ax.barh(ypos, valores, color=colors, height=0.58, zorder=3)
ax.set_yticks(ypos)
ax.set_yticklabels(paises)
ax.invert_yaxis()
ax.axvline(0, color=C["ink2"], lw=0.9)
data_axes(ax, xlabel="sub/sobrevaluación de la moneda frente al US$ (%)", ylabel="")
ax.grid(axis="x", color="#ebe9e3", lw=0.8)
ax.set_axisbelow(True)
for y, v in zip(ypos, valores):
    txt = f"{v:.1f}".replace(".", ",") + " %"
    if v < 0:
        ax.annotate(txt, (v, y), xytext=(-6, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=9, color=C["ink"], fontweight="bold")
    else:
        ax.annotate("+" + txt, (v, y), xytext=(6, 0), textcoords="offset points", ha="left", va="center",
                     fontsize=9, color=C["ink"], fontweight="bold")
ax.set_xlim(-42, 42)
label_curve(ax, -36, 4.55, "subvaluada", C["blue"], size=8.5)
label_curve(ax, 20, 4.55, "sobrevaluada", C["orange"], size=8.5)
fig.tight_layout()
save(fig, "p9_bigmac")
