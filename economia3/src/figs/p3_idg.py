"""TP3 Parte C: IDG en cuatro pasos (Argentina), comparación de los cuatro países del TP,
Argentina vs Tailandia por indicador y la trampa de lectura (índice de salud vs IDG).
Datos: práctica resuelta TP3 Parte C; parcial s/f (Namibia/Honduras) y prueba práctica 28/9/2024 (IDG de
Barbados, Guyana, Jamaica). Correr desde figs/: python3 p3_idg.py"""
from p3_util import *  # noqa: F403

# ------------------------------------------------------------------ 1) los cuatro pasos con Argentina
fig, ax = lienzo(6.8, 3.55, 10, 5.4)
cx = [2.0, 3.6, 5.2]
for x, t in zip(cx, ["salud\nreproductiva", "empodera-\nmiento", "mercado\nlaboral"]):
    ax.text(x, 5.08, t, ha="center", va="center", fontsize=7.8, color=C["ink2"], fontweight="bold", linespacing=1.1)
rows = [(4.15, "Mujeres", ["(10/45 · 1/26,4)^½\n= 0,0917", "(0,438·0,743)^½\n= 0,5705", "LFPR\n= 0,532"], "GM = 0,3031",
         C["blue"], C["blue_bg"]),
        (3.05, "Varones", ["1\n(no aplica)", "(0,562·0,722)^½\n= 0,6370", "LFPR\n= 0,722"], "GV = 0,7719",
         C["orange"], C["orange_bg"]),
        (1.0, "Referencia\n(ambos\npor igual)", ["(0,0917 + 1)/2\n= 0,5459", "(0,5705+0,6370)/2\n= 0,6037",
                                               "(0,532+0,722)/2\n= 0,6270"], "Ref = 0,5912", C["aqua"], C["aqua_bg"])]
for y, lab, vals, res, col, bg in rows:
    ax.text(0.6, y, lab, ha="center", va="center", fontsize=8.2, fontweight="bold", color=C["ink"], linespacing=1.1)
    for x, v in zip(cx, vals):
        caja(ax, x, y, 1.5, 0.82, v, fc="white", ec=col, size=7.4)
    flecha(ax, 5.97, y, 6.35, y, color=col, lw=1.2)
    caja(ax, 7.05, y, 1.35, 0.6, res, fc=bg, ec=col, size=8.2, weight="bold")
    ax.text(6.2, y + 0.46, "media geom." if lab != "Referencia\n(ambos\npor igual)" else "media geom.",
            ha="center", va="bottom", fontsize=6.6, color=C["ink3"])
# promedios hacia la referencia
for x in cx:
    flecha(ax, x, 2.62, x, 1.43, color=C["aqua"], lw=1.0, style="-|>")
ax.text(1.02, 2.02, "promedio\naritmético\npor dimensión", ha="center", va="center", fontsize=6.8, color=C["aqua"],
        fontweight="bold", linespacing=1.1)
# HARM
caja(ax, 9.05, 3.6, 1.7, 1.05, "② HARM\n= 0,4353", fc=C["gray_bg"], ec=C["ink"], size=8.4, weight="bold")
flecha(ax, 7.74, 4.15, 8.18, 3.85, color=C["ink2"], lw=1.1)
flecha(ax, 7.74, 3.05, 8.18, 3.35, color=C["ink2"], lw=1.1)
ax.text(9.05, 2.88, "media armónica:\nse pega al menor", ha="center", va="top", fontsize=6.8, color=C["ink2"],
        linespacing=1.1)
# IDG
caja(ax, 9.05, 1.0, 1.7, 1.3, "④ IDG\n1 − 0,4353/0,5912\n= 0,264", fc="white", ec=C["ink"], lw=1.8, size=8.2,
     weight="bold")
flecha(ax, 9.05, 2.3, 9.05, 1.66, color=C["ink"], lw=1.3)
flecha(ax, 7.74, 1.0, 8.19, 1.0, color=C["ink"], lw=1.3)
ax.text(7.05, 3.63, "①", ha="center", va="center", fontsize=9, color=C["ink2"], fontweight="bold")
ax.text(7.05, 0.52, "③", ha="center", va="center", fontsize=9, color=C["ink2"], fontweight="bold")
ax.plot([0.1, 9.95], [2.3, 2.3], color=C["rule"], lw=0.7, ls=(0, (2, 3)), zorder=0)
save(fig, "p3_idg_pasos")

# ------------------------------------------------------------------ 2) los cuatro países
P = [("Costa Rica", 0.3412, 0.7966, 0.4778, 0.5657, 0.7069, 0.5680, 0.6101, 0.217),
     ("Argentina", 0.3031, 0.7719, 0.4353, 0.5459, 0.6037, 0.6270, 0.5912, 0.264),
     ("Tailandia", 0.2718, 0.8086, 0.4068, 0.5575, 0.4891, 0.6860, 0.5719, 0.289),
     ("Guinea", 0.0965, 0.6406, 0.1677, 0.5062, 0.2701, 0.5760, 0.4286, 0.609)]
fig, (a1, a2) = new_fig(6.7, 2.85, ncols=2, gridspec_kw=dict(width_ratios=[1.12, 1]))
fig.subplots_adjust(wspace=0.5)
n = len(P)
for i, (p, gm, gv, hm, s, e, l, r, idg) in enumerate(P):
    y = n - 1 - i
    a1.plot([gm, gv], [y, y], color="#d9d7d0", lw=3, zorder=1, solid_capstyle="round")
    a1.plot(gm, y, "o", ms=7, color=C["blue"], mec="white", mew=1.2, zorder=3)
    a1.plot(gv, y, "s", ms=6.5, color=C["orange"], mec="white", mew=1.2, zorder=3)
    a1.plot(hm, y, "D", ms=5.5, color=C["ink"], mec="white", mew=1, zorder=4)
    a1.plot(r, y, "|", ms=11, mew=1.8, color=C["aqua"], zorder=4)
    a1.text(1.02, y, coma(idg), ha="left", va="center", fontsize=8.6, fontweight="bold",
            color=C["red"] if idg > 0.5 else C["ink"])
a1.text(1.02, n - 0.45, "IDG", ha="left", va="bottom", fontsize=8, fontweight="bold")
a1.set_yticks(range(n))
a1.set_yticklabels([p[0] for p in P][::-1], fontsize=8.4)
a1.tick_params(axis="y", length=0)
a1.set_xlim(0, 1.0)
a1.set_ylim(-0.6, n - 0.2)
a1.xaxis.set_major_formatter(fmt_coma(1))
a1.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
a1.grid(axis="x", color=GRID, lw=0.8)
a1.set_axisbelow(True)
a1.spines["left"].set_visible(False)
a1.set_title("Índice de género por sexo", fontsize=9, pad=6)
from matplotlib.lines import Line2D
a1.legend(handles=[Line2D([], [], marker="o", ls="", color=C["blue"], ms=6.5, label="GM mujeres"),
                   Line2D([], [], marker="s", ls="", color=C["orange"], ms=6, label="GV varones"),
                   Line2D([], [], marker="D", ls="", color=C["ink"], ms=5, label="HARM"),
                   Line2D([], [], marker="|", ls="", color=C["aqua"], ms=10, mew=1.8, label="referencia")],
          loc="upper center", bbox_to_anchor=(0.45, -0.13), ncol=4, fontsize=7.2, handletextpad=0.2,
          columnspacing=0.7)
# dimensiones de la referencia
dims = ["salud", "empoderam.", "laboral"]
w = 0.2
cols = ["#8fb8ea", C["blue"], C["ink2"], C["ink3"]]
mk = [None, None, None, None]
x0 = np.arange(3)
for k, (p, gm, gv, hm, s, e, l, r, idg) in enumerate(P):
    vals = [s, e, l]
    col = [C["blue"], C["orange"], C["aqua"], C["ink2"]][k]
    a2.bar(x0 + (k - 1.5) * w, vals, w * 0.92, color=col, zorder=2, label=p,
           hatch="///" if p == "Guinea" else None, edgecolor="white" if p == "Guinea" else None, lw=0)
for j, d in enumerate(dims):
    pass
for k, v in enumerate([0.7069, 0.6037, 0.4891, 0.2701]):
    a2.text(1 + (k - 1.5) * w, v + 0.012, coma(v, 2), ha="center", va="bottom", fontsize=6.3, fontweight="bold")
a2.set_xticks(x0)
a2.set_xticklabels(dims, fontsize=8)
a2.set_ylim(0, 0.85)
a2.yaxis.set_major_formatter(fmt_coma(1))
data_axes(a2)
a2.set_title("Referencia por dimensión (Paso 3)", fontsize=9, pad=6)
a2.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), ncol=4, fontsize=7.2, handlelength=1.0,
          columnspacing=0.7, handletextpad=0.3)
save(fig, "p3_idg_paises")

# ------------------------------------------------------------------ 3) Argentina vs Tailandia (M/V)
filas = [("Bancas parlamentarias", (43.8, 56.2), (16.0, 84.0)),
         ("Con secundaria o más", (74.3, 72.2), (51.9, 56.7)),
         ("Participación laboral", (53.2, 72.2), (60.6, 76.6))]
fig, axs = new_fig(6.7, 2.2, ncols=2, sharey=True)
fig.subplots_adjust(wspace=0.16)
for j, (ax, pais) in enumerate(zip(axs, ["Argentina", "Tailandia"])):
    for i, (lab, arg, tha) in enumerate(filas):
        m, v = (arg, tha)[j]
        y = len(filas) - 1 - i
        ax.plot([m, v], [y, y], color="#d9d7d0", lw=3, zorder=1)
        ax.plot(m, y, "o", ms=7.5, color=C["blue"], mec="white", mew=1.2, zorder=3)
        ax.plot(v, y, "s", ms=7, color=C["orange"], mec="white", mew=1.2, zorder=3)
        lo_is_m = m < v
        ax.text(m + (-2.2 if lo_is_m else 2.2), y + 0.02, coma(m, 1), ha="right" if lo_is_m else "left", va="center",
                fontsize=7.4, color=C["ink"])
        ax.text(v + (2.2 if lo_is_m else -2.2), y + 0.02, coma(v, 1), ha="left" if lo_is_m else "right", va="center",
                fontsize=7.4, color=C["ink2"])
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.6, 2.6)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.xaxis.set_major_formatter(fmt_pct())
    ax.tick_params(axis="x", labelsize=7.6)
    ax.grid(axis="x", color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    extra = "MMR 45 · AFR 26,4" if j == 0 else "MMR 29 · AFR 26,1"
    ax.set_title(f"{pais}   ", fontsize=9, pad=5, loc="left")
    ax.text(1.0, 1.035, extra, transform=ax.transAxes, ha="right", va="bottom", fontsize=7.4, color=C["ink2"])
axs[0].set_yticks(range(3))
axs[0].set_yticklabels([f[0] for f in filas][::-1], fontsize=8)
fig.legend(handles=[Line2D([], [], marker="o", ls="", color=C["blue"], ms=7, label="mujeres"),
                    Line2D([], [], marker="s", ls="", color=C["orange"], ms=6.5, label="varones")],
           loc="lower center", bbox_to_anchor=(0.55, -0.2), ncol=2, fontsize=7.8, handletextpad=0.2)
save(fig, "p3_idg_arg_tha")

# ------------------------------------------------------------------ 4) la trampa de lectura
fig, (a1, a2) = new_fig(6.7, 2.6, nrows=2)
fig.subplots_adjust(hspace=0.55)


def escala(ax, x0, x1, mejor_derecha, titulo, nota):
    m = 0.1 * (x1 - x0)
    ax.set_xlim(x0 - m, x1 + m)
    ax.set_ylim(-1.35, 1.75)
    ax.axis("off")
    ax.plot([x0, x1], [0, 0], color=C["ink3"], lw=1.4, zorder=1)
    if mejor_derecha:
        ax.annotate("", xy=(x1, 0), xytext=(x0, 0), arrowprops=dict(arrowstyle="-|>", color=C["green"], lw=1.8,
                    mutation_scale=11))
        izq, der = ("peor", C["red"]), ("mejor", C["green"])
    else:
        ax.annotate("", xy=(x0, 0), xytext=(x1, 0), arrowprops=dict(arrowstyle="-|>", color=C["green"], lw=1.8,
                    mutation_scale=11))
        izq, der = ("mejor", C["green"]), ("peor", C["red"])
    ax.text(x0 - 0.015 * (x1 - x0), 0, izq[0], ha="right", va="center", fontsize=8, color=izq[1], fontweight="bold")
    ax.text(x1 + 0.015 * (x1 - x0), 0, der[0], ha="left", va="center", fontsize=8, color=der[1], fontweight="bold")
    ax.text(x0 - m, 1.75, titulo, ha="left", va="bottom", fontsize=8.8, fontweight="bold")
    ax.text(x1 + m, 1.75, nota, ha="right", va="bottom", fontsize=7.8, color=C["green"], fontweight="bold")


def punto(ax, v, lab, tier, ha, col, bold):
    ax.plot(v, 0, "o", ms=7.5, color=col, mec="white", mew=1.3, zorder=3)
    y = {1: 0.45, -1: -0.45, -2: -0.95, 2: 0.95}[tier]
    if abs(tier) == 2:
        ax.plot([v, v], [0, y * 0.8], color=C["ink3"], lw=0.6, zorder=1)
    ax.text(v, y, lab, ha=ha, va="bottom" if tier > 0 else "top", fontsize=7.4, color=C["ink"],
            fontweight="bold" if bold else "normal")


escala(a1, 0.0, 0.14, True, "Índice de salud reproductiva de las mujeres (Paso 1 del IDG): un LOGRO",
       "más alto = mejor")
punto(a1, 0.0281, "Namibia 0,0281", -1, "center", C["blue"], True)
punto(a1, 0.0464, "Honduras 0,0464", 1, "center", C["blue"], True)
punto(a1, 0.0917, "Argentina 0,0917", 1, "center", C["ink3"], False)
punto(a1, 0.1149, "Tailandia 0,1149", -1, "center", C["ink3"], False)
escala(a2, 0.0, 0.7, False, "IDG final (Paso 4): mide DESIGUALDAD, 0 = igualdad perfecta", "más bajo = mejor")
for v, lab, tier, ha, par in ((0.217, "Costa Rica 0,217", 1, "right", False), (0.268, "Barbados 0,268", 1, "left", True),
                              (0.454, "Guyana 0,454", 2, "center", True), (0.609, "Guinea 0,609", 1, "center", False),
                              (0.264, "Argentina 0,264", -1, "right", False), (0.335, "Jamaica 0,335", -1, "left", True),
                              (0.289, "Tailandia 0,289", -2, "center", False)):
    punto(a2, v, lab, tier, ha, C["orange"] if par else C["ink3"], par)
save(fig, "p3_idg_trampa")
