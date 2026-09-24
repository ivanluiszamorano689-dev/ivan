"""Paso a paso §3 — Índices de desarrollo humano (IDH, IDH-D, pérdida, IDG).

Correr desde figs/:  python3 s3_indices.py
Genera figs/out/s3_*.svg:
  s3_arbol_idh     el cálculo del IDH como árbol, con los números de Namibia (P3 a)
  s3_mordisco      Namibia y Honduras: índices de dimensión, ajustados y la "mordida" de la desigualdad (4 pasos)
  s3_ingreso       el índice de ingreso es logarítmico: despeje del INB de Australia (P2 2023) y las opciones
  s3_escala        escala de niveles del PNUD con los siete países de los parciales (IDH e IDH-D)
Todos los números salen de los enunciados (CLAVE_PARCIALES.md y lib/calculos_parciales.py).
"""
import os
import sys
from math import log

sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403,E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle  # noqa: E402

PNG_DIR = os.environ.get("S3_PNG")  # opcional: copia PNG para revisar

DARK = {"blue": "#184f95", "orange": "#a8431b", "aqua": "#0f6e4c", "yellow": "#8a5d00",
        "violet": "#3a2d86", "red": "#a82b2a", "green": "#006100", "gray": C["ink2"]}
GHOST = "#c9c7c0"


def coma(v, dec=3):
    v = v + (5e-10 if v >= 0 else -5e-10)
    return f"{v:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def out(fig, name):
    if PNG_DIR:
        fig.savefig(os.path.join(PNG_DIR, name + ".png"), dpi=120)
    save(fig, name)


def gm(*xs):
    p = 1.0
    for x in xs:
        p *= x
    return p ** (1 / len(xs))


def canvas(w, h, W=100.0):
    fig = plt.figure(figsize=(w, h))
    ax = fig.add_axes([0, 0, 1, 1])
    H = W * h / w
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax, H


def rbox(ax, cx, cy, w, h, fc, ec, lw=1.2, r=1.3, z=2):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw, zorder=z))


def txt(ax, x, y, s, size=8.2, color=None, weight="normal", ha="center", va="center", z=5, ls=1.3):
    ax.text(x, y, s, fontsize=size, color=color or C["ink"], fontweight=weight, ha=ha, va=va, zorder=z,
            linespacing=ls)


def conn(ax, p0, p1, color=None, lw=1.2):
    """Conector vertical en codo (baja, cruza, baja) con flecha al final."""
    x0, y0 = p0
    x1, y1 = p1
    ym = (y0 + y1) / 2
    col = color or C["ink3"]
    ax.plot([x0, x0, x1], [y0, ym, ym], color=col, lw=lw, zorder=1, solid_capstyle="butt")
    ax.add_patch(FancyArrowPatch((x1, ym), (x1, y1), arrowstyle="-|>", mutation_scale=8, color=col, lw=lw,
                                 shrinkA=0, shrinkB=0, zorder=1))


# =====================================================================================
# 1) Árbol del IDH con los números de Namibia (P3 a)
# =====================================================================================
le, eys, mys, gni = 63.7, 12.6, 7.0, 9357
iv = (le - 20) / 65
iesp, iprom = eys / 18, mys / 15
ie = (iesp + iprom) / 2
ii = log(gni / 100) / log(750)
idh = gm(iv, ie, ii)

fig, ax, H = canvas(6.5, 4.55)
X = [29.6, 49.9, 70.2, 90.2]      # columnas de las cuatro hojas
BW, BH = 18.6, 7.6
NH, DH = 12.4, 10.4               # alto de las cajas "normalizar" y "dimensión"
rows = {"dat": H - 6.0, "nor": H - 21.5, "dim": H - 38.0, "idh": H - 52.5, "niv": H - 63.8}
# rótulos de nivel a la izquierda
lab = [("dat", "Datos", "del enunciado"), ("nor", "① Normalizar", "(x − mín)/(máx − mín)"),
       ("dim", "② Índices de", "dimensión"), ("idh", "③ Media", "geométrica"), ("niv", "④ Clasificar", "")]
for key, a, b in lab:
    txt(ax, 1.0, rows[key] + (1.6 if b else 0), a, size=8.3, weight="bold", ha="left", color=C["ink"])
    if b:
        txt(ax, 1.0, rows[key] - 1.9, b, size=7.3, ha="left", color=C["ink2"])
ax.plot([18.8, 18.8], [rows["niv"] - 4, H - 1.5], color=C["rule"], lw=0.8)

# hojas: datos
dat = [("Esperanza de vida", "63,7 años"), ("Años esperados", "12,6"), ("Años promedio", "7,0"),
       ("INB per cápita", "US$ 9.357")]
for x, (a, b) in zip(X, dat):
    rbox(ax, x, rows["dat"], BW, BH, C["gray_bg"], C["ink3"])
    txt(ax, x, rows["dat"] + 1.6, a, size=7.4, color=C["ink2"])
    txt(ax, x, rows["dat"] - 1.7, b, size=8.6, weight="bold")
# normalizar
nor = [(r"$\dfrac{63{,}7-20}{85-20}$", "0,6723"), (r"$\dfrac{12{,}6-0}{18-0}$", "0,7000"),
       (r"$\dfrac{7{,}0-0}{15-0}$", "0,4667"), (r"$\dfrac{\ln(9.357/100)}{\ln 750}$", "0,6856")]
for x, (f, v) in zip(X, nor):
    rbox(ax, x, rows["nor"], BW, NH, "#ffffff", C["blue"])
    txt(ax, x, rows["nor"] + 2.2, f, size=9.0)
    txt(ax, x, rows["nor"] - 3.9, "= " + v, size=8.6, weight="bold", color=DARK["blue"])
    conn(ax, (x, rows["dat"] - BH / 2), (x, rows["nor"] + NH / 2))
# dimensión
xe = (X[1] + X[2]) / 2
dims = [(X[0], "Salud", "0,6723", BW), (xe, "Educación: promedio simple",
        r"$\dfrac{0{,}7000+0{,}4667}{2}=0{,}5833$", 31), (X[3], "Ingreso", "0,6856", BW)]
for x, a, b, w in dims:
    rbox(ax, x, rows["dim"], w, DH, C["blue_bg"], C["blue"], lw=1.4)
    txt(ax, x, rows["dim"] + 2.9, a, size=7.6, color=DARK["blue"], weight="bold")
    txt(ax, x, rows["dim"] - 1.9, b, size=9.2, weight="bold")
top_n = rows["nor"] - NH / 2
top_d = rows["dim"] + DH / 2
conn(ax, (X[0], top_n), (X[0], top_d))
conn(ax, (X[3], top_n), (X[3], top_d))
conn(ax, (X[1], top_n), (xe - 4, top_d))
conn(ax, (X[2], top_n), (xe + 4, top_d))
# IDH (raíz)
xr = (X[0] + X[3]) / 2
IH = 8.6
rbox(ax, xr, rows["idh"], 60, IH, C["blue"], C["blue"], lw=1.4)
txt(ax, xr, rows["idh"] + 0.2, "IDH = (0,6723 · 0,5833 · 0,6856)" + r"$^{1/3}$" + " = 0,6454  →  0,645",
    size=9.4, color="white", weight="bold")
bot_d = rows["dim"] - DH / 2
top_i = rows["idh"] + IH / 2
for x in (X[0], xe, X[3]):
    conn(ax, (x, bot_d), (xr + (x - xr) * 0.35, top_i), color=C["blue"])
# clasificación
rbox(ax, xr, rows["niv"], 60, 6.8, C["yellow_bg"], C["yellow"])
txt(ax, xr, rows["niv"], "0,550 ≤ 0,645 < 0,700   →   desarrollo humano MEDIO", size=8.6, weight="bold",
    color=DARK["yellow"])
ax.add_patch(FancyArrowPatch((xr, rows["idh"] - IH / 2), (xr, rows["niv"] + 3.4),
                             arrowstyle="-|>", mutation_scale=8, color=C["ink3"], lw=1.2, shrinkA=0, shrinkB=0))
out(fig, "s3_arbol_idh")


# =====================================================================================
# 2) Namibia y Honduras: el "mordisco" de la desigualdad, en 4 pasos
# =====================================================================================
nam = dict(idx=[iv, ie, ii], A=[0.221, 0.25, None], aj=[iv * 0.779, ie * 0.75, 0.318])
hiv, hie, hii = (76.3 - 20) / 65, (10.1 / 18 + 6.6 / 15) / 2, log(5308 / 100) / log(750)
hon = dict(idx=[hiv, hie, hii], A=[0.133, 0.233, None], aj=[hiv * 0.867, hie * 0.767, 0.373])
for d in (nam, hon):
    d["idh"] = gm(*d["idx"])
    d["idhd"] = gm(*d["aj"])
    d["loss"] = [1 - a / i for a, i in zip(d["aj"], d["idx"])]

fig, axs = plt.subplots(2, 2, figsize=(6.5, 5.4))
fig.subplots_adjust(wspace=0.22, hspace=0.55, left=0.07, right=0.99, top=0.94, bottom=0.06)
axs = axs.ravel()
dimn = ["Salud", "Educación", "Ingreso"]
xc = np.arange(3)
bw = 0.36
cols = [C["blue"], C["orange"]]
YT = 1.13


def base(ax, n, title, xt=None, xl=None, xlim=(-0.6, 2.6)):
    ax.set_xlim(*xlim)
    ax.set_ylim(0, YT)
    ax.set_xticks(xc if xt is None else xt)
    ax.set_xticklabels(dimn if xl is None else xl, fontsize=8.2)
    ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: coma(v, 1)))
    ax.tick_params(axis="both", labelsize=7.6, length=0)
    ax.grid(axis="y", color="#ebe9e3", lw=0.8)
    ax.set_axisbelow(True)
    ax.set_title(f"{n} · {title}", fontsize=8.9, loc="left", pad=6, color=C["ink"])
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)


def legend(ax, x0=1.45, y0=1.05):
    for j, (nm, c) in enumerate([("Namibia", cols[0]), ("Honduras", cols[1])]):
        ax.add_patch(Rectangle((x0 + j * 0.9, y0 - 0.022), 0.1, 0.045, fc=c, ec="none", clip_on=False))
        ax.text(x0 + 0.14 + j * 0.9, y0, nm, fontsize=7.4, va="center", color=C["ink"])


# paso 1: ejes
ax = axs[0]
base(ax, 1, "Ejes: tres dimensiones, índice de 0 a 1")
legend(ax, x0=0.75)
ax.text(1.0, 0.5, "una barra por país en cada dimensión;\nel índice nunca pasa de 1", ha="center",
        va="center", fontsize=7.6, color=C["ink3"], linespacing=1.4)
# paso 2: índices sin ajustar
ax = axs[1]
base(ax, 2, "Índices de dimensión (sin ajustar)")
legend(ax, x0=0.75)
for j, d in enumerate((nam, hon)):
    for i in range(3):
        x = xc[i] + (j - 0.5) * bw
        ax.bar(x, d["idx"][i], bw * 0.92, color=cols[j], zorder=2)
        ax.text(x, d["idx"][i] + 0.018, coma(d["idx"][i]), ha="center", va="bottom", fontsize=6.7, color=C["ink"])
# paso 3: mordisco
ax = axs[2]
base(ax, 3, "× (1 − A): lo rayado es lo que se pierde")
for j, d in enumerate((nam, hon)):
    for i in range(3):
        x = xc[i] + (j - 0.5) * bw
        ax.bar(x, d["idx"][i], bw * 0.92, fc="white", ec=cols[j], lw=0.9, hatch="////", zorder=2)
        ax.bar(x, d["aj"][i], bw * 0.92, color=cols[j], zorder=3)
        ax.text(x, d["aj"][i] - 0.02, coma(d["aj"][i]), ha="center", va="top", fontsize=6.3, color="white",
                fontweight="bold", zorder=4, rotation=90)
        ax.text(x, d["idx"][i] + 0.018, f"−{coma(100 * d['loss'][i], 1)} %", ha="center", va="bottom",
                fontsize=6.2, color=C["ink2"], rotation=90)
# paso 4: IDH vs IDH-D
ax = axs[3]
base(ax, 4, "Media geométrica: IDH contra IDH-D", xt=[0, 1.25], xl=["Namibia", "Honduras"], xlim=(-0.5, 2.0))
for k_, (j, d) in enumerate(zip((0, 1.25), (nam, hon))):
    ax.bar(j - 0.17, d["idh"], 0.3, fc="white", ec=cols[k_], lw=1.2, hatch="////", zorder=2)
    ax.bar(j + 0.17, d["idhd"], 0.3, color=cols[k_], zorder=2)
    ax.text(j - 0.17, d["idh"] + 0.02, "IDH\n" + coma(d["idh"]), ha="center", va="bottom", fontsize=6.9,
            color=C["ink"], linespacing=1.1)
    ax.text(j + 0.17, d["idhd"] - 0.025, "IDH-D\n" + coma(d["idhd"]), ha="center", va="top", fontsize=6.9,
            color="white", fontweight="bold", linespacing=1.1, zorder=4)
    xa = j + 0.40
    ax.plot([j + 0.02, xa + 0.03], [d["idh"], d["idh"]], color=C["ink3"], lw=0.8, ls=(0, (2, 2)), zorder=1)
    ax.annotate("", xy=(xa, d["idhd"]), xytext=(xa, d["idh"]),
                arrowprops=dict(arrowstyle="-|>", color=C["ink"], lw=1.1, mutation_scale=8, shrinkA=0, shrinkB=0))
    loss = 1 - d["idhd"] / d["idh"]
    ax.text(xa + 0.04, (d["idh"] + d["idhd"]) / 2, f"pierde\n{coma(100 * loss, 1)} %", ha="left", va="center",
            fontsize=7.2, color=C["ink"], fontweight="bold", linespacing=1.1)
out(fig, "s3_mordisco")


# =====================================================================================
# 3) Índice de ingreso logarítmico: despeje del INB (Australia, P2 2023)
# =====================================================================================
fig, ax = new_fig(6.3, 3.1)
x = np.linspace(100, 75000, 600)
f = np.log(x / 100) / np.log(750)
ax.plot(x / 1000, f, color=C["blue"], lw=LW, zorder=3)
x2 = np.linspace(75000, 130000, 200)
ax.plot(x2 / 1000, np.log(x2 / 100) / np.log(750), color=C["blue"], lw=1.3, ls=(0, (2, 2)), zorder=3)
ax.axhline(1.0, color=C["ink3"], lw=0.8, zorder=1)
ax.axvline(75, color=C["ink3"], lw=0.8, ls=(0, (3, 3)), zorder=1)
ax.text(76.5, 0.06, "máximo\n75.000", fontsize=7.4, color=C["ink2"], ha="left", va="bottom", linespacing=1.1)
gA = 100 * 750 ** 0.936
ax.plot([0, gA / 1000], [0.936, 0.936], color=C["orange"], lw=1.2, ls=(0, (3, 2)), zorder=2)
ax.annotate("", xy=(gA / 1000, 0.015), xytext=(gA / 1000, 0.915),
            arrowprops=dict(arrowstyle="-|>", color=C["orange"], lw=1.3, mutation_scale=9))
ax.plot([gA / 1000], [0.936], "o", ms=7, color=C["orange"], mec="white", mew=1.5, zorder=6)
ax.text(51.5, 0.60, "Australia: índice 0,936\n" + r"INB $=100\cdot 750^{\,0{,}936}=$" + " 49.097",
        fontsize=7.9, color=DARK["orange"], fontweight="bold", ha="left", va="center", linespacing=1.35)
ax.text(1.5, 0.955, "0,936", fontsize=7.4, color=DARK["orange"], ha="left", va="bottom", fontweight="bold")
ax.text(gA / 1000 + 1.2, 0.03, "49.097", fontsize=7.4, color=DARK["orange"], ha="left", va="bottom",
        fontweight="bold")
for g, lab_, dx, dy, ha in [(9238, "c) 9.238 → 0,684", 6, -9, "left"), (25782, "a) 25.782 → 0,839", 6, -10, "left"),
                            (122607, "b) 122.607 → 1,074 (> 1)", 8, -27, "right")]:
    v = log(g / 100) / log(750)
    ax.plot([g / 1000], [v], "o", ms=6, color="white", mec=C["ink2"], mew=1.4, zorder=6)
    ax.annotate(lab_, (g / 1000, v), xytext=(dx, dy), textcoords="offset points",
                fontsize=7.4, color=C["ink2"], ha=ha, va="center")
ax.set_xlim(0, 130)
ax.set_ylim(0, 1.15)
ax.set_xticks([0, 25, 50, 75, 100, 125])
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: coma(v * 1000, 0) if v else "0"))
ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: coma(v, 1)))
data_axes(ax, "INB per cápita (US$ PPA)", "índice de ingreso")
ax.xaxis.label.set_size(8.4)
ax.yaxis.label.set_size(8.4)
ax.text(88, 0.36, r"$I_{ing}=\dfrac{\ln(\mathrm{INB}/100)}{\ln 750}$", fontsize=10.5, color=DARK["blue"])
out(fig, "s3_ingreso")


# =====================================================================================
# 4) Escala de niveles del PNUD con los siete países de los parciales
# =====================================================================================
jiv, jie, jii = (70.5 - 20) / 65, (13.4 / 18 + 9.2 / 15) / 2, log(8834 / 100) / log(750)
giv, gie, gii = (65.7 - 20) / 65, (12.5 / 18 + 8.6 / 15) / 2, log(22465 / 100) / log(750)
yem = [0.6738, 0.3595, 0.3891]
paises = [
    ("Australia", "P2 · 2023", gm(0.993, 0.925, 0.936), gm(0.966, 0.896, 0.776)),
    ("Barbados", "P6 y P7 · 2024", gm(0.886, 0.766, 0.727), None),
    ("Guyana", "P6 · 2024", gm(giv, gie, gii), gm(giv * 0.842, gie * 0.896, gii * 0.749)),
    ("Jamaica", "P7 · 2024", gm(jiv, jie, jii), gm(jiv * 0.913, jie * 0.935, jii * 0.68)),
    ("Namibia", "P3", nam["idh"], nam["idhd"]),
    ("Honduras", "P3", hon["idh"], hon["idhd"]),
    ("Yemen", "P8 · 2025", gm(*yem), gm(yem[0] * 0.733, yem[1] * 0.539, yem[2] * 0.782)),
]
fig, ax = new_fig(6.5, 3.75)
X0, X1 = 0.2, 1.0
bands = [(X0, 0.55, "DH bajo", "< 0,550", "#f4f3ef"), (0.55, 0.70, "DH medio", "0,550–0,699", "#ffffff"),
         (0.70, 0.80, "DH alto", "0,700–0,799", "#f4f3ef"), (0.80, X1, "DH muy alto", "≥ 0,800", "#ffffff")]
n = len(paises)
for a, b, t, r_, fc in bands:
    ax.axvspan(a, b, color=fc, zorder=0)
    ax.text((a + b) / 2, n + 0.05, t, ha="center", va="bottom", fontsize=7.9, color=C["ink"], fontweight="bold")
    ax.text((a + b) / 2, n - 0.05, r_, ha="center", va="top", fontsize=6.9, color=C["ink2"])
for c in (0.55, 0.70, 0.80):
    ax.axvline(c, color=C["ink3"], lw=0.9, ls=(0, (3, 3)), zorder=1)
for i, (nm, src, h, hd) in enumerate(paises):
    y = n - 1 - i - 0.55
    if hd is not None:
        ax.plot([hd, h], [y, y], color=GHOST, lw=5, solid_capstyle="butt", zorder=2)
        ax.plot([hd], [y], "o", ms=8, color="white", mec=C["orange"], mew=2.0, zorder=4)
        ax.text(hd - 0.013, y, coma(hd), ha="right", va="center", fontsize=7.3, color=DARK["orange"])
        loss = 1 - hd / h
        ax.text((h + hd) / 2, y + 0.26, f"pierde {coma(100 * loss, 1)} %", ha="center", va="bottom", fontsize=6.7,
                color=C["ink2"], zorder=3, bbox=dict(fc="white", ec="none", pad=0.6, alpha=0.9))
    ax.plot([h], [y], "o", ms=8, color=C["blue"], mec="white", mew=1.4, zorder=5)
    ax.text(h + 0.013, y, coma(h), ha="left", va="center", fontsize=7.3, color=DARK["blue"], fontweight="bold")
ax.set_yticks([n - 1 - i - 0.55 for i in range(n)])
ax.set_yticklabels([f"{p[0]}  ({p[1]})" for p in paises], fontsize=7.8)
ax.tick_params(axis="y", length=0)
ax.set_ylim(-1.0, n + 0.75)
ax.set_xlim(X0, X1)
ax.set_xticks([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: coma(v, 1)))
ax.tick_params(axis="x", labelsize=7.4)
for s_ in ("left", "top", "right"):
    ax.spines[s_].set_visible(False)
ax.axhline(n - 0.3, color=C["rule"], lw=0.8)
ax.plot([0.215], [-1.95], "o", ms=7, color=C["blue"], mec="white", mew=1.2, clip_on=False)
ax.text(0.228, -1.95, "IDH: fija el nivel", va="center", fontsize=7.4, color=C["ink"])
ax.plot([0.40], [-1.95], "o", ms=7, color="white", mec=C["orange"], mew=1.8, clip_on=False)
ax.text(0.413, -1.95, "IDH-D: lo que queda después de descontar la desigualdad", va="center", fontsize=7.4,
        color=C["ink"])
out(fig, "s3_escala")
print("ok")
