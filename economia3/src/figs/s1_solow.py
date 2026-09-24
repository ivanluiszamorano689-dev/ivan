"""Paso a paso §1 — Solow-Swan y Harrod-Domar.

Correr desde figs/:  python3 s1_solow.py
Genera figs/out/s1_*.svg:
  s1_2022_tasas    construcción en 4 pasos del diagrama en tasas (P1 2022, δ a la mitad)
  s1_2023_niveles  construcción en 4 pasos del diagrama en niveles (P2 2023)
  s1_hd_umbral     umbral de v en Harrod-Domar (P2 2023, inciso d) + opciones sobre la recta
  s1_2024_signo    la trampa del signo del exponente (P6 2024, inciso c)
  s1_2025_tasas    construcción en 4 pasos del gráfico a completar (P8 2025, inciso c)
Todos los números salen de los enunciados (ver CLAVE_PARCIALES.md y lib/calculos_parciales.py).
"""
import os
import sys

sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403

PNG_DIR = os.environ.get("S1_PNG")  # opcional: copia PNG para revisar


def coma(v, dec=2):
    return f"{v:.{dec}f}".replace(".", ",")


def out(fig, name):
    if PNG_DIR:
        fig.savefig(os.path.join(PNG_DIR, name + ".png"), dpi=110)
    save(fig, name)


def panel_title(ax, n, text):
    ax.set_title(f"{n} · {text}", fontsize=9.2, loc="left", pad=15, color=C["ink"])


def grid4(w=6.4, h=4.5):
    fig, axs = plt.subplots(2, 2, figsize=(w, h))
    fig.subplots_adjust(wspace=0.30, hspace=0.62)
    return fig, axs.ravel()


def ghost(ax, x, y, **kw):
    """Curva ya dibujada en un paso anterior (gris claro, para que resalte lo nuevo)."""
    ax.plot(x, y, color=kw.pop("color", "#b9b7b0"), lw=kw.pop("lw", 1.5), **kw)


# =====================================================================================
# 1) P1 2022 — diagrama en tasas, δ a la mitad
# =====================================================================================
sA, a = 0.65, 3 / 7
nd0, nd1 = 0.13, 0.085
k0 = (sA / nd0) ** (1 / (1 - a))
k1 = (sA / nd1) ** (1 / (1 - a))
XL, YL = (0, 46), (0, 0.46)
k = np.linspace(0.9, 46, 500)
CA = sA / k ** (1 - a)

fig, axs = grid4()
# paso 1: ejes
ax = axs[0]
econ_axes(ax, r"$k$", r"$\gamma_k$", xlim=XL, ylim=YL)
panel_title(ax, 1, "Ejes y rótulos")
ax.text(23, 0.30, "horizontal: $k$ = capital per cápita\nvertical: $\\gamma_k$ = tasa de\ncrecimiento de $k$",
        ha="center", va="center", fontsize=8.2, color=C["ink2"], linespacing=1.45)
# paso 2: CA
ax = axs[1]
ax.plot(k, CA, color=C["orange"], lw=LW)
econ_axes(ax, r"$k$", r"$\gamma_k$", xlim=XL, ylim=YL)
panel_title(ax, 2, "Curva de ahorro (decreciente)")
label_curve(ax, 9, sA / 9 ** (1 - a), r"CA $=0{,}65/k^{4/7}$", C["orange"], dx=8, dy=10, size=8.8)
ax.text(45, 0.43, "sale de muy arriba y baja:\nrendimientos decrecientes", ha="right", va="top",
        fontsize=7.8, color=C["ink2"], linespacing=1.35)
# paso 3: CD inicial y nueva
ax = axs[2]
ghost(ax, k, CA)
ax.plot(k, nd0 + 0 * k, color=C["aqua"], lw=LW)
ax.plot(k, nd1 + 0 * k, color=C["aqua"], lw=LW, ls="--")
econ_axes(ax, r"$k$", r"$\gamma_k$", xlim=XL, ylim=YL)
panel_title(ax, 3, "Rectas de depreciación")
ax.text(45, nd0 + 0.014, r"CD $=0{,}04+0{,}09=0{,}13$", color=C["aqua"], fontsize=8.4, ha="right", va="bottom",
        fontweight="bold")
ax.text(1.5, nd1 - 0.012, "CD$'=0{,}04+0{,}045=0{,}085$\n($\\delta$ a la mitad)", color=C["aqua"], fontsize=8.2,
        ha="left", va="top", fontweight="bold", linespacing=1.3)
arrow(ax, 42, nd0 - 0.004, 42, nd1 + 0.006, C["ink2"], lw=1.2)
# paso 4: cortes
ax = axs[3]
ax.plot(k, CA, color=C["orange"], lw=LW)
ax.plot(k, nd0 + 0 * k, color=C["aqua"], lw=LW)
ax.plot(k, nd1 + 0 * k, color=C["aqua"], lw=LW, ls="--")
econ_axes(ax, r"$k$", r"$\gamma_k$", xlim=XL, ylim=YL)
panel_title(ax, 4, "Cortes = estados estacionarios")
vguide(ax, k0, nd0, coma(k0), size=8.2)
vguide(ax, k1, nd1, coma(k1), size=8.2)
hguide(ax, k0, nd0, "0,13", size=8)
hguide(ax, k1, nd1, "0,085", size=8)
point(ax, k0, nd0)
point(ax, k1, nd1)
ax.annotate("", xy=(k1 - 0.8, nd1 + 0.03), xytext=(k0 + 0.8, nd0 + 0.03),
            arrowprops=dict(arrowstyle="-|>", color=C["ink"], lw=1.2, mutation_scale=9,
                            connectionstyle="arc3,rad=-0.25"))
ax.text((k0 + k1) / 2, nd0 + 0.075, r"$k^*$ sube", ha="center", fontsize=8.2, color=C["ink"], fontweight="bold")
label_curve(ax, 6, sA / 6 ** (1 - a), "CA no cambia", C["orange"], dx=8, dy=8, size=8.2)
out(fig, "s1_2022_tasas")

# =====================================================================================
# 2) P2 2023 — diagrama en niveles
# =====================================================================================
sA2, a2, nd2, s2 = 0.285, 5 / 6, 0.175, 0.19
ks2 = (sA2 / nd2) ** (1 / (1 - a2))
h2 = nd2 * ks2
XL2, YL2 = (0, 32), (0, 5.9)
kk = np.linspace(0, 32, 400)
FA = sA2 * kk ** a2
FD = nd2 * kk

fig, axs = grid4()
ax = axs[0]
econ_axes(ax, r"$k$", r"FA, FD", xlim=XL2, ylim=YL2)
panel_title(ax, 1, "Ejes y rótulos")
ax.text(16, 3.6, "horizontal: $k$ = capital per cápita\nvertical: ahorro-inversión y\ndepreciación efectiva por trabajador",
        ha="center", va="center", fontsize=8.0, color=C["ink2"], linespacing=1.45)
ax = axs[1]
ax.plot(kk, FA, color=C["orange"], lw=LW)
econ_axes(ax, r"$k$", r"FA, FD", xlim=XL2, ylim=YL2)
panel_title(ax, 2, "Función de ahorro (cóncava)")
ax.annotate(r"FA $=0{,}285\,k^{5/6}$", (8, sA2 * 8 ** a2), xytext=(1.5, 4.4), color=C["orange"], fontsize=8.8,
            fontweight="bold", arrowprops=dict(arrowstyle="-", color=C["orange"], lw=0.8))
ax.text(31.5, 0.12, r"con $\alpha=5/6$ casi es una recta", ha="right", va="bottom", fontsize=7.8, color=C["ink2"])
ax = axs[2]
ghost(ax, kk, FA)
ax.plot(kk, FD, color=C["aqua"], lw=LW)
econ_axes(ax, r"$k$", r"FA, FD", xlim=XL2, ylim=YL2)
panel_title(ax, 3, "Función de depreciación (recta)")
label_curve(ax, 26, nd2 * 26, r"FD $=0{,}175\,k$", C["aqua"], dx=-6, dy=10, ha="right", size=8.8)
ax.text(31.5, 0.12, "sale del origen con pendiente $n+\\delta$", ha="right", va="bottom", fontsize=7.8,
        color=C["ink2"])
ax = axs[3]
ax.plot(kk, FA, color=C["orange"], lw=LW)
ax.plot(kk, FD, color=C["aqua"], lw=LW)
econ_axes(ax, r"$k$", r"FA, FD", xlim=XL2, ylim=YL2)
panel_title(ax, 4, "Corte = estado estacionario")
vguide(ax, ks2, h2, r"$k^*=18{,}66$", size=8.2)
hguide(ax, ks2, h2, "3,265", size=8)
point(ax, ks2, h2)
ax.text(0.9, 5.55, r"$y^*=\dfrac{3{,}265}{s}=\dfrac{3{,}265}{0{,}19}=17{,}18$", fontsize=8.4, color=C["ink"],
        va="top")
arrow(ax, 6, 0.28, 12.5, 0.28, C["ink2"], lw=1.2)
arrow(ax, 30.5, 0.28, 24.5, 0.28, C["ink2"], lw=1.2)
out(fig, "s1_2023_niveles")

# =====================================================================================
# 3) Harrod-Domar — umbral de v (P2 2023 d)
# =====================================================================================
s, nd, d = 0.19, 0.175, 0.13
vc, va = s / nd, s / d
fig = plt.figure(figsize=(6.3, 3.9))
gs = fig.add_gridspec(2, 1, height_ratios=[3.0, 1.55], hspace=0.12)
ax = fig.add_subplot(gs[0])
v = np.linspace(0.35, 2.6, 500)
ax.axvspan(0.0, vc, color=C["green_bg"], zorder=0)
ax.axvspan(vc, 2.6, color=C["red_bg"], zorder=0)
ax.axhline(0, color=C["ink2"], lw=0.9)
ax.plot(v, s / v - nd, color=C["blue"], lw=LW)
ax.plot(v, s / v - d, color=C["orange"], lw=1.5, ls="--")
data_axes(ax, "", "tasa de crecimiento")
ax.set_xlim(0, 2.6)
ax.set_ylim(-0.12, 0.24)
ax.tick_params(axis="x", labelbottom=False, length=0)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{100 * x:.0f} %".replace("-", "−")))
ax.plot([vc], [0], "o", color=C["blue"], ms=6.5, mec="white", mew=1.5, zorder=5)
ax.plot([va], [0], "o", color=C["orange"], ms=5.5, mec="white", mew=1.3, zorder=5)
ax.annotate(r"$v=s/(n+\delta)=1{,}0857$", (vc, 0), xytext=(-6, -14), textcoords="offset points", ha="right",
            fontsize=8.3, color=C["blue"], fontweight="bold")
ax.annotate(r"$s/\delta=1{,}46$", (va, 0), xytext=(4, 7), textcoords="offset points", ha="left",
            fontsize=8.0, color=C["orange"], fontweight="bold")
ax.text(2.55, 0.225, r"per cápita: $g_y=\dfrac{0{,}19}{v}-0{,}175$  (la del parcial)", color=C["blue"], fontsize=8.4,
        ha="right", va="top", fontweight="bold")
ax.text(2.55, 0.16, r"agregada: $g_Y=\dfrac{0{,}19}{v}-0{,}13$  (no da ninguna opción)", color=C["orange"],
        fontsize=8.0, ha="right", va="top")
ax.text(0.06, -0.035, r"$g_y>0$", fontsize=9, color=C["green"], fontweight="bold", va="top")
ax.text(1.2, -0.108, r"$g_y<0$", fontsize=9, color=C["red"], fontweight="bold", va="bottom", ha="left")
# recta de opciones
ax2 = fig.add_subplot(gs[1], sharex=ax)
ax2.set_xlim(0, 2.6)
ax2.set_ylim(-0.1, 4.8)
for sp in ("left", "top", "right"):
    ax2.spines[sp].set_visible(False)
ax2.set_yticks([])
ax2.set_xticks([0, 0.5, 1.0, vc, 1.5, 2.0, 2.5])
ax2.set_xticklabels(["0", "0,5", "1", "", "1,5", "2", "2,5"])
ax2.set_xlabel(r"$v=K/Y$", loc="right")
rows = [("i)", 4.2, "pt", C["ink3"]), ("ii)", 3.0, "open", C["green"]), ("iii)", 1.8, "closed", C["ink3"]),
        ("iv)", 0.6, "right", C["ink3"])]
for lab, yy, kind, col in rows:
    ax2.text(-0.03, yy, lab, ha="right", va="center", fontsize=8.4, color=C["ink"], fontweight="bold")
    if kind == "pt":
        ax2.plot([vc], [yy], "o", color=col, ms=5.5)
        ax2.text(vc + 0.06, yy, r"$v=1{,}085$: $g=0$, no positiva", fontsize=7.8, va="center", color=C["ink2"])
    elif kind == "open":
        ax2.plot([0, vc], [yy, yy], color=col, lw=3, clip_on=False)
        ax2.plot([0, vc], [yy, yy], "o", color=col, mfc="white", ms=5.5, mew=1.5, clip_on=False, zorder=4)
        ax2.text(vc + 0.06, yy, r"$0<v<1{,}085$: correcta", fontsize=7.8, va="center", color=C["green"],
                 fontweight="bold")
    elif kind == "closed":
        ax2.plot([0, vc], [yy, yy], color=col, lw=3, clip_on=False)
        ax2.plot([0, vc], [yy, yy], "o", color=col, ms=5.5, clip_on=False, zorder=4)
        ax2.text(vc + 0.06, yy, r"$0\leq v\leq 1{,}085$: mete los bordes",
                 fontsize=7.8, va="center", color=C["ink2"])
    else:
        ax2.plot([vc, 2.6], [yy, yy], color=col, lw=3)
        ax2.plot([vc], [yy], "o", color=col, mfc="white", ms=5.5, mew=1.5)
        ax2.text(1.75, yy + 0.25, r"$v>1{,}085$: ahí $g<0$", fontsize=7.8, va="bottom", color=C["ink2"])
ax2.axvline(vc, color=C["ink3"], lw=0.8, ls=(0, (3, 3)), ymin=0, ymax=1)
out(fig, "s1_hd_umbral")

# =====================================================================================
# 4) P6 2024 — la trampa del signo del exponente
# =====================================================================================
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.3, 2.75))
fig.subplots_adjust(wspace=0.32)
kh = np.linspace(0.03, 1.2, 400)
a1.plot(kh, 0.2 / kh ** 0.5, color=C["orange"], lw=LW)
a1.plot(kh, 0.4 + 0 * kh, color=C["aqua"], lw=LW)
econ_axes(a1, r"$\hat k$", r"$\gamma_{\hat k}$", xlim=(0, 1.2), ylim=(0, 1.0))
a1.set_title("Lo correcto", fontsize=9.2, loc="left", pad=15, color=C["green"])
label_curve(a1, 0.08, 0.2 / 0.08 ** 0.5, r"CA $=0{,}2/\hat{k}{}^{0{,}5}$", C["orange"], dx=8, dy=4, size=8.6)
a1.text(1.18, 0.42, r"CD $=0{,}4$", color=C["aqua"], fontsize=8.6, ha="right", va="bottom", fontweight="bold")
vguide(a1, 0.25, 0.4, "0,25", size=8.2)
point(a1, 0.25, 0.4)
a1.text(0.45, 0.93, "decrece y corta a CD\ndesde arriba: estable", fontsize=7.8, color=C["ink2"], va="top",
        linespacing=1.35)
kh2 = np.linspace(0.0, 5.2, 400)
a2.plot(kh2, 0.2 * kh2 ** 0.5, color=C["red"], lw=LW, ls="--")
a2.plot(kh2, 0.4 + 0 * kh2, color=C["aqua"], lw=LW)
econ_axes(a2, r"$\hat k$", r"$\gamma_{\hat k}$", xlim=(0, 5.2), ylim=(0, 1.0))
a2.set_title("Lo que dice la 1.ª opción", fontsize=9.2, loc="left", pad=15, color=C["red"])
label_curve(a2, 1.0, 0.2, r"$0{,}2/\hat{k}{}^{-0{,}5}=0{,}2\,\hat{k}{}^{0{,}5}$", C["red"], dx=2, dy=-15, size=8.4)
a2.text(0.2, 0.42, r"CD $=0{,}4$", color=C["aqua"], fontsize=8.6, ha="left", va="bottom", fontweight="bold")
vguide(a2, 4.0, 0.4, "4", size=8.2)
a2.plot([4.0], [0.4], "o", ms=6.5, color=C["red"], mec="white", mew=1.6, zorder=5)
a2.text(0.2, 0.93, "CRECE: corta desde abajo en $\\hat k=4$,\nno en 0,25 (no es una curva de Solow)",
        fontsize=7.8, color=C["ink2"], va="top", linespacing=1.35)
out(fig, "s1_2024_signo")

# =====================================================================================
# 5) P8 2025 — gráfico a completar (tasas, con tecnología)
# =====================================================================================
aa, ngd = 0.4, 0.35
sa, sb = 0.15, 0.10
ka = (sa / ngd) ** (1 / (1 - aa))
kb = (sb / ngd) ** (1 / (1 - aa))
XL5, YL5 = (0, 0.43), (0, 0.95)
kx = np.linspace(0.035, 0.43, 400)
CAa = sa * kx ** (aa - 1)
CAb = sb * kx ** (aa - 1)
top = sa * kb ** (aa - 1)  # 0,525

fig, axs = grid4()
ax = axs[0]
econ_axes(ax, r"$\hat k$", r"$\gamma_{\hat k}$", xlim=XL5, ylim=YL5)
panel_title(ax, 1, "Ejes y rótulos")
ax.text(0.215, 0.62, "horizontal: $\\hat k$ = capital por\nunidad de trabajo efectivo\nvertical: $\\gamma_{\\hat k}$ = su tasa de crecimiento",
        ha="center", va="center", fontsize=8.0, color=C["ink2"], linespacing=1.45)
ax = axs[1]
ax.plot(kx, CAa, color=C["orange"], lw=LW)
ax.plot(kx, ngd + 0 * kx, color=C["aqua"], lw=LW)
econ_axes(ax, r"$\hat k$", r"$\gamma_{\hat k}$", xlim=XL5, ylim=YL5)
panel_title(ax, 2, "Inciso a): CA y CD")
label_curve(ax, 0.075, sa * 0.075 ** (aa - 1), r"CA$_a=0{,}15/\hat{k}{}^{0{,}6}$", C["orange"], dx=8, dy=6, size=8.5)
ax.text(0.012, ngd - 0.03, r"CD $=0{,}35$", color=C["aqua"], fontsize=8.5, ha="left", va="top", fontweight="bold")
vguide(ax, ka, ngd, "0,244", size=8.2)
point(ax, ka, ngd)
ax = axs[2]
ghost(ax, kx, CAa)
ax.plot(kx, ngd + 0 * kx, color=C["aqua"], lw=LW)
ax.plot(kx, CAb, color=C["orange"], lw=LW, ls="--")
econ_axes(ax, r"$\hat k$", r"$\gamma_{\hat k}$", xlim=XL5, ylim=YL5)
panel_title(ax, 3, "Inciso b): CA baja con $s=0{,}10$")
label_curve(ax, 0.30, sb * 0.30 ** (aa - 1), r"CA$_b=0{,}10/\hat{k}{}^{0{,}6}$", C["orange"], dx=-10, dy=-14,
            size=8.5)
vguide(ax, kb, ngd, "0,124", size=8.2)
point(ax, kb, ngd)
arrow(ax, 0.30, sa * 0.30 ** (aa - 1) + 0.005, 0.30, sb * 0.30 ** (aa - 1) + 0.03, C["ink2"], lw=1.2)
ax.text(0.312, 0.275, "baja", fontsize=7.8, color=C["ink2"], va="center")
ax = axs[3]
ax.plot(kx, CAa, color=C["orange"], lw=LW)
ax.plot(kx, CAb, color=C["orange"], lw=LW, ls="--")
ax.plot(kx, ngd + 0 * kx, color=C["aqua"], lw=LW)
econ_axes(ax, r"$\hat k$", r"$\gamma_{\hat k}$", xlim=XL5, ylim=YL5)
panel_title(ax, 4, "Cortes, valores y flecha doble")
vguide(ax, kb, ngd, "0,124", size=8.2)
vguide(ax, ka, ngd, "0,244", size=8.2)
hguide(ax, kb, ngd, "0,35", size=8)
hguide(ax, kb, top, "0,525", size=8, color=C["ink3"])
point(ax, kb, ngd)
point(ax, ka, ngd)
arrow(ax, kb, ngd + 0.004, kb, top - 0.004, C["ink"], lw=1.4, both=True)
ax.annotate(r"$\gamma_{\hat k}=0{,}525-0{,}35=+0{,}175$", (kb + 0.003, (ngd + top) / 2), xytext=(0.2, 0.70),
            fontsize=8.4, color=C["ink"], fontweight="bold", va="center",
            arrowprops=dict(arrowstyle="-", color=C["ink3"], lw=0.8))
ax.text(0.425, 0.95, r"CA$_a$ (arriba) y CA$_b$ (abajo)", fontsize=7.8, color=C["orange"], ha="right", va="top")
out(fig, "s1_2025_tasas")
print("ok", coma(k0, 3), coma(k1, 3), coma(ks2, 3), coma(ka, 4), coma(kb, 4), coma(top, 3))
