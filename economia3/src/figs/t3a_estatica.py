# Tema 3.4 — Estática comparativa (niveles y tasas) y dinámica de transición simulada
# correr con: cd figs && python3 t3a_estatica.py
import sys; sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403

a = 0.4
BASE = dict(A=1.0, s=0.25, nd=0.10)


def kstar(A, s, nd):
    return (s * A / nd) ** (1 / (1 - a))


def shift_arrow(ax, x0, y0, x1, y1, color):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.4, shrinkA=0, shrinkB=0, mutation_scale=10))


def kguides(ax, k0, y0, k1, y1, lab0=r"$k^*$", lab1=r"$k^{*\prime}$"):
    vguide(ax, k0, y0, lab0)
    vguide(ax, k1, y1, lab1)
    lo, hi = sorted([k0, k1])
    arrow(ax, k0, ax.get_ylim()[1] * 0.035, k1, ax.get_ylim()[1] * 0.035, color=C["ink"], lw=1.5)


def figura(nombre, new, titulo_niv, titulo_tas, ymax_niv=2.9, show_f_shift=False, move="CA"):
    A0, s0, nd0 = BASE["A"], BASE["s"], BASE["nd"]
    A1, s1, nd1 = new.get("A", A0), new.get("s", s0), new.get("nd", nd0)
    k0, k1 = kstar(A0, s0, nd0), kstar(A1, s1, nd1)
    fig, (a1, a2) = new_fig(6.4, 2.95, ncols=2, gridspec_kw=dict(wspace=0.3))
    # ---------------- niveles
    econ_axes(a1, r"$k$", "", xlim=(0, 11.5), ylim=(0, ymax_niv))
    k = np.linspace(0, 11, 400)
    a1.plot(k, A0 * k ** a, color=C["blue"], lw=LW)
    a1.plot(k, s0 * A0 * k ** a, color=C["orange"], lw=LW)
    a1.plot(k, nd0 * k, color=C["aqua"], lw=LW)
    label_curve(a1, 11, A0 * 11 ** a, r"$f(k)$", C["blue"], dx=3)
    label_curve(a1, 11, s0 * A0 * 11 ** a, r"$s f(k)$", C["orange"], dx=3, dy=-4)
    label_curve(a1, 11, nd0 * 11, r"$(n+\delta)k$", C["aqua"], dx=3, dy=3)
    if A1 != A0:
        a1.plot(k, A1 * k ** a, color=C["blue"], lw=LW, ls="--")
        label_curve(a1, 11, A1 * 11 ** a, r"$f(k)'$", C["blue"], dx=3)
        shift_arrow(a1, 1.4, A0 * 1.4 ** a, 1.4, A1 * 1.4 ** a, C["blue"])
    if s1 != s0 or A1 != A0:
        a1.plot(k, s1 * A1 * k ** a, color=C["orange"], lw=LW, ls="--")
        label_curve(a1, 11, s1 * A1 * 11 ** a, r"$s f(k)'$", C["orange"], dx=3, dy=2)
        shift_arrow(a1, 9.3, s0 * A0 * 9.3 ** a, 9.3, s1 * A1 * 9.3 ** a, C["orange"])
    if nd1 != nd0:
        kk = np.linspace(0, ymax_niv / nd1 * 0.97, 50)
        kk = kk[kk <= 11]
        a1.plot(kk, nd1 * kk, color=C["aqua"], lw=LW, ls="--")
        label_curve(a1, kk[-1], nd1 * kk[-1], r"$(n+\delta)'k$", C["aqua"], dx=3)
        shift_arrow(a1, 9.0, nd0 * 9.0, 7.6, nd1 * 7.6, C["aqua"])
    point(a1, k0, s0 * A0 * k0 ** a, color=C["ink"])
    point(a1, k1, s1 * A1 * k1 ** a, color=C["ink"])
    point(a1, k0, A0 * k0 ** a, color=C["blue"])
    point(a1, k1, A1 * k1 ** a, color=C["blue"])
    hguide(a1, k0, A0 * k0 ** a, r"$y^*$")
    hguide(a1, k1, A1 * k1 ** a, r"$y^{*\prime}$")
    kguides(a1, k0, A0 * k0 ** a, k1, A1 * k1 ** a)
    a1.set_title(titulo_niv, fontsize=9, pad=10)
    # ---------------- tasas
    econ_axes(a2, r"$k$", r"$\gamma_k$", xlim=(0, 11.5), ylim=(0, 0.42))
    k = np.linspace(0.3, 11, 400)
    a2.plot(k, s0 * A0 * k ** (a - 1), color=C["orange"], lw=LW)
    a2.axhline(nd0, color=C["aqua"], lw=LW, xmax=11 / 11.5)
    label_curve(a2, 11, s0 * A0 * 11 ** (a - 1), "CA", C["orange"], dx=3, dy=-3)
    if nd1 == nd0:
        label_curve(a2, 10.9, nd0, "CD", C["aqua"], dx=0, dy=8, ha="right")
    else:
        label_curve(a2, 11, nd0, "CD", C["aqua"], dx=3, dy=-3)
    if s1 != s0 or A1 != A0:
        a2.plot(k, s1 * A1 * k ** (a - 1), color=C["orange"], lw=LW, ls="--")
        label_curve(a2, 11, s1 * A1 * 11 ** (a - 1), "CA'", C["orange"], dx=3, dy=2)
        shift_arrow(a2, 2.0, s0 * A0 * 2.0 ** (a - 1), 2.0, s1 * A1 * 2.0 ** (a - 1), C["orange"])
    if nd1 != nd0:
        a2.axhline(nd1, color=C["aqua"], lw=LW, ls="--", xmax=11 / 11.5)
        label_curve(a2, 11, nd1, "CD'", C["aqua"], dx=3, dy=3)
        shift_arrow(a2, 8.5, nd0, 8.5, nd1, C["aqua"])
    point(a2, k0, nd0, color=C["ink"])
    point(a2, k1, nd1, color=C["ink"])
    kguides(a2, k0, nd0, k1, nd1)
    a2.set_title(titulo_tas, fontsize=9, pad=10)
    save(fig, nombre)
    print(nombre, round(k0, 3), round(k1, 3))


figura("t3a_ce_ahorro", dict(s=0.35), "Niveles: $s\\,f(k)$ sube", "Tasas: CA sube")
figura("t3a_ce_depreciacion", dict(nd=0.14), "Niveles: $(n+\\delta)k$ más empinada", "Tasas: CD sube")
figura("t3a_ce_tecnologia", dict(A=1.3), "Niveles: $f(k)$ y $s\\,f(k)$ suben", "Tasas: CA sube", ymax_niv=3.6)

# ------------------------------------------------------------------ Fig: transición tras un aumento de s
# Parámetros del parcial 2022 (A = 5/2, alfa = 3/7, n = 4 %, delta = 9 %); s pasa de 26 % a 35 % en t = 5
A, al, n, d = 2.5, 3 / 7, 0.04, 0.09
s0, s1 = 0.26, 0.35
dt = 0.01
T = np.arange(0, 60 + dt, dt)
kk = np.empty_like(T)
kk[0] = (s0 * A / (n + d)) ** (1 / (1 - al))
for i in range(1, len(T)):
    s_ = s0 if T[i - 1] < 5 else s1
    kk[i] = kk[i - 1] + dt * (s_ * A * kk[i - 1] ** al - (n + d) * kk[i - 1])
yy = A * kk ** al
sv = np.where(T < 5, s0, s1)
gk = sv * A * kk ** (al - 1) - (n + d)
gy = al * gk
k_new = (s1 * A / (n + d)) ** (1 / (1 - al))
y_new = A * k_new ** al
print("transicion", kk[0], yy[0], k_new, y_new, gy[T >= 5][0])

fig, (b1, b2, b3) = new_fig(6.5, 2.35, ncols=3, gridspec_kw=dict(wspace=0.42))
for ax_ in (b1, b2, b3):
    ax_.axvline(5, color=C["ink3"], lw=0.8, ls=(0, (2, 2)))
b1.plot(T, kk, color=C["blue"], lw=LW)
b1.axhline(k_new, color=C["ink3"], lw=0.8, ls=(0, (4, 3)))
b1.set_ylim(14, 30)
b1.text(6, 29.2, "sube $s$", fontsize=7.6, color=C["ink2"], va="center")
b1.set_title("Capital per cápita $k$", fontsize=9)
b1.annotate("16,72", (5, kk[0]), xytext=(5, -10), textcoords="offset points", fontsize=7.6, color=C["ink2"])
b1.annotate(f"{k_new:.2f}".replace(".", ","), (60, k_new), xytext=(-2, 4), textcoords="offset points",
            fontsize=7.6, color=C["ink2"], ha="right")
b2.plot(T, yy, color=C["blue"], lw=LW)
b2.plot(T[T >= 5], np.full((T >= 5).sum(), yy[0]), color=C["ink3"], lw=1.1, ls=(0, (4, 3)))
b2.annotate("", xy=(52, y_new), xytext=(52, yy[0]),
            arrowprops=dict(arrowstyle="<|-|>", color=C["ink"], lw=1.1, mutation_scale=8, shrinkA=0, shrinkB=0))
b2.annotate("efecto\nnivel", (52, (y_new + yy[0]) / 2), xytext=(-4, 0), textcoords="offset points", ha="right",
            va="center", fontsize=8, fontweight="bold", color=C["ink"])
b2.annotate("8,36", (5, yy[0]), xytext=(5, -10), textcoords="offset points", fontsize=7.6, color=C["ink2"])
b2.annotate(f"{y_new:.2f}".replace(".", ","), (60, y_new), xytext=(-2, 4), textcoords="offset points",
            fontsize=7.6, color=C["ink2"], ha="right")
b2.set_ylim(7.8, 11)
b2.set_title("Producto per cápita $y$", fontsize=9)
b3.plot(T, gy * 100, color=C["orange"], lw=LW)
b3.axhline(0, color=C["ink2"], lw=0.8)
b3.annotate("salta y después\nse apaga: efecto\ncrecimiento\ntransitorio", (8, gy[T >= 8][0] * 100), xytext=(14, 1.3),
            textcoords="data", fontsize=7.6, color=C["ink"], va="center",
            arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=0.8, mutation_scale=7, shrinkB=3))
b3.set_ylim(-0.2, 2.3)
b3.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.1f} %".replace(".", ",")))
b3.set_title("Tasa de crecimiento $\\gamma_y$", fontsize=9)
for ax_ in (b1, b2, b3):
    data_axes(ax_, "años", "")
    ax_.set_xlim(0, 60)
    ax_.set_xticks([0, 20, 40, 60])
    ax_.xaxis.label.set_size(8)
b1.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:g}".replace(".", ",")))
b2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:g}".replace(".", ",")))
save(fig, "t3a_transicion")
# vida media de la brecha
lam = (1 - al) * (n + d)
print("lambda", lam, "vida media", np.log(2) / lam)
