"""Arte de portada de 'Paso a paso': escalera de pasos numerados que sube hacia un tilde."""
import sys; sys.path.insert(0, "../lib")
from econ_style import *
from matplotlib.patches import FancyBboxPatch, Circle

fig, ax = plt.subplots(figsize=(6.2, 5.2))
fig.patch.set_alpha(0); ax.set_facecolor("none"); ax.axis("off")
ax.set_xlim(0, 10); ax.set_ylim(0, 8.4)
W = "white"
xs = [0.6, 2.4, 4.2, 6.0, 7.8]
for i, x in enumerate(xs):
    h = 1.2 + i * 1.35
    ax.add_patch(FancyBboxPatch((x, 0.3), 1.55, h, boxstyle="round,pad=0,rounding_size=0.18",
                                color=W, alpha=0.16 + 0.1 * i, lw=0))
    ax.add_patch(Circle((x + 0.78, 0.3 + h + 0.55), 0.38, fill=False, ec=W, lw=1.6, alpha=0.8))
    ax.text(x + 0.78, 0.3 + h + 0.55, str(i + 1), color=W, ha="center", va="center", fontsize=13,
            fontweight="bold", alpha=0.9)
# trazo que une los pasos
px = [x + 0.78 for x in xs]; py = [0.3 + 1.2 + i * 1.35 + 0.55 for i in range(5)]
ax.plot(px, py, color=W, lw=1.2, alpha=0.45, ls=(0, (2, 3)))
fig.savefig(OUT / "cover_pasoapaso.svg", format="svg", transparent=True, metadata={"Date": None})
