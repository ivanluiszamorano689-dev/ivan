"""§0 · Valor esperado de arriesgar con la penalización +10 / −5 (y su equivalente en la práctica)."""
from s0_util import *

fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.6, 2.75), gridspec_kw=dict(width_ratios=[1, 1.12], wspace=0.34))

# ---- panel 1: al azar entre k opciones
ks = [5, 4, 3, 2]
ev = [15 / k - 5 for k in ks]                   # -2, -1.25, 0, +2.5
pr = [5 * (3 - k) / (2 * k) for k in ks]        # inciso de 5 ptos: -1, -0.625, 0, +1.25
cols = [C["red"] if v < -1e-9 else (C["green"] if v > 1e-9 else C["ink3"]) for v in ev]
x = np.arange(len(ks))
a1.bar(x, [v if abs(v) > 1e-9 else 0.07 for v in ev], width=0.6, color=cols, zorder=3)
a1.axhline(0, color=C["ink2"], lw=1.0, zorder=4)
lab = ["−2", "−1,25", "0", "+2,5"]
lab2 = ["−1", "−0,63", "0", "+1,25"]
for xi, v, t, t2 in zip(x, ev, lab, lab2):
    if v >= 0:
        a1.text(xi, v + 0.25, t, ha="center", va="bottom", fontsize=9.5, fontweight="bold", color=C["ink"])
        a1.text(xi, -0.35, f"({t2})", ha="center", va="top", fontsize=7.4, color=C["ink2"])
    else:
        a1.text(xi, v - 0.25, t, ha="center", va="top", fontsize=9.5, fontweight="bold", color=C["ink"])
        a1.text(xi, 0.3, f"({t2})", ha="center", va="bottom", fontsize=7.4, color=C["ink2"])
a1.set_xticks(x)
a1.set_xticklabels([str(k) for k in ks], fontsize=8.5)
a1.tick_params(axis="x", length=0, pad=4)
a1.set_ylim(-3.4, 3.6)
a1.set_yticks([-3, -2, -1, 0, 1, 2, 3])
a1.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:+.0f}".replace("+0", "0").replace("-", "−")))
data_axes(a1)
a1.set_title("Elegir al azar entre las que quedan", fontsize=9, pad=6)
a1.set_ylabel("puntos esperados (teórica +10 / −5)", fontsize=7.6, color=C["ink2"])
a1.set_xlabel("opciones que quedan en pie\n(entre paréntesis: inciso práctico de 5 ptos)", fontsize=7.6,
              color=C["ink2"], labelpad=3, linespacing=1.25)

# ---- panel 2: según qué tan seguro estás
p = np.linspace(0, 1, 50)
a2.axvspan(0, 1 / 3, color=C["red_bg"], zorder=0)
a2.axvspan(1 / 3, 1, color=C["green_bg"], zorder=0)
a2.plot(p, 15 * p - 5, color=C["blue"], lw=LW, zorder=3)
a2.axhline(0, color=C["ink2"], lw=1.0, zorder=2)
a2.plot([1 / 3, 1 / 3], [-5.5, 0], ls=(0, (3, 3)), lw=0.9, color=C["ink3"], zorder=2)
a2.plot([0.2], [-2], "o", ms=6, color=C["ink"], mec="white", mew=1.4, zorder=5)
a2.annotate("5 opciones\nal azar: −2", (0.2, -2), xytext=(0.03, 2.2), textcoords="data", ha="left", va="center",
            fontsize=7.8, color=C["ink"], fontweight="bold", linespacing=1.1,
            arrowprops=dict(arrowstyle="-", color=C["ink3"], lw=0.8, shrinkA=2, shrinkB=4))
for pp, t, dx, dy, ha in [(0.5, "quedan 2: +2,5", 8, -9, "left"),
                          (1 / 3, "umbral: p = 1/3", 6, -12, "left")]:
    v = 15 * pp - 5
    a2.plot([pp], [v], "o", ms=6, color=C["ink"], mec="white", mew=1.4, zorder=5)
    a2.annotate(t, (pp, v), xytext=(dx, dy), textcoords="offset points", ha=ha, va="center", fontsize=7.8,
                color=C["ink"], fontweight="bold")
a2.text(0.165, 7.4, "dejá en\nblanco", ha="center", va="center", fontsize=7.8, color=DARK["red"], fontweight="bold", linespacing=1.1)
a2.text(0.72, -3.6, "arriesgá", ha="center", va="center", fontsize=7.8, color=DARK["green"], fontweight="bold")
a2.text(0.97, 8.9, r"$E = 10p - 5(1-p) = 15p - 5$", ha="right", va="center", fontsize=8.4, color=C["ink"])
a2.set_xlim(0, 1)
a2.set_ylim(-5.5, 10.5)
a2.set_xticks([0, 0.2, 1 / 3, 0.5, 1])
a2.set_xticklabels(["0", "0,2", "1/3", "0,5", "1"], fontsize=8)
a2.set_yticks([-5, 0, 5, 10])
a2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:+.0f}".replace("+0", "0").replace("-", "−")))
data_axes(a2, "", "", grid=False)
a2.set_xlabel("probabilidad de acertar  p", fontsize=8, color=C["ink2"], labelpad=2)
a2.set_title("Según qué tan seguro estás", fontsize=9, pad=6)
save(fig, "s0_valor_esperado")
