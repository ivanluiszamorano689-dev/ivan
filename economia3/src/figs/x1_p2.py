"""Parciales resueltos · P2 (1er parcial 2023) y P3 (Namibia y Honduras).
Figura P2.1 — Solow 2023 en niveles: FA = 0,285 k^(5/6) vs FD = 0,175 k; y* = 1,5 k*^(5/6).
Figura P2.2 — Harrod-Domar per cápita: g = 0,19/v − 0,175 (corte en v = 1,086).
Figura P2.3 — Australia: índice sin ajustar vs ajustado por desigualdad, por dimensión.
Figura P2.4 — Dolar City vs Ciudad Pesos: PBI en dólares a TCm y a PPA.
Figura P3.1 — Namibia y Honduras: IDH, IDH-D y pérdida.
Correr desde figs/:  python3 x1_p2.py
"""
import sys; sys.path.insert(0, "../lib")
from econ_style import *


def coma(v, d=2):
    return f"{v:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


# ---------------------------------------------------------------- Figura P2.1
s, n, d, A, a = 0.19, 0.045, 0.13, 1.5, 5 / 6
sA, nd = s * A, n + d
ks = (sA / nd) ** (1 / (1 - a))
ys = A * ks ** a
k = np.linspace(0, 27, 400)
fig, (ax2, ax1) = new_fig(6.6, 3.0, ncols=2)
fig.subplots_adjust(wspace=0.62)
# panel derecho: FA vs FD (opción iv)
ax1.plot(k, sA * k ** a, color=C["orange"], lw=LW)
ax1.plot(k, nd * k, color=C["aqua"], lw=LW)
econ_axes(ax1, r"$k$", "", xlim=(0, 27), ylim=(0, 5.2))
ax1.set_title("b) Funciones de ahorro y depreciación", fontsize=9, pad=14)
label_curve(ax1, 27, sA * 27 ** a, r"$FA = 0{,}285\,k^{5/6}$", C["orange"], dx=4, dy=-4)
label_curve(ax1, 27, nd * 27, r"$FD = 0{,}175\,k$", C["aqua"], dx=4, dy=4)
vguide(ax1, ks, sA * ks ** a, r"$k^*=18{,}66$")
hguide(ax1, ks, sA * ks ** a, r"$3{,}27$")
point(ax1, ks, sA * ks ** a, C["ink"])
# panel izquierdo: producción con y sin A
ax2.plot(k, A * k ** a, color=C["blue"], lw=LW)
ax2.plot(k, k ** a, color=C["blue"], lw=1.4, ls="--", alpha=0.75)
econ_axes(ax2, r"$k$", "", xlim=(0, 27), ylim=(0, 24))
ax2.set_title("a) Producción per cápita en el EE", fontsize=9, pad=14)
label_curve(ax2, 27, A * 27 ** a, r"$y = 1{,}5\,k^{5/6}$", C["blue"], dx=4)
label_curve(ax2, 27, 27 ** a, r"$k^{5/6}$ (sin $A$)", C["blue"], dx=4, weight="normal")
vguide(ax2, ks, A * ks ** a, r"$k^*=18{,}66$")
hguide(ax2, ks, ys, r"$17{,}18$")
hguide(ax2, ks, ks ** a, r"$11{,}46$")
point(ax2, ks, ys, C["ink"], r"$y^*$ correcto", dx=-6, dy=7, ha="right")
point(ax2, ks, ks ** a, C["red"])
ax2.annotate("opción ii:\nolvida A", (ks, ks ** a), xytext=(8, -22), textcoords="offset points",
             fontsize=8.2, color=C["red"], ha="left", fontweight="bold")
save(fig, "x1_p2_solow")

# ---------------------------------------------------------------- Figura P2.2
v = np.linspace(0.22, 3.0, 400)
g = s / v - nd
gY = s / v - d
vs = s / nd
fig, ax = new_fig(6.0, 3.0)
ax.axvspan(0, vs, color=C["green_bg"], zorder=0)
ax.axhline(0, color=C["ink2"], lw=1.0, zorder=2)
ax.plot(v, gY, color=C["ink3"], lw=1.3, ls=(0, (4, 3)), zorder=2)
ax.plot(v, g, color=C["blue"], lw=LW, zorder=3)
point(ax, vs, 0, C["ink"])
ax.annotate(r"$v = \dfrac{0{,}19}{0{,}175} = 1{,}086$:  $g = 0$" + "\n(no es positiva)", (vs, 0),
            xytext=(1.55, 0.3), fontsize=8.6, ha="left", va="center", color=C["ink"],
            arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=1.0, mutation_scale=8, shrinkA=2, shrinkB=6))
ax.text(0.62, -0.1, "opción ii:\n0 < v < 1,085", ha="center", va="center", fontsize=8.8, fontweight="bold",
        color=C["green"])
ax.text(2.2, -0.215, r"$g_y = \dfrac{0{,}19}{v} - 0{,}175$", color=C["blue"], fontsize=9.5, ha="center", va="center")
ax.plot([s / d], [0], "o", ms=6, mfc="white", mec=C["ink3"], mew=1.4, zorder=4)
ax.text(3.0, 0.035, "- - -  versión agregada s/v − δ: corta en 1,46,\nun valor que no está entre las opciones",
        ha="right", va="bottom", fontsize=7.8, color=C["ink2"])
ax.set_xlim(0, 3.05)
ax.set_ylim(-0.29, 0.52)
ax.set_xticks([0, 0.5, 1, 1.5, 2, 2.5, 3])
ax.set_yticks([-0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5])
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: coma(x, 1)))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: coma(x, 1).replace("-", "−")))
data_axes(ax, "relación capital-producto  v", "tasa de crecimiento del producto per cápita")
ax.yaxis.label.set_size(8.2)
save(fig, "x1_p2_harrod")

# ---------------------------------------------------------------- Figura P2.3
dims = ["Salud\n(esperanza de vida)", "Educación", "Ingresos\n(estándar de vida)", "IDH  →  IDH-D"]
sin = [0.993, 0.925, 0.936, 0.951]
aj = [0.966, 0.896, 0.776, 0.876]
perd = ["−2,7 %", "−3,1 %", "−17,1 %", "pérdida 7,9 %"]
fig, ax = new_fig(6.0, 2.7)
y = np.arange(len(dims))[::-1]
for yi, s0, s1, p in zip(y, sin, aj, perd):
    ax.plot([s1, s0], [yi, yi], color=C["rule"], lw=4, solid_capstyle="round", zorder=2)
    ax.plot([s0], [yi], "o", ms=9, color=C["blue"], mec="white", mew=1.5, zorder=4)
    ax.plot([s1], [yi], "o", ms=9, color=C["orange"], mec="white", mew=1.5, zorder=4)
    ax.annotate(coma(s0, 3), (s0, yi), xytext=(9, 0), textcoords="offset points", va="center", fontsize=8.6,
                color=C["ink"])
    ax.annotate(coma(s1, 3), (s1, yi), xytext=(-9, 0), textcoords="offset points", va="center", ha="right",
                fontsize=8.6, color=C["ink"], fontweight="bold")
    ax.annotate(p, ((s0 + s1) / 2, yi), xytext=(0, 9), textcoords="offset points", ha="center", fontsize=8,
                color=C["ink2"])
ax.axhline(0.5, color=C["rule"], lw=0.9)
ax.set_yticks(y)
ax.set_yticklabels(dims, fontsize=8.6)
ax.tick_params(axis="y", length=0)
ax.set_xlim(0.72, 1.03)
ax.set_ylim(-0.6, 3.6)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: coma(x, 2)))
ax.grid(axis="x", color="#ebe9e3", lw=0.8)
ax.set_axisbelow(True)
ax.spines["left"].set_visible(False)
ax.text(0.725, 3.45, "●", color=C["blue"], fontsize=9, va="center")
ax.text(0.735, 3.45, "sin ajustar", color=C["ink"], fontsize=8.4, va="center")
ax.text(0.79, 3.45, "●", color=C["orange"], fontsize=9, va="center")
ax.text(0.80, 3.45, "ajustado por desigualdad", color=C["ink"], fontsize=8.4, va="center")
save(fig, "x1_p2_australia")

# ---------------------------------------------------------------- Figura P2.4
labels = ["Dolar City", "Ciudad Pesos a PPA\n(462.500 / 10,8824)", "Ciudad Pesos a TC de mercado\n(462.500 / 25)"]
vals = [51000, 42500, 18500]
cols = [C["blue"], C["orange"], C["orange"]]
fig, ax = new_fig(6.2, 2.45)
y = np.array([2, 1, 0])
bars = ax.barh(y, vals, height=0.56, color=cols, zorder=3)
bars[2].set_hatch("////")
bars[2].set_facecolor("white")
bars[2].set_edgecolor(C["orange"])
bars[2].set_linewidth(1.4)
for yi, val in zip(y, vals):
    ax.text(val + 800, yi, "US$ " + coma(val, 0), va="center", ha="left", fontsize=9, fontweight="bold",
            color=C["ink"])
ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=8.6)
ax.set_xlim(0, 66000)
ax.set_xticks([0, 10000, 20000, 30000, 40000, 50000])
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: coma(x, 0)))
ax.grid(axis="x", color="#ebe9e3", lw=0.8)
ax.set_axisbelow(True)
ax.spines["left"].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.set_xlabel("PBI en dólares", fontsize=8.6, color=C["ink2"])
ax.text(59500, 1.0, "DC / CP\n= 1,2", fontsize=8.4, ha="center", va="center", color=C["ink"],
        fontweight="bold")
ax.text(59500, 0.0, "DC / CP\n= 2,76", fontsize=8.4, ha="center", va="center", color=C["ink"])
save(fig, "x1_p2_dolarcity")

# ---------------------------------------------------------------- Figura P3.1
paises = ["Namibia", "Honduras"]
idh = [0.645433, 0.638348]
idhd = [0.417673, 0.475543]
perd = [35.288, 25.504]
fig, ax = new_fig(5.8, 3.0)
x = np.array([0, 1.3])
w = 0.34
ax.axhspan(0.55, 0.70, color=C["gray_bg"], zorder=0)
ax.text(2.28, 0.625, "rango «medio»\ndel IDH\n(0,550–0,699)", fontsize=7.8, color=C["ink2"], va="center",
        ha="left")
ax.bar(x - w / 2 - 0.01, idh, width=w, color=C["blue"], zorder=3)
ax.bar(x + w / 2 + 0.01, idhd, width=w, color=C["orange"], zorder=3)
for xi, v0, v1, p in zip(x, idh, idhd, perd):
    xb, xo = xi - w / 2 - 0.01, xi + w / 2 + 0.01
    ax.text(xb, v0 + 0.012, coma(v0, 3), ha="center", va="bottom", fontsize=8.8, fontweight="bold",
            color=C["ink"])
    ax.text(xo, v1 + 0.012, coma(v1, 3), ha="center", va="bottom", fontsize=8.8, fontweight="bold",
            color=C["ink"])
    ax.plot([xb + w / 2, xo + w / 2 + 0.02], [v0, v0], color=C["red"], lw=1, ls=(0, (2, 2)), zorder=4)
    ax.annotate("", xy=(xo + w / 2 + 0.02, v1), xytext=(xo + w / 2 + 0.02, v0),
                arrowprops=dict(arrowstyle="-|>", color=C["red"], lw=1.3, mutation_scale=9, shrinkA=0, shrinkB=0))
    ax.text(xo + w / 2 + 0.07, (v0 + v1) / 2, "pérdida\n" + coma(p, 1) + " %", fontsize=8.4, color=C["red"],
            va="center", ha="left", fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(paises, fontsize=9.5)
ax.set_xlim(-0.55, 2.95)
ax.set_ylim(0, 0.8)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: coma(v, 1)))
data_axes(ax, "", "")
ax.text(-0.5, 0.77, "■", color=C["blue"], fontsize=9, va="center")
ax.text(-0.42, 0.77, "IDH", color=C["ink"], fontsize=8.6, va="center")
ax.text(-0.18, 0.77, "■", color=C["orange"], fontsize=9, va="center")
ax.text(-0.10, 0.77, "IDH-D", color=C["ink"], fontsize=8.6, va="center")
save(fig, "x1_p3_namibia")
