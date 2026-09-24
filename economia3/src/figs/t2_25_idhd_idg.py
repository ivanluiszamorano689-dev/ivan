"""Tema 2.5: IDH vs IDH-D, los 4 pasos del IDG, IDG por región."""
from t2_util import *

# ---------------------------------------------------------------- Figura 2.13
# (nombre, IDH, IDH-D, fuente). Cuentas en lib/calculos_parciales.py y en el manual (Nigeria).
def _g(*v):
    return float(np.prod(v)) ** (1 / len(v))


data = [("Australia", _g(0.993, 0.925, 0.936), _g(0.993 * 0.973, 0.896, 0.776), "P. 2023"),
        ("Guyana", 0.71430, 0.59060, "P. 2024"), ("Jamaica", 0.70940, 0.59180, "P. 2024"),
        ("Namibia", 0.64543, 0.41767, "P. s/f"), ("Honduras", 0.63835, 0.47554, "P. s/f"),
        ("Nigeria", 0.56003, 0.37938, "manual"), ("Yemen", 0.45509, 0.30765, "P. 2025")]
fig, ax = new_fig(6.5, 3.0)
n = len(data)
for i, (name, h, hd, src) in enumerate(data):
    y = n - 1 - i
    ax.plot([hd, h], [y, y], color="#d6d4cc", lw=6, solid_capstyle="round", zorder=1)
    ax.plot([h], [y], "o", ms=8.5, color=C["blue"], mec="white", mew=1.4, zorder=3)
    ax.plot([hd], [y], "o", ms=8.5, color=C["orange"], mec="white", mew=1.4, zorder=3)
    ax.annotate(fmt(h, 3), (h, y), xytext=(7, 0), textcoords="offset points", va="center", fontsize=7.6,
                color=C["blue_bg"] if False else C["ink2"])
    ax.annotate(fmt(hd, 3), (hd, y), xytext=(-7, 0), textcoords="offset points", ha="right", va="center",
                fontsize=7.6, color=C["ink2"])
    loss = 100 * (1 - hd / h)
    ax.annotate(fmt(loss, 1) + " %", (1.15, y), ha="right", va="center", fontsize=8.4, fontweight="bold",
                color=C["red"] if loss > 30 else C["ink"], annotation_clip=False)
ax.set_yticks(range(n))
ax.set_yticklabels([f"{d[0]}" for d in data][::-1], fontsize=8.8)
ax.set_xlim(0.2, 1.08)
ax.spines["bottom"].set_bounds(0.2, 1.0)
ax.set_ylim(-0.6, n - 0.2)
ax.set_xticks([0.2, 0.4, 0.6, 0.8, 1.0])
comma_axis(ax, "x", 1)
ax.spines["left"].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.grid(axis="x", color="#ebe9e3", lw=0.8)
ax.set_axisbelow(True)
ax.annotate("pérdida", (1.15, n - 0.45), ha="right", fontsize=7.8, color=C["ink2"], fontweight="bold",
            annotation_clip=False)
ax.plot([0.24], [n - 0.45], "o", ms=7, color=C["blue"], mec="white")
ax.annotate("IDH (potencial)", (0.24, n - 0.45), xytext=(6, 0), textcoords="offset points", va="center",
            fontsize=7.8, annotation_clip=False)
ax.plot([0.45], [n - 0.45], "o", ms=7, color=C["orange"], mec="white")
ax.annotate("IDH-D (real)", (0.45, n - 0.45), xytext=(6, 0), textcoords="offset points", va="center",
            fontsize=7.8, annotation_clip=False)
for v in (0.55, 0.70, 0.80):
    ax.axvline(v, color=C["ink3"], lw=0.8, ls=(0, (2, 2)), zorder=0.8)
save(fig, "t2_idhd_barras")

# ---------------------------------------------------------------- Figura 2.14
W, H = 6.8, 3.55
fig, ax = canvas(W, H)
hy = 3.38
for x, t in ((1.1, "Dimensiones (por sexo)"), (3.28, "① Índice de cada sexo"), (4.93, "② Media armónica"),
             (6.26, "④ Comparar")):
    txt(ax, x, hy, t, size=8.4, weight="bold", color=C["ink2"])
dims = [("Salud reproductiva", r"M: $\sqrt{\frac{10}{MMR}\cdot\frac{1}{AFR}}$    V: 1", C["blue"], C["blue_bg"]),
        ("Empoderamiento", r"$\sqrt{PR\cdot SE}$  de cada sexo", C["orange"], C["orange_bg"]),
        ("Mercado laboral", r"$LFPR$  de cada sexo", C["aqua"], C["aqua_bg"])]
dx, dw, dh = 0.05, 2.1, 0.78
dys = [2.35, 1.42, 0.49]
for (t, f, c, cb), y in zip(dims, dys):
    rbox(ax, dx, y, dw, dh, fc=cb, ec=c, lw=1.4)
    txt(ax, dx + dw / 2, y + dh - 0.2, t, size=8.8, weight="bold")
    txt(ax, dx + dw / 2, y + 0.27, f, size=8.6)
# paso 1: G_M y G_V
gx, gw = 2.55, 1.46
for y, lab, val in ((2.47, r"$G_M$  (mujeres)", "Nigeria: 0,102"), (1.55, r"$G_V$  (varones)", "Nigeria: 0,858")):
    rbox(ax, gx, y, gw, 0.66, fc="white", ec=C["ink2"], lw=1.3)
    txt(ax, gx + gw / 2, y + 0.44, lab, size=9.4)
    txt(ax, gx + gw / 2, y + 0.18, val, size=7.6, color=C["ink2"])
txt(ax, gx + gw / 2, 1.38, "media geométrica de las\n3 dimensiones de cada sexo", size=7.2, color=C["ink2"], va="top")
# paso 3: referencia
rx, rw = 2.55, 2.98
rbox(ax, rx, 0.05, rw, 0.78, fc=C["gray_bg"], ec=C["ink2"], lw=1.3, ls=(0, (4, 2)))
txt(ax, rx + 0.12, 0.62, "③ Referencia (trata igual a los dos sexos)", size=8.2, weight="bold", ha="left")
txt(ax, rx + 0.12, 0.38, "promedio M-V en cada dimensión → media geométrica", size=7.4, color=C["ink2"], ha="left")
txt(ax, rx + 0.12, 0.16, "Nigeria: salud 0,505 · empod. 0,435 · laboral 0,826 → 0,566", size=7.2, color=C["ink"],
    ha="left")
# paso 2: HARM
hx, hw = 4.3, 1.25
rbox(ax, hx, 1.62, hw, 1.44, fc="white", ec=C["ink2"], lw=1.3)
txt(ax, hx + hw / 2, 2.72, r"$HARM(G_M,G_V)$", size=8.6)
txt(ax, hx + hw / 2, 2.36, r"$\left[\dfrac{1/G_M+1/G_V}{2}\right]^{-1}$", size=8.6)
txt(ax, hx + hw / 2, 1.98, "se pega al más bajo:\npenaliza la brecha", size=7.0, color=C["red"], weight="bold")
txt(ax, hx + hw / 2, 1.72, "Nigeria: 0,182", size=7.4, color=C["ink2"])
# paso 4: IDG
ix, iw = 5.82, 0.93
rbox(ax, ix, 0.05, iw, 3.01, fc=C["violet_bg"], ec=C["violet"], lw=1.6)
txt(ax, ix + iw / 2, 2.6, "IDG", size=15, weight="bold", color=C["violet"])
txt(ax, ix + iw / 2, 2.02, r"$1-\dfrac{HARM}{Ref.}$", size=10.5)
txt(ax, ix + iw / 2, 1.45, "0 = igualdad\n1 = máxima\ndesigualdad", size=7.3, color=C["ink2"])
txt(ax, ix + iw / 2, 0.72, "Nigeria:\n0,679", size=8.4, weight="bold", color=C["violet"])
# flechas
arr(ax, dx + dw, 2.74, gx, 2.8, C["ink2"])
arr(ax, dx + dw, 2.0, gx, 1.9, C["ink2"])
arr(ax, dx + dw, 0.62, rx, 0.52, C["ink2"])
arr(ax, gx + gw, 2.8, hx, 2.6, C["ink2"])
arr(ax, gx + gw, 1.88, hx, 2.1, C["ink2"])
arr(ax, hx + hw, 2.34, ix, 2.34, C["violet"], lw=1.5)
arr(ax, rx + rw, 0.44, ix, 0.44, C["violet"], lw=1.5)
save(fig, "t2_idg_pasos")

# ---------------------------------------------------------------- Figura 2.15
reg = [("Europa y Asia Central", 0.23), ("Asia Oriental y el Pacífico", 0.32), ("América Latina y el Caribe", 0.38),
       ("Estados Árabes", 0.54), ("África Subsahariana", 0.56)]
DEC = {0.23: 2, 0.32: 2, 0.38: 2, 0.54: 2, 0.56: 2}
pai = [("Barbados (P. 2024)", 0.268), ("Jamaica (P. 2024)", 0.335), ("Guyana (P. 2024)", 0.454),
       ("Nigeria (manual)", 0.679)]
fig, ax = new_fig(6.3, 2.95)
labels, vals, cols = [], [], []
for nme, v in reg:
    labels.append(nme); vals.append(v); cols.append(C["blue"])
labels.append(""); vals.append(np.nan); cols.append("white")
for nme, v in pai:
    labels.append(nme); vals.append(v); cols.append(C["ink3"])
ys = np.arange(len(labels))[::-1]
bars = ax.barh(ys, np.nan_to_num(vals), color=cols, height=0.62)
for b, v in zip(bars, vals):
    if not np.isnan(v):
        ax.annotate(fmt(v, DEC.get(v, 3)), (v, b.get_y() + b.get_height() / 2), xytext=(4, 0),
                    textcoords="offset points", va="center", fontsize=8.0)
ax.set_yticks(ys)
ax.set_yticklabels(labels, fontsize=8.4)
ax.axvline(0.455, color=C["ink"], lw=1.1, ls=(0, (3, 2)))
ax.annotate("media mundial 0,455", (0.455, ys[0] + 0.62), ha="center", fontsize=7.8, fontweight="bold",
            annotation_clip=False, bbox=dict(boxstyle="square,pad=0.15", fc="white", ec="none"))
ax.annotate("regiones (Informe 2025)", (0.0, ys[0] + 0.62), xytext=(-2, 0), textcoords="offset points",
            ha="right", fontsize=7.6, color=C["blue"], fontweight="bold", annotation_clip=False)
ax.annotate("países (parciales y manual)", (0.0, ys[6] + 0.55), xytext=(-2, 0), textcoords="offset points",
            ha="right", fontsize=7.6, color=C["ink2"], fontweight="bold", annotation_clip=False)
ax.set_xlim(0, 0.78)
ax.set_xticks([0, 0.2, 0.4, 0.6])
comma_axis(ax, "x", 1)
clean_hbar(ax, "IDG  (← más igualdad · más desigualdad →)")
ax.xaxis.label.set_size(8.4)
ax.set_ylim(-0.6, len(labels) - 0.1)
save(fig, "t2_idg_regiones")
