"""§4 · P3 c: IDH (potencial) contra IDH-D (efectivo) de Namibia y Honduras; la barra gris es la pérdida."""
from s0_util import *

data = [("Namibia", 0.645, 0.418, "35,3 %"), ("Honduras", 0.638, 0.476, "25,5 %")]
fig, ax = new_fig(6.0, 1.95)
ax.set_xlim(0.34, 0.76)
ax.set_ylim(-0.45, 1.95)
for s in ("left", "top", "right"):
    ax.spines[s].set_visible(False)
# cortes de clasificación
for c in (0.55, 0.70):
    ax.axvline(c, color=C["ink3"], lw=0.8, ls=(0, (3, 3)), zorder=0)
for x, t in [(0.455, "bajo"), (0.625, "medio"), (0.73, "alto")]:
    ax.text(x, 1.72, f"DH {t}", ha="center", va="center", fontsize=7.4, color=C["ink3"])
for i, (name, idh, idhd, loss) in enumerate(data):
    y = 1 - i
    ax.plot([idhd, idh], [y, y], color=C["rule"], lw=6, solid_capstyle="butt", zorder=1)
    ax.plot([idh], [y], "o", ms=8, color=C["blue"], mec="white", mew=1.5, zorder=3)
    ax.plot([idhd], [y], "o", ms=8, color=C["orange"], mec="white", mew=1.5, zorder=3)
    ax.text(idh + 0.008, y, f"IDH {comma(idh, 3)}", ha="left", va="center", fontsize=8, color=DARK["blue"],
            fontweight="bold")
    ax.text(idhd - 0.008, y, f"IDH-D {comma(idhd, 3)}", ha="right", va="center", fontsize=8,
            color=DARK["orange"], fontweight="bold")
    ax.text((idh + idhd) / 2, y + 0.26, f"pierde {loss}", ha="center", va="bottom", fontsize=7.6, color=C["ink2"],
            bbox=dict(fc="white", ec="none", pad=1.2))
ax.set_yticks([1, 0])
ax.set_yticklabels([d[0] for d in data], fontsize=8.8, fontweight="bold", color=C["ink"])
ax.tick_params(axis="y", length=0, pad=6)
ax.set_xticks([0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75])
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: comma(v, 2)))
ax.tick_params(axis="x", labelsize=7.6, colors=C["ink3"])
ax.spines["bottom"].set_color(C["ink3"])
save(fig, "s0_nam_hon")
