"""TP3 Parte A: estructura del IDH (Argentina), índices de los diez países, tope del ingreso y Yemen.
Datos: práctica resuelta, TP3 Parte A (IDH 2023). Correr desde figs/: python3 p3_idh.py"""
from p3_util import *  # noqa: F403
from math import log

# ------------------------------------------------------------------ 1) estructura con Argentina
fig, ax = lienzo(6.7, 3.55, 10, 6.1)
hy = 5.78
for x, t in ((0.85, "① Dimensión"), (3.05, "② Indicador · dato de Argentina"), (5.5, "③ Índice (0 a 1)"),
             (8.9, "④ Agregación")):
    ax.text(x, hy, t, ha="center", va="center", fontsize=8.3, color=C["ink2"], fontweight="bold")
ax.plot([0.05, 9.95], [5.5, 5.5], color=C["rule"], lw=0.8)

filas = [  # y, dimensión, indicador, índice
    (4.75, "Vida larga\ny saludable", "Esperanza de vida: 77,4 años\nrango 20 – 85", "(77,4 − 20) / 65\n= 0,883", C["blue"], C["blue_bg"]),
    (3.35, "Conocimientos", "Años esperados: 18,8\nrango 0 – 18", "18,8 > 18 → tope\n= 1,000", C["orange"], C["orange_bg"]),
    (2.25, None, "Años promedio: 11,2\nrango 0 – 15", "11,2 / 15\n= 0,747", C["orange"], C["orange_bg"]),
    (0.85, "Nivel de vida\ndigno", "INB pc: 25.876 US$ PPA\nrango 100 – 75.000 · en ln", "ln(258,76) / ln(750)\n= 0,839", C["aqua"], C["aqua_bg"]),
]
for y, dim, ind, idx, col, bg in filas:
    if dim:
        yd = 2.8 if dim == "Conocimientos" else y
        caja(ax, 0.85, yd, 1.55, 0.95 if dim != "Conocimientos" else 1.95, dim, fc=bg, ec=col, size=8.6, weight="bold")
    caja(ax, 3.05, y, 2.45, 0.86, ind, fc="white", ec=col, size=8.1)
    caja(ax, 5.5, y, 1.75, 0.86, idx, fc=bg, ec=col, size=8.1)
    x0 = 0.85 + 1.55 / 2 if dim or True else 0
    flecha(ax, 0.85 + 0.78, y, 3.05 - 1.23, y, color=C["ink3"], lw=1.0)
    flecha(ax, 3.05 + 1.23, y, 5.5 - 0.88, y, color=C["ink3"], lw=1.0)
# tope resaltado
ax.text(5.5, 3.35 + 0.57, "truncado en 1", ha="center", va="bottom", fontsize=7.4, color=C["red"], fontweight="bold")
# educación: media aritmética
caja(ax, 7.13, 2.8, 1.1, 1.0, "media\naritmética\n= 0,873", fc=C["orange_bg"], ec=C["orange"], size=8.0, weight="bold")
flecha(ax, 6.38, 3.35, 6.58, 3.05, color=C["orange"], lw=1.1)
flecha(ax, 6.38, 2.25, 6.58, 2.55, color=C["orange"], lw=1.1)
# IDH
caja(ax, 8.9, 2.8, 2.1, 2.7, "", fc=C["gray_bg"], ec=C["ink"], lw=1.5)
ax.text(8.9, 3.75, "media\ngeométrica", ha="center", va="center", fontsize=8.3, color=C["ink2"], fontweight="bold")
ax.text(8.9, 3.0, r"$(0{,}883\cdot 0{,}873\cdot 0{,}839)^{1/3}$", ha="center", va="center", fontsize=8.4)
ax.text(8.9, 2.3, "IDH = 0,865", ha="center", va="center", fontsize=11, fontweight="bold", color=C["ink"])
ax.text(8.9, 1.8, "muy alto (≥ 0,800)", ha="center", va="center", fontsize=7.8, color=C["ink2"])
flecha(ax, 6.38, 4.75, 8.2, 4.15, color=C["blue"], lw=1.2, rad=-0.12)
flecha(ax, 7.68, 2.8, 7.85, 2.8, color=C["orange"], lw=1.2)
flecha(ax, 6.38, 0.85, 8.2, 1.45, color=C["aqua"], lw=1.2, rad=0.12)
save(fig, "p3_idh_estructura")

# ------------------------------------------------------------------ 2) los diez países (dot plot)
P = [  # país, salud, educ, ingreso, IDH, categoría
    ("Suiza", 0.985, 0.927, 1.000, 0.970), ("Australia", 0.983, 0.930, 0.962, 0.958),
    ("Estados Unidos", 0.912, 0.905, 0.997, 0.937), ("Argentina", 0.883, 0.873, 0.839, 0.865),
    ("Perú", 0.888, 0.754, 0.750, 0.795), ("Bután", 0.815, 0.560, 0.745, 0.698),
    ("El Salvador", 0.802, 0.552, 0.704, 0.678), ("Senegal", 0.749, 0.349, 0.565, 0.529),
    ("Yemen", 0.758, 0.392, 0.351, 0.470), ("Sudán del Sur", 0.578, 0.346, 0.291, 0.388)]
fig, ax = new_fig(6.6, 4.1)
n = len(P)
bands = [(0.25, 0.55, "bajo"), (0.55, 0.70, "medio"), (0.70, 0.80, "alto"), (0.80, 1.03, "muy alto")]
shade = ["#f7f6f2", "#ffffff", "#f7f6f2", "#ffffff"]
for (a, b, lab), s in zip(bands, shade):
    ax.axvspan(a, b, color=s, zorder=0)
    ax.text((a + b) / 2, n - 0.35, lab, ha="center", va="bottom", fontsize=8, color=C["ink3"], fontweight="bold")
for x in (0.55, 0.70, 0.80):
    ax.axvline(x, color=C["rule"], lw=0.9, ls=(0, (3, 3)), zorder=1)
for i, (pais, s, e, y, h) in enumerate(P):
    yy = n - 1 - i
    lo, hi = min(s, e, y), max(s, e, y)
    ax.plot([lo, hi], [yy, yy], color="#d9d7d0", lw=3.2, solid_capstyle="round", zorder=2)
    ax.plot(s, yy, "o", ms=7, color=C["blue"], mec="white", mew=1.2, zorder=4)
    ax.plot(e, yy, "s", ms=6.5, color=C["orange"], mec="white", mew=1.2, zorder=4)
    ax.plot(y, yy, "^", ms=7.5, color=C["aqua"], mec="white", mew=1.2, zorder=4)
    ax.plot([h, h], [yy - 0.33, yy + 0.33], color=C["ink"], lw=2.4, zorder=5)
    ax.text(1.045, yy, coma(h), ha="left", va="center", fontsize=8.6, fontweight="bold", color=C["ink"])
ax.set_yticks(range(n))
ax.set_yticklabels([p[0] for p in P][::-1], fontsize=8.6)
ax.tick_params(axis="y", length=0)
ax.set_xlim(0.25, 1.03)
ax.set_ylim(-0.6, n + 0.25)
ax.xaxis.set_major_formatter(fmt_coma(1))
ax.set_xticks([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax.spines["left"].set_visible(False)
ax.text(1.045, n - 0.35, "IDH", ha="left", va="bottom", fontsize=8, fontweight="bold", color=C["ink"])
ax.set_xlabel("valor del índice (0 a 1)", fontsize=8.6)
# leyenda manual
from matplotlib.lines import Line2D
hs = [Line2D([], [], marker="o", ls="", color=C["blue"], ms=7, label="salud"),
      Line2D([], [], marker="s", ls="", color=C["orange"], ms=6.5, label="educación"),
      Line2D([], [], marker="^", ls="", color=C["aqua"], ms=7.5, label="ingreso"),
      Line2D([], [], marker="|", ls="", color=C["ink"], ms=10, mew=2.4, label="IDH (media geométrica)"),
      Line2D([], [], color="#d9d7d0", lw=3.2, label="dispersión entre dimensiones")]
ax.legend(handles=hs, loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=5, fontsize=7.8, handletextpad=0.3,
          columnspacing=1.0)
save(fig, "p3_idh_paises")

# ------------------------------------------------------------------ 3) tope del ingreso + Yemen
fig, (a1, a2) = new_fig(6.6, 2.75, ncols=2, gridspec_kw=dict(width_ratios=[1.35, 1]))
fig.subplots_adjust(wspace=0.38)
x = np.linspace(100, 90000, 800)
Ii = np.minimum(1, np.log(x / 100) / log(750))
a1.plot(x, Ii, color=C["blue"], lw=LW, zorder=3)
a1.axvline(75000, color=C["ink3"], lw=0.9, ls=(0, (3, 3)))
a1.text(75000, 0.36, "tope\n75.000", ha="center", va="bottom", fontsize=7.4, color=C["ink2"],
        bbox=dict(fc="white", ec="none", pad=0.6))
pts = [("Bután", 13843, 0.745, None, None, None), ("Perú 0,750 · Bután", 14339, 0.750, 8, -12, "left"),
       ("Argentina", 25876, 0.839, 6, -11, "left"), ("EE.UU.", 73650, 0.997, -6, 7, "right"),
       ("Suiza", 81949, 1.000, 4, 7, "left")]
for nm, v, idx, dx, dy, ha in pts:
    a1.plot(v, idx, "o", ms=6, color=C["orange"], mec="white", mew=1.2, zorder=5)
    if dx is None:
        continue
    a1.annotate(f"{nm} {coma(idx if nm[0] != 'P' else 0.745)}", (v, idx), xytext=(dx, dy), textcoords="offset points", ha=ha,
                fontsize=7.4, color=C["ink"], fontweight="bold")
a1.set_xlim(0, 90000)
a1.set_ylim(0.3, 1.08)
a1.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: miles(v)))
a1.set_xticks([0, 25000, 50000, 75000])
a1.yaxis.set_major_formatter(fmt_coma(1))
data_axes(a1, "INB per cápita (US$ PPA)", "índice de ingreso")
a1.xaxis.label.set_size(8.2); a1.yaxis.label.set_size(8.2)
a1.set_title("El ln y el tope aplanan la punta", fontsize=9, pad=6)

vals = [("salud", 0.758, C["blue"]), ("educ.", 0.392, C["orange"]), ("ingreso", 0.351, C["aqua"])]
for k, (nm, v, col) in enumerate(vals):
    a2.bar(k, v, 0.62, color=col, zorder=2)
    a2.text(k, v + 0.015, coma(v), ha="center", va="bottom", fontsize=7.8, fontweight="bold")
a2.axhline(0.500, color=C["ink3"], lw=1.3, ls=(0, (4, 3)), zorder=3)
a2.axhline(0.470, color=C["ink"], lw=1.8, zorder=3)
a2.text(2.4, 0.512, "aritmética\n0,500", ha="left", va="bottom", fontsize=7.4, color=C["ink2"], linespacing=1.1)
a2.text(2.4, 0.455, "geométrica\n= IDH 0,470", ha="left", va="top", fontsize=7.4, color=C["ink"], fontweight="bold",
        linespacing=1.1)
a2.set_xlim(-0.5, 3.35)
a2.set_xticks(range(3))
a2.set_xticklabels([v[0] for v in vals], fontsize=8)
a2.set_ylim(0, 0.85)
a2.yaxis.set_major_formatter(fmt_coma(1))
data_axes(a2, "", "")
a2.set_title("Yemen: la geométrica castiga", fontsize=9, pad=6)
save(fig, "p3_idh_tope_yemen")
