"""Arte de portada del manual de teoría: diagrama de Solow estilizado en trazo blanco."""
import sys; sys.path.insert(0, "../lib")
from econ_style import *

fig, ax = plt.subplots(figsize=(6.2, 5.2))
fig.patch.set_alpha(0); ax.set_facecolor("none"); ax.axis("off")
k = np.linspace(0.001, 10, 300)
W = "white"
ax.plot(k, 3.2 * k**0.4, color=W, lw=2.4, alpha=0.8)
ax.plot(k, 1.3 * k**0.4, color=W, lw=2.0, alpha=0.55)
ax.plot(k, 0.42 * k, color=W, lw=2.0, alpha=0.4)
ks = (1.3 / 0.42) ** (1 / 0.6)
ax.plot([ks], [0.42 * ks], "o", ms=11, color=W, alpha=0.9)
ax.plot([ks, ks], [0, 3.2 * ks**0.4], color=W, lw=1, alpha=0.35, ls=(0, (3, 3)))
ax.plot([0, 10], [0, 0], color=W, lw=1.2, alpha=0.5); ax.plot([0, 0], [0, 8.5], color=W, lw=1.2, alpha=0.5)
ax.set_xlim(-0.3, 10.3); ax.set_ylim(-0.3, 8.6)
fig.savefig(OUT / "cover_teoria.svg", format="svg", transparent=True, metadata={"Date": None})
