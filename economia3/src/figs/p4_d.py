# TP4 · Parte D: ej. 9 (Solow con progreso tecnológico), ej. 10 (Romer) y estudio de casos Chile.
# correr con: cd figs && python3 p4_d.py
from p4_util import *  # noqa: F401,F403
from p4_util import (C, LW, np, plt, new_fig, econ_axes, data_axes, save, point, dec, mdec, bracket, vline,
                     ktick, label_curve, arrow, comma_fmt, canvas, box, arr, hguide)

# ------------------------------------------------------------ TP4.14  ej. 9: niveles y tasas con tres x
s, d, n, a = 0.45, 0.04, 0.10, 1 / 3
STY = {"ini": "-", "hi": (0, (1.5, 2)), "lo": (0, (6, 3))}
cases = [("lo", 0.16), ("ini", 0.20), ("hi", 0.35)]
X = 2.5
fig, (a1, a2) = new_fig(6.6, 3.3, ncols=2, gridspec_kw=dict(wspace=0.3))
kk = np.linspace(0, X, 500)
kr = np.linspace(0.05, X, 500)
econ_axes(a1, r"$\tilde k$", r"$\tilde y,\ \tilde\imath$", xlim=(0, X * 1.04), ylim=(0, 1.55))
econ_axes(a2, r"$\tilde k$", r"$\gamma_{\tilde k}$", xlim=(0, X * 1.04), ylim=(0, 1.0))
a1.plot(kk, kk ** a, color=C["blue"], lw=LW)
a1.plot(kk, s * kk ** a, color=C["orange"], lw=LW)
a2.plot(kr, s * kr ** (a - 1), color=C["orange"], lw=LW)
tick_dy = {}
for key, x in cases:
    dnx = d + n + x
    ks = (s / dnx) ** (1 / (1 - a))
    lw = LW if key == "ini" else 1.8
    a1.plot(kk, dnx * kk, color=C["aqua"], lw=lw, ls=STY[key])
    a2.plot([0, X], [dnx, dnx], color=C["aqua"], lw=lw, ls=STY[key])
    for ax_, yv in ((a1, dnx * ks), (a2, dnx)):
        vline(ax_, ks, yv)
        point(ax_, ks, yv, C["ink"])
        ktick(ax_, ks, dec(ks, 4), size=7.4, dy=-3 if key != "ini" else -13)
ks0 = (s / 0.34) ** 1.5
point(a1, ks0, ks0 ** a, C["blue"])
vline(a1, ks0, ks0 ** a)
hguide(a1, ks0, ks0 ** a, r"$\tilde y^*=1{,}1504$", size=7.8)
for ax_, x, y, t, col, dx, dy in [
        (a1, X, X ** a, r"$\tilde y = \tilde k^{1/3}$", C["blue"], 3, 0),
        (a1, X, 0.49 * X, "0,49 $\\tilde k$", C["aqua"], 3, 0),
        (a1, X, 0.34 * X, "0,34 $\\tilde k$", C["aqua"], 3, 2),
        (a1, X, 0.30 * X, "0,30 $\\tilde k$", C["aqua"], 3, -2),
        (a1, X, s * X ** a, "0,45 $\\tilde k^{1/3}$", C["orange"], 3, -3),
        (a2, X, 0.49, "0,49 ($x$ = 35 %)", C["aqua"], 3, 0), (a2, X, 0.34, "0,34 ($x$ = 20 %)", C["aqua"], 3, 3),
        (a2, X, 0.30, "0,30 ($x$ = 16 %)", C["aqua"], 3, -3),
        (a2, 0.32, s * 0.32 ** (a - 1), r"$CA=0{,}45\,\tilde k^{-2/3}$", C["orange"], 5, 2)]:
    ax_.annotate(t, (x, y), xytext=(dx, dy), textcoords="offset points", ha="left", va="center", fontsize=7.8,
                 color=col, fontweight="bold", annotation_clip=False)
a1.set_title("(b, e) Niveles por unidad de trabajo efectivo", fontsize=8.8, pad=14)
a2.set_title("(e) Tasas: CD = $\\delta+n+x$", fontsize=8.8, pad=14)
save(fig, "p4_d_ej9")

# ------------------------------------------------------------ TP4.15  ej. 9 e: la "paradoja"
fig, (a1, a2) = new_fig(6.6, 2.8, ncols=2, gridspec_kw=dict(wspace=0.32))
t = np.linspace(0, 6, 300)
vals = {0.16: (1.8371, 1.2247, (0, (6, 3))), 0.20: (1.5227, 1.1504, "-"), 0.35: (0.8801, 0.9583, (0, (1.5, 2)))}
for x, (kt, yt, ls) in vals.items():
    a1.plot(t, np.full_like(t, yt), color=C["blue"], lw=LW if x == 0.20 else 1.8, ls=ls)
    a1.text(5.9, yt + 0.012, f"$x$ = {dec(x * 100, 0)} %: $\\tilde y^*$ = {dec(yt, 4)}", ha="right", va="bottom",
            fontsize=7.6, color=C["ink"])
    a2.plot(t, np.log(yt) + x * t, color=C["blue"], lw=LW if x == 0.20 else 1.8, ls=ls)
a1.set_xlim(0, 6)
a1.set_ylim(0.85, 1.3)
a1.yaxis.set_major_formatter(comma_fmt(1))
data_axes(a1, "años", "", grid=True)
a1.set_title("(a) Por unidad de trabajo efectivo: $\\tilde y^*$ constante;\nmás bajo cuanto mayor es $x$",
             fontsize=8.4, pad=6)
for x, (kt, yt, ls) in vals.items():
    a2.text(6.05, np.log(yt) + x * 6, f"{dec(x * 100, 0)} %", ha="left", va="center", fontsize=7.8,
            color=C["blue"], fontweight="bold")
tc = (np.log(1.1504) - np.log(0.9583)) / 0.15
point(a2, tc, np.log(1.1504) + 0.20 * tc, C["ink"])
a2.annotate(f"lo pasa en {dec(tc, 1)} años", (tc, np.log(1.1504) + 0.2 * tc), xytext=(8, -12),
            textcoords="offset points", fontsize=7.8, fontweight="bold", color=C["ink"], va="top")
a2.set_xlim(0, 6)
a2.set_ylim(-0.2, 2.3)
a2.yaxis.set_major_formatter(comma_fmt(1))
data_axes(a2, "años", "", grid=True)
a2.set_title("(b) Per cápita: $\\ln y = \\ln \\tilde y^* + \\ln A_0 + x\\,t$\n(con $A_0$ = 1): pendiente $x$",
             fontsize=8.4, pad=6)
save(fig, "p4_d_ej9_paradoja")

# ------------------------------------------------------------ TP4.16  Romer: diagrama de flujo
fig, ax, W, H = canvas(6.6, 3.6, W=100)
box(ax, 1, 22, 15, 14, "Población\ntrabajadora\n$L$", fc=C["gray_bg"], ec=C["ink3"], size=8.4)
box(ax, 21, 41, 22, 10, "$L_Y$: producen bienes", fc=C["blue_bg"], ec=C["blue"], size=8.4)
box(ax, 21, 17, 22, 12, "$L_A$: investigadores\n(crecen a la tasa $n$)", fc=C["orange_bg"], ec=C["orange"], size=8.2)
box(ax, 49, 15, 21, 16, "Producción de ideas\n$\\dot A = \\delta\\,L_A^{\\lambda}\\,A^{\\phi}$", fc="white",
    ec=C["orange"], size=8.4, lw=1.6)
box(ax, 76, 17, 22, 12, "Stock de ideas $A$\n(bien no rival)", fc=C["aqua_bg"], ec=C["aqua"], size=8.4)
box(ax, 76, 41, 22, 10, "Producto $Y$", fc=C["blue_bg"], ec=C["blue"], size=8.6)
box(ax, 1, 1.5, 42, 11, "$g = \\dfrac{\\lambda\\,n}{1-\\phi}$", fc=C["yellow_bg"], ec=C["yellow"], size=10.5)
ax.text(2.5, 11.2, "senda de crecimiento\nequilibrado:", fontsize=7.4, color=C["ink2"], va="top", fontweight="bold")
arr(ax, 16, 32, 21, 45)
arr(ax, 16, 26, 21, 23)
arr(ax, 43, 46, 76, 46, color=C["blue"])
arr(ax, 43, 23, 49, 23, color=C["orange"])
ax.text(46, 24.2, "$\\lambda$", ha="center", va="bottom", fontsize=10.5, color=C["orange"])
arr(ax, 70, 23, 76, 23, color=C["aqua"])
ax.text(73, 24.2, "$\\dot A$", ha="center", va="bottom", fontsize=9.5, color=C["aqua"])
arr(ax, 87, 29, 87, 41, color=C["aqua"])
ax.text(85.5, 35, "no rival: la misma\nidea la usan todos", ha="right", va="center", fontsize=7.2, color=C["ink2"])
arr(ax, 82, 17, 63, 15, color=C["aqua"], rad=-0.55)
ax.text(72.5, 5.6, "$\\phi$: “a hombros de gigantes”: lo ya\nsabido ayuda a descubrir más", fontsize=7.4,
        color=C["aqua"], ha="center", va="center", fontweight="bold")
save(fig, "p4_d_romer_flujo")

# ------------------------------------------------------------ TP4.17  Romer: seis variantes + simulación
def g(l, f, nn):
    return l * nn / (1 - f)


g0 = g(0.30, 0.15, 0.10)
cases = [("Original", g0, C["ink2"]), ("a) λ = 20 %", g(0.20, 0.15, 0.10), C["blue"]),
         ("b) λ = 35 %", g(0.35, 0.15, 0.10), C["blue"]), ("c) φ = 25 %", g(0.30, 0.25, 0.10), C["orange"]),
         ("d) φ = 10 %", g(0.30, 0.10, 0.10), C["orange"]), ("e) n = 12 %", g(0.30, 0.15, 0.12), C["aqua"]),
         ("f) n = 8 %", g(0.30, 0.15, 0.08), C["aqua"])]
fig, (a1, a2) = new_fig(6.6, 3.0, ncols=2, gridspec_kw=dict(width_ratios=[1, 1.15], wspace=0.35))
ys = np.arange(len(cases))[::-1]
for yv, (lab, gg, col) in zip(ys, cases):
    a1.barh(yv, gg * 100, color=col, height=0.62, zorder=2)
    ch = (gg / g0 - 1) * 100
    txt = dec(gg * 100, 3) + " %" + ("" if lab == "Original" else f"  ({'+' if ch > 0 else '−'}{dec(abs(ch), 1)} %)")
    a1.text(max(gg * 100, g0 * 100) + 0.1, yv, txt, va="center", fontsize=7.3, color=C["ink"])
a1.axvline(g0 * 100, color=C["ink2"], lw=0.9, ls=(0, (3, 3)), zorder=3)
a1.set_yticks(ys)
a1.set_yticklabels([c[0] for c in cases], fontsize=7.8)
a1.set_xlim(0, 6.6)
a1.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.0f} %"))
a1.grid(axis="x", color="#ebe9e3", lw=0.8)
a1.set_axisbelow(True)
a1.set_title("(a) $g = \\lambda n/(1-\\phi)$ en los seis incisos", fontsize=8.6, pad=6)
# (b) g en función de phi (no lineal) y de n (lineal)
ph = np.linspace(-0.3, 0.8, 300)
a2.plot(ph * 100, g(0.30, ph, 0.10) * 100, color=C["orange"], lw=LW)
for pv, lab, dx, dy, ha in [(0.10, "d) 3,333 %", 2, -16, "left"), (0.15, "original 3,529 %", -8, 11, "right"),
                            (0.25, "c) 4,000 %", 8, -10, "left")]:
    point(a2, pv * 100, g(0.30, pv, 0.10) * 100, C["ink"])
    a2.annotate(lab, (pv * 100, g(0.30, pv, 0.10) * 100), xytext=(dx, dy), textcoords="offset points", ha=ha,
                va="center", fontsize=7.4, fontweight="bold", color=C["ink"])
a2.axvspan(-30, 0, color=C["red_bg"], zorder=0)
a2.text(-28, 12.2, "$\\phi<0$: “las ideas\nfáciles ya se\ndescubrieron”", fontsize=7.2, color=C["red"], va="top")
a2.text(62, 14.5, "$\\phi \\to 1$: $g \\to \\infty$", fontsize=7.6, color=C["ink"], ha="right", va="top")
a2.set_xlim(-30, 80)
a2.set_ylim(0, 16)
a2.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.0f} %".replace("-", "−")))
a2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.0f} %"))
data_axes(a2, "tasa de desbordamiento $\\phi$", "", grid=True)
a2.set_title("(b) El efecto de $\\phi$ es no lineal ($\\lambda$ = 30 %, $n$ = 10 %)", fontsize=8.6, pad=6)
save(fig, "p4_d_romer_variantes")

# simulación: nivel vs tasa de investigadores
lam, phi, nn = 0.30, 0.15, 0.10
gs = lam * nn / (1 - phi)
dt = 0.02
T = np.arange(0, 150 + dt, dt)
t0 = 20.0
A0 = gs ** (1 / (phi - 1))           # L_A(0) = 1 y g_A(0) = g* (senda equilibrada)


def sim(kind):
    A, LA = A0, 1.0
    gA, lnA = [], []
    for t in T:
        n_t = nn
        if kind == "tasa" and t >= t0:
            n_t = 0.12
        gA.append(LA ** lam * A ** (phi - 1))
        lnA.append(np.log(A))
        A += LA ** lam * A ** phi * dt
        LA *= np.exp(n_t * dt)
        if kind == "nivel" and abs(t - (t0 - dt)) < dt / 2:
            LA *= 2.0
    return np.array(gA), np.array(lnA)


base = sim("base")
niv = sim("nivel")
tas = sim("tasa")
fig, (a1, a2) = new_fig(6.6, 2.9, ncols=2, gridspec_kw=dict(wspace=0.3))
a1.plot(T, base[0] * 100, color=C["ink3"], lw=1.6)
a1.plot(T, niv[0] * 100, color=C["blue"], lw=LW)
a1.plot(T, tas[0] * 100, color=C["orange"], lw=LW)
a1.axvline(t0, color=C["ink3"], lw=0.8, ls=":")
a1.text(149, gs * 100 - 0.05, "sin cambios: 3,529 %", ha="right", va="top", fontsize=7.4, color=C["ink2"])
a1.text(149, 4.13, "$n$ → 12 %: 4,235 % para siempre", ha="right", va="top", fontsize=7.4,
        color=C["orange"], fontweight="bold")
a1.annotate("se duplican los investigadores\nde una vez: salto transitorio", (t0 + 1, niv[0].max() * 100),
            xytext=(38, 4.55), textcoords="data", fontsize=7.4, color=C["blue"], fontweight="bold", va="center",
            arrowprops=dict(arrowstyle="-|>", color=C["blue"], lw=0.8, mutation_scale=7))
a1.set_xlim(0, 150)
a1.set_ylim(3.3, 4.8)
a1.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: dec(v, 1) + " %"))
data_axes(a1, "años", "", grid=True)
a1.set_title("(a) Tasa de crecimiento de las ideas $g_A$", fontsize=8.6, pad=6)
a2.plot(T, (niv[1] - base[1]), color=C["blue"], lw=LW)
a2.plot(T, (tas[1] - base[1]), color=C["orange"], lw=LW)
a2.axvline(t0, color=C["ink3"], lw=0.8, ls=":")
a2.text(148, (niv[1] - base[1])[-1] + 0.05, "doble de $L_A$: más nivel,\nla brecha deja de crecer", ha="right",
        va="bottom", fontsize=7.4, color=C["blue"], fontweight="bold")
a2.text(100, (tas[1] - base[1])[int(100 / dt)] + 0.05, "$n$ más alto: la brecha\ncrece sin límite", ha="right",
        va="bottom", fontsize=7.4, color=C["orange"], fontweight="bold")
a2.set_xlim(0, 150)
a2.set_ylim(0, max(tas[1] - base[1]) * 1.05)
a2.yaxis.set_major_formatter(comma_fmt(1))
data_axes(a2, "años", "", grid=True)
a2.set_title("(b) Nivel de ideas vs. escenario base ($\\ln A - \\ln A_{base}$)", fontsize=8.6, pad=6)
save(fig, "p4_d_romer_sim")
print("romer: salto", niv[0].max(), "fin", niv[0][-1], tas[0][-1], "brechas", (niv[1] - base[1])[-1],
      (tas[1] - base[1])[-1])

# ------------------------------------------------------------ TP4.18  Chile: los datos del texto
fig, ax, W, H = canvas(6.6, 3.7, W=100)
cats = {"ptf": (C["blue"], C["blue_bg"], "Productividad (residuo de Solow)"),
        "rom": (C["orange"], C["orange_bg"], "Innovación e ideas (Romer)"),
        "cap": (C["aqua"], C["aqua_bg"], "Acumulación de capital (Solow)"),
        "hum": (C["violet"], C["violet_bg"], "Capital humano (Tema 7)"),
        "inf": (C["yellow"], C["yellow_bg"], "Infraestructura e integración")}
tiles = [("ptf", "2 %", "crecimiento anual del PIB real\nen la última década: menos de\nla mitad que antes"),
         ("rom", "0,39 %", "del PIB se invierte en I+D:\nmuy por debajo del\npromedio de la OCDE"),
         ("cap", "> 380", "tipos de permisos distintos\n(regulación fragmentada)"),
         ("cap", "8 años", "hasta ocho años para aprobar\nun proyecto minero"),
         ("cap", "20 %", "sobrecostos de hasta 20 %\nen esos proyectos"),
         ("hum", "≈ 50 %", "de las empresas no encuentra\ntrabajadores con competencias\nadecuadas (sobre todo digitales)"),
         ("inf", "80 %", "del transporte de carga va por\ncarretera: congestión y costos\nlogísticos altos")]
Ht = 15.8
rows = [H - 1 - Ht, H - 2 * (Ht + 1.6) + 0.6, H - 3 * (Ht + 1.6) + 0.6]
pos = [(1, rows[0]), (34.5, rows[0]), (68, rows[0]), (1, rows[1]), (34.5, rows[1]), (68, rows[1]), (1, rows[2])]
wt = 31
for (cat, big, small), (x, y) in zip(tiles, pos):
    col, bg, _ = cats[cat]
    box(ax, x, y, wt, Ht, fc=bg, ec=col, lw=1.2, r=1.4)
    ax.add_patch(plt.Rectangle((x, y + 0.5), 1.3, Ht - 1.0, color=col, zorder=3))
    ax.text(x + 3.4, y + Ht - 1.6, big, fontsize=14, fontweight="bold", color=col, va="top", zorder=4)
    ax.text(x + 3.4, y + 1.4, small, fontsize=7.0, color=C["ink"], va="bottom", zorder=4, linespacing=1.22)
lx, ly = 36, rows[2] + Ht - 2.0
ax.text(lx, ly, "Qué determinante del crecimiento toca cada dato:", fontsize=7.8, fontweight="bold",
        color=C["ink"], va="center")
for i, (key, (col, bg, lab)) in enumerate(cats.items()):
    yy = ly - 2.9 * (i + 1)
    ax.add_patch(plt.Rectangle((lx, yy - 0.9), 2.2, 1.8, color=col, zorder=3))
    ax.text(lx + 3.3, yy, lab, fontsize=7.4, va="center", color=C["ink"])
save(fig, "p4_d_chile")

# ------------------------------------------------------------ TP4.19  Parcial 2025 Ej. 1 c: gráfico en tasas
a25, dnx = 0.4, 0.35
ka = (0.15 / dnx) ** (1 / (1 - a25))
kb = (0.10 / dnx) ** (1 / (1 - a25))
k = np.linspace(0.02, 0.42, 400)
fig, ax = new_fig(5.6, 3.0)
econ_axes(ax, r"$\hat k$", r"$\gamma$", xlim=(0, 0.44), ylim=(0, 1.1))
ax.plot(k, 0.15 * k ** (a25 - 1), color=C["orange"], lw=LW)
ax.plot(k, 0.10 * k ** (a25 - 1), color=C["orange"], lw=1.8, ls=(0, (6, 3)))
ax.plot([0, 0.42], [dnx, dnx], color=C["aqua"], lw=LW)
for kk, lab in [(kb, "0,124"), (ka, "0,244")]:
    point(ax, kk, dnx, C["ink"])
    vline(ax, kk, dnx)
    ktick(ax, kk, lab, size=8.2)
bracket(ax, kb, dnx, 0.15 * kb ** (a25 - 1), None, C["green"])
ax.annotate(r"en $\hat k$ = 0,124 con $s$ = 15 %: $\gamma_{\hat k} = +0{,}175 > 0$", (kb, 0.44), xytext=(0.2, 0.62),
            textcoords="data", fontsize=8.0, color=C["green"], fontweight="bold", va="center",
            arrowprops=dict(arrowstyle="-", color=C["green"], lw=0.7))
ax.text(0.09, 0.86, r"$CA_a = 0{,}15/\hat k^{\,0{,}6}$ ($s$ = 15 %, inicial)", fontsize=8.2, color=C["orange"],
        fontweight="bold", va="center")
ax.annotate(r"$CA_b = 0{,}10/\hat k^{\,0{,}6}$ ($s$ = 10 %)", (0.42, 0.10 * 0.42 ** (a25 - 1)), xytext=(-2, -12),
            textcoords="offset points", ha="right", fontsize=8.2, color=C["orange"], fontweight="bold")
ax.annotate(r"$CD = n+g+\delta = 0{,}35$", (0.42, dnx), xytext=(-2, 7), textcoords="offset points", ha="right",
            fontsize=8.2, color=C["aqua"], fontweight="bold")
arrow(ax, 0.36, 0.15 * 0.36 ** (a25 - 1) - 0.02, 0.36, 0.10 * 0.36 ** (a25 - 1) + 0.03, C["ink2"])
save(fig, "p4_r_2025_tasas")
print("ok")
