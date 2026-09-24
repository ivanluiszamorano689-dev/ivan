# Tema 3.2 — Harrod-Domar: coeficientes fijos, filo de la navaja y umbral de v (parcial 2023, Ej. 1 d)
# correr con: cd figs && python3 t3a_harrod.py
import sys; sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403

comma = plt.FuncFormatter(lambda v, p: f"{v:g}".replace(".", ","))

# ------------------------------------------------------------------ Fig 3.4: isocuantas Leontief vs neoclásica
fig, (a1, a2) = new_fig(6.4, 2.75, ncols=2, gridspec_kw=dict(wspace=0.32))
theta_u = 1.0  # K/L eficiente (esquemático)
for q, lab in zip([1, 2, 3], ["$Y_1$", "$Y_2$", "$Y_3$"]):
    Lc, Kc = 1.2 * q, 1.2 * q * theta_u
    a1.plot([Lc, Lc, 4.6], [4.6, Kc, Kc], color=C["blue"], lw=LW, solid_joinstyle="miter")
    a1.plot([Lc], [Kc], "o", ms=5.5, color=C["blue"], mec="white", mew=1.2, zorder=5)
    a1.annotate(lab, (4.6, Kc), xytext=(3, 0), textcoords="offset points", va="center", fontsize=9.5,
                color=C["blue"], fontweight="bold")
a1.plot([0, 4.75], [0, 4.75 * theta_u], color=C["ink3"], lw=1, ls=(0, (4, 3)))
a1.annotate("$K/L$\nfija", (4.75, 4.75), xytext=(3, 0), textcoords="offset points", ha="left", va="center",
            fontsize=8, color=C["ink2"])
# capital ocioso (brazo vertical) y desempleo (brazo horizontal) sobre Y1
a1.plot([1.2], [3.9], "o", ms=5.5, color=C["orange"], mec="white", mew=1.2, zorder=5)
a1.annotate("capital\nocioso", (1.2, 3.9), xytext=(-5, 0), textcoords="offset points", ha="right", va="center",
            fontsize=7.3, color=C["ink"])
a1.plot([3.9], [1.2], "o", ms=5.5, color=C["orange"], mec="white", mew=1.2, zorder=5)
a1.text(4.7, 0.88, "más $L$ con el mismo $K$: $Y$ no sube\n(trabajadores desempleados)", ha="right", va="top",
        fontsize=7.3, color=C["ink"])
econ_axes(a1, r"$L$", r"$K$", xlim=(0, 5.2), ylim=(0, 4.9))
a1.set_title("Harrod-Domar: coeficientes fijos\n(isocuantas en L, sin sustitución)", fontsize=9)

L = np.linspace(0.25, 4.8, 300)
for q, lab in zip([1.2, 2.4, 3.6], ["$Y_1$", "$Y_2$", "$Y_3$"]):
    Kq = q ** 2 / L  # K^0.5 L^0.5 = q
    m = Kq <= 4.7
    a2.plot(L[m], Kq[m], color=C["blue"], lw=LW)
    a2.annotate(lab, (L[-1], Kq[-1]), xytext=(3, 0), textcoords="offset points", va="center", fontsize=9.5,
                color=C["blue"], fontweight="bold")
# dos combinaciones sobre Y2 con distinta K/L
for Lp, lab in [(1.4, "A"), (3.0, "B")]:
    Kp = 2.4 ** 2 / Lp
    a2.plot([0, Lp * 1.3], [0, Kp * 1.3], color=C["ink3"], lw=0.9, ls=(0, (4, 3)))
    a2.plot([Lp], [Kp], "o", ms=5.5, color=C["orange"], mec="white", mew=1.2, zorder=5)
    a2.annotate(lab, (Lp, Kp), xytext=(-5, -5), textcoords="offset points", ha="right", va="top", fontsize=9,
                color=C["ink"], fontweight="bold")
econ_axes(a2, r"$L$", r"$K$", xlim=(0, 5.2), ylim=(0, 4.9))
a2.set_title("Solow: función neoclásica\n(isocuantas suaves, $K/L$ se ajusta)", fontsize=9)
save(fig, "t3a_hd_isocuantas")

# ------------------------------------------------------------------ Fig 3.5: filo de la navaja
fig, (a1, a2) = new_fig(6.4, 2.8, ncols=2, gridspec_kw=dict(wspace=0.3))
theta, delta, n = 3.0, 0.05, 0.02
s = np.linspace(0.08, 0.40, 50)
gw = s / theta - delta
a1.plot(s, gw, color=C["orange"], lw=LW)
a1.axhline(n, color=C["aqua"], lw=LW)
s_eq = theta * (n + delta)
label_curve(a1, s[-1], gw[-1], r"$g_w = s/\theta - \delta$", C["orange"], dx=-4, dy=10, ha="right")
label_curve(a1, 0.40, n, r"$g_n = n$", C["aqua"], dx=0, dy=-9, ha="right")
point(a1, s_eq, n, color=C["ink"])
a1.annotate("el filo: un único $s$\n(pura casualidad)", (s_eq, n), xytext=(-40, 26), textcoords="offset points",
            ha="center", fontsize=7.8, color=C["ink"],
            arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=0.9, mutation_scale=7, shrinkB=5))
vguide(a1, s_eq, n)
a1.text(s_eq - 0.01, -0.047, "← $g_w < n$:\ndesempleo creciente", fontsize=7.6, color=C["ink"], ha="right", va="center")
a1.text(s_eq + 0.01, -0.047, "$g_w > n$: →\nfalta mano de obra", fontsize=7.6, color=C["ink"], ha="left", va="center")
econ_axes(a1, r"$s$", "tasas", xlim=(0.03, 0.42), ylim=(-0.065, 0.1))
a1.set_title("(a) Garantizada vs natural: son\nparámetros independientes", fontsize=9, pad=16)

t = np.linspace(0, 10, 200)
for gdif, col, lab in [(0.06, C["orange"], "$g_w > n$: falta\nmano de obra"),
                       (0.0, C["ink"], "$g_w = n$: el filo\n(pleno empleo)"),
                       (-0.06, C["blue"], "$g_w < n$: desempleo\ncreciente")]:
    r_ = np.exp(gdif * t)
    a2.plot(t, r_, color=col, lw=LW)
    a2.annotate(lab, (t[-1], r_[-1]), xytext=(5, 0), textcoords="offset points", ha="left", va="center",
                fontsize=7.3, color=C["ink"])
econ_axes(a2, r"$t$", r"$L^{req}/L$", xlim=(0, 10.3), ylim=(0.45, 1.9))
a2.set_title("(b) Cualquier desvío se amplifica", fontsize=9, pad=16)
save(fig, "t3a_hd_filo")

# ------------------------------------------------------------------ Fig 3.6: umbral de v (parcial 2023, Ej. 1 d)
s, nd, d = 0.19, 0.175, 0.13
v = np.linspace(0.3, 3.0, 400)
g = s / v - nd
gY = s / v - d
vstar, vstarY = s / nd, s / d
fig, ax = new_fig(6.0, 3.0)
ax.fill_between(v, 0, g, where=v <= vstar, color=C["green_bg"], zorder=1)
ax.fill_between(v, g, 0, where=v >= vstar, color=C["red_bg"], zorder=1)
ax.plot(v, g, color=C["blue"], lw=LW, zorder=3)
ax.axhline(0, color=C["ink2"], lw=0.9)
point(ax, vstar, 0, color=C["blue"])
point(ax, vstarY, 0, color=C["ink3"])
ax.annotate(r"$v = \dfrac{s}{n+\delta} = \dfrac{0{,}19}{0{,}175} = 1{,}0857$", (vstar, 0), xytext=(34, 62),
            textcoords="offset points", fontsize=9, color=C["ink"], ha="left",
            arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=0.9, mutation_scale=7, shrinkB=5))
ax.annotate("1,46 = $s/\\delta$: umbral de la versión agregada\n$g_Y = s/v - \\delta$ (no es la que pide el parcial)",
            (vstarY, 0), xytext=(26, 22), textcoords="offset points", fontsize=7.8, color=C["ink2"], ha="left",
            arrowprops=dict(arrowstyle="-|>", color=C["ink3"], lw=0.8, mutation_scale=7, shrinkB=5))
label_curve(ax, 0.42, s / 0.42 - nd, r"$g_y = \dfrac{0{,}19}{v} - 0{,}175$", C["blue"], dx=8, dy=4)
ax.text(0.62, 0.035, "$g_y > 0$\ncrece", fontsize=8.5, color=C["green"], fontweight="bold", ha="center")
ax.text(2.35, -0.05, "$g_y < 0$: el producto per cápita cae", fontsize=8.5, color=C["red"], fontweight="bold",
        ha="center")
ax.set_xlim(0, 3.05)
ax.set_ylim(-0.13, 0.36)
ax.set_xticks([0, 0.5, 1, 1.5, 2, 2.5, 3])
ax.xaxis.set_major_formatter(comma)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{x * 100:.0f} %"))
data_axes(ax, r"relación capital-producto $v = K/Y$", "tasa de crecimiento")
save(fig, "t3a_hd_umbral")
print(vstar, vstarY, s_eq)
