# TP4 · Parte C: ej. 6 (A = 100), ej. 7 (despeje de alfa), ej. 8 c (divergencia por x).
# correr con: cd figs && python3 p4_c.py
from p4_util import *  # noqa: F401,F403
from p4_util import (C, LW, np, plt, new_fig, econ_axes, data_axes, save, point, dec, mdec, bracket, vline,
                     ktick, label_curve, arrow, comma_fmt)

a, s, nd = 0.65, 0.30, 0.15


def miles(v):
    return f"{v:,.0f}".replace(",", ".")


# ------------------------------------------------------------ TP4.11  ej. 6: A = 100 en escala log + formas con alfa
fig, (a1, a2) = new_fig(6.6, 3.2, ncols=2, gridspec_kw=dict(wspace=0.3))
k = np.logspace(-1, 8, 400)
for A, ls, lab in [(1, "-", "$A$ = 1"), (100, (0, (6, 3)), "$A$ = 100")]:
    a1.loglog(k, s * A * k ** a, color=C["orange"], lw=LW, ls=ls)
a1.loglog(k, nd * k, color=C["aqua"], lw=LW)
k1 = (s / nd) ** (1 / (1 - a))
k100 = (s * 100 / nd) ** (1 / (1 - a))
for kk, lab, xy, ha, va in [(k1, "$k^*$ = 7,246", (6, -8), "left", "top"),
                           (k100, "$k^*$ = 3.752.938", (-6, 8), "right", "bottom")]:
    point(a1, kk, nd * kk, C["ink"])
    a1.plot([kk, kk], [1e-3, nd * kk], ls=(0, (3, 3)), lw=0.9, color=C["ink3"])
    a1.annotate(lab, (kk, nd * kk), xytext=xy, textcoords="offset points", ha=ha, va=va, fontsize=7.8,
                fontweight="bold", color=C["ink"])
a1.annotate("", xy=(k100, 3e-3), xytext=(k1, 3e-3),
            arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=1.2, mutation_scale=9))
a1.text(np.sqrt(k1 * k100), 4.5e-3, "× 517.947 = $100^{1/0{,}35}$", ha="center", va="bottom", fontsize=7.8,
        color=C["ink"], fontweight="bold")
a1.text(0.13, 150, "$A$ = 100", fontsize=7.8, color=C["orange"], fontweight="bold", va="bottom")
a1.text(0.13, 0.7, "$A$ = 1", fontsize=7.8, color=C["orange"], fontweight="bold", va="bottom")
a1.text(0.35, 0.004, "$0{,}15\\,k$", fontsize=7.8, color=C["aqua"], fontweight="bold", va="bottom")
a1.set_xlim(1e-1, 1e8)
a1.set_ylim(1e-3, 1e7)
a1.set_xticks([1e-1, 1e1, 1e3, 1e5, 1e7])
a1.set_xticklabels(["0,1", "10", "1.000", "$10^5$", "$10^7$"], fontsize=7.6)
a1.set_yticks([1e-2, 1, 1e2, 1e4, 1e6])
a1.set_yticklabels(["0,01", "1", "100", "$10^4$", "$10^6$"], fontsize=7.6)
a1.minorticks_off()
data_axes(a1, "$k$ (escala logarítmica)", "", grid=False)
a1.set_title("(a) En escala log: el mismo gráfico,\ncorrido 5,7 órdenes de magnitud", fontsize=8.6, pad=6)
# (b) formas de f(k) con distinto alfa, frente a la recta (delta+n)k/s = 0,5 k
k = np.linspace(0, 10, 400)
for al, ls in [(0.35, (0, (1.5, 2))), (0.65, "-"), (0.94, (0, (6, 3)))]:
    a2.plot(k, k ** al, color=C["blue"], lw=LW if al == 0.65 else 1.8, ls=ls)
a2.plot(k, 0.5 * k, color=C["aqua"], lw=LW)
econ_axes(a2, "$k$", "", xlim=(0, 10.4), ylim=(0, 9.5))
for al, dy in [(0.35, 0), (0.65, 0), (0.94, 0)]:
    ks = 2 ** (1 / (1 - al))
    if ks < 10:
        point(a2, ks, 0.5 * ks, C["ink"])
        vline(a2, ks, 0.5 * ks)
        ktick(a2, ks, dec(ks, 3), size=7.6, dy=-3)
a2.annotate("$\\alpha$ = 0,94", (10, 10 ** 0.94), xytext=(-4, 4), textcoords="offset points", ha="right",
            fontsize=7.8, color=C["blue"], fontweight="bold")
a2.annotate("$\\alpha$ = 0,65", (10, 10 ** 0.65), xytext=(3, -1), textcoords="offset points", ha="left",
            fontsize=7.8, color=C["blue"], fontweight="bold", annotation_clip=False)
a2.annotate("$\\alpha$ = 0,35", (10, 10 ** 0.35), xytext=(3, 0), textcoords="offset points", ha="left",
            fontsize=7.8, color=C["blue"], fontweight="bold", annotation_clip=False)
a2.annotate("$0{,}5\\,k$", (10, 5.0), xytext=(3, 3), textcoords="offset points",
            ha="left", fontsize=7.8, color=C["aqua"], fontweight="bold", annotation_clip=False)
a2.text(0.3, 9.3, "con $\\alpha$ = 0,94 las\ncurvas recién se cortan\nen $k^*$ ≈ 104.000\n(fuera del gráfico)",
        fontsize=7.4, color=C["ink"], va="top")
a2.set_title("(b) Cuanto más cerca de 1 está $\\alpha$, más\n“recta” es $f(k)$ y más lejos queda $k^*$", fontsize=8.6,
             pad=6)
save(fig, "p4_c_ej6")

# ------------------------------------------------------------ TP4.12  ej. 7: despeje de alfa
fig, (a1, a2) = new_fig(6.6, 3.0, ncols=2, gridspec_kw=dict(wspace=0.32))
al = np.linspace(0.3, 1.0, 400)
a1.plot(al, 534 ** al, color=C["blue"], lw=LW)
a1.axhline(358, color=C["orange"], lw=1.6, ls=(0, (5, 3)))
alpha = np.log(358) / np.log(534)
point(a1, alpha, 358, C["ink"])
a1.plot([alpha, alpha], [0, 358], ls=(0, (3, 3)), lw=0.9, color=C["ink3"])
a1.annotate("$\\alpha$ = ln 358 / ln 534\n= 0,9363", (alpha, 358), xytext=(-8, 20), textcoords="offset points",
            ha="right", fontsize=7.8, fontweight="bold", color=C["ink"])
a1.text(0.31, 372, "$y^*$ = 358", fontsize=7.8, color=C["orange"], fontweight="bold", va="bottom")
a1.text(0.45, 150, "$y^* = 534^{\\alpha}$", fontsize=8.4, color=C["blue"], fontweight="bold")
a1.set_xlim(0.3, 1.0)
a1.set_ylim(0, 560)
a1.xaxis.set_major_formatter(comma_fmt(1))
data_axes(a1, "$\\alpha$", "", grid=True)
a1.set_title("(a) Solución gráfica: ¿qué $\\alpha$ lleva 534 a 358?", fontsize=8.6, pad=6)
al = np.linspace(0.2, 0.965, 400)
for r, col, lab in [(2.0, C["blue"], "$s/(\\delta+n)$ = 2 (datos del ej. 5)"),
                    (534 / 358, C["orange"], "$s/(\\delta+n)$ = 1,49 (implícito en el ej. 7)")]:
    a2.semilogy(al, r ** (1 / (1 - al)), color=col, lw=LW)
point(a2, 0.65, 7.2458, C["blue"])
a2.annotate("ej. 5: $k^*$ = 7,246", (0.65, 7.2458), xytext=(-6, 6), textcoords="offset points", ha="right",
            fontsize=7.6, fontweight="bold", color=C["ink"])
point(a2, alpha, 534, C["orange"])
a2.annotate("ej. 7: $k^*$ = 534", (alpha, 534), xytext=(0.47, 280), textcoords="data", ha="center",
            va="center", fontsize=7.6, fontweight="bold", color=C["ink"],
            arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=0.8, mutation_scale=7, shrinkB=4))
point(a2, alpha, 53467.5, C["blue"])
a2.annotate("≈ 53.500", (alpha, 53467.5), xytext=(-8, 0), textcoords="offset points", ha="right",
            va="center", fontsize=7.6, fontweight="bold", color=C["ink"])
a2.text(0.21, 2.2e4, "$k^* = \\left(\\dfrac{s}{\\delta+n}\\right)^{1/(1-\\alpha)}$", fontsize=8.6, color=C["ink"])
a2.text(0.21, 1.2e4, "azul: $s/(\\delta+n)$ = 2 (ej. 5)", fontsize=7.4, color=C["blue"], va="top", fontweight="bold")
a2.text(0.21, 5.0e3, "naranja: $s/(\\delta+n)$ = 1,49 (ej. 7)", fontsize=7.4, color=C["orange"], va="top",
        fontweight="bold")
a2.set_xlim(0.2, 1.0)
a2.set_ylim(1, 3e5)
a2.xaxis.set_major_formatter(comma_fmt(1))
a2.set_yticks([1, 10, 100, 1e3, 1e4, 1e5])
a2.set_yticklabels(["1", "10", "100", "1.000", "10.000", "100.000"], fontsize=7.6)
a2.minorticks_off()
data_axes(a2, "$\\alpha$", "", grid=True)
a2.set_title("(b) $k^*$ según $\\alpha$ (escala log)", fontsize=8.6, pad=6)
save(fig, "p4_c_ej7")

# ------------------------------------------------------------ TP4.13  ej. 8 c: divergencia por x (esquemático)
t = np.linspace(0, 150, 400)
fig, (a1, a2) = new_fig(6.6, 2.8, ncols=2, gridspec_kw=dict(wspace=0.3))
a1.plot(t, np.exp(0.02 * t), color=C["blue"], lw=LW)
a1.plot(t, np.exp(0.01 * t), color=C["orange"], lw=LW)
a1.text(148, np.exp(0.02 * 148), "país A: $x_A$ = 2 %", ha="right", va="bottom", fontsize=7.8, color=C["blue"],
        fontweight="bold")
a1.text(148, np.exp(0.01 * 148) + 0.6, "país B: $x_B$ = 1 %", ha="right", va="bottom", fontsize=7.8,
        color=C["orange"], fontweight="bold")
a1.set_xlim(0, 150)
a1.set_ylim(0, 21)
a1.set_yticks([0, 5, 10, 15, 20])
data_axes(a1, "años", "", grid=True)
a1.set_title("(a) Ingreso per cápita (igual al inicio = 1)", fontsize=8.6, pad=6)
ratio = np.exp(0.01 * t)
a2.plot(t, ratio, color=C["ink"], lw=LW)
for tt, rr in [(np.log(2) / 0.01, 2), (np.log(4) / 0.01, 4)]:
    point(a2, tt, rr, C["ink"])
    a2.plot([tt, tt], [1, rr], ls=(0, (3, 3)), lw=0.9, color=C["ink3"])
    a2.annotate(f"{dec(tt, 0)} años: × {rr}", (tt, rr), xytext=(-6, 5), textcoords="offset points", ha="right",
                fontsize=7.8, fontweight="bold", color=C["ink"])
a2.set_xlim(0, 150)
a2.set_ylim(1, 4.8)
a2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: "× " + dec(v)))
data_axes(a2, "años", "", grid=True)
a2.set_title("(b) Brecha $y_A/y_B$: se duplica cada ≈ 70 años", fontsize=8.6, pad=6)
save(fig, "p4_c_divergencia")
print("ok", alpha)
