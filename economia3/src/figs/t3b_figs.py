"""Tema 3 (segunda parte, 3.6 a 3.8) — gráficos del manual de teoría.

Correr desde figs/:  python3 t3b_figs.py
Genera figs/out/t3b_*.svg:
  t3b_niveles_tasas   Solow con tecnología en niveles y en tasas (números del parcial 2024, P6 Ej. 3)
  t3b_signo           la trampa del signo del exponente en la curva de ahorro (P6 2024, Ej. 3 c)
  t3b_parcial2025     el gráfico del parcial 2025 (Ej. 1 c) completo, con sus números
  t3b_sendas          senda de crecimiento balanceado: tres pendientes y convergencia a la senda
  t3b_contabilidad    contabilidad del crecimiento: Argentina 1991 (manual) y E11 (práctica)
  t3b_convergencia    convergencia absoluta vs condicional (tasas y trayectorias; esquemático)
  t3b_trampa          trampa de pobreza con tres equilibrios (esquemático)
  t3b_romer_flujo     diagrama del modelo de Romer (sector de ideas y sector de bienes)
  t3b_romer_param     g = λn/(1−φ): efecto no lineal de φ y proporcional de n (TP4 ej. 10)
  t3b_romer_nivel     duplicar investigadores de una vez vs. que crezcan más rápido (esquemático)
Opcional: T3B_PNG=<carpeta> guarda además una copia PNG de cada figura para revisarla.
"""
import os
import sys

sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch  # noqa: E402

PNG_DIR = os.environ.get("T3B_PNG")


def coma(v, dec=2):
    return f"{v:.{dec}f}".replace(".", ",").replace("-", "−")


def out(fig, name):
    if PNG_DIR:
        fig.savefig(os.path.join(PNG_DIR, name + ".png"), dpi=120)
    save(fig, name)


def ptitle(ax, text):
    ax.set_title(text, fontsize=9.4, loc="left", pad=14, color=C["ink"])


def dbl(ax, x, y0, y1, color, lw=1.4):
    ax.annotate("", xy=(x, y1), xytext=(x, y0),
                arrowprops=dict(arrowstyle="<|-|>", color=color, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=9))


def axis_arrow(ax, x0, x1, y, color=None):
    ax.annotate("", xy=(x1, y), xytext=(x0, y),
                arrowprops=dict(arrowstyle="-|>", color=color or C["ink2"], lw=1.5, shrinkA=0, shrinkB=0,
                                mutation_scale=10), annotation_clip=False)


# =====================================================================================
# 1) Solow con tecnología: niveles y tasas (P6 2024: s = 0,2; α = 0,5; n+g+δ = 0,4)
# =====================================================================================
s, a, ngd = 0.20, 0.5, 0.40
kst = (s / ngd) ** (1 / (1 - a))          # 0,25
yst = kst ** a                            # 0,5
fig, (a1, a2) = new_fig(6.5, 2.75, ncols=2, gridspec_kw=dict(wspace=0.36))
k = np.linspace(0.0005, 0.8, 500)
# niveles
a1.plot(k, k ** a, color=C["blue"], lw=LW)
a1.plot(k, s * k ** a, color=C["orange"], lw=LW)
a1.plot(k, ngd * k, color=C["aqua"], lw=LW)
econ_axes(a1, r"$\tilde k$", "", xlim=(0, 0.8), ylim=(0, 1.0))
label_curve(a1, 0.8, 0.8 ** a, r"$\tilde y=\tilde k^{0{,}5}$", C["blue"], dx=-4, dy=10, ha="right", size=9)
label_curve(a1, 0.8, s * 0.8 ** a, r"$s\,\tilde k^{0{,}5}=0{,}2\,\tilde k^{0{,}5}$", C["orange"], dx=-4, dy=-19,
            ha="right", size=8.6)
label_curve(a1, 0.62, ngd * 0.62, r"$0{,}4\,\tilde k$", C["aqua"], dx=-6, dy=9, ha="right", size=9)
vguide(a1, kst, yst, r"$\tilde k^*=0{,}25$", size=8.6)
hguide(a1, kst, yst, r"$\tilde y^*=0{,}5$", size=8.6)
point(a1, kst, s * yst, C["ink"])
point(a1, kst, yst, C["blue"])
a1.annotate("EE", (kst, s * yst), xytext=(8, -12), textcoords="offset points", fontsize=8.5,
            fontweight="bold", color=C["ink"])
ptitle(a1, "Versión en niveles")
# tasas
kk = np.linspace(0.03, 0.8, 500)
a2.fill_between(kk[kk <= kst], ngd, s * kk[kk <= kst] ** (a - 1), color=C["green_bg"], lw=0)
a2.fill_between(kk[kk >= kst], s * kk[kk >= kst] ** (a - 1), ngd, color=C["red_bg"], lw=0)
a2.plot(kk, s * kk ** (a - 1), color=C["orange"], lw=LW)
a2.plot(kk, ngd + 0 * kk, color=C["aqua"], lw=LW)
econ_axes(a2, r"$\tilde k$", r"$\gamma_{\tilde k}$", xlim=(0, 0.8), ylim=(0, 1.0))
label_curve(a2, 0.8, s * 0.8 ** (a - 1), r"CA $=0{,}2/\tilde k^{0{,}5}$", C["orange"], dx=-4, dy=-11, ha="right",
            size=8.8)
label_curve(a2, 0.8, ngd, r"CD $=n+g+\delta=0{,}4$", C["aqua"], dx=-4, dy=9, ha="right", size=8.8)
vguide(a2, kst, ngd, r"$\tilde k^*=0{,}25$", size=8.6)
point(a2, kst, ngd, C["ink"])
a2.text(0.14, 0.465, r"$\gamma>0$", fontsize=9, color=C["green"], ha="center", fontweight="bold")
a2.text(0.52, 0.33, r"$\gamma<0$", fontsize=9, color=C["red"], ha="center", fontweight="bold")
a2.annotate("", xy=(kst - 0.03, 0.035), xytext=(0.05, 0.035),
            arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=1.3, mutation_scale=9))
a2.annotate("", xy=(kst + 0.03, 0.035), xytext=(0.62, 0.035),
            arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=1.3, mutation_scale=9))
ptitle(a2, "Versión en tasas")
out(fig, "t3b_niveles_tasas")

# =====================================================================================
# 2) La trampa del signo (P6 2024, Ej. 3 c)
# =====================================================================================
fig, ax = new_fig(4.6, 2.9)
k = np.linspace(0.04, 4.6, 600)
ax.plot(k, 0.2 * k ** -0.5, color=C["orange"], lw=LW)
ax.plot(k, 0.2 * k ** 0.5, color=C["red"], lw=LW, ls="--")
ax.plot(k, 0.4 + 0 * k, color=C["aqua"], lw=LW)
econ_axes(ax, r"$\tilde k$", r"$\gamma_{\tilde k}$", xlim=(0, 4.8), ylim=(0, 1.05))
ax.text(0.42, 0.93, r"bien: CA $=0{,}2/\tilde k^{0{,}5}$ (decrece)", fontsize=8.6, color=C["orange"],
        fontweight="bold", va="center")
ax.text(4.65, 0.72, r"opción impresa: $0{,}2/\tilde k^{-0{,}5}=0{,}2\,\tilde k^{0{,}5}$ (crece)", fontsize=8.4,
        color=C["red"], fontweight="bold", ha="right", va="center")
label_curve(ax, 4.6, 0.4, r"CD $=0{,}4$", C["aqua"], dx=-2, dy=-9, ha="right", size=8.6)
point(ax, 0.25, 0.4, C["green"])
ax.annotate(r"EE: $\tilde k^*=0{,}25$", (0.25, 0.4), xytext=(12, 10), textcoords="offset points", fontsize=8.4,
            color=C["green"], fontweight="bold", va="bottom")
point(ax, 4.0, 0.4, C["red"])
ax.text(3.45, 0.53, r"corte en $\tilde k=4$ desde abajo: inestable" + "\n(no es el EE del ejercicio)", fontsize=7.9,
        color=C["red"], ha="center", va="center", linespacing=1.3)
out(fig, "t3b_signo")

# =====================================================================================
# 3) Parcial 2025, Ej. 1 c: el gráfico completo
# =====================================================================================
a = 0.4
ngd = 0.35
ka = (0.15 / ngd) ** (1 / (1 - a))     # 0,2436
kb = (0.10 / ngd) ** (1 / (1 - a))     # 0,1239
CAa_kb = 0.15 * kb ** (a - 1)          # 0,525
fig, ax = new_fig(6.2, 3.8)
k = np.linspace(0.026, 0.46, 600)
ax.plot(k, 0.15 * k ** (a - 1), color=C["orange"], lw=LW)
ax.plot(k, 0.10 * k ** (a - 1), color=C["orange"], lw=LW, ls="--")
ax.plot(k, ngd + 0 * k, color=C["aqua"], lw=LW)
econ_axes(ax, r"$\tilde k$  (capital por unidad de trabajo efectivo)", "", xlim=(0, 0.48), ylim=(0, 0.95))
ax.set_ylabel(r"$\gamma_{\tilde k}$  (tasa de crecimiento de $\tilde k$)", loc="top", rotation=0, fontsize=9.5)
ax.yaxis.set_label_coords(0.0, 1.03)
ax.yaxis.label.set_horizontalalignment("left")
ax.xaxis.label.set_fontsize(9.3)
ax.xaxis.labelpad = 27
vguide(ax, kb, ngd, r"$\tilde k^*_b=0{,}124$", size=8.6)
vguide(ax, ka, ngd, r"$\tilde k^*_a=0{,}244$", size=8.6)
point(ax, kb, ngd, C["ink"])
point(ax, ka, ngd, C["ink"])
dbl(ax, kb, ngd, CAa_kb, C["green"], lw=1.6)
point(ax, kb, CAa_kb, C["orange"])
ax.annotate("flecha doble en " + r"$\tilde k=0{,}124$" + ":\n" +
            r"$\gamma=0{,}15\cdot 0{,}124^{-0{,}6}-0{,}35=0{,}525-0{,}35=+0{,}175$",
            (kb + 0.002, (ngd + CAa_kb) / 2), xytext=(0.19, 0.64), textcoords="data", ha="left", va="center",
            fontsize=8.4, color=C["green"], fontweight="bold", linespacing=1.4,
            arrowprops=dict(arrowstyle="-", color=C["green"], lw=0.9, shrinkA=2, shrinkB=2,
                            connectionstyle="angle3,angleA=180,angleB=60"))
# rótulos de curvas
ax.text(0.068, 0.80, r"CA$_a=0{,}15/\tilde k^{0{,}6}$  (inciso a: s = 0,15)", fontsize=8.6, color=C["orange"],
        fontweight="bold", va="center")
label_curve(ax, 0.46, 0.10 * 0.46 ** (a - 1), r"CA$_b=0{,}10/\tilde k^{0{,}6}$  (inciso b: s = 0,10)", C["orange"],
            dx=-2, dy=-11, ha="right", size=8.6)
label_curve(ax, 0.46, ngd, r"CD $=n+g+\delta=0{,}35$", C["aqua"], dx=-2, dy=9, ha="right", size=8.6)
# desplazamiento de la curva de ahorro
xk = 0.43
ax.annotate("", xy=(xk, 0.10 * xk ** (a - 1) + 0.008), xytext=(xk, 0.15 * xk ** (a - 1) - 0.008),
            arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=1.3, mutation_scale=9))
ax.text(xk - 0.006, 0.212, "baja s ⇒ CA baja", ha="right", va="center", fontsize=7.8, color=C["ink2"])
out(fig, "t3b_parcial2025")

# =====================================================================================
# 4) Senda de crecimiento balanceado
# =====================================================================================
fig, (a1, a2) = new_fig(6.5, 2.65, ncols=2, gridspec_kw=dict(wspace=0.30))
t = np.linspace(0, 50, 200)
n_, g_ = 0.010, 0.020
a1.plot(t, 1.0 + 0 * t, color=C["aqua"], lw=LW)
a1.plot(t, 1.4 + g_ * t, color=C["blue"], lw=LW)
a1.plot(t, 1.8 + (n_ + g_) * t, color=C["orange"], lw=LW)
econ_axes(a1, r"$t$", r"$\ln$", xlim=(0, 58), ylim=(0.6, 3.9))
label_curve(a1, 50, 1.0, r"$\ln\tilde y$: pendiente $0$", C["aqua"], dx=-2, dy=10, ha="right", size=8.6)
label_curve(a1, 50, 1.4 + g_ * 50, r"$\ln y$: pendiente $g$", C["blue"], dx=-2, dy=12, ha="right", size=8.6)
label_curve(a1, 50, 1.8 + (n_ + g_) * 50, r"$\ln Y$: pendiente $n+g$", C["orange"], dx=-2, dy=12, ha="right",
            size=8.6)
ptitle(a1, "En el EE: tres variables, tres pendientes")
# convergencia a la senda (dinámica verdadera de Solow con tecnología, parámetros ilustrativos)
s_, al, d_ = 0.20, 1 / 3, 0.05
ngd_ = n_ + g_ + d_
kss = (s_ / ngd_) ** (1 / (1 - al))
T = np.linspace(0, 80, 1601)
dt = T[1] - T[0]


def path(k0):
    kk = [k0]
    for _ in T[1:]:
        kk.append(kk[-1] + dt * (s_ * kk[-1] ** al - ngd_ * kk[-1]))
    return np.array(kk)


lnA = g_ * T
bgp = al * np.log(kss) + lnA
a2.plot(T, bgp, color=C["ink3"], lw=1.4, ls=(0, (5, 3)))
low = al * np.log(path(0.25 * kss)) + lnA
high = al * np.log(path(2.6 * kss)) + lnA
a2.plot(T, low, color=C["blue"], lw=LW)
a2.plot(T, high, color=C["orange"], lw=LW)
econ_axes(a2, r"$t$", r"$\ln y$", xlim=(0, 88), ylim=(bgp[0] - 0.62, bgp[-1] + 0.45))
label_curve(a2, 80, bgp[-1], "senda de\ncrecimiento\nbalanceado", C["ink2"], dx=4, dy=0, size=7.8, weight="normal")
a2.annotate(r"arranca con $\tilde k_0<\tilde k^*$:" + "\ncrece más rápido que $g$", (8, low[160]), xytext=(10, -22),
            textcoords="offset points", fontsize=7.8, color=C["blue"], fontweight="bold", linespacing=1.3)
a2.text(2, bgp[0] + 1.2, r"arranca con $\tilde k_0>\tilde k^*$:" + "\ncrece más lento que $g$", va="bottom",
        fontsize=7.8, color=C["orange"], fontweight="bold", linespacing=1.3)
ptitle(a2, "Fuera del EE: convergencia a la senda")
out(fig, "t3b_sendas")

# =====================================================================================
# 5) Contabilidad del crecimiento
# =====================================================================================
sK = 0.35
casos = {
    "Argentina 1991\n(manual)": dict(gY=9.7, gL=3.8, gK=-0.1),
    "País del E11\n(práctica)": dict(gY=4.2, gL=1.1, gK=5.6),
}
fig, (a1, a2) = new_fig(6.5, 3.3, ncols=2, gridspec_kw=dict(wspace=0.34))
cols = {"cap": C["blue"], "trab": C["orange"], "ptf": C["aqua"]}
x = np.arange(len(casos))
wbar = 0.5
for i, (nom, d) in enumerate(casos.items()):
    capK = sK * d["gK"]
    trab = (1 - sK) * d["gL"]
    ptf = d["gY"] - capK - trab
    gk = d["gK"] - d["gL"]
    gy = d["gY"] - d["gL"]
    capk = sK * gk
    # panel 1: producto total
    pos, neg = 0.0, 0.0
    for val, key in [(capK, "cap"), (trab, "trab"), (ptf, "ptf")]:
        if val >= 0:
            a1.bar(i, val, wbar, bottom=pos, color=cols[key], edgecolor="white", lw=0.8)
            if val > 0.5:
                a1.text(i, pos + val / 2, coma(val, 3), ha="center", va="center", fontsize=8,
                        color="white", fontweight="bold")
            pos += val
        else:
            a1.bar(i, val, wbar, bottom=neg, color=cols[key], edgecolor="white", lw=0.8)
            neg += val
    if capK < 0:
        a1.annotate(f"capital: {coma(capK, 3)}", (i + wbar / 2, capK), xytext=(4, -6), textcoords="offset points",
                    fontsize=7.4, color=C["blue"], ha="left", va="top")
    a1.plot([i - wbar / 2 - 0.06, i + wbar / 2 + 0.06], [d["gY"], d["gY"]], color=C["ink"], lw=1.6)
    a1.text(i, d["gY"] + 0.25, r"$g_Y$ = " + coma(d["gY"], 1) + " %", ha="center", va="bottom", fontsize=8.4,
            fontweight="bold", color=C["ink"])
    # panel 2: producto por trabajador
    if capk >= 0:
        a2.bar(i, capk, wbar, color=cols["cap"], edgecolor="white", lw=0.8)
        a2.text(i, capk / 2, coma(capk, 3), ha="center", va="center", fontsize=8, color="white", fontweight="bold")
        a2.bar(i, ptf, wbar, bottom=capk, color=cols["ptf"], edgecolor="white", lw=0.8)
        a2.text(i, capk + ptf / 2, coma(ptf, 3), ha="center", va="center", fontsize=8, color="white",
                fontweight="bold")
    else:
        a2.bar(i, capk, wbar, color=cols["cap"], edgecolor="white", lw=0.8)
        a2.text(i, capk / 2, coma(capk, 3), ha="center", va="center", fontsize=8, color="white", fontweight="bold")
        a2.bar(i, ptf, wbar, color=cols["ptf"], edgecolor="white", lw=0.8)
        a2.text(i, ptf / 2, coma(ptf, 3), ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    a2.plot([i - wbar / 2 - 0.06, i + wbar / 2 + 0.06], [gy, gy], color=C["ink"], lw=1.6)
    a2.text(i, max(gy, ptf) + 0.25, r"$g_y$ = " + coma(gy, 1) + " %", ha="center", va="bottom", fontsize=8.4,
            fontweight="bold", color=C["ink"])
for ax_, tt in [(a1, r"Producto total: $g_Y = s_K g_K + s_L g_L + g_A$"),
                (a2, r"Por trabajador: $g_y = s_K g_k + g_A$")]:
    data_axes(ax_, "", "puntos porcentuales")
    ax_.set_xticks(x)
    ax_.set_xticklabels(list(casos.keys()), fontsize=8.2)
    ax_.axhline(0, color=C["ink2"], lw=0.9)
    ax_.set_ylim(-2.2, 11.2)
    ax_.set_xlim(-0.6, 1.6)
    ax_.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:g}".replace(".", ",")))
    ax_.set_title(tt, fontsize=9.2, loc="left", pad=10, color=C["ink"])
    ax_.yaxis.label.set_fontsize(8.4)
# leyenda manual
from matplotlib.patches import Patch  # noqa: E402

fig.legend(handles=[Patch(color=cols["cap"], label=r"capital ($s_K g_K$ o $s_K g_k$)"),
                    Patch(color=cols["trab"], label=r"trabajo ($s_L g_L$)"),
                    Patch(color=cols["ptf"], label=r"residuo de Solow = PTF ($g_A$)")],
           loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.13), fontsize=8.3, handlelength=1.2)
out(fig, "t3b_contabilidad")

# =====================================================================================
# 6) Convergencia absoluta vs condicional (esquemático)
# =====================================================================================
al, cd = 0.4, 0.10
sR, sP = 0.36, 0.16
kR_ss = (sR / cd) ** (1 / (1 - al))     # 8,44
kP_ss = (sP / cd) ** (1 / (1 - al))     # 2,19
fig, axs = plt.subplots(2, 2, figsize=(6.5, 4.9), gridspec_kw=dict(wspace=0.30, hspace=0.66))
(b1, b2), (b3, b4) = axs
k = np.linspace(0.45, 9.6, 500)
# --- absoluta: una sola curva
b1.plot(k, sR * k ** (al - 1), color=C["orange"], lw=LW)
b1.plot(k, cd + 0 * k, color=C["aqua"], lw=LW)
econ_axes(b1, r"$\tilde k$", r"$\gamma_{\tilde k}$", xlim=(0, 10), ylim=(0, 0.46))
kP, kR = 1.0, 3.0
for kx, lab in [(kP, "P"), (kR, "R")]:
    gx = sR * kx ** (al - 1)
    dbl(b1, kx, cd, gx, C["green"])
    vguide(b1, kx, cd, r"$\tilde k_{%s}$" % lab, size=8.6)
    b1.annotate(r"$\gamma_{%s}$" % lab, (kx, (cd + gx) / 2), xytext=(4, 0), textcoords="offset points", ha="left",
                va="center", fontsize=8.8, color=C["green"], fontweight="bold")
vguide(b1, kR_ss, cd, r"$\tilde k^*$", size=8.6)
point(b1, kR_ss, cd, C["ink"])
b1.text(1.75, 0.40, "CA común", fontsize=8.4, color=C["orange"], fontweight="bold", va="center")
label_curve(b1, 9.6, cd, "CD", C["aqua"], dx=-2, dy=8, ha="right", size=8.4)
ptitle(b1, "Absoluta: mismo $s$, un solo $\\tilde k^*$")
b1.text(9.6, 0.27, r"$\gamma_P>\gamma_R$", ha="right", fontsize=9.4, color=C["green"], fontweight="bold")
# --- condicional: dos curvas
b2.plot(k, sR * k ** (al - 1), color=C["orange"], lw=LW)
b2.plot(k, sP * k ** (al - 1), color=C["orange"], lw=LW, ls="--")
b2.plot(k, cd + 0 * k, color=C["aqua"], lw=LW)
econ_axes(b2, r"$\tilde k$", r"$\gamma_{\tilde k}$", xlim=(0, 10), ylim=(0, 0.46))
kP2, kR2 = 1.3, 3.0
for kx, lab, ss, side in [(kP2, "P", sP, -1), (kR2, "R", sR, 1)]:
    gx = ss * kx ** (al - 1)
    dbl(b2, kx, cd, gx, C["green"])
    vguide(b2, kx, cd, r"$\tilde k_{%s}$" % lab, size=8.6)
    b2.annotate(r"$\gamma_{%s}$" % lab, (kx, (cd + gx) / 2 + (0.018 if side < 0 else 0)), xytext=(4 * side, 0),
                textcoords="offset points", ha="left" if side > 0 else "right",
                va="center", fontsize=8.8, color=C["green"], fontweight="bold")
point(b2, kP_ss, cd, C["ink"])
vguide(b2, kP_ss, cd, r"$\tilde k^*_P$", size=8.6, dy=-26)
point(b2, kR_ss, cd, C["ink"])
vguide(b2, kR_ss, cd, r"$\tilde k^*_R$", size=8.6)
b2.text(1.75, 0.40, r"CA$_R$ ($s$ alto)", fontsize=8.2, color=C["orange"], fontweight="bold", va="center")
b2.text(4.0, 0.028, r"CA$_P$ ($s$ bajo)", fontsize=8.2, color=C["orange"], fontweight="bold", va="center")
ptitle(b2, "Condicional: cada uno con su $\\tilde k^*$")
b2.text(9.6, 0.27, r"$\gamma_P<\gamma_R$", ha="right", fontsize=9.4, color=C["red"], fontweight="bold")
# --- trayectorias ln y(t)
g_ = 0.02
T = np.linspace(0, 120, 2401)
dt = T[1] - T[0]


def traj(k0, ss):
    kk = [k0]
    for _ in T[1:]:
        kk.append(kk[-1] + dt * (ss * kk[-1] ** al - cd * kk[-1]))
    return al * np.log(np.array(kk)) + g_ * T


yP = traj(kP, sR)
yR = traj(kR, sR)
b3.plot(T, al * np.log(kR_ss) + g_ * T, color=C["ink3"], lw=1.2, ls=(0, (5, 3)))
b3.plot(T, yR, color=C["orange"], lw=LW)
b3.plot(T, yP, color=C["blue"], lw=LW)
econ_axes(b3, r"$t$", r"$\ln y$", xlim=(0, 130), ylim=(-0.3, 3.6))
label_curve(b3, 4, yR[80], "R", C["orange"], dx=0, dy=9, size=9)
label_curve(b3, 4, yP[80], "P", C["blue"], dx=0, dy=-10, size=9)
b3.text(126, 0.35, "una sola senda:\nlas rentas se igualan", ha="right", va="bottom", fontsize=7.8, color=C["ink2"],
        linespacing=1.3)
ptitle(b3, "Absoluta: P alcanza a R")
yP2 = traj(kP2, sP)
yR2 = traj(kR2, sR)
b4.plot(T, al * np.log(kR_ss) + g_ * T, color=C["ink3"], lw=1.2, ls=(0, (5, 3)))
b4.plot(T, al * np.log(kP_ss) + g_ * T, color=C["ink3"], lw=1.2, ls=(0, (5, 3)))
b4.plot(T, yR2, color=C["orange"], lw=LW)
b4.plot(T, yP2, color=C["blue"], lw=LW)
econ_axes(b4, r"$t$", r"$\ln y$", xlim=(0, 130), ylim=(-0.3, 3.6))
label_curve(b4, 4, yR2[80], "R", C["orange"], dx=0, dy=9, size=9)
label_curve(b4, 4, yP2[80], "P", C["blue"], dx=0, dy=-10, size=9)
b4.text(126, 0.35, "dos sendas paralelas:\nla brecha no se cierra", ha="right", va="bottom", fontsize=7.8,
        color=C["ink2"], linespacing=1.3)
ptitle(b4, "Condicional: cada uno a su senda")
out(fig, "t3b_convergencia")

# =====================================================================================
# 7) Trampa de pobreza (esquemático)
# =====================================================================================
al, s_, cd = 0.35, 0.20, 0.10
AL_, AH_, kT, w = 1.0, 3.0, 7.0, 0.6


def Atec(k):
    return AL_ + (AH_ - AL_) / (1 + np.exp(-(k - kT) / w))


def CA(k):
    return s_ * Atec(k) * k ** (al - 1)


k = np.linspace(0.3, 18, 3000)
ca = CA(k)
dif = ca - cd
cruces = k[:-1][np.sign(dif[:-1]) != np.sign(dif[1:])]
kP_, kU_, kR_ = cruces[:3]
fig, (a1, a2) = new_fig(6.5, 2.5, ncols=2, gridspec_kw=dict(wspace=0.32))
a1.plot(k, s_ * Atec(k) * k ** al, color=C["orange"], lw=LW)
a1.plot(k, cd * k, color=C["aqua"], lw=LW)
econ_axes(a1, r"$k$", "", xlim=(0, 18.8), ylim=(0, 2.1))
label_curve(a1, 10.5, s_ * Atec(10.5) * 10.5 ** al, r"$s\,f(k)$", C["orange"], dx=0, dy=11, ha="center", size=9)
label_curve(a1, 18, cd * 18, r"$(n+\delta)\,k$", C["aqua"], dx=-2, dy=11, ha="right", size=9)
for kx, lab, col in [(kP_, r"$k_P$", C["ink"]), (kU_, r"$k_U$", C["red"]), (kR_, r"$k_R$", C["ink"])]:
    vguide(a1, kx, cd * kx, lab, size=8.8)
    point(a1, kx, cd * kx, col)
a1.text(1.0, 1.55, "tramo convexo:\nrendimientos\ncrecientes", fontsize=7.8, color=C["ink2"], linespacing=1.3)
a1.annotate("", xy=(6.9, s_ * Atec(6.9) * 6.9 ** al), xytext=(4.0, 1.36),
            arrowprops=dict(arrowstyle="-|>", color=C["ink3"], lw=1.0, mutation_scale=8))
ptitle(a1, "Niveles: tres cruces")
a2.plot(k, ca, color=C["orange"], lw=LW)
a2.plot(k, cd + 0 * k, color=C["aqua"], lw=LW)
econ_axes(a2, r"$k$", r"$\gamma_k$", xlim=(0, 18.8), ylim=(0, 0.25))
a2.text(13.2, 0.158, r"CA $=s\,f(k)/k$", color=C["orange"], ha="center", va="bottom", fontsize=8.6, fontweight="bold")
label_curve(a2, 18, cd, "CD", C["aqua"], dx=-2, dy=8, ha="right", size=8.6)
for kx, lab, col in [(kP_, r"$k_P$", C["ink"]), (kU_, r"$k_U$", C["red"]), (kR_, r"$k_R$", C["ink"])]:
    vguide(a2, kx, cd, lab, size=8.8)
    point(a2, kx, cd, col)
# flechas de dinámica sobre el eje
y0 = 0.012
for x0, x1 in [(0.5, kP_ - 0.4), (kU_ - 0.3, kP_ + 0.4), (kU_ + 0.3, kR_ - 0.4), (18.3, kR_ + 0.4)]:
    a2.annotate("", xy=(x1, y0), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=1.3, mutation_scale=9))
a2.annotate("", xy=(kU_ + 2.2, 0.205), xytext=(kP_, 0.205),
            arrowprops=dict(arrowstyle="-|>", color=C["violet"], lw=1.8, mutation_scale=11))
a2.text((kP_ + kU_) / 2 + 1.1, 0.212, "big push", ha="center", va="bottom", fontsize=8.4, color=C["violet"],
        fontweight="bold")
ptitle(a2, "Tasas: CA no monótona")
out(fig, "t3b_trampa")
print("trampa", kP_, kU_, kR_)

# =====================================================================================
# 8) Romer: diagrama de flujo
# =====================================================================================
fig, ax = new_fig(6.5, 3.9)
ax.set_xlim(0, 100)
ax.set_ylim(0, 68)
ax.axis("off")


def caja(x, y, w, h, titulo, texto, color, bg):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=1.6", fc=bg, ec=color, lw=1.5))
    ax.text(x + w / 2, y + h - 2.2, titulo, ha="center", va="top", fontsize=8.6, fontweight="bold", color=C["ink"])
    ax.text(x + w / 2, y + h - 7.2, texto, ha="center", va="top", fontsize=7.9, color=C["ink2"], linespacing=1.35)


def flecha(x0, y0, x1, y1, color=None, rad=0.0, txt=None, tx=0, ty=0, lw=1.5, ha="center"):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=11, lw=lw,
                                 color=color or C["ink2"], connectionstyle=f"arc3,rad={rad}"))
    if txt:
        ax.text((x0 + x1) / 2 + tx, (y0 + y1) / 2 + ty, txt, ha=ha, va="center", fontsize=7.7,
                color=color or C["ink2"], fontweight="bold")


caja(1, 20, 19, 16, "Población L", "crece a la\ntasa n", C["ink3"], C["gray_bg"])
caja(29, 36, 30, 17, "Sector de ideas (I+D)", r"$\dot A=\delta\,L_A^{\lambda}\,A^{\phi}$" + "\ninvestigadores $L_A$",
     C["violet"], C["violet_bg"])
caja(29, 2, 30, 17, "Sector de bienes", r"$Y=K^{\alpha}(A\,L_Y)^{1-\alpha}$" + "\ntrabajadores $L_Y$",
     C["blue"], C["blue_bg"])
caja(69, 36, 29, 17, "Stock de ideas A", "no rival: lo usan\ntodos a la vez", C["aqua"], C["aqua_bg"])
caja(69, 2, 29, 17, "Ingreso per cápita", r"crece a $g=\dfrac{\lambda\,n}{1-\phi}$", C["green"], C["green_bg"])
flecha(20.8, 32, 28.2, 42, txt=r"$L_A$", tx=-2.5, ty=2)
flecha(20.8, 24, 28.2, 12, txt=r"$L_Y$", tx=-2.5, ty=-2)
flecha(59.6, 46, 68.2, 46)
ax.text(64, 48.5, "ideas\nnuevas", ha="center", va="bottom", fontsize=7.2, color=C["ink2"], linespacing=1.15)
flecha(79, 35.3, 60, 16.5, color=C["aqua"])
ax.text(73.5, 26, "todos la usan\nsin agotarla", ha="left", va="center", fontsize=7.6, color=C["aqua"],
        fontweight="bold", linespacing=1.25)
flecha(59.6, 10, 68.2, 10)
# realimentación φ
ax.add_patch(FancyArrowPatch((83.5, 53.9), (44, 53.9), arrowstyle="-|>", mutation_scale=11, lw=1.5,
                             color=C["violet"], connectionstyle="arc3,rad=0.32"))
ax.text(63.7, 61.5, r"$\phi$: el stock de ideas ayuda a crear ideas (“a hombros de gigantes”)", ha="center",
        va="bottom", fontsize=7.7, color=C["violet"], fontweight="bold")
# patentes
flecha(38, 19.8, 38, 35.2, color=C["orange"])
ax.text(39.5, 27.5, "patente: la renta\nmonopólica paga la I+D", ha="left", va="center", fontsize=7.4,
        color=C["orange"], fontweight="bold", linespacing=1.25)
out(fig, "t3b_romer_flujo")

# =====================================================================================
# 9) Romer: parámetros (TP4 ej. 10: λ = 0,30; φ = 0,15; n = 0,10)
# =====================================================================================
lam, phi0, n0 = 0.30, 0.15, 0.10
fig, (a1, a2) = new_fig(6.5, 2.65, ncols=2, gridspec_kw=dict(wspace=0.32))
ph = np.linspace(-0.4, 0.8, 400)
gph = 100 * lam * n0 / (1 - ph)
a1.axvspan(-0.4, 0, color=C["gray_bg"], lw=0)
a1.plot(ph, gph, color=C["violet"], lw=LW)
for p_, lab, dx, dy, ha, va in [(0.10, "d) 3,333 %", -8, 12, "right", "bottom"),
                                (0.15, "original 3,529 %", 6, -10, "left", "top"),
                                (0.25, "c) 4,000 %", 9, -2, "left", "top")]:
    v = 100 * lam * n0 / (1 - p_)
    point(a1, p_, v, C["violet"])
    a1.annotate(lab, (p_, v), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va, fontsize=7.9,
                color=C["ink"])
data_axes(a1, r"$\phi$ (desbordamiento de ideas)", r"$g$ (%)")
a1.set_xlim(-0.4, 0.8)
a1.set_ylim(0, 16)
a1.text(-0.2, 13.5, r"$\phi<0$:" + "\n“estanque\nagotado”", ha="center", va="center", fontsize=7.8, color=C["ink2"],
        linespacing=1.25)
a1.text(0.76, 14.8, r"$\phi\to 1$: explota", ha="right", va="center", fontsize=7.8, color=C["violet"])
a1.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:g}".replace(".", ",")))
a1.set_title(r"$\phi$ está en el denominador: no lineal", fontsize=9.2, loc="left", pad=10, color=C["ink"])
nn = np.linspace(0, 0.16, 50)
a2.plot(nn * 100, 100 * lam * nn / (1 - phi0), color=C["blue"], lw=LW)
for n_, lab, dx, dy, ha in [(0.08, "f) 2,824 %", 6, -8, "left"), (0.10, "original 3,529 %", -6, 8, "right"),
                            (0.12, "e) 4,235 %", 6, -8, "left")]:
    v = 100 * lam * n_ / (1 - phi0)
    point(a2, n_ * 100, v, C["blue"])
    a2.annotate(lab, (n_ * 100, v), xytext=(dx, dy), textcoords="offset points", ha=ha, fontsize=7.9, color=C["ink"])
data_axes(a2, r"$n$ (crecimiento de los investigadores, %)", r"$g$ (%)")
a2.set_xlim(0, 16)
a2.set_ylim(0, 6)
for axx in (a1, a2):
    axx.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:g}".replace(".", ",")))
    axx.xaxis.label.set_fontsize(8.6)
    axx.yaxis.label.set_fontsize(8.6)
a2.set_title(r"$n$ (y $\lambda$) en el numerador: proporcional", fontsize=9.2, loc="left", pad=10, color=C["ink"])
out(fig, "t3b_romer_param")

# =====================================================================================
# 10) Romer: nivel vs tasa de los investigadores (esquemático)
# =====================================================================================
lam_, phi_, n_ = 1.0, 0.2, 0.03
gss = lam_ * n_ / (1 - phi_)
T = np.linspace(0, 150, 6001)
dt = T[1] - T[0]
t0 = 40.0


def idea_path(jump=1.0, n_new=None):
    A = 1.0
    LA = gss * A ** (1 - phi_)      # arranca en la senda: g_A(0) = gss (con δ = 1)
    out_ = [np.log(A)]
    done = False
    for t in T[1:]:
        nn_ = n_ if (n_new is None or t < t0) else n_new
        LA = LA * np.exp(nn_ * dt)
        if jump != 1.0 and not done and t >= t0:
            LA *= jump
            done = True
        A = A + dt * (LA ** lam_) * A ** phi_
        out_.append(np.log(A))
    return np.array(out_)


base = idea_path()
dup = idea_path(jump=2.0)
fast = idea_path(n_new=0.045)
fig, (a1, a2) = new_fig(6.5, 2.3, ncols=2, gridspec_kw=dict(wspace=0.30))
for axx, alt, col, tt, lab in [(a1, dup, C["orange"], "Se duplica $L_A$ de una vez", "nivel más alto,\nmisma pendiente"),
                               (a2, fast, C["blue"], "Sube $n$ (de 3 % a 4,5 %)", "pendiente más alta\npara siempre")]:
    axx.plot(T, base, color=C["ink3"], lw=1.4, ls=(0, (5, 3)))
    axx.plot(T, alt, color=col, lw=LW)
    top = max(alt.max(), base.max())
    econ_axes(axx, r"$t$", r"$\ln A$", xlim=(0, 162), ylim=(-0.4, top + 1.4))
    axx.axvline(t0, color=C["rule"], lw=1.0, zorder=0)
    axx.text(t0, -0.35, r"$t_0$", ha="center", va="bottom", fontsize=8.6, color=C["ink2"])
    label_curve(axx, 147, alt[-1], lab, col, dx=-4, dy=18, ha="right", size=7.8)
    label_curve(axx, 147, base[-1], "sin cambio", C["ink3"], dx=-2, dy=-12, ha="right", size=7.8, weight="normal")
    ptitle(axx, tt)
out(fig, "t3b_romer_nivel")
print("ok t3b")
