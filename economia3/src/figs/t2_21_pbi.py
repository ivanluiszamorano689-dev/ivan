"""Tema 2.1: PBI = sum P*Q y los tres problemas; Brasil vs Canadá."""
from t2_util import *

# ---------------------------------------------------------------- Figura 2.1
W, H = 6.6, 3.05
fig, ax = canvas(W, H)
# fórmula grande, armada por partes para poder señalar cada término
y0 = 2.62
txt(ax, 1.55, y0, r"$\mathrm{PBI}$", size=22)
txt(ax, 2.40, y0, r"$=\ \sum_{i=1}^{n}$", size=21)
txt(ax, 3.22, y0, r"$P_i$", size=23, color=C["orange"])
txt(ax, 3.66, y0 + 0.02, r"$\cdot$", size=23)
txt(ax, 4.10, y0, r"$Q_i$", size=23, color=C["aqua"])
# etiqueta de la moneda pegada al PBI
rbox(ax, 0.80, 1.95, 1.50, 0.3, fc=C["blue_bg"], ec=C["blue"], lw=1.0, r=0.06)
txt(ax, 1.55, 2.10, "medido en \\$, ¥, €, R\\$…", size=8, color=C["blue"], weight="bold")
txt(ax, 4.70, y0 + 0.02, "valor de lo producido\n= precios × cantidades", size=8.4, color=C["ink2"], ha="left")

bw, bh, by = 2.02, 1.38, 0.08
xs = [0.08, 2.29, 4.50]
cols = [("blue", "blue_bg"), ("orange", "orange_bg"), ("aqua", "aqua_bg")]
titles = ["① Signos monetarios", "② Precios correctos", "③ Cantidades"]
qs = ["¿En qué moneda está P?", "¿Qué P uso para comparar?", "¿Se registra toda la Q?"]
bodies = ["Se convierte con el TC de\nmercado… pero el TCm sólo\nrefleja los bienes transables.",
          "Misma canasta valuada en\ncada país → TC de PPA\n(o Big Mac: un solo bien).",
          "Informalidad, evasión,\nautoconsumo, ilegales →\nQ subestimada."]
for x, (c, cb), t, q, b in zip(xs, cols, titles, qs, bodies):
    rbox(ax, x, by, bw, bh, fc=C[cb], ec=C[c], lw=1.5, r=0.1)
    txt(ax, x + bw / 2, by + bh - 0.2, t, size=9.6, weight="bold", color=C["ink"])
    txt(ax, x + bw / 2, by + bh - 0.45, q, size=8.3, color=C[c], weight="bold")
    txt(ax, x + bw / 2, by + 0.43, b, size=8.0, color=C["ink2"], linespacing=1.35)
# flechas desde cada término hacia su problema
arr(ax, 1.40, 1.95, xs[0] + bw * 0.55, by + bh + 0.02, C["blue"], lw=1.5, rad=0.1)
arr(ax, 3.20, 2.30, xs[1] + bw * 0.52, by + bh + 0.02, C["orange"], lw=1.5, rad=0.0)
arr(ax, 4.18, 2.30, xs[2] + bw * 0.45, by + bh + 0.02, C["aqua"], lw=1.5, rad=0.12)
save(fig, "t2_pbi_problemas")

# ---------------------------------------------------------------- Figura 2.2
pais = ["Brasil", "Canadá"]
col = [C["blue"], C["orange"]]
pbi = [2125.958, 2364.551]          # miles de millones de US$ (manual: 2.125.958 y 2.364.551 millones)
pob = [213, 41.5]                   # millones de habitantes
pc = [9964, 56909]                  # US$ por habitante
fig, axs = plt.subplots(1, 3, figsize=(6.6, 1.75))
fig.subplots_adjust(wspace=0.55)
specs = [(pbi, "PBI total\n(miles de millones de US$)", lambda v: fmt(v, 0)),
         (pob, "Población\n(millones de habitantes)", lambda v: fmt(v, 1) if v % 1 else fmt(v, 0)),
         (pc, "PBI per cápita\n(US$ por habitante)", lambda v: fmt(v, 0))]
for ax, (vals, tit, f) in zip(axs, specs):
    bars = ax.barh([1, 0], vals, color=col, height=0.62)
    ax.set_yticks([1, 0])
    ax.set_yticklabels(pais if ax is axs[0] else ["", ""])
    ax.set_xlim(0, max(vals) * 1.42)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_color(C["ink3"])
    ax.tick_params(axis="y", length=0, labelsize=9)
    ax.set_title(tit, fontsize=8.6, loc="left", pad=6, color=C["ink"])
    hbar_labels(ax, bars, [f(v) for v in vals], size=8.6)
axs[1].annotate("5,1 veces\nmás gente", xy=(0.97, 0.5), xycoords="axes fraction", ha="right", va="center",
                fontsize=7.6, color=C["ink2"])
axs[2].annotate("×5,7", xy=(0.99, 0.72), xycoords="axes fraction", ha="right", va="center", fontsize=10,
                color=C["ink"], fontweight="bold")
save(fig, "t2_brasil_canada")
