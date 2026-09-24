"""§0 · Controles de rango: el resultado tiene que caer dentro de un intervalo que se ve a simple vista."""
from s0_util import *

fig, axs = plt.subplots(2, 2, figsize=(6.6, 2.55), gridspec_kw=dict(hspace=0.7, wspace=0.16))

panels = [
    dict(ax=axs[0, 0], title="TC PPA · P2 (2023)", xlim=(0, 30), ticks=[0, 5, 10, 15, 20, 25, 30], dec=0,
         lo=(10, "corte de pelo\n2.000/200 = 10", "center"), hi=(25, "pendrive = TCm\n2.500/100 = 25", "center"),
         res=(10.88, "TC PPA = 10,88"), col="blue", extra=None),
    dict(ax=axs[0, 1], title="TC PPA · P1 (2022)", xlim=(0, 45), ticks=[0, 10, 20, 30, 40], dec=0,
         lo=(12.5, "torta\n125/10 = 12,5", "center"), hi=(40, "tablet = TCm\n12.000/300 = 40", "center"),
         res=(30.43, "TC PPA = 30,43"), col="blue", extra=None),
    dict(ax=axs[1, 0], title="IDH · Australia (P2, 2023)", xlim=(0.85, 1.0), ticks=[0.85, 0.9, 0.95, 1.0], dec=2,
         lo=(0.925, "educ. 0,925", "right"), hi=(0.993, "vida 0,993", "center"), mid=(0.936, "ingr. 0,936", "left"),
         res=(0.951, "IDH = 0,951"), col="orange", extra=(0.876, "IDH-D = 0,876")),
    dict(ax=axs[1, 1], title="IDH · Namibia (P3)", xlim=(0.35, 0.75), ticks=[0.4, 0.5, 0.6, 0.7], dec=1,
         lo=(0.583, "educ. 0,583", "center"), hi=(0.686, "ingr. 0,686", "left"), mid=(0.672, "vida 0,672", "right", 1),
         res=(0.645, "IDH = 0,645"), col="orange", extra=(0.418, "IDH-D = 0,418")),
]

for P in panels:
    ax = P["ax"]
    ax.set_xlim(*P["xlim"])
    ax.set_ylim(-1.25, 1.55)
    for s in ("left", "top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_position(("data", 0))
    ax.set_yticks([])
    ax.set_xticks(P["ticks"])
    d = P["dec"]
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p, d=d: f"{v:.{d}f}".replace(".", ",")))
    ax.tick_params(axis="x", labelsize=7.2, length=3, pad=2, colors=C["ink3"])
    col = P["col"]
    lo, hi = P["lo"][0], P["hi"][0]
    ax.spines["bottom"].set_zorder(1)
    ax.add_patch(plt.Rectangle((lo, -0.16), hi - lo, 0.32, fc=BG[col], ec=MID[col], lw=0.9, zorder=3))
    for lab in [P["lo"], P["hi"]] + ([P["mid"]] if "mid" in P else []):
        v, t, ha = lab[:3]
        lvl = lab[3] if len(lab) > 3 else 0
        ax.plot([v, v], [0, 0.42 + 0.5 * lvl], color=MID[col], lw=1.1 if lvl == 0 else 0.8, zorder=3)
        ax.text(v, 0.5 + 0.5 * lvl, t, ha=ha, va="bottom", fontsize=6.7, color=C["ink2"], linespacing=1.1)
    rv, rt = P["res"]
    ax.plot([rv], [0], "o", ms=7.5, color=MID[col], mec="white", mew=1.5, zorder=5)
    ax.annotate(rt, (rv, 0), xytext=(0, -15), textcoords="offset points", ha="center", va="top", fontsize=7.8,
                fontweight="bold", color=DARK[col])
    if P["extra"]:
        ev, et = P["extra"]
        ax.plot([ev], [0], "D", ms=5.5, color=C["ink2"], mec="white", mew=1.2, zorder=5)
        ax.annotate(et, (ev, 0), xytext=(0, -15), textcoords="offset points", ha="center", va="top", fontsize=7.4,
                    color=C["ink2"], fontweight="bold")
    ax.set_title(P["title"], fontsize=8.6, pad=2, loc="left")
save(fig, "s0_controles")
