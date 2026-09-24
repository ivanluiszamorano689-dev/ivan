"""TP2 Parte A: dispersión, tres países, Argentina 2010-2023, China-Argentina.
Correr desde figs/:  python3 p2_crecimiento.py"""
from p2_util import *  # noqa: F403

# ---------------------------------------------------------------- datos (práctica TP2, ej. 3)
paises = [  # nombre, PIB pc PPA (US$ 2017), esperanza de vida varones, empleo vulnerable varones (%)
    ("Estados Unidos", 75698, 76, 4.86), ("Uruguay", 32149, 74, 25.27), ("San Vicente y las Gr.", 18714, 69, 23.31),
    ("Ucrania", 16371, 67, None), ("Uzbekistán", 10997, 69, 39.62), ("Tuvalu", 5592, 64, None),
    ("Tanzanía", 3713, 64, 78.34), ("Uganda", 2880, 65, 66.07)]


def disp(nombre, col, ylab, ylim, offs_log, offs_lin, par=None, yfmt=None, yticks=None):
    pts = [(p[0], p[1], p[col]) for p in paises if p[col] is not None]
    x = np.array([p[1] for p in pts], float)
    y = np.array([p[2] for p in pts], float)
    fig, axs = new_fig(6.5, 2.35, ncols=2)
    fig.subplots_adjust(wspace=0.28)
    for j, ax in enumerate(axs):
        logx = j == 1
        xx = np.log(x) if logx else x
        r = np.corrcoef(xx, y)[0, 1]
        b, a = np.polyfit(xx, y, 1)
        xs = np.linspace(xx.min() * (0.97 if logx else 0), xx.max() * 1.02, 100)
        xplot = np.exp(xs) if logx else xs
        ax.plot(xplot, a + b * xs, ls=(0, (4, 3)), lw=1.2, color=C["ink3"], zorder=1)
        colors = [C["orange"] if (par and nm in par) else C["blue"] for nm, _, _ in pts]
        ax.scatter(x, y, s=34, c=colors, edgecolor="white", linewidth=1.0, zorder=3)
        if logx:
            ax.set_xscale("log")
            ax.set_xticks([3000, 10000, 30000, 100000])
            ax.set_xlim(2200, 110000)
        else:
            ax.set_xlim(0, 82000)
            ax.set_xticks([0, 20000, 40000, 60000, 80000])
        ax.xaxis.set_major_formatter(fmt_miles())
        ax.xaxis.set_minor_formatter(plt.NullFormatter())
        ax.set_ylim(*ylim)
        if yticks:
            ax.set_yticks(yticks)
        if yfmt:
            ax.yaxis.set_major_formatter(yfmt)
        data_axes(ax, "PIB pc PPA (US$ 2017)" + (" · escala logarítmica" if logx else ""), ylab if j == 0 else "")
        ax.xaxis.label.set_size(8.3)
        ax.set_title(("En logaritmos del ingreso" if logx else "En niveles"), fontsize=9.5, pad=6)
        ax.text(0.97 if b < 0 else 0.04, 0.95, f"r = {coma(r, 2)}", transform=ax.transAxes,
                ha="right" if b < 0 else "left", va="top", fontsize=10, fontweight="bold",
                color=C["ink"], bbox=dict(fc="white", ec=C["rule"], boxstyle="round,pad=0.25"))
        offs = offs_log if logx else offs_lin
        for (nm, xi, yi) in pts:
            if nm in offs:
                dx, dy, ha = offs[nm][:3]
                txt = offs[nm][3] if len(offs[nm]) > 3 else nm
                ax.annotate(txt, (xi, yi), xytext=(dx, dy), textcoords="offset points", fontsize=7.4,
                            color=C["ink2"], ha=ha, va="center")
    save(fig, nombre)


disp("p2_disp_ev", 2, "Esperanza de vida varones (años)", (61.5, 78.5),
     offs_log={"Estados Unidos": (-4, 7, "right"), "Uruguay": (-5, 5, "right"), "San Vicente y las Gr.": (6, 0, "left"),
               "Ucrania": (0, -9, "center"), "Uzbekistán": (-6, 0, "right"), "Tuvalu": (3, -9, "left"),
               "Tanzanía": (-2, -9, "right"), "Uganda": (0, 8, "center")},
     offs_lin={"Estados Unidos": (-5, -8, "right"), "Uruguay": (0, 8, "center"), "San Vicente y las Gr.": (6, 0, "left"),
               "Uzbekistán": (0, 8, "center"), "Ucrania": (5, -5, "left"), "Uganda": (5, 6, "left"),
               "Tuvalu": (6, -6, "left", "Tanzanía y Tuvalu")},
     par={"San Vicente y las Gr.", "Uzbekistán"}, yticks=[62, 66, 70, 74, 78])

disp("p2_disp_empleo", 3, "Empleo vulnerable varones (%)", (0, 88),
     offs_log={"Estados Unidos": (0, 9, "center", "EEUU"), "Uruguay": (5, 6, "left"), "San Vicente y las Gr.": (-4, -9, "center"),
               "Uzbekistán": (5, 5, "left"), "Tanzanía": (5, 3, "left"), "Uganda": (4, -8, "left")},
     offs_lin={"Estados Unidos": (0, 9, "center", "EEUU"), "Uruguay": (5, 5, "left"), "San Vicente y las Gr.": (5, -4, "left"),
               "Uzbekistán": (6, 4, "left"), "Tanzanía": (6, 2, "left"), "Uganda": (6, -3, "left")},
     yfmt=fmt_pct())

# ---------------------------------------------------------------- ej. 4: tres países desde 1950
t = np.arange(1950, 2026)
fig, axs = new_fig(6.5, 2.35, ncols=2)
fig.subplots_adjust(wspace=0.62)
series = [("A · 3%", 0.03, C["blue"], "-"), ("B · 2%", 0.02, C["orange"], "-"), ("C · 1%", 0.01, C["aqua"], "-")]
for j, ax in enumerate(axs):
    for lab, g, col, ls in series:
        y = 8000 * (1 + g) ** (t - 1950)
        ax.plot(t, y, color=col, lw=LW, ls=ls)
        ax.annotate(f"{lab}\nUS$ {miles(y[-1])}", (2025, y[-1]), xytext=(5, 0), textcoords="offset points",
                    fontsize=7.3, color=col, fontweight="bold", va="center", linespacing=1.1)
    ax.set_xlim(1950, 2025)
    ax.set_xticks([1950, 1975, 2000, 2025])
    if j == 1:
        ax.set_yscale("log")
        ax.set_yticks([8000, 16000, 32000, 64000])
        ax.set_ylim(7000, 90000)
        ax.yaxis.set_minor_formatter(plt.NullFormatter())
        ax.set_title("Escala logarítmica: rectas", fontsize=9.5, pad=6)
        ax.text(1953, 50000, "pendiente = tasa\nde crecimiento", fontsize=8, color=C["ink2"], va="center")
    else:
        ax.set_ylim(0, 80000)
        ax.set_title("Escala lineal: curvas que se abren", fontsize=9.5, pad=6)
        y_a, y_c = 8000 * 1.03 ** 75, 8000 * 1.01 ** 75
        arrow(ax, 2021, y_c + 1500, 2021, y_a - 1500, C["ink"], lw=1.1, both=True)
        ax.text(1953, 76000, "En 2025:\nA/C = 4,35 veces\nA/B = 2,08 · B/C = 2,09", ha="left", va="top",
                fontsize=7.8, color=C["ink"], linespacing=1.3,
                bbox=dict(fc="white", ec=C["rule"], boxstyle="round,pad=0.35"))
    ax.yaxis.set_major_formatter(fmt_miles())
    data_axes(ax, "", "PIB per cápita (US$)" if j == 0 else "")
save(fig, "p2_tres_paises")

# ---------------------------------------------------------------- ej. 5: Argentina 2010-2023
arg = {2010: 670524, 2011: 710782, 2012: 703486, 2013: 720407, 2014: 702306, 2015: 721487, 2016: 706478,
       2017: 726390, 2018: 707377, 2019: 693224, 2020: 624591, 2021: 689810, 2022: 726162, 2023: 714464}
yrs = np.array(sorted(arg))
Y = np.array([arg[a] for a in yrs], float)
tasas = Y[1:] / Y[:-1] - 1
g_geo = (Y[-1] / Y[0]) ** (1 / 13) - 1
g_ari = tasas.mean()
fig, axs = new_fig(6.5, 2.5, ncols=2, gridspec_kw=dict(width_ratios=[1.25, 1]))
fig.subplots_adjust(wspace=0.3)
ax = axs[0]
ax.plot(yrs, Y / 1000, color=C["blue"], lw=LW, marker="o", ms=4, mec="white", mew=0.8, zorder=3,
        label="PBI observado")
ax.plot(yrs, Y[0] * (1 + g_geo) ** (yrs - 2010) / 1000, color=C["ink"], lw=1.3, ls=(0, (5, 3)), zorder=2,
        label=f"media geométrica {coma(100 * g_geo, 3)}%:\nllega justo a {miles(Y[-1] / 1000, 1)}")
ax.plot(yrs, Y[0] * (1 + g_ari) ** (yrs - 2010) / 1000, color=C["orange"], lw=1.5, ls=(0, (1.5, 2)), zorder=2,
        label=f"promedio aritmético {coma(100 * g_ari, 3)}%:\nllega a {miles(Y[0] * (1 + g_ari) ** 13 / 1000, 1)}, se pasa")
ax.legend(loc="lower left", fontsize=6.8, handlelength=2.0, borderaxespad=0.3, labelspacing=0.4)
ax.annotate("2020: −9,9%", (2020, Y[10] / 1000), xytext=(5, -3), textcoords="offset points", ha="left",
            va="top", fontsize=7.4, color=C["red"])
ax.set_ylim(540, 740)
ax.set_xticks([2010, 2013, 2016, 2019, 2022])
data_axes(ax, "", "PBI (miles de millones de $ de 2004)")
ax.yaxis.label.set_size(8.2)
ax.set_title("Serie en niveles y dos «tasas medias»", fontsize=9.5, pad=6)
ax = axs[1]
acum = (Y / Y[0] - 1) * 100
ax.axhline(0, color=C["ink2"], lw=0.8)
ax.fill_between(yrs, 0, acum, where=acum >= 0, color=C["blue_bg"], zorder=1, interpolate=True)
ax.fill_between(yrs, 0, acum, where=acum < 0, color=C["red_bg"], zorder=1, interpolate=True)
ax.plot(yrs, acum, color=C["blue"], lw=LW, marker="o", ms=3.5, mec="white", mew=0.8, zorder=3)
ax.annotate(f"+{coma(acum[-1], 2)}%\nacumulado", (2023, acum[-1]), xytext=(0, 12), textcoords="offset points",
            ha="center", fontsize=8, fontweight="bold", color=C["blue"])
ax.annotate(f"{coma(acum[10], 1)}%", (2020, acum[10]), xytext=(0, -11), textcoords="offset points",
            ha="center", fontsize=7.4, color=C["red"])
ax.set_ylim(-9, 13)
ax.set_xticks([2010, 2014, 2018, 2022])
ax.yaxis.set_major_formatter(fmt_pct())
data_axes(ax, "", "")
ax.set_title("Crecimiento acumulado desde 2010", fontsize=9.5, pad=6)
save(fig, "p2_arg_serie")

# barras período a período + comparación de promedios
fig, axs = new_fig(6.5, 2.2, ncols=2, gridspec_kw=dict(width_ratios=[2.1, 1]))
fig.subplots_adjust(wspace=0.55)
ax = axs[0]
cols = [C["blue"] if v >= 0 else C["red"] for v in tasas]
ax.bar(yrs[1:], tasas * 100, color=cols, width=0.68, zorder=2)
for a, v in zip(yrs[1:], tasas * 100):
    ax.text(a, v + (0.5 if v >= 0 else -0.5), coma(v, 1), ha="center", va="bottom" if v >= 0 else "top",
            fontsize=6.9, color=C["ink2"])
ax.axhline(0, color=C["ink2"], lw=0.8)
ax.set_ylim(-12.5, 13)
ax.set_xticks(yrs[1:])
ax.set_xticklabels([f"{a % 100:02d}" for a in yrs[1:]])
ax.yaxis.set_major_formatter(fmt_pct())
data_axes(ax, "año (20…)", "Variación anual del PBI")
ax.set_title("Tasa período a período: 6 subas y 7 caídas", fontsize=9.5, pad=6)
ax = axs[1]
labs = ["Promedio\naritmético\nde las 13 tasas", "Media\ngeométrica\n(n = 13) ✓", "Mal: n = 14"]
vals = [g_ari * 100, g_geo * 100, ((Y[-1] / Y[0]) ** (1 / 14) - 1) * 100]
colb = [C["orange"], C["blue"], C["ink3"]]
ax.barh([2, 1, 0], vals, color=colb, height=0.6, zorder=2)
for yv, v in zip([2, 1, 0], vals):
    ax.text(v + 0.015, yv, coma(v, 3) + "%", va="center", fontsize=8, fontweight="bold", color=C["ink"])
ax.set_yticks([2, 1, 0])
ax.set_yticklabels(labs, fontsize=7.4)
ax.set_xlim(0, 0.85)
ax.xaxis.set_major_formatter(fmt_pct(1))
ax.set_xticks([0, 0.4, 0.8])
ax.grid(axis="x", color="#ebe9e3", lw=0.8)
ax.set_axisbelow(True)
ax.set_title("¿Cuál es «la» tasa media?", fontsize=9.5, pad=6)
save(fig, "p2_arg_tasas")

# ---------------------------------------------------------------- ej. 6: China y Argentina
fig, axs = new_fig(6.5, 2.3, ncols=2, gridspec_kw=dict(width_ratios=[1, 1.15]))
fig.subplots_adjust(wspace=0.35)
ax = axs[0]
niv = {"China": (27114429, 33592045), "Argentina": (1079053, 1223376)}
xp = np.arange(2)
w = 0.36
for k, (anio, col) in enumerate(((2020, C["ink3"]), (2024, C["blue"]))):
    vals = [niv[p][k] / 1e6 for p in niv]
    ax.bar(xp + (k - 0.5) * w, vals, w * 0.95, color=col, zorder=2, label=str(anio))
    for xi, v in zip(xp + (k - 0.5) * w, vals):
        ax.text(xi, v + 0.5, coma(v, 2), ha="center", va="bottom", fontsize=7.4, color=C["ink2"])
ax.set_xticks(xp)
ax.set_xticklabels(list(niv))
ax.set_ylim(0, 38)
ax.legend(loc="upper right", fontsize=8, handlelength=1.0)
data_axes(ax, "", "PIB PPA (billones de US$ de 2017)")
ax.yaxis.label.set_size(8.2)
ax.set_title("Tamaño (nivel del PIB)", fontsize=9.5, pad=6)
ax = axs[1]
tas = {"China": (23.89, 5.502), "Argentina": (13.37, 3.188)}
for k, (lab, col) in enumerate((("acumulada 2020–24", C["aqua"]), ("media anual", C["orange"]))):
    vals = [tas[p][k] for p in tas]
    ax.bar(xp + (k - 0.5) * w, vals, w * 0.95, color=col, zorder=2, label=lab)
    for xi, v in zip(xp + (k - 0.5) * w, vals):
        ax.text(xi, v + 0.4, coma(v, 2 if k == 0 else 3) + "%", ha="center", va="bottom", fontsize=7.6,
                color=C["ink"], fontweight="bold")
ax.set_xticks(xp)
ax.set_xticklabels(list(tas))
ax.set_ylim(0, 30)
ax.yaxis.set_major_formatter(fmt_pct())
ax.legend(loc="upper right", fontsize=8, handlelength=1.0)
data_axes(ax, "", "")
ax.set_title("Ritmo (tasas, n = 4)", fontsize=9.5, pad=6)
save(fig, "p2_china_arg")
print("ok")
