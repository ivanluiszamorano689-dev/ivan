"""TP3 Parte B: IDH vs IDH-D (diez países), cascada de la pérdida por dimensión (Argentina y Bután),
cambio de ranking y diagrama de despejes para los parciales.
Datos: práctica resuelta, TP3 Parte B. Correr desde figs/: python3 p3_idhd.py"""
from p3_util import *  # noqa: F403
from math import log

T = [("Suiza", 0.970, 0.894, 7.8, 7.5), ("Australia", 0.958, 0.873, 8.9, 8.6),
     ("Estados Unidos", 0.937, 0.832, 11.2, 10.7), ("Argentina", 0.865, 0.761, 12.0, 11.6),
     ("Perú", 0.795, 0.633, 20.3, 19.9), ("Bután", 0.698, 0.478, 31.5, 30.0),
     ("El Salvador", 0.678, 0.555, 18.1, 17.8), ("Senegal", 0.529, 0.339, 35.9, 34.8),
     ("Yemen", 0.470, 0.325, 30.9, 29.8), ("Sudán del Sur", 0.388, 0.225, 42.0, 41.7)]

# ------------------------------------------------------------------ 1) barras apareadas
fig, ax = new_fig(6.6, 4.0)
n = len(T)
h = 0.36
for i, (p, idh, idhd, per, cdh) in enumerate(T):
    y = n - 1 - i
    ax.barh(y + h / 2, idh, h, color=C["blue"], zorder=2)
    ax.barh(y - h / 2, idhd, h, color=C["orange"], zorder=2)
    # tramo perdido
    ax.barh(y - h / 2, idh - idhd, h, left=idhd, color="white", edgecolor=C["ink3"], hatch="////", lw=0.6, zorder=2)
    ax.text(idh - 0.008, y + h / 2, coma(idh), va="center", ha="right", fontsize=7.4, color="white", fontweight="bold")
    ax.text(idhd - 0.008, y - h / 2, coma(idhd), va="center", ha="right", fontsize=7.4, color="white", fontweight="bold")
    col = C["red"] if per >= 30 else C["ink"]
    ax.text(1.075, y, coma(per, 1) + " %", va="center", ha="right", fontsize=8.4, fontweight="bold", color=col)
    ax.text(1.19, y, coma(cdh, 1) + " %", va="center", ha="right", fontsize=8.2, color=C["ink2"])
ax.text(1.075, n - 0.35, "pérdida", ha="right", va="bottom", fontsize=7.8, fontweight="bold")
ax.text(1.19, n - 0.35, "CDH", ha="right", va="bottom", fontsize=7.8, fontweight="bold", color=C["ink2"])
ax.set_yticks(range(n))
ax.set_yticklabels([t[0] for t in T][::-1], fontsize=8.6)
ax.tick_params(axis="y", length=0)
ax.set_xlim(0, 1.2)
ax.set_ylim(-0.6, n + 0.2)
ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax.xaxis.set_major_formatter(fmt_coma(1))
ax.grid(axis="x", color=GRID, lw=0.8)
ax.set_axisbelow(True)
ax.spines["left"].set_visible(False)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=C["blue"], label="IDH (potencial)"), Patch(color=C["orange"], label="IDH-D (efectivo)"),
                   Patch(fc="white", ec=C["ink3"], hatch="////", label="lo que se pierde por desigualdad")],
          loc="upper center", bbox_to_anchor=(0.45, -0.07), ncol=3, fontsize=7.9)
save(fig, "p3_idhd_barras")

# ------------------------------------------------------------------ 2) cascada por dimensión
def cascada(ax, nombre, idh, A, nota):
    lg = [log(1 - a) for a in A]
    tot = sum(lg)
    idhd = idh * np.exp(tot / 3)
    perd = idh - idhd
    partes = [perd * l / tot for l in lg]
    cols = [C["blue"], C["orange"], C["aqua"]]
    labs = ["salud", "educación", "ingreso"]
    ax.bar(0, idh, 0.62, color=C["ink2"], zorder=2)
    ax.text(0, idh + 0.012, coma(idh), ha="center", va="bottom", fontsize=8, fontweight="bold")
    top = idh
    for k, (pp, a) in enumerate(zip(partes, A)):
        ax.bar(k + 1, pp, 0.62, bottom=top - pp, color=cols[k], zorder=2)
        ax.plot([k + 0.69, k + 1.31], [top, top], color=C["ink3"], lw=0.7, zorder=1)
        ax.text(k + 1, top + 0.012, "−" + coma(pp), ha="center", va="bottom", fontsize=7.6, fontweight="bold")
        ax.text(k + 1, top - pp - 0.014, f"{coma(100 * pp / perd, 0)} %\nA = {coma(100 * a, 1)} %",
                ha="center", va="top", fontsize=6.9, color=C["ink2"], linespacing=1.15)
        top -= pp
    ax.plot([3.69, 4.31], [top, top], color=C["ink3"], lw=0.7, zorder=1)
    ax.bar(4, idhd, 0.62, color=C["orange"], zorder=2, hatch="", edgecolor="white")
    ax.text(4, idhd + 0.012, coma(idhd), ha="center", va="bottom", fontsize=8, fontweight="bold")
    ax.set_xticks(range(5))
    ax.set_xticklabels(["IDH", "salud", "educ.", "ingreso", "IDH-D"], fontsize=7.8)
    ax.set_ylim(0, 1.0)
    ax.yaxis.set_major_formatter(fmt_coma(1))
    data_axes(ax)
    ax.set_title(f"{nombre}: pierde {coma(perd, 3)} ({coma(100 * (1 - idhd / idh), 1)} %)", fontsize=9, pad=6)
    if nota:
        ax.text(0.99, 0.02, nota, transform=ax.transAxes, ha="right", va="bottom", fontsize=6.6, color=C["ink3"])


fig, (a1, a2) = new_fig(6.6, 2.9, ncols=2)
fig.subplots_adjust(wspace=0.22)
cascada(a1, "Argentina", 0.865, (0.074, 0.049, 0.226), "")
cascada(a2, "Bután", 0.698, (0.131, 0.482, 0.287), "")
save(fig, "p3_idhd_cascada")

# ------------------------------------------------------------------ 3) cambio de ranking (pendientes)
fig, ax = new_fig(3.25, 3.55)
for p, idh, idhd, per, cdh in T:
    hl = p in ("Bután", "El Salvador")
    col = C["orange"] if p == "Bután" else (C["blue"] if p == "El Salvador" else "#c9c7c0")
    ax.plot([0, 1], [idh, idhd], color=col, lw=2.2 if hl else 1.1, zorder=3 if hl else 2,
            marker="o", ms=4.5 if hl else 3, mec="white", mew=0.8)
lab_r = {"Suiza": 0.905, "Australia": 0.875, "Estados Unidos": 0.838, "Argentina": 0.761, "Perú": 0.633,
         "El Salvador": 0.560, "Bután": 0.475, "Senegal": 0.352, "Yemen": 0.318, "Sudán del Sur": 0.225}
for p, idh, idhd, per, cdh in T:
    hl = p in ("Bután", "El Salvador")
    ax.text(1.05, lab_r[p], f"{p} {coma(idhd)}" if hl else p, va="center", fontsize=7.3 if not hl else 7.8,
            color=C["ink"] if hl else C["ink3"], fontweight="bold" if hl else "normal")
ax.text(-0.05, 0.698 + 0.008, "Bután 0,698", ha="right", va="bottom", fontsize=7.8, fontweight="bold")
ax.text(-0.05, 0.678 - 0.008, "El Salvador 0,678", ha="right", va="top", fontsize=7.8, fontweight="bold")
ax.set_xlim(-0.95, 1.95)
ax.set_ylim(0.18, 1.02)
ax.set_xticks([0, 1])
ax.set_xticklabels(["IDH", "IDH-D"], fontsize=8.6, fontweight="bold")
ax.set_yticks([])
for s in ("left", "bottom"):
    ax.spines[s].set_visible(False)
ax.tick_params(axis="x", length=0)
for x in (0, 1):
    ax.axvline(x, color=C["rule"], lw=0.8, zorder=1)
save(fig, "p3_idhd_ranking")

# ------------------------------------------------------------------ 4) despejes
fig, ax = lienzo(6.7, 2.1, 10, 3.1)
Y = 2.45
caja(ax, 1.25, Y, 2.2, 0.95, "Dato del cuadro\nesp. de vida · años · INB", fc="white", ec=C["ink2"], size=8.2)
caja(ax, 5.0, Y, 2.0, 0.95, "Índice de dimensión\n" + r"$I_x$", fc=C["blue_bg"], ec=C["blue"], size=8.4, weight="bold")
caja(ax, 8.7, Y, 2.3, 0.95, "Índice ajustado\n" + r"$I_x^{*}=I_x\,(1-A_x)$", fc=C["orange_bg"], ec=C["orange"], size=8.4,
     weight="bold")
flecha(ax, 2.37, Y + 0.18, 3.98, Y + 0.18, color=C["blue"], lw=1.3)
ax.text(3.17, Y + 0.27, r"$I=\frac{\mathrm{dato}-\mathrm{mín}}{\mathrm{máx}-\mathrm{mín}}$", ha="center", va="bottom", fontsize=8.8)
flecha(ax, 3.98, Y - 0.18, 2.37, Y - 0.18, color=C["ink2"], lw=1.1)
ax.text(3.17, Y - 0.27, "despeje:\n" + r"$\mathrm{dato}=\mathrm{mín}+I\,(\mathrm{máx}-\mathrm{mín})$", ha="center", va="top",
        fontsize=7.6, color=C["ink2"], linespacing=1.3)
flecha(ax, 6.02, Y + 0.18, 7.53, Y + 0.18, color=C["orange"], lw=1.3)
ax.text(6.78, Y + 0.27, r"$\times(1-A_x)$", ha="center", va="bottom", fontsize=9)
flecha(ax, 7.53, Y - 0.18, 6.02, Y - 0.18, color=C["ink2"], lw=1.1)
ax.text(6.78, Y - 0.27, "despejes:\n" + r"$A_x=1-I_x^{*}/I_x$" + "\n" + r"$I_x=I_x^{*}/(1-A_x)$", ha="center", va="top",
        fontsize=7.6, color=C["ink2"], linespacing=1.3)
Y2 = 0.45
caja(ax, 1.55, Y2, 3.0, 0.72, "Ingreso (ln):  " + r"$\mathrm{INB}=100\cdot 750^{\,I_{ing}}$", fc=C["aqua_bg"],
     ec=C["aqua"], size=8.4)
caja(ax, 5.0, Y2, 3.6, 0.72, "Educación:  " + r"$I_{edu}=\frac{I_{esp}+I_{prom}}{2}$" + "  (aritmética)",
     fc=C["orange_bg"], ec=C["orange"], size=8.4)
caja(ax, 8.45, Y2, 3.0, 0.72, "IDH-D = " + r"$(I_s^{*}\cdot I_e^{*}\cdot I_i^{*})^{1/3}$", fc=C["gray_bg"], ec=C["ink"],
     size=8.4)
save(fig, "p3_despejes")
