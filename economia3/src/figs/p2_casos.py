"""TP2 Estudio de casos «El mundo es más igual de lo que piensas: datos PPA 2026».
Datos citados en el texto del caso (práctica) y en el manual de teoría (Tema 2.2).
Correr desde figs/:  python3 p2_casos.py"""
from p2_util import *  # noqa: F403

fig, axs = new_fig(6.5, 4.5, ncols=2, nrows=2)
fig.subplots_adjust(hspace=0.75, wspace=0.42)

# (a) PBI mundial a PPA por grupo de ingreso
ax = axs[0, 0]
grupos = [("Ingreso medio y bajo", 53, C["aqua"]), ("Ingreso alto", 46, C["blue"])]
for k, (g, v, col) in enumerate(grupos):
    ax.barh(1 - k, v, color=col, height=0.55, zorder=2)
    ax.text(v + 1, 1 - k, f"{v}%", va="center", fontsize=9, fontweight="bold")
ax.set_yticks([1, 0])
ax.set_yticklabels([g[0] for g in grupos], fontsize=8)
ax.set_xlim(0, 65)
ax.xaxis.set_major_formatter(fmt_pct())
ax.set_xticks([0, 20, 40, 60])
ax.tick_params(axis="y", length=0)
ax.grid(axis="x", color="#ebe9e3", lw=0.8)
ax.set_axisbelow(True)
ax.set_title("(a) Participación en el PBI mundial a PPA", fontsize=9, pad=7)

# (b) China y EEUU: TCm vs PPA
ax = axs[0, 1]
xp = np.arange(2)
w = 0.36
vals = {"a TC de mercado": ((26.0, 16.5), C["orange"]), "a PPA": ((14.6, 19.5), C["blue"])}
for k, (lab, (v, col)) in enumerate(vals.items()):
    ax.bar(xp + (k - 0.5) * w, v, w * 0.95, color=col, label=lab, zorder=2)
    for xi, vi in zip(xp + (k - 0.5) * w, v):
        ax.text(xi, vi + 0.6, coma(vi, 1), ha="center", va="bottom", fontsize=7.8, fontweight="bold")
ax.set_xticks(xp)
ax.set_xticklabels(["Estados Unidos", "China"], fontsize=8.2)
ax.set_ylim(0, 34)
ax.yaxis.set_major_formatter(fmt_pct())
ax.legend(loc="upper right", fontsize=7.5, handlelength=1.0, borderaxespad=0.1)
data_axes(ax)
ax.set_title("(b) % de la economía mundial", fontsize=9, pad=7)

# (c) distribución interna del ingreso ajustado por PPA
ax = axs[1, 0]
seg = [("50% más pobre", 50, 8, C["orange"]), ("40% del medio", 40, 40, C["ink3"]), ("10% más rico", 10, 52, C["blue"])]
for yv, idx, tit in ((1, 1, "Población"), (0, 2, "Ingreso")):
    left = 0
    for nm, pob, ing, col in seg:
        v = pob if idx == 1 else ing
        ax.barh(yv, v, left=left, color=col, height=0.55, edgecolor="white", lw=1.2, zorder=2)
        if v >= 7:
            ax.text(left + v / 2, yv, f"{v}%", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
        left += v
ax.set_yticks([1, 0])
ax.set_yticklabels(["Población", "Ingreso"], fontsize=8.2)
ax.set_xlim(0, 100)
ax.xaxis.set_major_formatter(fmt_pct())
ax.tick_params(axis="y", length=0)
for nm, pob, ing, col in seg:
    ax.bar(0, 0, color=col, label=nm)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=3, fontsize=7.2, handlelength=0.9,
          columnspacing=0.8, handletextpad=0.4)
ax.set_title("(c) Desigualdad interna (ingreso a PPA)", fontsize=9, pad=7)

# (d) 74 de 96 países
ax = axs[1, 1]
ncol, nfil = 16, 6
k = 0
for fila in range(nfil):
    for col in range(ncol):
        c = C["blue"] if k < 74 else C["rule"]
        ax.add_patch(plt.Rectangle((col, nfil - 1 - fila), 0.82, 0.82, color=c))
        k += 1
ax.set_xlim(-0.2, ncol)
ax.set_ylim(-0.2, nfil)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("(d) Salario mínimo ×2 a ×4 al pasarlo a PPA", fontsize=9, pad=7)
ax.text(0, -0.9, "74 de 96 países de renta baja y media (■ azul)", fontsize=7.6, color=C["ink2"], va="top")
save(fig, "p2_casos")
print("ok")
