"""Tema 2.4: estructura del IDH, índice de ingreso en logaritmos, media geométrica, escala del IDH."""
from math import log

from t2_util import *

DIM = {"s": (C["blue"], C["blue_bg"]), "e": (C["orange"], C["orange_bg"]), "i": (C["aqua"], C["aqua_bg"])}

# ---------------------------------------------------------------- Figura 2.9
W, H = 6.8, 3.25
fig, ax = canvas(W, H)
hy = 3.08
for x, t in ((0.78, "3 dimensiones"), (2.78, "4 indicadores [mín – máx]"), (4.83, "índices de dimensión (0 a 1)"),
             (6.2, "índice final")):
    txt(ax, x, hy, t, size=8.4, weight="bold", color=C["ink2"])
rows = {"ev": (2.28, 0.5), "ae": (1.58, 0.5), "ap": (1.02, 0.5), "inb": (0.22, 0.5)}
# columna 1: dimensiones
c1x, c1w = 0.05, 1.46
for key, (y, hh), name, sub in (("s", (2.28, 0.5), "Salud", "vida larga y saludable"),
                                ("e", (1.02, 1.06), "Educación", "adquirir conocimientos"),
                                ("i", (0.22, 0.5), "Nivel de vida", "vida digna")):
    c, cb = DIM[key]
    rbox(ax, c1x, y, c1w, hh, fc=cb, ec=c, lw=1.4)
    txt(ax, c1x + c1w / 2, y + hh / 2 + 0.09, name, size=9.4, weight="bold")
    txt(ax, c1x + c1w / 2, y + hh / 2 - 0.12, sub, size=7.6, color=C["ink2"])
# columna 2: indicadores
c2x, c2w = 1.78, 2.0
ind = [("ev", "s", "Esperanza de vida al nacer", "[20 – 85 años]"),
       ("ae", "e", "Años esperados de escolaridad", "[0 – 18]"),
       ("ap", "e", "Años promedio de escolaridad", "(25 años y más) [0 – 15]"),
       ("inb", "i", "INB per cápita (US\\$ PPA)", "[100 – 75.000]")]
for key, d, a, b in ind:
    y, hh = rows[key]
    c, cb = DIM[d]
    rbox(ax, c2x, y, c2w, hh - 0.06, fc="white", ec=c, lw=1.3)
    txt(ax, c2x + c2w / 2, y + (hh - 0.06) / 2 + 0.09, a, size=8.1, weight="bold")
    txt(ax, c2x + c2w / 2, y + (hh - 0.06) / 2 - 0.11, b, size=7.6, color=C["ink2"])
    arr(ax, c1x + c1w, y + (hh - 0.06) / 2, c2x, y + (hh - 0.06) / 2, c, lw=1.2, ms=8)
# columna 3: índices
c3x, c3w = 4.05, 1.58
idx_boxes = [("s", 2.28, 0.44, r"$I_{salud}=\dfrac{EV-20}{85-20}$", "normalizar"),
             ("e", 1.02, 1.0, r"$I_{educ}=\dfrac{I_{AE}+I_{AP}}{2}$", "media aritmética\nde los dos índices"),
             ("i", 0.22, 0.44, r"$I_{ing}=\dfrac{\ln x-\ln 100}{\ln 75.000-\ln 100}$", "en logaritmos")]
for d, y, hh, f, note in idx_boxes:
    c, cb = DIM[d]
    rbox(ax, c3x, y, c3w, hh, fc=cb, ec=c, lw=1.3)
    if d == "e":
        txt(ax, c3x + c3w / 2, y + hh / 2 + 0.16, f, size=9.2)
        txt(ax, c3x + c3w / 2, y + hh / 2 - 0.25, note, size=7.4, color=C[{"s": "blue", "e": "orange", "i": "aqua"}[d]],
            weight="bold")
    else:
        txt(ax, c3x + c3w / 2, y + hh / 2, f, size=8.4 if d == "i" else 9.2)
# flechas indicador -> índice
for key in ("ev", "inb"):
    y, hh = rows[key]
    d = "s" if key == "ev" else "i"
    arr(ax, c2x + c2w, y + (hh - 0.06) / 2, c3x, y + (hh - 0.06) / 2, DIM[d][0], lw=1.2, ms=8)
for key in ("ae", "ap"):
    y, hh = rows[key]
    arr(ax, c2x + c2w, y + (hh - 0.06) / 2, c3x, 1.52 + (0.18 if key == "ae" else -0.02), DIM["e"][0], lw=1.2, ms=8)
txt(ax, 3.92, 0.12, "en ln: el ingreso rinde menos a más ingreso", size=6.9, color=C["aqua"], ha="right",
    weight="bold")
# columna 4: IDH
c4x, c4w = 5.88, 0.86
rbox(ax, c4x, 0.22, c4w, 2.5, fc=C["violet_bg"], ec=C["violet"], lw=1.6)
txt(ax, c4x + c4w / 2, 1.9, "IDH", size=15, weight="bold", color=C["violet"])
txt(ax, c4x + c4w / 2, 1.42, "media\ngeométrica", size=7.8, color=C["ink2"])
txt(ax, c4x + c4w / 2, 0.95, r"$\sqrt[3]{I_s\, I_e\, I_i}$", size=11)
txt(ax, c4x + c4w / 2, 0.5, "0 a 1", size=7.6, color=C["ink2"])
for y in (2.5, 1.52, 0.44):
    arr(ax, c3x + c3w, y, c4x, y if y != 1.52 else 1.52, C["violet"], lw=1.3, ms=9)
save(fig, "t2_idh_estructura")

# ---------------------------------------------------------------- Figura 2.10
def iing(x):
    return (np.log(x) - log(100)) / (log(75000) - log(100))


xx = np.linspace(100, 75000, 600)
fig, ax = new_fig(6.4, 2.75)
ax.plot(xx, iing(xx), color=C["aqua"], lw=LW)
ax.plot(xx, (xx - 100) / (75000 - 100), color=C["ink3"], lw=1.2, ls=(0, (4, 3)))
ax.annotate("si fuera lineal", (52000, (52000 - 100) / 74900), xytext=(8, -12), textcoords="offset points",
            fontsize=7.8, color=C["ink3"])
ax.annotate(r"$I_{ing}=\dfrac{\ln x-\ln 100}{\ln 75.000-\ln 100}$", (7000, 1.0), ha="left", va="center",
            fontsize=9.5, color=C["aqua"])
pts = [("Honduras", 5308, (8, -16), "left"), ("Namibia", 9357, (6, -12), "left"), ("Guyana", 22465, (6, -13), "left"),
       ("Australia", 49097, (4, -13), "left")]
for n, v, off, ha in pts:
    ax.plot([v], [iing(v)], "o", ms=6, color=C["ink"], mec="white", mew=1.3, zorder=5)
    ax.annotate(f"{n} ({fmt(v)}): {fmt(iing(v), 3)}", (v, iing(v)), xytext=off, textcoords="offset points",
                fontsize=7.7, ha=ha, color=C["ink"], bbox=dict(boxstyle="square,pad=0.1", fc="white", ec="none"))
d_h = iing(5308 + 1000) - iing(5308)
d_a = iing(49097 + 1000) - iing(49097)
ax.annotate(f"+US\\$1.000 → +{fmt(d_h, 3)} en Honduras\n+US\\$1.000 → +{fmt(d_a, 3)} en Australia\n(≈ 9 veces menos)",
            (0.57, 0.07), xycoords="axes fraction", fontsize=7.8, color=C["ink"],
            bbox=dict(boxstyle="round,pad=0.4", fc=C["gray_bg"], ec="none"))
ax.set_xlim(0, 80000)
ax.set_ylim(0, 1.08)
ax.set_xticks([0, 20000, 40000, 60000, 75000])
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: fmt(v)))
data_axes(ax, "INB per cápita (US$ PPA)", "índice de ingreso")
comma_axis(ax, "y", 1)
save(fig, "t2_idh_ingreso_log")

# ---------------------------------------------------------------- Figura 2.11
groups = [("País A (parejo)", [0.70, 0.70, 0.70]), ("País B (desparejo)", [0.90, 0.90, 0.30]),
          ("Yemen 2021 (real)", [0.6738, 0.3595, 0.3891])]
fig, ax = new_fig(6.5, 2.7)
w = 0.22
cols = [C["blue"], C["orange"], C["aqua"]]
names = ["salud", "educación", "ingreso"]
for gi, (gname, vals) in enumerate(groups):
    x0 = gi * 1.25
    for j, v in enumerate(vals):
        ax.bar(x0 + (j - 1) * (w + 0.02), v, w, color=cols[j], label=names[j] if gi == 0 else None)
    am = sum(vals) / 3
    gm = (vals[0] * vals[1] * vals[2]) ** (1 / 3)
    xl, xr = x0 - 1.5 * w - 0.06, x0 + 1.5 * w + 0.06
    ax.plot([xl, xr], [am, am], color=C["ink3"], lw=1.5, ls=(0, (4, 2)), zorder=5)
    ax.plot([xl, xr], [gm, gm], color=C["ink"], lw=2.0, zorder=5)
    d = 3 if gi < 2 else 3
    same = abs(am - gm) < 0.005
    lab_a = f"aritmética {fmt(am, d if gi == 2 else 2)}"
    lab_g = f"geométrica {fmt(gm, d if gi == 2 else 2)}"
    if same:
        ax.annotate("aritmética = geométrica\n= " + fmt(gm, 2), (x0, am), xytext=(0, 6), textcoords="offset points",
                    ha="center", va="bottom", fontsize=7.6, color=C["ink"], fontweight="bold")
    else:
        ax.annotate(lab_a, (xr, am), xytext=(4, 5), textcoords="offset points", va="center", fontsize=7.6,
                    color=C["ink2"])
        ax.annotate(lab_g, (xr, gm), xytext=(4, -5), textcoords="offset points", va="center", fontsize=7.6,
                    color=C["ink"], fontweight="bold")
ax.set_xticks([0, 1.25, 2.5])
ax.set_xticklabels([g[0] for g in groups], fontsize=8.6)
ax.set_xlim(-0.45, 3.35)
ax.set_ylim(0, 1.05)
ax.tick_params(axis="x", length=0)
data_axes(ax, "", "índice de dimensión")
comma_axis(ax, "y", 1)
ax.legend(loc="upper right", ncol=3, fontsize=7.8, handlelength=1.0, bbox_to_anchor=(1.0, 1.1))
save(fig, "t2_media_geometrica")

# ---------------------------------------------------------------- Figura 2.12
fig, ax = canvas(6.8, 2.05)
x0, x1 = 0.40, 1.0
X = lambda v: 0.2 + (v - x0) / (x1 - x0) * 6.4  # noqa: E731
cats = [(0.40, 0.55, "BAJO", "menos de 0,550", "#e3eefb", C["ink"]),
        (0.55, 0.70, "MEDIO", "0,550 – 0,699", "#b8d3f3", C["ink"]),
        (0.70, 0.80, "ALTO", "0,700 – 0,799", "#79aee9", C["ink"]),
        (0.80, 1.00, "MUY ALTO", "0,800 y más", C["blue"], "white")]
by, bh = 1.45, 0.5
for a, b, n, r, fc, tc in cats:
    ax.add_patch(plt.Rectangle((X(a), by), X(b) - X(a), bh, fc=fc, ec="white", lw=2))
    txt(ax, (X(a) + X(b)) / 2, by + bh / 2 + 0.09, n, size=8.6, weight="bold", color=tc)
    txt(ax, (X(a) + X(b)) / 2, by + bh / 2 - 0.12, r, size=7.4, color=tc)
base = 1.18
ax.plot([X(0.40), X(1.0)], [base, base], color=C["ink2"], lw=1.0)
for v in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0):
    ax.plot([X(v), X(v)], [base - 0.04, base + 0.04], color=C["ink2"], lw=0.9)
    txt(ax, X(v) + (0.04 if v < 1.0 else -0.04), base + 0.12, fmt(v, 1), size=6.6, color=C["ink3"], z=6,
        ha="left" if v < 1.0 else "right")
for v in (0.55, 0.70, 0.80):
    ax.plot([X(v), X(v)], [base, by], color=C["ink3"], lw=0.8, ls=(0, (2, 2)), zorder=1)
paises = [("Yemen", 0.455, 1), ("Nigeria", 0.560, 1), ("Honduras", 0.638, 1), ("Namibia", 0.645, 2),
          ("Jamaica", 0.709, 1), ("Guyana", 0.714, 2), ("Barbados", 0.790, 1), ("Argentina", 0.865, 1),
          ("Australia", 0.951, 1), ("Islandia", 0.972, 2)]
shift = {"Honduras": -0.018, "Namibia": 0.012, "Jamaica": -0.016, "Guyana": 0.014, "Australia": -0.016,
         "Islandia": 0.012, "Barbados": 0.0}
for n, v, lvl in paises:
    ly = 0.78 if lvl == 1 else 0.36
    lx = X(v + shift.get(n, 0))
    ax.plot([X(v), lx], [base, ly + 0.2], color=C["ink3"], lw=0.7, zorder=2)
    ax.plot([X(v)], [base], "o", ms=6.5, color=C["ink"], mec="white", mew=1.3, zorder=5)
    txt(ax, lx, ly + 0.07, n, size=7.8, weight="bold")
    txt(ax, lx, ly - 0.12, fmt(v, 3), size=7.6, color=C["ink2"])
save(fig, "t2_idh_escala")
