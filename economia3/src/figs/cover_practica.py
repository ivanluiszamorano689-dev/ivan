"""Arte de portada de la práctica: barras y una curva de crecimiento en trazo blanco."""
import sys; sys.path.insert(0, "../lib")
from econ_style import *

fig, ax = plt.subplots(figsize=(6.2, 5.2))
fig.patch.set_alpha(0); ax.set_facecolor("none"); ax.axis("off")
x = np.arange(8)
h = 1.2 * 1.25 ** x
ax.bar(x, h, width=0.62, color="white", alpha=0.22, lw=0)
xx = np.linspace(0, 7, 200)
ax.plot(xx, 1.2 * 1.25 ** xx + 0.6, color="white", lw=2.4, alpha=0.8)
ax.plot(x, h + 0.6, "o", color="white", ms=6, alpha=0.9)
ax.set_xlim(-0.8, 7.8); ax.set_ylim(0, 8.5)
fig.savefig(OUT / "cover_practica.svg", format="svg", transparent=True, metadata={"Date": None})
