# Tema 3.5 — Regla de oro: gráfico en niveles, c*(s) con máximo en s = alfa y trayectorias del consumo
# correr con: cd figs && python3 t3a_oro.py
import sys; sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403

A, a, nd = 1.0, 0.35, 0.10          # alfa = 0,35 como en el ejemplo del manual
k_oro = (a * A / nd) ** (1 / (1 - a))
y_oro = A * k_oro ** a
c_oro = y_oro - nd * k_oro
VIO = C["violet"]


def css(s):
    """consumo de estado estacionario en función de s (Cobb-Douglas)."""
    k = (s * A / nd) ** (1 / (1 - a))
    return (1 - s) * A * k ** a


# ------------------------------------------------------------------ Fig: regla de oro (dos paneles)
fig, (a1, a2) = new_fig(6.5, 3.0, ncols=2, gridspec_kw=dict(wspace=0.3, width_ratios=[1.15, 1]))
econ_axes(a1, r"$k$", "", xlim=(0, 14.5), ylim=(0, 2.9))
k = np.linspace(0, 14, 400)
a1.plot(k, A * k ** a, color=C["blue"], lw=LW)
a1.plot(k, nd * k, color=C["aqua"], lw=LW)
a1.plot(k, a * A * k ** a, color=C["orange"], lw=LW)
# tangente paralela a (n+delta)k en k_oro
kt = np.linspace(k_oro - 5, k_oro + 5, 10)
a1.plot(kt, y_oro + nd * (kt - k_oro), color=C["blue"], lw=1.1, ls=(0, (4, 3)))
label_curve(a1, 14, A * 14 ** a, r"$f(k)$", C["blue"], dx=3)
label_curve(a1, 14, nd * 14, r"$(n+\delta)k$", C["aqua"], dx=3)
label_curve(a1, 14, a * A * 14 ** a, r"$s_{oro} f(k)$", C["orange"], dx=3, dy=-2)
point(a1, k_oro, y_oro, color=C["blue"])
point(a1, k_oro, nd * k_oro, color=C["ink"])
vguide(a1, k_oro, y_oro, r"$k_{oro}$")
a1.annotate("", xy=(k_oro, y_oro), xytext=(k_oro, nd * k_oro),
            arrowprops=dict(arrowstyle="<|-|>", color=VIO, lw=1.6, shrinkA=0, shrinkB=0, mutation_scale=9))
a1.annotate("$c_{oro}$:\ndistancia\nmáxima", (k_oro, (y_oro + nd * k_oro) / 2), xytext=(6, 0),
            textcoords="offset points", ha="left", va="center", fontsize=8.4, color=VIO, fontweight="bold")
a1.annotate("tangente paralela a $(n+\\delta)k$:\n$f'(k_{oro}) = n+\\delta$", (k_oro - 2.6, y_oro - 0.26),
            xytext=(0.4, 2.85), textcoords="data", ha="left", va="top", fontsize=7.9, color=C["ink"],
            arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=0.8, mutation_scale=7, shrinkB=2))
a1.set_title("(a) Niveles: pendientes iguales en $k_{oro}$", fontsize=9, pad=14)

sv = np.linspace(0.001, 0.999, 500)
cv = css(sv)
econ_axes(a2, r"$s$", r"$c^*$", xlim=(0, 1.05), ylim=(0, 1.6))
a2.fill_between(sv[sv <= a], 0, cv[sv <= a], color=C["yellow_bg"], zorder=0)
a2.fill_between(sv[sv >= a], 0, cv[sv >= a], color=C["red_bg"], zorder=0)
a2.plot(sv, cv, color=VIO, lw=LW)
point(a2, a, c_oro, color=VIO)
vguide(a2, a, c_oro, r"$s_{oro} = \alpha$")
a2.annotate("máximo", (a, c_oro), xytext=(0, 8), textcoords="offset points", ha="center", fontsize=8.4,
            fontweight="bold", color=C["ink"])
a2.text(0.165, 0.06, "sub-\nacumulación\n$s < \\alpha$", ha="center", va="bottom", fontsize=7.2, color=C["ink"])
a2.text(0.64, 0.06, "sobreacumulación\n$s > \\alpha$\n(ineficiencia\ndinámica)", ha="center", va="bottom", fontsize=7.2,
        color=C["ink"])
a2.set_title("(b) $c^*$ según la tasa de ahorro", fontsize=9, pad=14)
save(fig, "t3a_regla_oro")
print("oro", k_oro, y_oro, c_oro, css(0.2), css(0.5), css(0.6))

# ------------------------------------------------------------------ Fig: consumo en el tiempo al moverse hacia la regla de oro
dt = 0.01
T = np.arange(0, 70 + dt, dt)


def sim(s0, s1, t0=5):
    k = np.empty_like(T)
    k[0] = (s0 * A / nd) ** (1 / (1 - a))
    for i in range(1, len(T)):
        s_ = s0 if T[i - 1] < t0 else s1
        k[i] = k[i - 1] + dt * (s_ * A * k[i - 1] ** a - nd * k[i - 1])
    s_path = np.where(T < t0, s0, s1)
    return (1 - s_path) * A * k ** a


fig, (b1, b2) = new_fig(6.4, 2.5, ncols=2, gridspec_kw=dict(wspace=0.38))
for ax_, s0, tit in [(b1, 0.6, "(a) Sobreacumulación: $s$ baja de 0,60 a 0,35"),
                     (b2, 0.2, "(b) Subacumulación: $s$ sube de 0,20 a 0,35")]:
    c = sim(s0, a)
    ax_.plot(T, c, color=VIO, lw=LW)
    ax_.axhline(c[0], color=C["ink3"], lw=1.0, ls=(0, (4, 3)))
    ax_.axvline(5, color=C["ink3"], lw=0.8, ls=(0, (2, 2)))
    ax_.annotate("consumo inicial", (70, c[0]), xytext=(-2, -4), textcoords="offset points", ha="right", va="top",
                 fontsize=7.6, color=C["ink2"])
    ax_.set_xlim(0, 70)
    ax_.set_ylim(0.85, 1.8)
    data_axes(ax_, "años", "")
    ax_.xaxis.label.set_size(8)
    ax_.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.1f}".replace(".", ",")))
    ax_.set_title(tit, fontsize=8.8)
    print(s0, c[0], c.min(), c.max(), c[-1])
    if s0 > a:
        ax_.annotate("sube hoy y queda arriba\nsiempre: ganancia gratis", (8, c[T >= 8][0]), xytext=(22, 1.62),
                     textcoords="data", fontsize=7.8, color=C["ink"], va="center",
                     arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=0.8, mutation_scale=7, shrinkB=3))
    else:
        ax_.annotate("primero cae\n(costo de la transición)", (5.3, c.min()), xytext=(14, 0.93), textcoords="data",
                     fontsize=7.8, color=C["ink"], va="center",
                     arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=0.8, mutation_scale=7, shrinkB=3))
        ax_.annotate("después supera\nal inicial", (45, c[T >= 45][0]), xytext=(40, 1.55), textcoords="data",
                     fontsize=7.8, color=C["ink"], va="center", ha="center",
                     arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=0.8, mutation_scale=7, shrinkB=3))
save(fig, "t3a_oro_transicion")
