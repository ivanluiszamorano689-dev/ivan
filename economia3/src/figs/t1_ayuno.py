"""Figura 1.3 — El ejemplo del ayuno: mismo funcionamiento, conjuntos de capacidad opuestos (esquemático)."""
import sys; sys.path.insert(0, "../lib")
from econ_style import *

fig, axs = plt.subplots(1, 2, figsize=(6.6, 2.9))
fig.subplots_adjust(wspace=0.32)
xf = 0.55    # nivel de nutrición observado (el mismo en los dos casos)


def frontier(ax, xmax, ymax, color, bg):
    t = np.linspace(0, np.pi / 2, 200)
    xs, ys = xmax * np.cos(t) ** 0.8, ymax * np.sin(t) ** 0.8
    ax.fill(np.r_[0, xs, 0], np.r_[0, ys, 0], color=bg, lw=0, zorder=1)
    ax.plot(xs, ys, color=color, lw=LW, zorder=2)


for ax, title, (xm, ym), py in [(axs[0], "Ayuna por decisión (persona rica)", (4.0, 3.2), 2.25),
                                (axs[1], "Pasa hambre (persona pobre)", (0.95, 0.75), 0.33)]:
    frontier(ax, xm, ym, C["violet"], C["violet_bg"])
    econ_axes(ax, "nutrición", "otros\nfuncionamientos", xlim=(0, 4.6), ylim=(0, 3.8))
    ax.set_title(title, fontsize=9.4, pad=14)
    ax.plot([xf, xf], [0, py], ls=(0, (3, 3)), lw=0.9, color=C["ink3"])
    point(ax, xf, py, C["orange"])
    ax.annotate("desnutrición", (xf, 0), xytext=(0, -11), textcoords="offset points", ha="center", va="top",
                fontsize=8, color=C["ink"])

# panel rico
a = axs[0]
a.text(2.25, 1.0, "conjunto de capacidad\n(el menú): amplio", ha="center", fontsize=8.2, color=C["violet"],
       fontweight="bold")
a.annotate("elige ayunar\n(el plato)", (xf, 2.25), xytext=(1.25, 3.25), fontsize=8, color=C["ink"],
           fontweight="bold", ha="left", arrowprops=dict(arrowstyle="-", color=C["ink3"], lw=0.8))
a.plot([3.0], [1.9], "o", ms=6.5, mfc="white", mec=C["ink2"], mew=1.3, zorder=5)
a.annotate("podía comer bien", (3.0, 1.9), xytext=(3.2, 2.75), fontsize=7.8, color=C["ink2"], ha="left",
           arrowprops=dict(arrowstyle="-", color=C["ink3"], lw=0.8))
# panel pobre
b = axs[1]
b.annotate("conjunto de capacidad:\ncasi vacío", (0.75, 0.45), xytext=(1.6, 1.55), fontsize=8.2,
           color=C["violet"], fontweight="bold", ha="left",
           arrowprops=dict(arrowstyle="-", color=C["violet"], lw=0.8))
b.annotate("no tiene otra opción", (xf, 0.33), xytext=(1.6, 2.85), fontsize=8, color=C["ink"],
           fontweight="bold", ha="left", arrowprops=dict(arrowstyle="-", color=C["ink3"], lw=0.8))
save(fig, "t1_ayuno")
