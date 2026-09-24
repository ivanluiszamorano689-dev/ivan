# TP4 · Parte B: ejercicio 5 (Solow sin tecnología) con los números del TP.
# Y = K^0,65 L^0,35 ; s = 30 % ; n = 10 % ; delta = 5 %  ->  f(k) = k^0,65 ; (delta+n) = 0,15
# correr con: cd figs && python3 p4_b.py
from p4_util import *  # noqa: F401,F403
from p4_util import (C, LW, np, plt, new_fig, econ_axes, save, point, dec, mdec, bracket, vline, ktick,
                     label_curve, arrow, hguide)

a, s0, nd0 = 0.65, 0.30, 0.15


def kstar(s, nd, A=1.0):
    return (s * A / nd) ** (1 / (1 - a))


k0 = kstar(s0, nd0)          # 7,246
y0 = k0 ** a                 # 3,623

# ------------------------------------------------------------ TP4.4  niveles
k = np.linspace(0, 12.0, 600)
fig, ax = new_fig(6.0, 3.9)
econ_axes(ax, r"$k$", r"$y,\ i,\ (\delta+n)k$", xlim=(0, 12.6), ylim=(0, 6.4))
ax.plot(k, k ** a, color=C["blue"], lw=LW)
ax.plot(k, s0 * k ** a, color=C["orange"], lw=LW)
ax.plot(k, nd0 * k, color=C["aqua"], lw=LW)
label_curve(ax, 12.0, 12.0 ** a, r"$f(k)=k^{0{,}65}$", C["blue"], dx=14)
label_curve(ax, 12.0, nd0 * 12.0, r"$(\delta+n)k=0{,}15\,k$", C["aqua"], dx=14, dy=3)
label_curve(ax, 12.0, s0 * 12.0 ** a, r"$s\,f(k)=0{,}30\,k^{0{,}65}$", C["orange"], dx=14, dy=-4)
vguide(ax, k0, y0, None)
ktick(ax, k0, r"$k^*=7{,}246$", dy=-4, size=8.6)
hguide(ax, k0, y0, r"$y^*=3{,}623$", size=8.6)
hguide(ax, k0, s0 * y0, r"$i^*=1{,}087$", size=8.6)
point(ax, k0, y0, C["blue"])
point(ax, k0, s0 * y0, C["ink"])
bracket(ax, k0 + 0.25, s0 * y0, y0, r"$c^*=(1-s)\,y^*=2{,}536$", C["ink2"], size=8.2)
arrow(ax, 3.2, 0.13, 5.6, 0.13, C["ink2"])
arrow(ax, 11.3, 0.13, 8.9, 0.13, C["ink2"])
ax.text(4.4, 0.22, r"$\dot k>0$", ha="center", va="bottom", fontsize=8.4, color=C["green"], fontweight="bold")
ax.text(10.1, 0.22, r"$\dot k<0$", ha="center", va="bottom", fontsize=8.4, color=C["red"], fontweight="bold")
# zoom: k = 0,9 y k = 2
ins = ax.inset_axes([0.07, 0.63, 0.33, 0.33])
kk = np.linspace(0, 2.35, 200)
ins.plot(kk, s0 * kk ** a, color=C["orange"], lw=1.6)
ins.plot(kk, nd0 * kk, color=C["aqua"], lw=1.6)
for kx, kd in [(0.9, 0.1451), (2.0, 0.1708)]:
    ins.plot([kx, kx], [nd0 * kx, s0 * kx ** a], color=C["green"], lw=2.6, solid_capstyle="butt")
    ins.plot([kx, kx], [0, nd0 * kx], color=C["ink3"], lw=0.7, ls=(0, (2, 2)))
    ins.annotate(r"$\dot{k}=" + mdec(kd, 3) + "$", (kx, (nd0 * kx + s0 * kx ** a) / 2), xytext=(-4, 0),
                 textcoords="offset points", ha="right", va="center", fontsize=7.6, color=C["green"],
                 fontweight="bold")
ins.set_xlim(0, 2.4)
ins.set_ylim(0, 0.62)
ins.set_xticks([0.9, 2.0])
ins.set_xticklabels(["0,9", "2"], fontsize=7.2)
ins.set_yticks([])
for sp in ("top", "right"):
    ins.spines[sp].set_visible(False)
ins.set_facecolor("#fbfbf9")
ins.set_title("zoom: incisos a) i) y a) ii)", fontsize=7.4, pad=3, color=C["ink2"], fontweight="bold")
save(fig, "p4_b_niveles")

# ------------------------------------------------------------ TP4.5  tasas
k = np.linspace(0.12, 12.5, 600)
fig, ax = new_fig(6.0, 3.1)
econ_axes(ax, r"$k$", r"$\gamma_k$", xlim=(0, 13.2), ylim=(0, 0.5))
ax.plot(k, s0 * k ** (a - 1), color=C["orange"], lw=LW)
ax.plot([0, 12.5], [nd0, nd0], color=C["aqua"], lw=LW)
ax.text(4.2, 0.24, r"$CA=\dfrac{s\,f(k)}{k}=0{,}30\,k^{-0{,}35}$", fontsize=9, color=C["orange"],
        fontweight="bold", va="bottom")
label_curve(ax, 12.5, nd0, r"$CD=\delta+n=0{,}15$", C["aqua"], dx=-2, dy=8, ha="right", size=9)
for kx, g, lab, xt in [(0.9, 0.1613, r"$\gamma_k(0{,}9)=16{,}13\,\%$", (1.35, 0.40)),
                       (2.0, 0.0854, r"$\gamma_k(2)=8{,}54\,\%$", (2.6, 0.33))]:
    bracket(ax, kx, nd0, nd0 + g, None, C["green"])
    ax.annotate(lab, (kx, nd0 + g * 0.75), xytext=xt, textcoords="data", fontsize=8.4, color=C["green"],
                fontweight="bold", va="center", arrowprops=dict(arrowstyle="-", color=C["green"], lw=0.7,
                                                                shrinkA=1, shrinkB=2))
    vline(ax, kx, nd0)
    ktick(ax, kx, dec(kx), size=8.4)
ax.text(12.4, 0.07, r"$CA<CD$: $\gamma_k<0$ ($k$ cae)", ha="right", fontsize=8.2, color=C["red"],
        fontweight="bold")
ax.text(2.4, 0.105, r"$CA>CD$: $\gamma_k>0$ ($k$ sube)", ha="left", fontsize=8.2, color=C["green"], fontweight="bold")
vguide(ax, k0, nd0, None)
ktick(ax, k0, r"$k^*=7{,}246$", size=8.6)
point(ax, k0, nd0, C["ink"])
ax.annotate(r"$0{,}15$", (0, nd0), xytext=(-5, 0), textcoords="offset points", ha="right", va="center", fontsize=8.6)
save(fig, "p4_b_tasas")


# ------------------------------------------------------------ helpers para estática comparativa
STY = {"ini": "-", "hi": (0, (6, 3)), "lo": (0, (1.5, 2))}


def statics(cases, which, X, ymax_lv, ymax_rt, title_l, title_r, labels, tick_dy):
    """cases: (clave, s, nd). which = 's' (se mueve el ahorro) o 'nd' (se mueve la depreciación efectiva).
    labels: lista (panel, x, y, texto, color, dx, dy, ha). tick_dy: dict k* -> desplazamiento del rótulo."""
    fig, (a1, a2) = new_fig(6.6, 3.2, ncols=2, gridspec_kw=dict(wspace=0.38))
    kk = np.linspace(0, X, 600)
    kr = np.linspace(0.1, X, 600)
    econ_axes(a1, r"$k$", "", xlim=(0, X * 1.04), ylim=(0, ymax_lv))
    econ_axes(a2, r"$k$", r"$\gamma_k$", xlim=(0, X * 1.04), ylim=(0, ymax_rt))
    drawn_s, drawn_nd = set(), set()
    for key, s, nd in cases:
        ks = kstar(s, nd)
        lw = LW if key == "ini" else 1.8
        if which == "s" or s not in drawn_s:
            ls = STY[key] if which == "s" else "-"
            a1.plot(kk, s * kk ** a, color=C["orange"], lw=lw if which == "s" else LW, ls=ls)
            a2.plot(kr, s * kr ** (a - 1), color=C["orange"], lw=lw if which == "s" else LW, ls=ls)
            drawn_s.add(s)
        if which == "nd" or nd not in drawn_nd:
            ls = STY[key] if which == "nd" else "-"
            a1.plot(kk, nd * kk, color=C["aqua"], lw=lw if which == "nd" else LW, ls=ls)
            a2.plot([0, X], [nd, nd], color=C["aqua"], lw=lw if which == "nd" else LW, ls=ls)
            drawn_nd.add(nd)
        for ax_, yv in ((a1, nd * ks), (a2, nd)):
            vline(ax_, ks, yv)
            point(ax_, ks, yv, C["ink"])
            ktick(ax_, ks, dec(ks, 3), size=7.6, dy=tick_dy.get(round(ks, 3), -3))
    for (pn, x, y, text, col, dx, dy, ha) in labels:
        ax_ = a1 if pn == 1 else a2
        ax_.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points", ha=ha, va="center", fontsize=7.8,
                     color=col, fontweight="bold", annotation_clip=False)
    a1.set_title(title_l, fontsize=8.8, pad=14)
    a2.set_title(title_r, fontsize=8.8, pad=14)
    return fig, a1, a2


# ------------------------------------------------------------ TP4.6  cambios en s
X = 21.0
labs = [(1, X, 0.15 * X, "$0{,}15\\,k$", C["aqua"], 3, 3, "left"),
        (1, X, 0.40 * X ** a, "$s$ = 40 %", C["orange"], 3, -2, "left"),
        (1, X, 0.30 * X ** a, "$s$ = 30 %", C["orange"], 3, 0, "left"),
        (1, X, 0.24 * X ** a, "$s$ = 24 %", C["orange"], 3, 0, "left"),
        (2, X, 0.40 * X ** (a - 1), "40 %", C["orange"], 3, 2, "left"),
        (2, X, 0.30 * X ** (a - 1), "30 %", C["orange"], 3, 0, "left"),
        (2, X, 0.24 * X ** (a - 1), "24 %", C["orange"], 3, -2, "left"),
        (2, 0.3, 0.15, "$CD$", C["aqua"], 0, -7, "left"),
        (2, 0, 0.15, "0,15", C["ink"], -4, 0, "right")]
fig, a1, a2 = statics([("lo", 0.24, 0.15), ("ini", 0.30, 0.15), ("hi", 0.40, 0.15)], "s", X, 3.4, 0.34,
                      "(e) Niveles: se mueve la curva $s\\,f(k)$", "(f) Tasas: se mueve la curva CA", labs, {})
bracket(a2, k0, 0.15, 0.15 + 0.05, "", C["green"])
bracket(a2, k0, 0.15 - 0.03, 0.15, "", C["red"])
a2.annotate("+5 %", (k0, 0.175), xytext=(-4, 0), textcoords="offset points", fontsize=7.6, color=C["green"],
            fontweight="bold", va="center", ha="right")
a2.annotate("−3 %", (k0, 0.135), xytext=(4, 0), textcoords="offset points", fontsize=7.6, color=C["red"],
            fontweight="bold", va="center", ha="left")
save(fig, "p4_b_ahorro")

# ------------------------------------------------------------ TP4.9  cambios en n
X = 30.0
labs = [(1, X, 0.17 * X, "0,17 k", C["aqua"], 3, 0, "left"),
        (1, X, 0.15 * X, "0,15 k", C["aqua"], 3, 0, "left"),
        (1, X, 0.10 * X, "0,10 k", C["aqua"], 3, 3, "left"),
        (1, X, 0.30 * X ** a, "$0{,}30\\,k^{0{,}65}$", C["orange"], 3, -4, "left"),
        (2, X, 0.17, "0,17 ($n$ = 12 %)", C["aqua"], 3, 3, "left"),
        (2, X, 0.15, "0,15 ($n$ = 10 %)", C["aqua"], 3, -2, "left"),
        (2, X, 0.10, "0,10 ($n$ = 5 %)", C["aqua"], 3, 2, "left"),
        (2, 1.1, 0.3 * 1.1 ** (a - 1), "CA", C["orange"], 5, 4, "left")]
fig, a1, a2 = statics([("lo", 0.30, 0.17), ("ini", 0.30, 0.15), ("hi", 0.30, 0.10)], "nd", X, 5.4, 0.34,
                      "(i) Niveles: rota la recta $(\\delta+n)k$", "(j) Tasas: se mueve la horizontal CD", labs,
                      {5.067: -13})
save(fig, "p4_b_poblacion")

# ------------------------------------------------------------ TP4.10  cambios en delta
X = 16.0
labs = [(1, X, 0.165 * X, "0,165 k", C["aqua"], 3, 2, "left"),
        (1, X, 0.15 * X, "0,15 k", C["aqua"], 3, 0, "left"),
        (1, X, 0.125 * X, "0,125 k", C["aqua"], 3, 2, "left"),
        (1, X, 0.30 * X ** a, "$0{,}30\\,k^{0{,}65}$", C["orange"], 3, -5, "left"),
        (2, X, 0.165, "0,165 (δ = 6,5 %)", C["aqua"], 3, 3, "left"),
        (2, X, 0.15, "0,15 (δ = 5 %)", C["aqua"], 3, -1, "left"),
        (2, X, 0.125, "0,125 (δ = 2,5 %)", C["aqua"], 3, 1, "left"),
        (2, 1.1, 0.3 * 1.1 ** (a - 1), "CA", C["orange"], 5, 4, "left")]
fig, a1, a2 = statics([("lo", 0.30, 0.165), ("ini", 0.30, 0.15), ("hi", 0.30, 0.125)], "nd", X, 2.9, 0.34,
                      "(m) Niveles: rota la recta $(\\delta+n)k$", "(n) Tasas: se mueve la horizontal CD", labs,
                      {5.518: -13})
save(fig, "p4_b_depreciacion")

# ------------------------------------------------------------ TP4.7  transición en el tiempo (simulación)
dt = 0.01
T = np.arange(-10, 80 + dt, dt)
res = {}
for s_new in (0.40, 0.24):
    kk_ = k0
    ys, gs = [], []
    for t in T:
        s = s0 if t < 0 else s_new
        y = kk_ ** a
        gk = s * kk_ ** (a - 1) - nd0
        ys.append(y)
        gs.append(a * gk)
        kk_ += (s * kk_ ** a - nd0 * kk_) * dt
    res[s_new] = (np.array(ys), np.array(gs))
fig, (a1, a2) = new_fig(6.6, 2.9, ncols=2, gridspec_kw=dict(wspace=0.3))
a1.plot(T, res[0.40][0], color=C["blue"], lw=LW)
a1.plot(T, res[0.24][0], color=C["blue"], lw=1.8, ls=(0, (1.5, 2)))
for yv, lab, up in [(6.181, "$y^*$ = 6,181 ($s$ = 40 %)", True), (3.623, "$y^*$ = 3,623 (inicial)", True),
                   (2.394, "$y^*$ = 2,394 ($s$ = 24 %)", False)]:
    a1.plot([-10, 80], [yv, yv], ls=(0, (3, 3)), lw=0.8, color=C["ink3"])
    a1.text(79, yv + (0.1 if up else -0.1), lab, ha="right", va="bottom" if up else "top", fontsize=7.5, color=C["ink"])
a1.axvline(0, color=C["ink3"], lw=0.8)
a1.text(0.8, 6.9, "shock en $t$ = 0", fontsize=7.5, color=C["ink2"], va="top")
a1.set_xlim(-10, 80)
a1.set_ylim(1.8, 7.0)
a1.yaxis.set_major_formatter(comma_fmt(0))
data_axes(a1, "años desde el cambio de $s$", "", grid=False)
a1.set_title("(a) Producto per cápita $y(t)$", fontsize=8.8, pad=8)
a2.plot(T, res[0.40][1] * 100, color=C["blue"], lw=LW)
a2.plot(T, res[0.24][1] * 100, color=C["blue"], lw=1.8, ls=(0, (1.5, 2)))
a2.axhline(0, color=C["ink2"], lw=0.9)
a2.axvline(0, color=C["ink3"], lw=0.8)
a2.annotate("salta a +3,25 %\n($= 0{,}65 \\times 5\\,\\%$)", (0, 3.25), xytext=(10, 3.0), textcoords="data",
            fontsize=7.5, color=C["ink"], va="center", arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=0.8,
                                                                          mutation_scale=7))
a2.annotate("cae a −1,95 %\n($= 0{,}65 \\times (-3\\,\\%)$)", (0, -1.95), xytext=(10, -2.3), textcoords="data",
            fontsize=7.5, color=C["ink"], va="center", arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=0.8,
                                                                          mutation_scale=7))
a2.text(79, 0.25, "vuelve a 0: efecto nivel,\nno efecto crecimiento", ha="right", va="bottom", fontsize=7.5,
        color=C["ink"], fontweight="bold")
a2.set_xlim(-10, 80)
a2.set_ylim(-2.8, 4.0)
a2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.0f} %".replace("-", "−")))
data_axes(a2, "años desde el cambio de $s$", "", grid=False)
a2.set_title("(b) Tasa de crecimiento $\\gamma_y(t)$", fontsize=8.8, pad=8)
save(fig, "p4_b_transicion")

# ------------------------------------------------------------ TP4.8  regla de oro con los datos del ej. 5
ss = np.linspace(0.005, 0.995, 500)
cs = (1 - ss) * (ss / nd0) ** (a / (1 - a))
fig, ax = new_fig(6.0, 2.9)
ax.plot(ss * 100, cs, color=C["blue"], lw=LW)
ax.axvspan(0, 65, color=C["green_bg"], zorder=0)
ax.axvspan(65, 100, color=C["red_bg"], zorder=0)
for sx, cx, lab, dy in [(24, 1.8193, "24 %: 1,819", 8), (30, 2.5360, "30 %: 2,536", 8), (40, 3.7088, "40 %: 3,709", 8)]:
    point(ax, sx, cx, C["ink"])
    ax.annotate(lab, (sx, cx), xytext=(-6, dy), textcoords="offset points", ha="right", va="bottom", fontsize=7.8,
                fontweight="bold", color=C["ink"])
point(ax, 65, 5.3301, C["blue"])
ax.annotate("regla de oro: $s_{oro}=\\alpha$ = 65 %\n$c^*_{oro}$ = 5,330  ($k_{oro}$ = 65,99)", (65, 5.33),
            xytext=(0, 8), textcoords="offset points", ha="center", va="bottom", fontsize=7.8, fontweight="bold",
            color=C["ink"])
ax.text(3, 0.35, "subacumulación ($s<\\alpha$):\nahorrar más sube $c^*$", fontsize=7.6, color=C["green"],
        fontweight="bold")
ax.text(97, 0.35, "sobreacumulación ($s>\\alpha$):\nahorrar menos sube $c^*$", fontsize=7.6, color=C["red"],
        fontweight="bold", ha="right")
ax.set_xlim(0, 100)
ax.set_ylim(0, 6.6)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.0f} %"))
ax.yaxis.set_major_formatter(comma_fmt(0))
data_axes(ax, "tasa de ahorro $s$", "")
ax.text(-0.5, 6.75, "$c^* = (1-s)\\,y^*$", fontsize=9, color=C["ink"], ha="left", va="bottom")
save(fig, "p4_b_oro")
print("ok", k0, y0)
