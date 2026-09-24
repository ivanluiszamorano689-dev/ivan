"""Paso a paso §2 — PBI, tipo de cambio, PPA y tasas de crecimiento.

Correr desde figs/:  python3 s2_pbi.py
Genera figs/out/s2_*.svg:
  s2_valuacion   matriz de valuación: cantidades de cada país × precios de cada país (P1 2022 y P2 2023)
  s2_barras      PBI a TC de mercado vs a PPA, construido en 4 pasos (P1 2022 y P2 2023)
  s2_ucrania     PBI pc indexado 2018 = 100: trayectoria real vs tasa media constante, en 4 pasos (P6 2024)
  s2_rusia       ídem para Rusia y EEUU, versión final (P7 2024)
  s2_bigmac      índice Big Mac de julio de 2024, barras divergentes en 4 pasos (P8 2025)
Todos los números salen de los enunciados (ver CLAVE_PARCIALES.md y lib/calculos_parciales.py).
"""
import os
import sys

sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403
from matplotlib.patches import FancyBboxPatch  # noqa: E402
from matplotlib.ticker import FixedLocator, NullLocator  # noqa: E402

PNG_DIR = os.environ.get("S2_PNG")  # opcional: copia PNG para revisar


def coma(v, dec=2):
    s = f"{v:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s.replace("-", "−")


def out(fig, name):
    if PNG_DIR:
        fig.savefig(os.path.join(PNG_DIR, name + ".png"), dpi=110)
    save(fig, name)


def panel_title(ax, n, text, pad=12):
    ax.set_title(f"{n} · {text}", fontsize=9.2, loc="left", pad=pad, color=C["ink"])


GHOST = "#c9c7c0"

# =====================================================================================
# 1) Matriz de valuación (P1 2022 y P2 2023)
# =====================================================================================


def box(ax, x, y, w, h, fc, ec, lw=1.0, ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=1.0", fc=fc, ec=ec, lw=lw,
                                ls=ls, zorder=2))


COLX = [0, 21.5, 48.5, 77.5]  # inicio de: rótulo de fila, col ①, col ②, col ③
COLW = [20, 25.5, 25.5, 22.5]
RH, GAP, BLOCK = 9.0, 2.0, 33.0


def matriz(ax, top, d):
    """Un bloque de la matriz de valuación; 'top' es el borde superior del bloque."""
    ax.text(0, top, d["titulo"], fontsize=8.8, fontweight="bold", color=C["ink"], va="top")
    ax.text(100, top - 0.2, d["tcm"], fontsize=7.4, color=C["ink2"], va="top", ha="right")
    hy = top - 7.2
    heads = [f"Cantidades de…", f"① × precios de\n{d['loc']} (en $)", f"② × precios de\n{d['base']} (en US$)",
             "③ = ① ÷ ②\nTC PPA"]
    for j, t in enumerate(heads):
        ax.text(COLX[j] + COLW[j] / 2, hy, t, ha="center", va="center", fontsize=7.3, color=C["ink2"],
                fontweight="bold", linespacing=1.2)
    rows = [
        (d["loc"], d["qloc"], C["orange"], C["orange_bg"], d["loc_loc"], d["loc_base"], d["ppa_loc"], (True, False)),
        (d["base"], d["qbase"], C["blue"], C["blue_bg"], d["base_loc"], d["base_base"], d["ppa_base"], (False, True)),
    ]
    for i, (lab, q, col, colbg, c1, c2, c3, diag) in enumerate(rows):
        y = top - 11.5 - RH - i * (RH + GAP)
        box(ax, COLX[0], y, COLW[0], RH, colbg, col, lw=1.1)
        ax.text(COLX[0] + COLW[0] / 2, y + RH * 0.68, lab, fontsize=7.8, fontweight="bold", color=col,
                va="center", ha="center")
        ax.text(COLX[0] + COLW[0] / 2, y + RH * 0.3, q, fontsize=7.1, color=C["ink"], va="center", ha="center")
        for j, (txt, is_diag) in enumerate(zip([c1, c2], diag)):
            x = COLX[j + 1]
            if is_diag:
                box(ax, x, y, COLW[j + 1], RH, colbg, col, lw=1.6)
            else:
                box(ax, x, y, COLW[j + 1], RH, "white", C["ink3"], lw=0.9, ls=(0, (3, 2)))
            ax.text(x + COLW[j + 1] / 2, y + RH * 0.68, txt[0], ha="center", va="center", fontsize=7.2,
                    color=C["ink2"])
            ax.text(x + COLW[j + 1] / 2, y + RH * 0.3, txt[1], ha="center", va="center", fontsize=7.9,
                    color=col if is_diag else C["ink"], fontweight="bold")
        x = COLX[3]
        box(ax, x, y, COLW[3], RH, C["gray_bg"], C["ink2"], lw=1.0)
        ax.text(x + COLW[3] / 2, y + RH * 0.68, c3[0], ha="center", va="center", fontsize=7.2, color=C["ink2"])
        ax.text(x + COLW[3] / 2, y + RH * 0.3, c3[1], ha="center", va="center", fontsize=8.1,
                color=C["ink"], fontweight="bold")
        ax.annotate("", xy=(COLX[3] - 0.3, y + RH / 2), xytext=(COLX[2] + COLW[2] + 0.3, y + RH / 2),
                    arrowprops=dict(arrowstyle="-|>", color=C["ink3"], lw=1.0, mutation_scale=8), zorder=1)


P1 = dict(
    titulo="P1 · 2022 — Argensur (pesos) y Norte Unidos (dólares)",
    loc="Argensur", base="Norte Unidos",
    qloc="50 tablets · 800 tortas", qbase="200 tablets · 3.200 tortas",
    loc_loc=("50·12.000 + 800·125", "$ 700.000 (su PBI)"),
    loc_base=("50·300 + 800·10", "US$ 23.000"),
    ppa_loc=("700.000 ÷ 23.000", "30,43"),
    tcm="(TCm = 12.000 ÷ 300 = 40: sólo el transable)",
    base_loc=("200·12.000 + 3.200·125", "$ 2.800.000"),
    base_base=("200·300 + 3.200·10", "US$ 92.000 (su PBI)"),
    ppa_base=("2.800.000 ÷ 92.000", "30,43  ✓"),
)
P2 = dict(
    titulo="P2 · 2023 — Ciudad Pesos (pesos) y Dolar City (dólares)",
    loc="Ciudad Pesos", base="Dolar City",
    qloc="25 pendrives · 200 cortes", qbase="30 pendrives · 240 cortes",
    loc_loc=("25·2.500 + 200·2.000", "$ 462.500 (su PBI)"),
    loc_base=("25·100 + 200·200", "US$ 42.500"),
    ppa_loc=("462.500 ÷ 42.500", "10,88"),
    tcm="(TCm = 2.500 ÷ 100 = 25: sólo el transable)",
    base_loc=("30·2.500 + 240·2.000", "$ 555.000"),
    base_base=("30·100 + 240·200", "US$ 51.000 (su PBI)"),
    ppa_base=("555.000 ÷ 51.000", "10,88  ✓"),
)

YTOT = 2 * BLOCK + 3.5
fig, ax = plt.subplots(figsize=(6.8, 6.8 * YTOT / 100))
fig.subplots_adjust(0, 0, 1, 1)
ax.set_xlim(0, 100)
ax.set_ylim(0, YTOT)
ax.axis("off")
matriz(ax, YTOT, P1)
ax.plot([0, 100], [BLOCK + 1.6, BLOCK + 1.6], color=C["rule"], lw=0.9)
matriz(ax, BLOCK, P2)
out(fig, "s2_valuacion")

# =====================================================================================
# 2) PBI a TCm vs PPA, en 4 pasos (P1 2022 y P2 2023)
# =====================================================================================
grupos = [
    dict(nom="P1 · 2022", ticks=["NU", "Arg.\nTCm", "Arg.\nPPA"], pbase=92.0, tcm=17.5, ppa=23.0,
         r_tcm="5,26", r_ppa="4"),
    dict(nom="P2 · 2023", ticks=["DC", "CP\nTCm", "CP\nPPA"], pbase=51.0, tcm=18.5, ppa=42.5,
         r_tcm="2,76", r_ppa="1,2"),
]
W = 0.78
X = {0: [0, 1, 2], 1: [3.6, 4.6, 5.6]}  # posiciones: base, otro a TCm, otro a PPA


def ejes_barras(ax):
    ax.set_xlim(-0.8, 6.3)
    ax.set_ylim(0, 108)
    data_axes(ax, "", "")
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_yticklabels(["0", "25.000", "50.000", "75.000", "100.000"])
    ax.tick_params(axis="y", labelsize=7.2)
    ax.set_xticks([X[g][k] for g in (0, 1) for k in range(3)])
    ax.set_xticklabels(grupos[0]["ticks"] + grupos[1]["ticks"], fontsize=7.3, linespacing=1.1)
    ax.tick_params(axis="x", length=0, pad=3)
    ax.text(-0.8, 110, "PBI en US$", fontsize=7.4, color=C["ink2"], ha="left", va="bottom")
    for gi, g in enumerate(grupos):
        ax.text(X[gi][1], -24, g["nom"], ha="center", va="top", fontsize=7.4, color=C["ink"],
                fontweight="bold")


def barra(ax, x, h, kind, lab=None, dy=2.0):
    if kind == "base":
        ax.bar(x, h, W, color=C["blue"], zorder=3)
    elif kind == "tcm":
        ax.bar(x, h, W, color="white", edgecolor=C["orange"], hatch="////", lw=1.2, zorder=3)
    elif kind == "ppa":
        ax.bar(x, h, W, color=C["orange"], zorder=3)
    elif kind == "ghost":
        ax.bar(x, h, W, color="#e9e7e1", zorder=3)
    if lab:
        ax.text(x, h + dy, lab, ha="center", va="bottom", fontsize=7.5, color=C["ink"], fontweight="bold")


fig, axs = plt.subplots(2, 2, figsize=(6.5, 5.5))
fig.subplots_adjust(left=0.11, wspace=0.34, hspace=0.78)
axs = axs.ravel()
# paso 1
ax = axs[0]
ejes_barras(ax)
panel_title(ax, 1, "Ejes: todo en la misma moneda", pad=16)
ax.text(2.8, 60, "Para comparar, los dos PBI tienen que\nestar en dólares. El del país base ya\nestá; "
        "el otro se convierte:\nPBI en $ ÷ TC (de mercado o PPA)", ha="center", va="center", fontsize=7.4,
        color=C["ink2"], linespacing=1.45)
# paso 2
ax = axs[1]
ejes_barras(ax)
panel_title(ax, 2, "El PBI del país base (ya en US$)", pad=16)
for gi, g in enumerate(grupos):
    barra(ax, X[gi][0], g["pbase"], "base", coma(g["pbase"] * 1000, 0))
# paso 3
ax = axs[2]
ejes_barras(ax)
panel_title(ax, 3, "El otro país a TC de mercado", pad=16)
for gi, g in enumerate(grupos):
    barra(ax, X[gi][0], g["pbase"], "ghost")
    barra(ax, X[gi][1], g["tcm"], "tcm", coma(g["tcm"] * 1000, 0))
    ax.text(X[gi][1] + (0.35 if gi == 0 else 0), 100, f"brecha {g['r_tcm']}×", ha="center", va="center",
            fontsize=7.8, color=C["red"], fontweight="bold")
# paso 4
ax = axs[3]
ejes_barras(ax)
panel_title(ax, 4, "…y a PPA: la brecha se achica", pad=16)
for gi, g in enumerate(grupos):
    barra(ax, X[gi][0], g["pbase"], "base")
    barra(ax, X[gi][1], g["tcm"], "tcm")
    barra(ax, X[gi][2], g["ppa"], "ppa", coma(g["ppa"] * 1000, 0))
    ax.text(X[gi][1] + (0.35 if gi == 0 else 0), 100, f"{g['r_tcm']}× → {g['r_ppa']}×", ha="center",
            va="center", fontsize=7.8, color=C["green"], fontweight="bold")
out(fig, "s2_barras")

# =====================================================================================
# 3) Ucrania y EEUU: PBI pc indexado, trayectoria real vs tasa media constante (P6 2024)
# =====================================================================================
YRS = np.arange(2018, 2024)
UCR = np.array([3097, 3661, 3752, 4828, 4576, 5181])
USA = np.array([63201, 65548, 64317, 71056, 77247, 81695])
RUS = np.array([11212, 11448, 10108, 12522, 15445, 13817])


def idx(s):
    return 100 * s / s[0]


def gmed(s):
    return (s[-1] / s[0]) ** (1 / 5) - 1


def ejes_idx(ax, ylim=(85, 185), ticks=(90, 100, 120, 140, 160, 180)):
    ax.set_yscale("log")
    ax.set_ylim(*ylim)
    ax.set_xlim(2017.7, 2023.9)
    data_axes(ax, "", "")
    ax.yaxis.set_major_locator(FixedLocator(ticks))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.set_yticklabels([str(t) for t in ticks])
    ax.set_xticks(YRS)
    ax.set_xticklabels([str(y) for y in YRS])
    ax.tick_params(labelsize=7.6)
    ax.text(2017.55, ylim[1] * 1.02, "índice (2018 = 100), escala log", fontsize=7.4, color=C["ink2"], ha="left",
            va="bottom")


def const_path(s):
    g = gmed(s)
    return 100 * (1 + g) ** (YRS - YRS[0])


fig, axs = plt.subplots(2, 2, figsize=(6.5, 5.3))
fig.subplots_adjust(wspace=0.2, hspace=0.62)
axs = axs.ravel()
iu, ie = idx(UCR), idx(USA)
cu, ce = const_path(UCR), const_path(USA)
# paso 1
ax = axs[0]
ejes_idx(ax)
panel_title(ax, 1, "Ejes: años e índice 2018 = 100", pad=16)
ax.text(2020.8, 138, "índice = valor del año ÷ valor 2018 × 100\n(así los dos países arrancan en 100)\n\n"
        "escala log: crecer a tasa constante\nse ve como una línea recta", ha="center", va="center",
        fontsize=7.4, color=C["ink2"], linespacing=1.4)
# paso 2
ax = axs[1]
ejes_idx(ax)
panel_title(ax, 2, "Trayectorias reales (datos)", pad=16)
ax.plot(YRS, iu, "-o", color=C["orange"], lw=LW, ms=3.8)
ax.plot(YRS, ie, "-o", color=C["blue"], lw=LW, ms=3.8)
ax.text(2018.1, 172, "Ucrania (US$ corrientes = TCm)", color=C["orange"], fontsize=7.6, fontweight="bold",
        ha="left", va="center")
ax.text(2021.3, 104, "EEUU", color=C["blue"], fontsize=7.8, fontweight="bold", ha="left", va="center")
# paso 3
ax = axs[2]
ejes_idx(ax)
panel_title(ax, 3, "Tasa media: recta entre extremos", pad=16)
ax.plot(YRS, iu, "-", color=GHOST, lw=1.5)
ax.plot(YRS, ie, "-", color=GHOST, lw=1.5)
ax.plot(YRS, cu, "--", color=C["orange"], lw=LW)
ax.plot(YRS, ce, "--", color=C["blue"], lw=LW)
for s, c in ((cu, C["orange"]), (ce, C["blue"])):
    ax.plot([YRS[0], YRS[-1]], [s[0], s[-1]], "o", color=c, ms=5, mec="white", mew=1.3, zorder=5)
ax.text(2020.1, 146, "×1,1084 por año", color=C["orange"], fontsize=7.6, fontweight="bold", ha="right",
        rotation=0)
ax.text(2021.2, 107, "×1,0527 por año", color=C["blue"], fontsize=7.6, fontweight="bold", ha="left")
for k in range(5):
    ax.annotate("", xy=(2019 + k - 0.06, 90), xytext=(2018 + k + 0.06, 90),
                arrowprops=dict(arrowstyle="-|>", color=C["ink3"], lw=0.8, mutation_scale=6))
    ax.text(2018.5 + k, 91.2, f"{k + 1}", fontsize=6.8, color=C["ink2"], ha="center", va="bottom")
ax.text(2023.0, 96.5, "5 períodos", fontsize=7.0, color=C["ink2"], ha="right", va="bottom")
# paso 4
ax = axs[3]
ejes_idx(ax)
panel_title(ax, 4, "Valores y el salto del inciso a", pad=16)
ax.plot(YRS, iu, "-o", color=C["orange"], lw=LW, ms=3.5)
ax.plot(YRS, ie, "-o", color=C["blue"], lw=LW, ms=3.5)
ax.plot(YRS, cu, "--", color=C["orange"], lw=1.2, alpha=0.8)
ax.plot(YRS, ce, "--", color=C["blue"], lw=1.2, alpha=0.8)
ax.text(2023.1, iu[-1] * 1.045, "167,3", fontsize=7.8, fontweight="bold", color=C["orange"], ha="center",
        va="bottom")
ax.text(2023.1, ie[-1] * 0.945, "129,3", fontsize=7.8, fontweight="bold", color=C["blue"], ha="center",
        va="top")
ax.text(2018.1, 176, "tasa media: Ucrania 10,84 %,\nEEUU 5,27 % anual", fontsize=7.3, color=C["ink"],
        ha="left", va="top", linespacing=1.3)
ax.annotate("", xy=(2021, iu[3]), xytext=(2020, iu[2]),
            arrowprops=dict(arrowstyle="-|>", color=C["ink"], lw=1.3, mutation_scale=9,
                            connectionstyle="arc3,rad=0.35"), zorder=6)
ax.text(2020.25, 140, "a) +28,68 %", fontsize=7.8, color=C["ink"], fontweight="bold", ha="right")
out(fig, "s2_ucrania")

# =====================================================================================
# 4) Rusia y EEUU (P7 2024) — versión final
# =====================================================================================
ir, cr = idx(RUS), const_path(RUS)
fig, ax = plt.subplots(figsize=(5.8, 3.3))
ejes_idx(ax, ylim=(84, 150), ticks=(90, 100, 110, 120, 130, 140))
ax.plot(YRS, ir, "-o", color=C["orange"], lw=LW, ms=4)
ax.plot(YRS, ie, "-o", color=C["blue"], lw=LW, ms=4)
ax.plot(YRS, cr, "--", color=C["orange"], lw=1.4)
ax.plot(YRS, ce, "--", color=C["blue"], lw=1.4)
ax.text(2023.12, ir[-1], "123,2  Rusia\n4,27 % anual", fontsize=7.8, color=C["orange"], fontweight="bold",
        va="top", ha="left", linespacing=1.3)
ax.text(2023.12, ie[-1] + 0.5, "129,3  EEUU\n5,27 % anual", fontsize=7.8, color=C["blue"], fontweight="bold",
        va="bottom", ha="left", linespacing=1.3)
ax.annotate("", xy=(2021, ir[3]), xytext=(2020, ir[2]),
            arrowprops=dict(arrowstyle="-|>", color=C["ink"], lw=1.3, mutation_scale=9,
                            connectionstyle="arc3,rad=0.3"), zorder=6)
ax.text(2021.12, 101.5, "a) +23,88 %", fontsize=7.8, color=C["ink"], fontweight="bold", ha="left")
ax.text(2019.1, 87.2, "2020: cae 11,71 %", fontsize=7.4, color=C["ink2"], ha="left")
ax.text(2022.05, 143, "2022→2023: cae 10,54 %", fontsize=7.4, color=C["ink2"], ha="center")
ax.set_xlim(2017.7, 2024.25)
out(fig, "s2_rusia")

# =====================================================================================
# 5) Índice Big Mac, julio de 2024 (P8 2025) — barras divergentes en 4 pasos
# =====================================================================================
PUS = 5.69
BM = [("Emiratos Árabes", 18, 3.67), ("Australia", 7.75, 1.53), ("Azerbaiyán", 6.15, 1.70),
      ("Bahrein", 1.7, 0.38)]
names = [b[0] for b in BM]
usd = np.array([p / t for _, p, t in BM])
ppa = np.array([p / PUS for _, p, _ in BM])
tcm = np.array([t for *_, t in BM])
pct = 100 * (ppa / tcm - 1)
ypos = np.arange(len(BM))[::-1]

fig, axs = plt.subplots(2, 2, figsize=(6.5, 4.9))
fig.subplots_adjust(wspace=0.55, hspace=0.62)
axs = axs.ravel()


def ejes_pct(ax, labels=True):
    ax.set_xlim(-45, 25)
    ax.set_ylim(-0.7, 3.7)
    ax.axvline(0, color=C["ink2"], lw=1.0, zorder=2)
    ax.set_yticks(ypos)
    ax.set_yticklabels(names if labels else [""] * 4, fontsize=7.6)
    ax.tick_params(axis="y", length=0)
    ax.set_xticks([-40, -30, -20, -10, 0, 10, 20])
    ax.set_xticklabels(["−40 %", "−30", "−20", "−10", "0", "+10", "+20 %"], fontsize=7.2)
    for sp in ("left", "top", "right"):
        ax.spines[sp].set_visible(False)
    ax.grid(axis="x", color="#ebe9e3", lw=0.8)
    ax.set_axisbelow(True)


# paso 1
ax = axs[0]
ejes_pct(ax)
panel_title(ax, 1, "Ejes: 0 = se cumple la PPA")
ax.axvspan(-45, 0, color=C["orange_bg"], zorder=0)
ax.axvspan(0, 25, color=C["blue_bg"], zorder=0)
ax.text(-22, 3.45, "infravaluada\n(BM barata en US$)", ha="center", va="top", fontsize=7.2, color=C["orange"],
        fontweight="bold", linespacing=1.25)
ax.text(12.5, 3.45, "sobre-\nvaluada\n(cara)", ha="center", va="top", fontsize=7.2, color=C["blue"],
        fontweight="bold", linespacing=1.25)
ax.text(-22, 1.5, "% = TC PPA ÷ TCm − 1", ha="center", va="center", fontsize=7.2, color=C["ink2"])
# paso 2
ax = axs[1]
ax.set_xlim(3.2, 6.1)
ax.set_ylim(-0.7, 3.7)
ax.axvline(PUS, color=C["blue"], lw=1.6, zorder=2)
for y, u in zip(ypos, usd):
    ax.plot([u, PUS], [y, y], color=C["orange"], lw=1.6, zorder=3)
    ax.plot([u], [y], "o", color=C["orange"], ms=6, mec="white", mew=1.3, zorder=4)
    ax.text(u - 0.07, y, coma(u), ha="right", va="center", fontsize=7.6, color=C["ink"], fontweight="bold")
ax.text(PUS + 0.05, 3.55, "EEUU\n5,69", ha="left", va="top", fontsize=7.4, color=C["blue"], fontweight="bold",
        linespacing=1.2)
ax.set_yticks(ypos)
ax.set_yticklabels([""] * 4)
ax.tick_params(axis="y", length=0)
ax.set_xticks([3.5, 4, 4.5, 5, 5.5, 6])
ax.set_xticklabels(["3,5", "4", "4,5", "5", "5,5", "6 US$"], fontsize=7.2)
for sp in ("left", "top", "right"):
    ax.spines[sp].set_visible(False)
panel_title(ax, 2, "Precio en US$ = P local ÷ TCm")
# paso 3
ax = axs[2]
ejes_pct(ax)
panel_title(ax, 3, "Barras: (US$ ÷ 5,69) − 1")
ax.barh(ypos, pct, 0.56, color=C["orange"], zorder=3)
for y, u, p in zip(ypos, usd, pct):
    ax.text(3, y, f"{coma(u)} ÷ 5,69 − 1", ha="left", va="center", fontsize=7.0, color=C["ink2"])
# paso 4
ax = axs[3]
ejes_pct(ax, labels=False)
panel_title(ax, 4, "Valores e interpretación")
cols = [C["orange"]] * 4
ax.barh(ypos, pct, 0.56, color=cols, zorder=3)
for y, p in zip(ypos, pct):
    ax.text(p - 1.0, y, coma(p, 1) + " %", ha="right", va="center", fontsize=7.6, color=C["ink"],
            fontweight="bold")
ax.text(1.5, ypos[1], "Australia: 5,07 < 5,69\n→ más barata", ha="left", va="center", fontsize=7.0,
        color=C["ink"], linespacing=1.2)
ax.text(1.5, ypos[3], "Bahrein: 0,299 < 0,38\n→ infravaloración", ha="left", va="center", fontsize=7.0,
        color=C["ink"], linespacing=1.2)
out(fig, "s2_bigmac")
