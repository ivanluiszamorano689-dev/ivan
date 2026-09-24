"""Tema 2.3: las tres tasas, por qué no sirve la media aritmética, divergencia y regla del 70."""
from t2_util import *

thousands = plt.FuncFormatter(lambda v, p: fmt(v, 0))

# ---------------------------------------------------------------- Figura 2.6
# Datos: prueba práctica 28/9/2024 (versión Ucrania), PBI pc en US$ corrientes a TC de mercado.
yrs = np.arange(2018, 2024)
ucr = np.array([3097, 3661, 3752, 4828, 4576, 5181])
g_med = (ucr[-1] / ucr[0]) ** (1 / 5) - 1
fig, ax = new_fig(6.6, 2.9)
tt = np.linspace(0, 5, 100)
ax.plot(2018 + tt, ucr[0] * (1 + g_med) ** tt, color=C["aqua"], lw=1.8, ls=(0, (5, 3)))
ax.plot(yrs, ucr, color=C["blue"], lw=LW, marker="o", ms=6, mec="white", mew=1.4, zorder=4)
for i in range(5):
    g = ucr[i + 1] / ucr[i] - 1
    xm, ym = yrs[i] + 0.5, (ucr[i] + ucr[i + 1]) / 2
    hi = i == 2
    ax.annotate(("+" if g > 0 else "") + fmt(100 * g, 1) + " %", (xm, ym), xytext=(-2 if g > 0 else 6, 9 if g > 0 else 6),
                textcoords="offset points", ha="right" if g > 0 else "left", fontsize=8.4,
                color=C["orange"] if hi else C["ink2"], fontweight="bold" if hi else "normal")
for x_, v in ((2018, ucr[0]), (2023, ucr[-1])):
    ax.annotate("US\\$" + fmt(v), (x_, v), xytext=(4 if x_ == 2018 else 0, -15 if x_ == 2018 else 8), textcoords="offset points",
                ha="left" if x_ == 2018 else "center", fontsize=7.8, color=C["ink2"])
ax.plot([2018, 2023.45], [ucr[0], ucr[0]], color=C["ink3"], lw=0.9, ls=(0, (2, 2)))
arrow(ax, 2023.45, ucr[0], 2023.45, ucr[-1], C["ink"], lw=1.3, both=True)
ax.annotate("acumulada\n+" + fmt(100 * (ucr[-1] / ucr[0] - 1), 1) + " %", (2023.52, (ucr[0] + ucr[-1]) / 2),
            ha="left", va="center", fontsize=8.4, fontweight="bold")
ax.annotate("media geométrica: " + fmt(100 * g_med, 2) + " % anual\n(tasa constante que llega al mismo punto)",
            (2020.9, ucr[0] * (1 + g_med) ** 2.9), xytext=(2020.35, 3420), textcoords="data", fontsize=7.9,
            color=C["aqua"], fontweight="bold", arrowprops=dict(arrowstyle="-", color=C["aqua"], lw=0.8))
ax.annotate("tasas período a período", (2018.3, 4950), fontsize=8.2, color=C["ink2"])
ax.set_xlim(2017.7, 2024.25)
ax.set_ylim(2500, 5600)
ax.set_xticks(yrs)
data_axes(ax, "", "PBI per cápita (US$ corrientes, TCm)")
ax.yaxis.label.set_size(8.4)
ax.yaxis.set_major_formatter(thousands)
save(fig, "t2_tasas_ucrania")

# ---------------------------------------------------------------- Figura 2.7
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.7, 2.7), gridspec_kw=dict(width_ratios=[1, 1.35]))
fig.subplots_adjust(wspace=0.32)
t = np.array([0, 1, 2])
real = np.array([100, 150, 75])
a1.plot(t, real, color=C["blue"], lw=LW, marker="o", ms=6, mec="white", mew=1.4, zorder=4)
a1.plot(t, [100, 100, 100], color=C["orange"], lw=1.6, ls=(0, (5, 3)))
gg = 0.75 ** 0.5
a1.plot(t, 100 * gg ** t, color=C["aqua"], lw=1.6, ls=(0, (5, 3)))
a1.annotate("+50 %", (0.5, 125), xytext=(7, -8), textcoords="offset points", ha="left", fontsize=8.2, color=C["ink2"])
a1.annotate("−50 %", (1.5, 112), xytext=(4, 4), textcoords="offset points", ha="left", fontsize=8.2, color=C["ink2"])
a1.annotate("aritmética 0 %\n→ 100 (falso)", (2, 100), xytext=(6, 0), textcoords="offset points", va="center",
            fontsize=7.8, color=C["orange"], fontweight="bold")
a1.annotate("geométrica\n−13,4 % → 75 ✓", (2, 75), xytext=(6, -2), textcoords="offset points", va="center",
            fontsize=7.8, color=C["aqua"], fontweight="bold")
a1.set_xticks(t)
a1.set_xticklabels(["año 0", "año 1", "año 2"])
a1.set_xlim(-0.2, 3.3)
a1.set_ylim(55, 165)
data_axes(a1, "", "")
a1.set_title("Ejemplo del manual", fontsize=8.8, pad=6)

rus = np.array([11212, 11448, 10108, 12522, 15445, 13817])
rates = rus[1:] / rus[:-1] - 1
g_ar = rates.mean()
g_ge = (rus[-1] / rus[0]) ** (1 / 5) - 1
a2.plot(yrs, rus, color=C["blue"], lw=LW, marker="o", ms=6, mec="white", mew=1.4, zorder=4, label="Rusia (real)")
a2.plot(2018 + tt, rus[0] * (1 + g_ar) ** tt, color=C["orange"], lw=1.6, ls=(0, (5, 3)))
a2.plot(2018 + tt, rus[0] * (1 + g_ge) ** tt, color=C["aqua"], lw=1.6, ls=(0, (5, 3)))
end_ar = rus[0] * (1 + g_ar) ** 5
a2.annotate("aritmética " + fmt(100 * g_ar, 2) + " %\n→ " + fmt(end_ar) + " (se pasa)", (2023, end_ar),
            xytext=(6, 4), textcoords="offset points", va="center", fontsize=7.8, color=C["orange"], fontweight="bold")
a2.annotate("geométrica " + fmt(100 * g_ge, 2) + " %\n→ " + fmt(rus[-1]) + " ✓", (2023, rus[-1]),
            xytext=(6, -8), textcoords="offset points", va="center", fontsize=7.8, color=C["aqua"], fontweight="bold")
tx = "tasas anuales: " + "; ".join(("+" if r > 0 else "") + fmt(100 * r, 1) for r in rates) + " %\n" \
    + "promedio aritmético = " + fmt(100 * g_ar, 2) + " %"
a2.annotate(tx, (0.02, 0.97), xycoords="axes fraction", va="top", fontsize=7.3, color=C["ink"],
            bbox=dict(boxstyle="round,pad=0.35", fc=C["gray_bg"], ec="none"))
a2.set_xlim(2017.8, 2025.3)
a2.set_ylim(9000, 17600)
a2.set_xticks(yrs)
a2.set_xticklabels([str(y) for y in yrs], fontsize=7.4)
data_axes(a2, "", "")
a2.yaxis.set_major_formatter(thousands)
a2.set_title("Rusia, PBI pc en US$ (TCm), prueba 28/9/2024", fontsize=8.8, pad=6)
save(fig, "t2_media_aritmetica")

# ---------------------------------------------------------------- Figura 2.8
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.7, 2.75), gridspec_kw=dict(width_ratios=[1.05, 1]))
fig.subplots_adjust(wspace=0.55)
arg0, arg1, us0, us1 = 4583, 18292, 8038, 58487
ga = (arg1 / arg0) ** (1 / 122) - 1
gu = (us1 / us0) ** (1 / 122) - 1
yy = np.linspace(1900, 2022, 200)
a1.plot(yy, us0 * (1 + gu) ** (yy - 1900) / 1000, color=C["orange"], lw=LW)
a1.plot(yy, arg0 * (1 + ga) ** (yy - 1900) / 1000, color=C["blue"], lw=LW)
for v, c in ((us0, C["orange"]), (arg0, C["blue"]), (us1, C["orange"]), (arg1, C["blue"])):
    x_ = 1900 if v in (us0, arg0) else 2022
    a1.plot([x_], [v / 1000], "o", ms=6, color=c, mec="white", mew=1.4, zorder=5)
a1.annotate("EEUU 1,6 %", (2022, us1 / 1000), xytext=(-6, 2), textcoords="offset points", ha="right", va="bottom",
            fontsize=8.2, color=C["orange"], fontweight="bold")
a1.annotate("Argentina 1,1 %", (1987, 4.6), ha="center", fontsize=8.2, color=C["blue"], fontweight="bold")
a1.annotate("1900: EEUU =\n1,75 × Arg.", (1900, us0 / 1000), xytext=(4, 18), textcoords="offset points",
            fontsize=7.6, color=C["ink"])
a1.annotate("2022: 3,20 ×", (2022, (us1 + arg1) / 2000), xytext=(8, 0), textcoords="offset points", va="center",
            fontsize=7.6, color=C["ink"], fontweight="bold")
arrow(a1, 2024, arg1 / 1000 + 1.2, 2024, us1 / 1000 - 1.2, C["ink"], lw=1.0, both=True)
a1.set_xlim(1895, 2030)
a1.set_ylim(0, 64)
a1.set_xticks([1900, 1940, 1980, 2022])
data_axes(a1, "", "")
a1.set_title("PBI pc (miles de US$), 1900–2022", fontsize=8.8, pad=6)

lat = [("Argentina", 1.1), ("Chile", 1.6), ("Perú", 2.0), ("Colombia", 2.1), ("Brasil", 2.3)][::-1]
bars = a2.barh(range(5), [v for _, v in lat], color=[C["blue"] if n == "Argentina" else C["ink3"] for n, _ in lat],
               height=0.58)
a2.set_yticks(range(5))
a2.set_yticklabels([n for n, _ in lat], fontsize=8.8)
a2.set_xlim(0, 4.1)
a2.set_xticks([0, 1, 2, 3])
a2.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: fmt(v, 0) + " %"))
clean_hbar(a2, "")
for b, (n, v) in zip(bars, lat):
    a2.annotate(f"{fmt(v, 1)} % · duplica en ~{round(70 / v)} años", (v, b.get_y() + b.get_height() / 2),
                xytext=(4, 0), textcoords="offset points", va="center", fontsize=7.6, color=C["ink"])
a2.set_title("Tasa media anual 1900–2022 y regla del 70", fontsize=8.8, pad=6)
save(fig, "t2_divergencia")
