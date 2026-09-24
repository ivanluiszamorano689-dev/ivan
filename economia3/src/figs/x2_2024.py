"""Gráficos de los parciales 2024 (P4-P5 teóricos, P6-P7 prácticos).

Correr desde figs/:  python3 x2_2024.py   -> figs/out/x2_*.svg
Datos: enunciados de las pruebas del 20/9/2024 y 28/9/2024 (CLAVE_PARCIALES.md).
"""
import sys

sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D


def coma(dec):
    return lambda v, p=None: f"{v:.{dec}f}".replace(".", ",")


def fmt(v, dec):
    return f"{v:.{dec}f}".replace(".", ",")


YRS = [2018, 2019, 2020, 2021, 2022, 2023]
USA = [63201, 65548, 64317, 71056, 77247, 81695]
UCR_TCM = [3097, 3661, 3752, 4828, 4576, 5181]
UCR_PPA = [12709, 14381, 15717, 18040, 16080, 18007]
RUS_TCM = [11212, 11448, 10108, 12522, 15445, 13817]
RUS_PPA = [28629, 30964, 31491, 38938, 40958, 44104]
UCR, RUS, USC = C["orange"], C["aqua"], C["blue"]

# ------------------------------------------------------------------ P4.1  brecha a TCm vs a PPA
fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.45))
fig.subplots_adjust(wspace=0.28)
paneles = [("EEUU / Ucrania", UCR_TCM, UCR_PPA, UCR, 23), ("EEUU / Rusia", RUS_TCM, RUS_PPA, RUS, 7.6)]
for ax, (tit, tcm, ppa, col, ymax) in zip(axs, paneles):
    ax.axvspan(2019.6, 2020.4, color=C["yellow_bg"], zorder=0)
    yt = [u / x for u, x in zip(USA, tcm)]
    yp = [u / x for u, x in zip(USA, ppa)]
    ax.plot(YRS, yt, color=col, lw=LW, marker="o", ms=3.8, mec="white", mew=0.8, zorder=3)
    ax.plot(YRS, yp, color=col, lw=LW, ls="--", marker="o", ms=3.5, mfc="white", mec=col, zorder=3)
    data_axes(ax, "", "veces" if ax is axs[0] else "")
    ax.set_ylim(0, ymax)
    ax.set_xlim(2017.6, 2024.9)
    ax.set_xticks(YRS)
    ax.set_xticklabels([str(a) if a in (2018, 2020, 2023) else f"'{str(a)[2:]}" for a in YRS])
    ax.set_title(tit, fontsize=9, loc="left", pad=6)
    ax.text(2023.2, yt[-1], "a TCm", color=col, fontsize=8, fontweight="bold", va="center")
    ax.text(2023.2, yp[-1], "a PPA", color=col, fontsize=8, fontweight="bold", va="center")
    ax.annotate(fmt(yt[2], 1), (2020, yt[2]), xytext=(0, 5), textcoords="offset points", ha="center",
                va="bottom", fontsize=7.8, color=C["ink"], fontweight="bold")
    ax.annotate(fmt(yp[2], 1), (2020, yp[2]), xytext=(0, 5), textcoords="offset points", ha="center",
                va="bottom", fontsize=7.8, color=C["ink"], fontweight="bold")
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.0f}"))
save(fig, "x2_brecha_tcm_ppa")

# ------------------------------------------------------------------ P4.2  efecto nivel vs efecto crecimiento
t = np.linspace(0, 10, 400)
t0, g0, g1 = 3.5, 0.10, 0.26
base = 1.0 + g0 * t
sub = base + np.where(t > t0, 0.55 * (1 - np.exp(-0.9 * (t - t0))), 0)
gup = np.where(t > t0, 1.0 + g0 * t0 + g1 * (t - t0), base)
fig, ax = new_fig(6.2, 2.75)
ax.plot(t, gup, color=C["aqua"], lw=LW)
ax.plot(t, sub, color=C["orange"], lw=LW)
ax.plot(t, base, color=C["blue"], lw=LW)
econ_axes(ax, r"$t$", r"$\ln y$", xlim=(0, 11.2), ylim=(0.6, 3.3))
vguide(ax, t0, 1.0 + g0 * t0, r"$t_0$", size=9.5)
ax.text(10, 1.47, "sin cambios: pendiente $g$", color=C["blue"], fontsize=8.6, fontweight="bold",
        ha="right", va="top")
ax.annotate("sube $g$: cambia la PENDIENTE\n(efecto crecimiento)", (7.2, 1.35 + g1 * (7.2 - t0)),
            xytext=(3.9, 3.22), fontsize=8.6, color=C["aqua"], fontweight="bold", ha="left", va="top",
            arrowprops=dict(arrowstyle="-", color=C["aqua"], lw=0.8))
i5 = np.searchsorted(t, 5.0)
ax.annotate("sube $s$: salta el NIVEL durante\nla transición; después, pendiente $g$", (5.0, sub[i5]),
            xytext=(0.25, 2.55), fontsize=8.6, color=C["orange"], fontweight="bold", ha="left", va="top",
            arrowprops=dict(arrowstyle="-", color=C["orange"], lw=0.8))
i9 = np.searchsorted(t, 9.6)
ax.annotate("", xy=(9.6, sub[i9]), xytext=(9.6, base[i9]),
            arrowprops=dict(arrowstyle="<|-|>", color=C["ink2"], lw=1.0, mutation_scale=8, shrinkA=2, shrinkB=2))
ax.text(9.75, (sub[i9] + base[i9]) / 2, "efecto\nnivel", fontsize=7.8, color=C["ink2"], va="center", ha="left")
save(fig, "x2_nivel_crecimiento")

# ------------------------------------------------------------------ P6.1  IDH e IDH-D con la escala + IDG
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.5, 2.55), gridspec_kw=dict(width_ratios=[2.35, 1]))
fig.subplots_adjust(wspace=0.08)
bands = [(0.50, 0.55, "Bajo", "#f3f2ee"), (0.55, 0.70, "Medio", "#e6eef8"), (0.70, 0.80, "Alto", "#cfe0f5"),
         (0.80, 0.86, "Muy alto", "#b4d0f1")]
for a_, b_, lab, col in bands:
    a1.add_patch(Rectangle((a_, -0.6), b_ - a_, 3.2, fc=col, ec="none", zorder=0))
    a1.text((a_ + b_) / 2, 2.45, lab, ha="center", va="bottom", fontsize=8, fontweight="bold", color=C["ink2"])
for v in (0.55, 0.70, 0.80):
    a1.plot([v, v], [-0.6, 2.4], color="white", lw=1.4, zorder=1)
paises = [("Barbados", 0.7902, None, None, USC), ("Guyana", 0.7143, 0.5906, 17.3, UCR),
          ("Jamaica", 0.7094, 0.5918, 16.6, RUS)]
for i, (nom, idh, idhd, perd, col) in enumerate(paises):
    y = 2 - i
    a1.text(0.497, y, nom, ha="right", va="center", fontsize=8.8, fontweight="bold", color=C["ink"])
    if idhd is not None:
        a1.annotate("", xy=(idhd + 0.004, y), xytext=(idh - 0.004, y),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=1.4, mutation_scale=9), zorder=3)
        a1.plot([idhd], [y], "o", ms=8, mfc="white", mec=col, mew=2, zorder=4)
        a1.text(idhd, y - 0.3, f"IDH-D {fmt(idhd, 3)}", ha="center", va="top", fontsize=7.8, color=C["ink"])
        a1.text((idh + idhd) / 2, y + 0.13, f"−{fmt(perd, 1)} %", ha="center", va="bottom", fontsize=7.8,
                color=col, fontweight="bold")
    a1.plot([idh], [y], "o", ms=8, color=col, mec="white", mew=1.2, zorder=4)
    a1.text(idh, y - 0.3, f"IDH {fmt(idh, 3)}", ha="center", va="top", fontsize=7.8, color=C["ink"],
            fontweight="bold")
a1.text(0.835, 2, "IDH-D\nno dado", ha="center", va="center", fontsize=7.2, color=C["ink3"])
a1.set_xlim(0.50, 0.86)
a1.set_ylim(-0.6, 2.85)
a1.axis("off")
a1.legend(handles=[Line2D([], [], marker="o", ls="", color=C["ink2"], ms=6, label="IDH"),
                   Line2D([], [], marker="o", ls="", mfc="white", mec=C["ink2"], mew=1.6, ms=6, label="IDH-D")],
          loc="lower left", bbox_to_anchor=(-0.02, -0.14), ncol=2, fontsize=7.8, handletextpad=0.2,
          columnspacing=0.9)
idg = [("Barbados", 0.268, USC), ("Guyana", 0.454, UCR), ("Jamaica", 0.335, RUS)]
for i, (nom, v, col) in enumerate(idg):
    y = 2 - i
    a2.barh(y, v, height=0.5, color=col, zorder=2)
    a2.text(v + 0.012, y, fmt(v, 3), va="center", ha="left", fontsize=8, color=C["ink"], fontweight="bold")
a2.set_xlim(0, 0.62)
a2.set_ylim(-0.6, 2.85)
a2.set_yticks([])
a2.spines["left"].set_visible(False)
a2.set_xticks([0, 0.2, 0.4, 0.6])
a2.xaxis.set_major_formatter(plt.FuncFormatter(coma(1)))
a2.axvline(0, color=C["ink2"], lw=0.9)
a2.text(0.0, 2.45, "IDG (0 = igualdad)", ha="left", va="bottom", fontsize=8, fontweight="bold", color=C["ink2"])
save(fig, "x2_idh_2024")


# ------------------------------------------------------------------ P6.2 / P7.1  índices 2018 = 100
def indice_fig(nom, tcm, ppa, col, name, jump_lbl, media, dy_lab, jl_x=2020.45, jl_ha="right"):
    idx = lambda s: [100 * v / s[0] for v in s]  # noqa: E731
    it, ip, iu = idx(tcm), idx(ppa), idx(USA)
    fig, ax = new_fig(6.2, 2.75)
    ax.plot(YRS, iu, color=USC, lw=LW, marker="o", ms=4, mec="white", mew=0.8, zorder=3)
    ax.plot(YRS, ip, color=col, lw=1.6, ls="--", marker="o", ms=3.5, mfc="white", mec=col, zorder=3)
    ax.plot(YRS, it, color=col, lw=LW, marker="o", ms=4, mec="white", mew=0.8, zorder=4)
    ax.axhline(100, color=C["ink3"], lw=0.8, zorder=1)
    data_axes(ax, "", "índice (2018 = 100)")
    ax.set_xlim(2017.7, 2025.3)
    ax.set_xticks(YRS)
    lo = min(it + ip + iu)
    ax.set_ylim(min(85, lo - 6), max(it + ip + iu) + 12)
    labs = [(f"EEUU (US$ corr.)\nmedia 5,27 % anual", iu[-1] + dy_lab[0], USC),
            (f"{nom} a TCm\nmedia {media} anual", it[-1] + dy_lab[1], col),
            (f"{nom} a PPA", ip[-1] + dy_lab[2], col)]
    for txt, y, c in labs:
        ax.text(2023.18, y, txt, color=c, fontsize=8.0, fontweight="bold", va="center", linespacing=1.1)
    ax.annotate("", xy=(2021, it[3]), xytext=(2020, it[2]),
                arrowprops=dict(arrowstyle="-|>", color=C["ink"], lw=1.1, mutation_scale=9,
                                connectionstyle="arc3,rad=0.35", shrinkA=5, shrinkB=5), zorder=5)
    ax.text(jl_x, (it[2] + it[3]) / 2 + jump_lbl[1], jump_lbl[0], ha=jl_ha, va="center", fontsize=8.2,
            color=C["ink"], fontweight="bold")
    save(fig, name)


indice_fig("Ucrania", UCR_TCM, UCR_PPA, UCR, "x2_ucrania_indice", ("+28,68 %\n(ej. 2 a)", 8), "10,84 %",
           (-4, 3, -3))
indice_fig("Rusia", RUS_TCM, RUS_PPA, RUS, "x2_rusia_indice", ("+23,88 %\n(ej. 2 a)", -8), "4,27 %",
           (4, -4, 0), jl_x=2020.72, jl_ha="left")

# ------------------------------------------------------------------ P6.3  veces más grande en 2020
fig, ax = new_fig(5.6, 2.35)
grupos = [("EEUU / Ucrania", USA[2] / UCR_TCM[2], USA[2] / UCR_PPA[2], UCR, "17", "4"),
          ("EEUU / Rusia", USA[2] / RUS_TCM[2], USA[2] / RUS_PPA[2], RUS, "6", "2")]
w = 0.36
for i, (lab, vt, vp, col, rt, rp) in enumerate(grupos):
    ax.bar(i - w / 2 - 0.02, vt, w, color=col, zorder=2)
    ax.bar(i + w / 2 + 0.02, vp, w, color="white", edgecolor=col, hatch="////", lw=1.4, zorder=2)
    ax.text(i - w / 2 - 0.02, vt + 0.4, f"{fmt(vt, 2)}\n→ {rt}", ha="center", va="bottom", fontsize=8.2,
            fontweight="bold", color=C["ink"], linespacing=1.05)
    ax.text(i + w / 2 + 0.02, vp + 0.4, f"{fmt(vp, 2)}\n→ {rp}", ha="center", va="bottom", fontsize=8.2,
            fontweight="bold", color=C["ink"], linespacing=1.05)
    ax.text(i - w / 2 - 0.02, -0.5, "a TCm", ha="center", va="top", fontsize=8, color=C["ink2"])
    ax.text(i + w / 2 + 0.02, -0.5, "a PPA", ha="center", va="top", fontsize=8, color=C["ink2"])
    ax.text(i, -2.4, lab, ha="center", va="top", fontsize=9, fontweight="bold", color=C["ink"])
data_axes(ax, "", "veces (PBI pc 2020)")
ax.set_xticks([])
ax.set_xlim(-0.65, 1.65)
ax.set_ylim(0, 22)
ax.spines["bottom"].set_position(("data", 0))
save(fig, "x2_veces_2020")


# ------------------------------------------------------------------ Solow con tecnología, en tasas
def solow_tasas(ax, s, ngd, col_ca=C["orange"], col_cd=C["aqua"], lw=LW, ls="-", label=True, xmax=1.0):
    k = np.linspace(0.012, xmax, 500)
    ax.plot(k, s / np.sqrt(k), color=col_ca, lw=lw, ls=ls, zorder=3)
    ax.plot([0, xmax], [ngd, ngd], color=col_cd, lw=lw, ls=ls, zorder=3)


def hat_axes(ax, ylim, xmax=1.0):
    econ_axes(ax, r"$\hat{k}$", r"$\gamma_{\hat{k}}$", xlim=(0, xmax), ylim=ylim)


# P6.4  versión g = 25 %
s, ngd, ks = 0.20, 0.40, 0.25
fig, ax = new_fig(5.8, 3.1)
solow_tasas(ax, s, ngd)
hat_axes(ax, (0, 1.05))
vguide(ax, ks, ngd, r"$\hat{k}^*=0{,}25$", size=9.5)
point(ax, ks, ngd, label="EE", dx=6, dy=6)
label_curve(ax, 0.075, s / np.sqrt(0.075), r"CA $=0{,}2\,\hat{k}^{-0{,}5}=\dfrac{0{,}2}{\hat{k}^{\,0{,}5}}$", C["orange"],
            dx=10, dy=4, size=9)
label_curve(ax, 1.0, ngd, r"CD $=n+g+\delta=0{,}40$", C["aqua"], dx=-2, dy=9, ha="right", size=9)
kx = 0.11
arrow(ax, kx, ngd, kx, s / np.sqrt(kx), C["ink2"], both=True, lw=1.1)
ax.text(kx - 0.012, (ngd + s / np.sqrt(kx)) / 2, r"$\gamma_{\hat{k}}>0$", fontsize=8.6, ha="right", va="center")
kx2 = 0.62
arrow(ax, kx2, s / np.sqrt(kx2), kx2, ngd, C["ink2"], both=True, lw=1.1)
ax.text(kx2 + 0.015, (ngd + s / np.sqrt(kx2)) / 2 - 0.02, r"$\gamma_{\hat{k}}<0$", fontsize=8.6, ha="left",
        va="center")
arrow(ax, 0.07, 0.035, 0.19, 0.035, C["ink2"])
arrow(ax, 0.55, 0.035, 0.31, 0.035, C["ink2"])
save(fig, "x2_solow_g25")

# P6.5  por qué 0,2/k^(-0,5) no puede ser la curva de ahorro
fig, ax = new_fig(6.2, 3.1)
kk = np.linspace(0.012, 5.2, 600)
ax.plot(kk, 0.2 / np.sqrt(kk), color=C["orange"], lw=LW, zorder=3)
ax.plot(kk, 0.2 * np.sqrt(kk), color=C["red"], lw=LW, ls="--", zorder=3)
ax.plot([0, 5.2], [0.4, 0.4], color=C["aqua"], lw=LW, zorder=2)
econ_axes(ax, r"$\hat{k}$", r"$\gamma_{\hat{k}}$", xlim=(0, 5.3), ylim=(0, 1.0))
point(ax, 0.25, 0.4)
ax.annotate("EE correcto: $\\hat{k}^*=0{,}25$\n(la CA corta a la CD desde arriba)", (0.25, 0.4), xytext=(0.45, 0.95),
            fontsize=8.4, color=C["ink"], va="top", arrowprops=dict(arrowstyle="-", color=C["ink2"], lw=0.8))
ax.plot([4], [0.4], "o", ms=7, mfc="white", mec=C["red"], mew=2, zorder=5)
ax.text(5.2, 0.665, "corta a la CD en $\\hat{k}=4$ desde ABAJO:\nequilibrio inestable, y no da 0,25", fontsize=8.2,
        color=C["red"], ha="right", va="bottom")
label_curve(ax, 5.2, 0.2 * np.sqrt(5.2), r"$\dfrac{0{,}2}{\hat{k}^{-0{,}5}}=0{,}2\,\hat{k}^{\,0{,}5}$ (creciente)",
            C["red"], dx=-4, dy=16, ha="right", size=9)
label_curve(ax, 4.0, 0.2 / np.sqrt(4.0), r"$\dfrac{0{,}2}{\hat{k}^{\,0{,}5}}$ (decreciente)", C["orange"], dx=0,
            dy=21, ha="center", size=9)
label_curve(ax, 1.75, 0.4, "CD = 0,40", C["aqua"], dx=0, dy=-9, ha="center", size=8.8)
save(fig, "x2_solow_signo")

# P7.2  versión g = 17 % (con la versión g = 25 % de fondo)
fig, ax = new_fig(6.0, 2.4)
solow_tasas(ax, 0.20, 0.40, col_ca=C["ink3"], col_cd=C["ink3"], lw=1.2, ls=(0, (4, 3)))
solow_tasas(ax, 0.15, 0.30)
hat_axes(ax, (0, 0.92))
vguide(ax, 0.25, 0.40, r"$\hat{k}^*=0{,}25$", size=9.5)
point(ax, 0.25, 0.30, label="EE", dx=-8, dy=-15, ha="right")
point(ax, 0.25, 0.40, color=C["ink3"])
label_curve(ax, 0.92, 0.15 / np.sqrt(0.92), r"CA $=0{,}15/\hat{k}^{\,0{,}5}$", C["orange"], dx=-2, dy=-11,
            ha="right", size=9)
label_curve(ax, 1.0, 0.30, r"CD $=0{,}30$", C["aqua"], dx=-2, dy=8, ha="right", size=9)
label_curve(ax, 1.0, 0.40, r"versión P6: CA $=0{,}2/\hat{k}^{\,0{,}5}$, CD $=0{,}40$", C["ink3"], dx=-2,
            dy=9, ha="right", size=8.2, weight="normal")
save(fig, "x2_solow_g17")
print("ok")
