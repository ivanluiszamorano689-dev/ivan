"""Arte de portada de 'Parciales resueltos': grilla de respuestas con tildes."""
import sys; sys.path.insert(0, "../lib")
from econ_style import *
from matplotlib.patches import FancyBboxPatch, Circle

fig, ax = plt.subplots(figsize=(6.2, 5.2))
fig.patch.set_alpha(0); ax.set_facecolor("none"); ax.axis("off")
ax.set_xlim(0, 10); ax.set_ylim(0, 8.4)
W = "white"
# grilla de opciones a-e, una fila por pregunta, con la correcta rellena
correct = [3, 0, 2, 4, 1, 0, 2, 3]
for r, c in enumerate(correct):
    y = 7.6 - r * 0.98
    for j in range(5):
        x = 1.0 + j * 1.25
        if j == c:
            ax.add_patch(Circle((x, y), 0.34, color=W, alpha=0.85, lw=0))
            ax.plot([x - 0.15, x - 0.03, x + 0.18], [y + 0.0, y - 0.13, y + 0.16], color="#1c3f73", lw=2.2,
                    solid_capstyle="round")
        else:
            ax.add_patch(Circle((x, y), 0.34, fill=False, ec=W, alpha=0.35, lw=1.3))
# columna de puntaje
for r in range(8):
    y = 7.6 - r * 0.98
    ax.add_patch(FancyBboxPatch((7.6, y - 0.22), 1.6 * (0.45 + 0.55 * ((r * 37) % 10) / 10), 0.44,
                                boxstyle="round,pad=0,rounding_size=0.2", color=W, alpha=0.28, lw=0))
fig.savefig(OUT / "cover_parciales.svg", format="svg", transparent=True, metadata={"Date": None})
