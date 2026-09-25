import sys; sys.path.insert(0, "../lib")
from econ_style import *

aporte_capital = 1.575   # puntos porcentuales, s_K * g_k = 0,35 * 4,5%
aporte_prod = 1.525      # residuo de Solow, g_A
gy = aporte_capital + aporte_prod  # 3,10 %

fig, ax = new_fig(3.6, 3.9)
x = 0
ax.bar(x, aporte_capital, width=0.5, color=C["blue"], zorder=3, label="capital")
ax.bar(x, aporte_prod, width=0.5, bottom=aporte_capital, color=C["orange"], zorder=3, label="productividad")
data_axes(ax, xlabel="", ylabel="puntos porcentuales de $g_y$")
ax.set_xticks([x])
ax.set_xticklabels([r"$g_y = 3{,}10\,\%$"])
ax.set_xlim(-0.55, 0.55)
ax.set_ylim(0, 3.5)
ax.annotate("acumulación\nde capital\n50,8 %", (x, aporte_capital / 2), ha="center", va="center",
            fontsize=8.7, color="white", fontweight="bold")
ax.annotate("productividad\n(residuo)\n49,2 %", (x, aporte_capital + aporte_prod / 2), ha="center", va="center",
            fontsize=8.7, color="white", fontweight="bold")
ax.annotate(r"$3{,}10\,\%$", (x, gy), xytext=(0, 5), textcoords="offset points", ha="center",
            fontsize=10, color=C["ink"], fontweight="bold")
fig.tight_layout()
save(fig, "p9_contabilidad_e11")
