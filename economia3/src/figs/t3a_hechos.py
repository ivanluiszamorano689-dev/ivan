# Tema 3.1 — Los hechos del crecimiento (datos del manual de la cátedra, págs. 22-23)
# correr con: cd figs && python3 t3a_hechos.py
import sys; sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403


def miles(v):
    return f"{v:,.0f}".replace(",", ".")


def coma(v, d=1):
    return f"{v:.{d}f}".replace(".", ",")


# ------------------------------------------------------------------ Fig 3.1: niveles 2024 (escala log)
paises = ["Estados Unidos", "Corea del Sur", "Etiopía", "Madagascar"]
pbi = [66683, 34121, 916, 453]
cols = [C["blue"], C["aqua"], C["orange"], C["orange"]]

fig, ax = new_fig(3.3, 2.5)
ypos = np.arange(len(paises))[::-1]
ax.barh(ypos, pbi, color=cols, height=0.58, zorder=3)
ax.set_xscale("log")
ax.set_xlim(200, 400000)
ax.set_yticks(ypos)
ax.set_yticklabels(paises, fontsize=8.8)
ax.tick_params(axis="y", length=0)
ax.set_xticks([100 * 10 ** i for i in range(1, 4)] + [100000])
ax.set_xticks([], minor=True)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: miles(v)))
for yy, v in zip(ypos, pbi):
    ax.annotate(miles(v), (v, yy), xytext=(4, 0), textcoords="offset points", va="center", fontsize=8.5,
                color=C["ink"], fontweight="bold")
ax.grid(axis="x", color="#ebe9e3", lw=0.8)
ax.set_axisbelow(True)
ax.spines["left"].set_visible(False)
ax.set_xlabel("PBI per cápita 2024 (US$ constantes de 2015, escala logarítmica)", fontsize=8)
# nota: factor entre extremos
ax.text(9000, (ypos[2] + ypos[3]) / 2, "EEUU / Madagascar\n≈ 147 veces", ha="left", va="center", fontsize=8.4,
        color=C["ink"], fontweight="bold", linespacing=1.25)
save(fig, "t3a_hechos_niveles")

# ------------------------------------------------------------------ Fig 3.2: tasas (dos paneles)
fig, (a1, a2) = new_fig(6.4, 2.7, ncols=2, gridspec_kw=dict(width_ratios=[1.1, 1], wspace=0.55))

# (a) 1981-2024 entre países
nom = ["China", "Corea del Sur", "Singapur", "Argentina", "México", "Países de\ningreso bajo", "Congo"]
tas = [8.1, 4.9, 3.6, 0.6, 0.3, -0.3, -0.6]
yp = np.arange(len(nom))[::-1]
bar_cols = [C["blue"] if t >= 0 else C["red"] for t in tas]
a1.barh(yp, tas, color=bar_cols, height=0.6, zorder=3)
a1.axvline(0, color=C["ink2"], lw=0.9, zorder=4)
a1.set_yticks(yp)
a1.set_yticklabels(nom, fontsize=8.4)
a1.tick_params(axis="y", length=0)
a1.set_xlim(-2.2, 10)
a1.set_xticks([0, 2, 4, 6, 8, 10])
a1.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.0f} %"))
for yy, t in zip(yp, tas):
    a1.annotate(coma(t) + " %", (max(t, 0), yy), xytext=(4, 0), textcoords="offset points",
                va="center", ha="left", fontsize=8.2, color=C["ink"])
a1.grid(axis="x", color="#ebe9e3", lw=0.8)
a1.set_axisbelow(True)
a1.spines["left"].set_visible(False)
a1.set_title("Hecho 2 · tasas muy distintas entre países\n(crecimiento anual del PBI pc, 1981-2024)", fontsize=9)

# (b) pendiente 1960-81 -> 1981-2024
datos = [("Corea del Sur", 7.0, 4.9, C["aqua"]), ("Singapur", 6.9, 3.6, C["blue"]),
         ("Congo", 3.0, -0.6, C["orange"]), ("Argentina", 1.2, 0.6, C["violet"])]
for nombre, t0, t1, col in datos:
    a2.plot([0, 1], [t0, t1], color=col, lw=LW, marker="o", ms=5.5, mec="white", mew=1.2, zorder=3)
# rótulos a la izquierda y derecha (acomodados para no pisarse)
lab_izq = {"Corea del Sur": 7.35, "Singapur": 6.55, "Congo": 3.0, "Argentina": 1.2}
lab_der = {"Corea del Sur": 4.9, "Singapur": 3.6, "Congo": -0.6, "Argentina": 0.75}
for nombre, t0, t1, col in datos:
    a2.text(-0.06, lab_izq[nombre], f"{coma(t0)} %", ha="right", va="center", fontsize=8.2, color=C["ink"])
    a2.text(1.06, lab_der[nombre], f"{coma(t1)} %  {nombre}", ha="left", va="center", fontsize=8.2,
            color=C["ink"])
a2.axhline(0, color=C["ink3"], lw=0.8, ls=(0, (3, 3)))
a2.set_xlim(-0.35, 1.9)
a2.set_ylim(-1.5, 8.2)
a2.set_xticks([0, 1])
a2.set_xticklabels(["1960-1981", "1981-2024"], fontsize=8.5)
a2.set_yticks([])
a2.spines["left"].set_visible(False)
a2.set_title("Hecho 3 · la tasa de un país cambia\ncon el tiempo (% anual)", fontsize=9)
save(fig, "t3a_hechos_tasas")

# ------------------------------------------------------------------ Fig 3.3: Corea vs Argentina, índice 1960 = 100
t = np.array([1960, 1981, 2024])
corea = np.array([100, 100 * 1.07 ** 21, 100 * 1.07 ** 21 * 1.049 ** 43])
arg = np.array([100, 100 * 1.012 ** 21, 100 * 1.012 ** 21 * 1.006 ** 43])
fig, ax = new_fig(3.3, 2.5)
ax.plot(t, corea, color=C["aqua"], lw=LW, marker="o", ms=5.5, mec="white", mew=1.2)
ax.plot(t, arg, color=C["violet"], lw=LW, marker="o", ms=5.5, mec="white", mew=1.2)
ax.set_yscale("log")
ax.set_ylim(60, 6000)
ax.set_xlim(1940, 2068)
ax.set_yticks([100, 300, 1000, 3000])
ax.set_yticks([], minor=True)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: miles(v)))
ax.set_xticks([1960, 1981, 2024])
ax.spines["bottom"].set_bounds(1940, 2030)
data_axes(ax, "", "índice 1960 = 100 (escala log)")
ax.yaxis.label.set_size(8)
ax.annotate(f"Corea\n×{corea[-1] / 100:.0f}".replace(".", ","), (2024, corea[-1]), xytext=(6, 0),
            textcoords="offset points", ha="left", va="center", fontsize=8.6, color=C["aqua"], fontweight="bold")
ax.annotate("Argentina\n×1,7", (2024, arg[-1]), xytext=(6, 0), textcoords="offset points", ha="left",
            va="center", fontsize=8.6, color=C["violet"], fontweight="bold")
ax.annotate("7,0 %", ((1960 + 1981) / 2, np.sqrt(corea[0] * corea[1])), xytext=(-5, 8), textcoords="offset points",
            ha="right", fontsize=7.8, color=C["ink2"])
ax.annotate("4,9 %", ((1981 + 2024) / 2, np.sqrt(corea[1] * corea[2])), xytext=(-6, 6), textcoords="offset points",
            ha="right", fontsize=7.8, color=C["ink2"])
ax.annotate("1,2 %", ((1960 + 1981) / 2, np.sqrt(arg[0] * arg[1])), xytext=(0, -10), textcoords="offset points",
            ha="center", fontsize=7.8, color=C["ink2"])
ax.annotate("0,6 %", ((1981 + 2024) / 2, np.sqrt(arg[1] * arg[2])), xytext=(0, -10), textcoords="offset points",
            ha="center", fontsize=7.8, color=C["ink2"])
save(fig, "t3a_corea_argentina")
print(corea, arg)
