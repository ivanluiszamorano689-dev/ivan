"""Gráficos del Formulario (práctica). Correr desde figs/: python3 p1_formulario.py"""
import sys

sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403
from matplotlib.patches import Rectangle


def miles(v, p=None):
    return f"{v:,.0f}".replace(",", ".")


def coma(dec):
    return lambda v, p=None: f"{v:.{dec}f}".replace(".", ",")


# ---------------------------------------------------------------- F.1  datos vs períodos
anios = list(range(2010, 2024))
pbi = [670524, 710782, 703486, 720407, 702306, 721487, 706478, 726390, 707377, 693224, 624591, 689810,
       726162, 714464]  # TP2 ej. 5, millones de $ de 2004
g = (pbi[-1] / pbi[0]) ** (1 / 13) - 1
fig, ax = new_fig(6.3, 3.05)
ax.plot(anios, pbi, color=C["blue"], lw=LW, marker="o", ms=4.5, mec="white", mew=1.0, zorder=3)
t = np.linspace(0, 13, 100)
ax.plot(2010 + t, pbi[0] * (1 + g) ** t, color=C["orange"], lw=1.6, ls="--", zorder=2)
data_axes(ax, "", "PBI (millones de $ de 2004)")
ax.set_ylim(560000, 760000)
ax.set_xlim(2009.4, 2023.9)
ax.yaxis.set_major_formatter(plt.FuncFormatter(miles))
ax.set_xticks(anios)
ax.set_xticklabels([str(a) if a in (2010, 2023) else f"'{str(a)[2:]}" for a in anios])
for i in range(13):
    xm = anios[i] + 0.5
    ax.annotate("", xy=(anios[i + 1] - 0.08, 578000), xytext=(anios[i] + 0.08, 578000),
                arrowprops=dict(arrowstyle="-|>", color=C["ink3"], lw=0.9, mutation_scale=7,
                                connectionstyle="arc3,rad=-0.45"))
    ax.text(xm, 593000, str(i + 1), ha="center", va="bottom", fontsize=7.2, color=C["ink2"])
ax.text(2016.5, 606000, "13 períodos (saltos entre años)", ha="center", va="bottom", fontsize=8.5,
        color=C["ink"], fontweight="bold")
ax.annotate("14 datos (puntos)", xy=(2011, 710782), xytext=(2011.3, 745000), fontsize=8.5, color=C["blue"],
            fontweight="bold", arrowprops=dict(arrowstyle="-", color=C["blue"], lw=0.8))
ax.annotate(f"camino a tasa media constante\n$\\bar g$ = 0,489 % anual", xy=(2019.6, pbi[0] * (1 + g) ** 9.6),
            xytext=(2017.6, 745000), fontsize=8.2, color=C["orange"], ha="left", fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=C["orange"], lw=0.8))
ax.text(2010.05, 655000, "$Y_0$ = 670.524", fontsize=8.2, color=C["ink"], ha="left", va="top")
ax.text(2023.3, 700000, "$Y_T$ = 714.464", fontsize=8.2, color=C["ink"], ha="right", va="top")
save(fig, "p1_f_periodos")

# ---------------------------------------------------------------- F.2  escala del IDH
fig, ax = new_fig(6.4, 2.05)
tramos = [(0.30, 0.55, "Bajo", "#dcebfb"), (0.55, 0.70, "Medio", "#b4d3f5"),
          (0.70, 0.80, "Alto", "#6fa8e6"), (0.80, 1.00, "Muy alto", "#2a78d6")]
for a, b, lab, col in tramos:
    ax.add_patch(Rectangle((a, 0), b - a, 1, fc=col, ec="white", lw=1.5))
    ax.text((a + b) / 2, 0.5, lab, ha="center", va="center", fontsize=9, fontweight="bold",
            color="white" if lab in ("Alto", "Muy alto") else C["ink"])
for v in (0.55, 0.70, 0.80):
    ax.text(v, -0.12, f"{v:.3f}".replace(".", ","), ha="center", va="top", fontsize=8.2, color=C["ink"],
            fontweight="bold")
ax.text(0.30, -0.12, "0", ha="left", va="top", fontsize=8, color=C["ink3"])
ax.text(1.00, -0.12, "1", ha="right", va="top", fontsize=8, color=C["ink3"])
paises = [("Yemen", 0.455, 1, 1), ("Honduras", 0.638, -1, 1), ("Namibia", 0.646, 1, 1), ("Jamaica", 0.709, -1, 2),
          ("Guyana", 0.714, 1, 2), ("Barbados", 0.790, -1, 1), ("Argentina", 0.865, 1, 1), ("Suiza", 0.970, -1, 1)]
for nom, v, lado, niv in paises:
    y0, y1 = (1.0, 1.25 + 0.42 * (niv - 1)) if lado == 1 else (0.0, -0.5 - 0.42 * (niv - 1))
    ax.plot([v, v], [y0, y1], color=C["ink"], lw=0.8)
    ax.plot([v], [y0], marker="v" if lado == 1 else "^", color=C["ink"], ms=4)
    ax.text(v, y1 + (0.04 if lado == 1 else -0.04), f"{nom} {v:.3f}".replace(".", ","), ha="center",
            va="bottom" if lado == 1 else "top", fontsize=7.8, color=C["ink"])
ax.set_xlim(0.28, 1.02)
ax.set_ylim(-1.3, 2.05)
ax.axis("off")
save(fig, "p1_f_idh_escala")

# ---------------------------------------------------------------- F.3  Solow: niveles vs tasas (parcial 2022)
sA, nd, a = 0.65, 0.13, 3 / 7
ks = (sA / nd) ** (1 / (1 - a))
k = np.linspace(0.02, 30, 500)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.5, 2.75))
fig.subplots_adjust(wspace=0.35)
a1.plot(k, sA * k ** a, color=C["orange"], lw=LW)
a1.plot(k, nd * k, color=C["aqua"], lw=LW)
econ_axes(a1, r"$k$", "", xlim=(0, 30), ylim=(0, 4.2))
a1.annotate(r"FA $=0{,}65\,k^{3/7}$", (4.0, sA * 4.0 ** a), xytext=(0.8, 3.0), color=C["orange"], fontsize=8.8,
            fontweight="bold", arrowprops=dict(arrowstyle="-", color=C["orange"], lw=0.8))
label_curve(a1, 27, nd * 27, r"FD $=0{,}13\,k$", C["aqua"], dx=-8, dy=4, ha="right", size=8.8)
vguide(a1, ks, sA * ks ** a, r"$k^*=16{,}72$", size=8.5)
point(a1, ks, sA * ks ** a)
a1.set_title("Niveles: FUNCIONES (FA y FD)", fontsize=8.8, loc="left")
k2 = np.linspace(0.6, 30, 500)
a2.plot(k2, sA / k2 ** (1 - a), color=C["orange"], lw=LW)
a2.plot(k2, nd + 0 * k2, color=C["aqua"], lw=LW)
econ_axes(a2, r"$k$", r"$\gamma_k$", xlim=(0, 30), ylim=(0, 0.62))
label_curve(a2, 3.2, sA / 3.2 ** (1 - a), r"CA $=0{,}65/k^{4/7}$", C["orange"], dx=6, dy=4, size=8.8)
label_curve(a2, 30, nd, r"CD $=0{,}13$", C["aqua"], dx=-2, dy=8, ha="right", size=8.8)
vguide(a2, ks, nd, r"$k^*=16{,}72$", size=8.5)
point(a2, ks, nd)
kx = 7.0
arrow(a2, kx, nd, kx, sA / kx ** (1 - a), C["ink2"], both=True, lw=1.1)
a2.text(kx - 0.7, (nd + sA / kx ** (1 - a)) / 2, r"$\gamma_k>0$", fontsize=8.5, color=C["ink"], va="center", ha="right")
a2.set_title("Tasas: CURVAS (CA y CD)", fontsize=8.8, loc="left", pad=16)
save(fig, "p1_f_solow_niveles_tasas")

# ---------------------------------------------------------------- F.4  Harrod-Domar: umbral de v (parcial 2023)
s, n_d, d = 0.19, 0.175, 0.13
v = np.linspace(0.45, 3.0, 400)
fig, ax = new_fig(3.35, 2.75)
ax.axvspan(0.45, s / n_d, color=C["green_bg"], zorder=0)
ax.axhline(0, color=C["ink2"], lw=0.9)
ax.plot(v, s / v - n_d, color=C["blue"], lw=LW)
ax.plot(v, s / v - d, color=C["orange"], lw=1.6, ls="--")
data_axes(ax, r"$v=K/Y$", "tasa de crecimiento")
ax.set_ylim(-0.14, 0.26)
ax.set_xlim(0.45, 3.0)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{100 * x:.0f} %"))
ax.xaxis.set_major_formatter(plt.FuncFormatter(coma(1)))
ax.plot([s / n_d], [0], "o", color=C["blue"], ms=5.5, mec="white", zorder=5)
ax.plot([s / d], [0], "o", color=C["orange"], ms=5.5, mec="white", zorder=5)
ax.annotate("1,086", (s / n_d, 0), xytext=(-2, -16), textcoords="offset points", ha="right", fontsize=8,
            color=C["blue"], fontweight="bold")
ax.annotate("1,46", (s / d, 0), xytext=(3, 6), textcoords="offset points", ha="left", fontsize=8,
            color=C["orange"], fontweight="bold")
ax.text(2.95, 0.225, "- - agregado: " + r"$g_Y=s/v-\delta$", color=C["orange"], fontsize=8.4, ha="right",
        va="top", fontweight="bold")
ax.text(2.95, 0.175, "— per cápita: " + r"$g_y=s/v-(n+\delta)$", color=C["blue"], fontsize=8.4, ha="right",
        va="top", fontweight="bold")
ax.text(0.55, 0.235, r"$g_y>0$", fontsize=8.4, color=C["green"], fontweight="bold", va="top")
save(fig, "p1_f_harrod_umbral")

# ---------------------------------------------------------------- F.5  Regla de oro (extras E8-E9)
al, nd5 = 0.4, 0.08
sg = np.linspace(0.01, 0.97, 400)
c = (1 - sg) * (sg / nd5) ** (al / (1 - al))
fig, ax = new_fig(3.35, 2.75)
ax.plot(sg, c, color=C["blue"], lw=LW)
data_axes(ax, "tasa de ahorro $s$", r"consumo de EE $c^*$")
ax.set_xlim(0, 1)
ax.set_ylim(0, 2.12)
ax.xaxis.set_major_formatter(plt.FuncFormatter(coma(1)))
ax.yaxis.set_major_formatter(plt.FuncFormatter(coma(1)))
for sv, col in ((0.25, C["orange"]), (0.40, C["blue"])):
    cv = (1 - sv) * (sv / nd5) ** (al / (1 - al))
    ax.plot([sv, sv], [0, cv], ls=(0, (3, 3)), lw=0.9, color=C["ink3"])
    ax.plot([sv], [cv], "o", color=col, ms=6, mec="white", mew=1.3, zorder=5)
ax.annotate("E8: s = 0,25\nc* = 1,603", (0.25, 1.603), xytext=(0.03, 2.06), ha="left", va="top", fontsize=7.9,
            color=C["ink"], arrowprops=dict(arrowstyle="-", color=C["ink3"], lw=0.8))
ax.annotate("regla de oro: s = α = 0,40\nc* = 1,754 (máximo)", (0.40, 1.754), xytext=(0.47, 2.06), ha="left",
            va="top", fontsize=7.9, color=C["ink"], arrowprops=dict(arrowstyle="-", color=C["ink3"], lw=0.8))
ax.text(0.72, 0.55, "sobreacumulación\n(s > α)", fontsize=7.8, color=C["ink2"], ha="center")
ax.text(0.148, 0.34, "subacumulación\n(s < α)", fontsize=7.6, color=C["ink2"], ha="center", va="bottom")
save(fig, "p1_f_regla_oro")
print("ok", round(g, 6), round(ks, 3))
