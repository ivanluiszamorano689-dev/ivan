# TP4 · Parte A: Solow sin vs con tecnología (esquema), ALC 1951-2023, Harrod-Domar.
# correr con: cd figs && python3 p4_a.py
from p4_util import *  # noqa: F401,F403
from p4_util import C, LW, np, plt, new_fig, econ_axes, data_axes, save, point, dec, mdec, bracket, vline, ktick

# ------------------------------------------------------------ TP4.1  ln y(t): sin vs con tecnología (esquemático)
a, s, nd = 0.65, 0.30, 0.15
x = 0.02
T = np.linspace(0, 120, 1201)
dt = T[1] - T[0]
k = 0.9
kt = 0.9
ln_y0, ln_y1, g0, g1 = [], [], [], []
for t in T:
    y = k ** a
    yt = kt ** a
    ln_y0.append(np.log(y))
    ln_y1.append(np.log(yt) + x * t)
    gk = s * k ** (a - 1) - nd
    gkt = s * kt ** (a - 1) - (nd + x)
    g0.append(a * gk)
    g1.append(a * gkt + x)
    k += (s * k ** a - nd * k) * dt
    kt += (s * kt ** a - (nd + x) * kt) * dt
fig, (a1, a2) = new_fig(6.5, 2.7, ncols=2, gridspec_kw=dict(wspace=0.34))
a1.plot(T, ln_y0, color=C["blue"], lw=LW)
a1.plot(T, ln_y1, color=C["orange"], lw=LW)
econ_axes(a1, r"$t$", r"$\ln y$", xlim=(0, 125), ylim=(-0.3, 3.4))
a1.text(122, ln_y0[-1] - 0.08, "sin tecnología:\nse aplana (pendiente 0)", ha="right", va="top", fontsize=8,
        color=C["blue"], fontweight="bold")
a1.text(88, ln_y1[880] + 0.28, "con tecnología:\nrecta de pendiente $x$", ha="right", va="bottom", fontsize=8,
        color=C["orange"], fontweight="bold")
a1.set_title("(a) Nivel del ingreso per cápita (log)", fontsize=9, pad=18)
a2.plot(T, np.array(g0) * 100, color=C["blue"], lw=LW)
a2.plot(T, np.array(g1) * 100, color=C["orange"], lw=LW)
econ_axes(a2, r"$t$", r"$\gamma_y$", xlim=(0, 125), ylim=(0, 11))
a2.plot([0, 125], [x * 100, x * 100], ls=(0, (3, 3)), lw=0.9, color=C["ink3"])
a2.annotate(r"$x$", (0, x * 100), xytext=(-5, 0), textcoords="offset points", ha="right", va="center",
            fontsize=9.5)
a2.annotate(r"$0$", (0, 0), xytext=(-5, 0), textcoords="offset points", ha="right", va="center", fontsize=9.5)
a2.text(40, 3.2, "con tecnología: $\\gamma_y \\to x$", fontsize=8, color=C["orange"], fontweight="bold")
a2.text(40, 0.55, "sin tecnología: $\\gamma_y \\to 0$", fontsize=8, color=C["blue"], fontweight="bold")
a2.set_title("(b) Tasa de crecimiento per cápita", fontsize=9, pad=18)
save(fig, "p4_a_sin_con_tec")

# ------------------------------------------------------------ TP4.2  América Latina y el Caribe
per = ["1951-\n1959", "1960-\n1969", "1970-\n1979", "1980-\n1989", "1990-\n1999", "2000-\n2009", "2010-\n2019",
       "2014-\n2023"]
val = [4.9, 5.7, 5.9, 2.0, 2.8, 3.0, 1.9, 0.9]
anios = ["2020", "2021", "2022", "2023"]
anual = [-6.9, 7.0, 4.0, 2.3]
fig, (a1, a2) = new_fig(6.5, 2.9, ncols=2, gridspec_kw=dict(width_ratios=[2.35, 1], wspace=0.22))
cols = [C["blue"]] * 3 + [C["orange"]] * 5
xs = np.arange(len(val))
bars = a1.bar(xs, val, color=cols, width=0.68, zorder=2)
bars[-1].set_hatch("////")
bars[-1].set_facecolor(C["orange_bg"])
bars[-1].set_edgecolor(C["orange"])
for xi, v in zip(xs, val):
    a1.text(xi, v + (0.12 if v > 1.2 else 0.3), dec(v, 1) + " %", ha="center", va="bottom", fontsize=8, color=C["ink"], fontweight="bold")
a1.set_xticks(xs)
a1.set_xticklabels(per, fontsize=7.4)
a1.set_ylim(0, 8.1)
a1.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.0f} %"))
data_axes(a1, "", "")
a1.axhline(1.0, color=C["ink2"], lw=1.0, ls=(0, (4, 3)), zorder=3)
a1.annotate("población:\n≈ 1 % anual", (6.5, 1.0), xytext=(6.5, 4.2), textcoords="data", ha="center", va="bottom",
            fontsize=7.4, color=C["ink2"], arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=0.8, mutation_scale=7))
a1.plot([2.5, 2.5], [0, 8.0], color=C["ink3"], lw=0.9, ls=":")
a1.text(1.0, 7.0, "antes de la crisis\nde la deuda", ha="center", fontsize=7.6, color=C["blue"], fontweight="bold")
a1.text(5.0, 7.0, "después de 1980:\nnunca más de 3 %", ha="center", fontsize=7.6, color=C["orange"],
        fontweight="bold")
a1.set_title("(a) Crecimiento promedio anual del PIB real, por década", fontsize=9, pad=8)
cols2 = [C["ink3"]] * 4
a2.bar(range(4), anual, color=[C["ink2"] if v > 0 else C["ink3"] for v in anual], width=0.62, zorder=2)
for i, v in enumerate(anual):
    a2.text(i, v + (0.3 if v > 0 else -0.3), ("+" if v > 0 else "−") + dec(abs(v), 1) + " %", ha="center",
            va="bottom" if v > 0 else "top", fontsize=7.8, color=C["ink"], fontweight="bold")
a2.axhline(0, color=C["ink2"], lw=0.9)
a2.set_xticks(range(4))
a2.set_xticklabels(anios, fontsize=7.6)
a2.set_ylim(-9, 9)
a2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.0f} %".replace("-", "−")))
data_axes(a2, "", "")
a2.set_title("(b) Datos anuales: volatilidad", fontsize=9, pad=8)
save(fig, "p4_a_alc")

# ------------------------------------------------------------ TP4.3  Harrod-Domar
s, v0, d, n0 = 0.25, 2.0, 0.035, 0.05
fig, (a1, a2) = new_fig(6.5, 3.0, ncols=2, gridspec_kw=dict(wspace=0.36))
# (a) g_y vs n
n = np.linspace(0, 0.135, 50)
gy = s / v0 - d - n
a1.axhspan(0, 0.11, color=C["green_bg"], zorder=0)
a1.axhspan(-0.05, 0, color=C["red_bg"], zorder=0)
a1.plot(n * 100, gy * 100, color=C["blue"], lw=LW)
a1.plot([0, 13.5], [9, 9], color=C["orange"], lw=LW)
a1.text(13.4, 9.4, "$g_Y = s/v-\\delta$ = 9 % (no depende de $n$)", ha="right", va="bottom", fontsize=7.6,
        color=C["orange"], fontweight="bold")
a1.text(0.4, 1.6, "$g_y = s/v-\\delta-n$", ha="left", va="bottom", fontsize=8.2, color=C["blue"],
        fontweight="bold")
a1.axhline(0, color=C["ink2"], lw=0.9)
for nn, lab, dx, dy, ha in [(5, "a) $n$ = 5 %: $g_y$ = 4 %", 6, 4, "left"), (9, "b) $n$ = 9 %: $g_y$ = 0", 6, 6, "left"),
                            (11.25, "c) $n$ = 11,25 %:\n$g_y$ = −2,25 %", -6, -4, "right")]:
    point(a1, nn, 9 - nn, C["ink"])
    a1.annotate(lab, (nn, 9 - nn), xytext=(dx, dy), textcoords="offset points", ha=ha,
                va="bottom" if dy > 0 else "top", fontsize=7.6, color=C["ink"], fontweight="bold")
a1.set_xlim(0, 13.5)
a1.set_ylim(-5, 11)
a1.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.0f} %"))
a1.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.0f} %".replace("-", "−")))
data_axes(a1, "tasa de crecimiento de la población $n$", "", grid=False)
a1.text(12.8, 3.0, "crece", fontsize=7.6, color=C["green"], ha="right")
a1.text(12.8, -4.3, "cae", fontsize=7.6, color=C["red"], ha="right")
a1.set_title("(a) Crecimiento según $n$ (con $v$ = 2)", fontsize=8.8, pad=8)
# (b) g vs v
v = np.linspace(1.2, 9.2, 300)
gY = s / v - d
gy = s / v - d - n0
a2.axhspan(0, 0.18 * 100, color=C["green_bg"], zorder=0)
a2.axhspan(-0.09 * 100, 0, color=C["red_bg"], zorder=0)
a2.plot(v, gY * 100, color=C["orange"], lw=LW)
a2.plot(v, gy * 100, color=C["blue"], lw=LW)
a2.axhline(0, color=C["ink2"], lw=0.9)
a2.text(1.85, 15.5, "$g_Y = 0{,}25/v - 0{,}035$", fontsize=7.8, color=C["orange"], fontweight="bold")
a2.text(5.7, -1.9, "$g_y = 0{,}25/v - 0{,}085$", fontsize=7.8, color=C["blue"], fontweight="bold")
point(a2, 2, 9, C["ink"])
point(a2, 2, 4, C["ink"])
a2.annotate("$v$ = 2: 9 % y 4 %", (2, 9), xytext=(8, 2), textcoords="offset points", fontsize=7.6,
            fontweight="bold", color=C["ink"])
for vv, lab, col, xy, ha, va in [(0.25 / 0.085, "$v$ = 2,94\n($g_y$ = 0)", C["blue"], (-5, -6), "right", "top"),
                                 (0.25 / 0.035, "$v$ = 7,14\n($g_Y$ = 0)", C["orange"], (0, 7), "center", "bottom")]:
    point(a2, vv, 0, col)
    a2.annotate(lab, (vv, 0), xytext=xy, textcoords="offset points", ha=ha, va=va, fontsize=7.6,
                fontweight="bold", color=C["ink"])
a2.set_xlim(1, 9.3)
a2.set_ylim(-8, 18)
a2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.0f} %".replace("-", "−")))
a2.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:g}"))
data_axes(a2, "relación capital-producto $v = K/Y$", "", grid=False)
a2.set_title("(b) Crecimiento según $v$ (con $n$ = 5 %)", fontsize=8.8, pad=8)
save(fig, "p4_a_harrod")
print("ok")
