# Tema 3.3 — Solow-Swan sin tecnología: función neoclásica, diagrama en niveles, en tasas,
# y "funciones" vs "curvas" con los números del parcial 2023 (Ej. 1 b)
# correr con: cd figs && python3 t3a_solow.py
import sys; sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403

comma = plt.FuncFormatter(lambda v, p: f"{v:g}".replace(".", ","))


def bracket(ax, x, y0, y1, text, color, side="right", dx=5, size=8.4):
    """Llave vertical (flecha doble) entre y0 e y1 en x, con rótulo al costado."""
    ax.annotate("", xy=(x, y1), xytext=(x, y0),
                arrowprops=dict(arrowstyle="<|-|>", color=color, lw=1.3, shrinkA=0, shrinkB=0, mutation_scale=8))
    ax.annotate(text, (x, (y0 + y1) / 2), xytext=(dx if side == "right" else -dx, 0), textcoords="offset points",
                ha="left" if side == "right" else "right", va="center", fontsize=size, color=C["ink"],
                fontweight="bold")


# ------------------------------------------------------------------ Fig 3.7: función neoclásica + Inada
A, a = 1.0, 0.4
fig, (a1, a2) = new_fig(6.4, 2.8, ncols=2, gridspec_kw=dict(wspace=0.32))
k = np.linspace(0, 12, 400)
f = A * k ** a
a1.plot(k, f, color=C["blue"], lw=LW)
label_curve(a1, 12, 12 ** a, r"$y = f(k) = A\,k^{\alpha}$", C["blue"], dx=-2, dy=12, ha="right")
for k0, lab in [(1.0, "PMgK alta"), (8.0, "PMgK baja")]:
    y0, y1 = A * k0 ** a, A * (k0 + 1.5) ** a
    a1.plot([k0, k0 + 1.5], [y0, y0], color=C["ink2"], lw=1.1)
    a1.plot([k0 + 1.5, k0 + 1.5], [y0, y1], color=C["orange"], lw=2.2)
    a1.annotate(r"$\Delta k$", (k0 + 0.75, y0), xytext=(0, -9), textcoords="offset points", ha="center",
                fontsize=8.5, color=C["ink2"])
    a1.annotate(r"$\Delta y$: " + lab, (k0 + 1.5, (y0 + y1) / 2), xytext=(5, 0), textcoords="offset points",
                ha="left", va="center", fontsize=8.2, color=C["ink"])
econ_axes(a1, r"$k$", r"$y$", xlim=(0, 12.5), ylim=(0, 3.0))
a1.set_title("(a) Rendimientos decrecientes: el mismo\n$\\Delta k$ agrega cada vez menos producto", fontsize=9,
             pad=16)

k = np.linspace(0.05, 12, 400)
pm = a * A * k ** (a - 1)
a2.plot(k, pm, color=C["blue"], lw=LW)
a2.text(12, 1.2, r"$PMgK = f'(k) = \alpha A\, k^{\alpha-1}$", ha="right", va="center", fontsize=9.5,
        color=C["blue"], fontweight="bold")
a2.annotate("Inada: si $k \\to 0$,\n$PMgK \\to \\infty$\n(poco capital rinde muchísimo)", (0.35, 1.6),
            xytext=(22, -4), textcoords="offset points", ha="left", va="center", fontsize=7.9, color=C["ink"],
            arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=0.9, mutation_scale=7, shrinkB=3))
a2.annotate("Inada: si $k \\to \\infty$, $PMgK \\to 0$\n(la acumulación se frena)", (11, a * A * 11 ** (a - 1)),
            xytext=(12, 0.55), textcoords="data", ha="right", va="bottom", fontsize=7.9, color=C["ink"],
            arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=0.9, mutation_scale=7, shrinkB=3))
econ_axes(a2, r"$k$", r"$PMgK$", xlim=(0, 12.5), ylim=(0, 2.2))
a2.set_title("(b) La productividad marginal es positiva\ny decreciente, y cumple Inada", fontsize=9, pad=16)
save(fig, "t3a_prod_neoclasica")

# ------------------------------------------------------------------ Fig 3.8: Solow en niveles
A, a, s, nd = 1.0, 0.4, 0.3, 0.1
ks = (s * A / nd) ** (1 / (1 - a))
ys = A * ks ** a
k = np.linspace(0, 12.5, 500)
f = A * k ** a
fig, ax = new_fig(6.0, 3.6)
econ_axes(ax, r"$k$", r"$y,\ i,\ (n+\delta)k$", xlim=(0, 12.8), ylim=(0, 3.0))
ax.plot(k, f, color=C["blue"], lw=LW)
ax.plot(k, s * f, color=C["orange"], lw=LW)
ax.plot(k, nd * k, color=C["aqua"], lw=LW)
label_curve(ax, 12.5, A * 12.5 ** a, r"$f(k)$", C["blue"], dx=4, ha="left")
label_curve(ax, 12.5, s * A * 12.5 ** a, r"$s\,f(k)$", C["orange"], dx=4, ha="left")
label_curve(ax, 12.5, nd * 12.5, r"$(n+\delta)\,k$", C["aqua"], dx=4, ha="left")
ax.text(12.4, A * 12.5 ** a - 0.2, "producto per cápita", ha="right", va="top", fontsize=8, color=C["ink2"])
ax.text(12.4, s * A * 12.5 ** a - 0.08, "inversión efectiva", ha="right", va="top", fontsize=8, color=C["ink2"])
ax.text(12.4, nd * 12.4 + 0.1, "depreciación efectiva", ha="right", va="bottom", fontsize=8, color=C["ink2"],
        rotation=0)
point(ax, ks, s * ys, color=C["ink"])
point(ax, ks, ys, color=C["blue"])
vguide(ax, ks, ys, r"$k^*$")
hguide(ax, ks, ys, r"$y^*$")
bracket(ax, ks + 0.25, s * ys, ys, r"$c^* = (1-s)\,y^*$", C["ink2"])
bracket(ax, ks + 0.25, 0, s * ys, r"$i^* = s\,y^*$", C["ink2"])
# brecha a la izquierda: k' > 0
k0 = 2.0
ax.plot([k0, k0], [nd * k0, s * A * k0 ** a], color=C["green"], lw=2.4, solid_capstyle="butt")
ax.annotate(r"$\dot k > 0$: $k$ sube", (k0, (nd * k0 + s * A * k0 ** a) / 2), xytext=(2.5, 0.95), textcoords="data",
            ha="center", va="center", fontsize=9, color=C["green"], fontweight="bold",
            arrowprops=dict(arrowstyle="-|>", color=C["green"], lw=0.9, mutation_scale=7, shrinkB=2))
vguide(ax, k0, nd * k0, r"$k_0$")
k1 = 10.5
ax.plot([k1, k1], [s * A * k1 ** a, nd * k1], color=C["red"], lw=2.4, solid_capstyle="butt")
ax.annotate(r"$\dot k < 0$: $k$ baja", (k1, (nd * k1 + s * A * k1 ** a) / 2), xytext=(5, 0), textcoords="offset points",
            ha="left", va="center", fontsize=9, color=C["red"], fontweight="bold")
vguide(ax, k1, s * A * k1 ** a, r"$k_1$")
# flechas de dinámica sobre el eje
arrow(ax, 2.6, 0.12, ks - 0.5, 0.12, color=C["ink"], lw=1.6)
arrow(ax, 10.0, 0.12, ks + 0.5, 0.12, color=C["ink"], lw=1.6)
save(fig, "t3a_solow_niveles")
print("niveles", ks, ys, s * ys, (1 - s) * ys)

# ------------------------------------------------------------------ Fig 3.9: Solow en tasas
k = np.linspace(0.35, 12.5, 500)
CA = s * A * k ** (a - 1)
fig, ax = new_fig(6.2, 3.0)
econ_axes(ax, r"$k$", r"$\gamma_k$", xlim=(0, 12.8), ylim=(0, 0.42))
ax.plot(k, CA, color=C["orange"], lw=LW)
ax.axhline(nd, color=C["aqua"], lw=LW)
label_curve(ax, 0.75, s * A * 0.75 ** (a - 1), r"CA $= \dfrac{s\,f(k)}{k} = \dfrac{sA}{k^{1-\alpha}}$  (curva de ahorro)",
            C["orange"], dx=10, dy=4, ha="left")
label_curve(ax, 12.5, nd, r"CD $= n+\delta$  (curva de depreciación)", C["aqua"], dx=0, dy=9, ha="right")
label_curve(ax, 12.5, s * A * 12.5 ** (a - 1), "CA", C["orange"], dx=4, dy=0, ha="left")
point(ax, ks, nd, color=C["ink"])
vguide(ax, ks, nd, r"$k^*$")
for kk, lab in [(1.2, r"$\gamma_k$ grande"), (3.0, r"$\gamma_k$ menor")]:
    ca = s * A * kk ** (a - 1)
    ax.annotate("", xy=(kk, ca), xytext=(kk, nd),
                arrowprops=dict(arrowstyle="<|-|>", color=C["green"], lw=1.5, shrinkA=0, shrinkB=0, mutation_scale=8))
    left = kk > 2
    ax.annotate(lab, (kk, (ca + nd) / 2), xytext=(-5 if left else 5, 0), textcoords="offset points",
                ha="right" if left else "left", va="center", fontsize=8.6, color=C["green"], fontweight="bold")
    vguide(ax, kk, nd, None)
kk = 10.5
ca = s * A * kk ** (a - 1)
ax.annotate("", xy=(kk, ca), xytext=(kk, nd),
            arrowprops=dict(arrowstyle="<|-|>", color=C["red"], lw=1.5, shrinkA=0, shrinkB=0, mutation_scale=8))
ax.annotate(r"$\gamma_k < 0$", (kk, (ca + nd) / 2), xytext=(5, 0), textcoords="offset points", ha="left",
            va="center", fontsize=8.6, color=C["red"], fontweight="bold")
ax.annotate(r"$k_0$", (1.2, 0), xytext=(0, -12), textcoords="offset points", ha="center", va="top", fontsize=9.5)
ax.annotate(r"$k_0'$", (3.0, 0), xytext=(0, -12), textcoords="offset points", ha="center", va="top", fontsize=9.5)
ax.annotate(r"$k_1$", (10.5, 0), xytext=(0, -12), textcoords="offset points", ha="center", va="top", fontsize=9.5)
vguide(ax, kk, ca, None)
arrow(ax, 4.0, 0.012, ks - 0.5, 0.012, color=C["ink"], lw=1.6)
arrow(ax, 10.0, 0.012, ks + 0.5, 0.012, color=C["ink"], lw=1.6)
ax.annotate(r"$\gamma_k = \dot k/k$ = distancia vertical entre CA y CD", (5.2, 0.2), fontsize=8.8, color=C["ink"],
            ha="left")
save(fig, "t3a_solow_tasas")

# ------------------------------------------------------------------ Fig 3.10: funciones vs curvas (parcial 2023)
A, a, s, nd = 1.5, 5 / 6, 0.19, 0.175
ks = (s * A / nd) ** (1 / (1 - a))
fig, (a1, a2) = new_fig(6.4, 2.9, ncols=2, gridspec_kw=dict(wspace=0.36))
k = np.linspace(0, 40, 400)
econ_axes(a1, r"$k$", r"$i,\ (n+\delta)k$", xlim=(0, 41), ylim=(0, 7.6))
a1.plot(k, s * A * k ** a, color=C["orange"], lw=LW)
a1.plot(k, nd * k, color=C["aqua"], lw=LW)
label_curve(a1, 24, s * A * 24 ** a, r"FA $= 0{,}285\,k^{5/6}$", C["orange"], dx=6, dy=-8, ha="left", va="top")
label_curve(a1, 27, nd * 27, r"FD $= 0{,}175\,k$", C["aqua"], dx=-8, dy=6, ha="right", va="bottom")
point(a1, ks, nd * ks, color=C["ink"])
vguide(a1, ks, nd * ks, r"$k^*=18{,}66$")
a1.set_title("FUNCIONES (niveles): se cortan en $k^*$", fontsize=9, pad=16)

k = np.linspace(0.02, 40, 600)
econ_axes(a2, r"$k$", r"$\gamma_k$", xlim=(0, 41), ylim=(0.1, 0.42))
a2.plot(k, s * A * k ** (a - 1), color=C["orange"], lw=LW)
a2.axhline(nd, color=C["aqua"], lw=LW)
label_curve(a2, 3, s * A * 3 ** (a - 1), r"CA $= 0{,}285/k^{1/6}$", C["orange"], dx=6, dy=8, ha="left")
label_curve(a2, 40, nd, r"CD $= 0{,}175$", C["aqua"], dx=4, dy=0, ha="left")
point(a2, ks, nd, color=C["ink"])
vguide(a2, ks, nd, r"$k^*=18{,}66$")
a2.set_title("CURVAS (tasas): se cortan en el mismo $k^*$", fontsize=9, pad=16)
save(fig, "t3a_funciones_curvas")
print("2023", ks, s * A * ks ** a, nd * ks)
