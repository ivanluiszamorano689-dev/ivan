"""TP2 Parte C: tipo de cambio de mercado vs PPA.
Cuadro de valuación (cantidades x precios), barras transable/no transable y cocientes.
Correr desde figs/:  python3 p2_ppa.py"""
from p2_util import *  # noqa: F403


# ---------------------------------------------------------------- cuadro de valuación 2x2
def cuadro(nombre, cols, filas, celdas, ppa_lab, tcm_lab, tcm_box, nota=None, w=6.5, h=3.45):
    """cols: (col A, col B); filas: (fila A, fila B);
    celdas: dict (i, j) -> texto; i = fila (0 = A, 1 = B), j = columna (0 = precios A, 1 = precios B)."""
    fig, ax = new_fig(w, h)
    ax.set_xlim(0, 13.4)
    ax.set_ylim(-1.4, 6.2)
    ax.axis("off")
    xc = (5.2, 11.2)
    yr = (4.05, 1.75)
    cw, ch = 4.2, 1.75
    for j, t in enumerate(cols):
        ax.text(xc[j], 5.65, t, ha="center", va="center", fontsize=8.6, fontweight="bold", color=C["ink"],
                linespacing=1.25)
    for i, t in enumerate(filas):
        ax.text(0.05, yr[i], t, ha="left", va="center", fontsize=8.2, color=C["ink"], linespacing=1.3)
    estilos = {(0, 0): (C["blue_bg"], C["blue"], "-", "bold"), (0, 1): ("#ffffff", C["ink3"], "--", "normal"),
               (1, 0): (C["aqua_bg"], C["aqua"], "-", "bold"), (1, 1): (C["orange_bg"], C["orange"], "-", "bold")}
    for (i, j), txt in celdas.items():
        fc, ec, ls, wt = estilos[(i, j)]
        caja(ax, xc[j], yr[i], cw, ch, txt, fc=fc, ec=ec, ls=ls, lw=1.6 if ls == "-" else 1.1, size=8.0,
             weight="normal")
    for i in range(2):
        flecha(ax, xc[1] - cw / 2 - 0.05, yr[i], xc[0] + cw / 2 + 0.05, yr[i], color=C["violet"], lw=1.5,
               texto=ppa_lab, tdy=0.1, size=8.3)
    # ruta del tipo de cambio de mercado
    ybox = -0.55
    caja(ax, xc[0], ybox, cw, 1.5, tcm_box, fc=C["red_bg"], ec=C["red"], lw=1.2, size=8.0)
    ax.annotate("", xy=(xc[0] + cw / 2 + 0.05, ybox), xytext=(xc[1], yr[1] - ch / 2 - 0.03),
                arrowprops=dict(arrowstyle="-|>", color=C["red"], lw=1.4, mutation_scale=10, shrinkA=0,
                                shrinkB=0, connectionstyle="angle,angleA=-90,angleB=180,rad=0"))
    ax.text(xc[1] + 0.12, (yr[1] - ch / 2 + ybox) / 2 - 0.05, tcm_lab, ha="left", va="center", fontsize=8.3,
            color=C["red"], fontweight="bold")
    if nota:
        ax.text(0.05, ybox, nota, ha="left", va="center", fontsize=7.6, color=C["ink2"], linespacing=1.3)
    save(fig, nombre)


cuadro("p2_cuadro_rp",
       cols=("a precios de A · Ricolandia\n(en US$)", "a precios de B · Pobrelandia\n(en $)"),
       filas=("A · Ricolandia\n800 t de soja\n4.800 lavados", "B · Pobrelandia\n500 t de soja\n3.000 lavados"),
       celdas={(0, 0): r"$\sum Q_A\,P_A$" + "\nUS\\$ 800.000\nPBI de Ricolandia",
               (0, 1): r"$\sum Q_A\,P_B$" + "\n\\$ 1.440.000\ncanasta de A a precios de B",
               (1, 0): r"$\sum Q_B\,P_A$" + "\nUS\\$ 500.000\n= PBI de Pobrelandia a PPA",
               (1, 1): r"$\sum Q_B\,P_B$" + "\n\\$ 900.000\nPBI de Pobrelandia"},
       ppa_lab="÷ TC PPA\n= 1,8", tcm_lab="÷ TCm = 3\n(sólo el\ntransable)",
       tcm_box="US$ 300.000\nPBI de B a TCm: subvalúa\nel no transable",
       nota="TC PPA =\ncociente de\ncada fila")


# ---------------------------------------------------------------- barras transable / no transable
def barras(nombre, filas, tlab, nlab, xmax, notas, w=6.5, h=1.7, unidad="US$"):
    """filas: lista (rótulo, transable, no transable) de arriba hacia abajo."""
    fig, ax = new_fig(w, h)
    n = len(filas)
    for k, (lab, t, nt) in enumerate(filas):
        y = n - 1 - k
        ax.barh(y, t, color=C["aqua"], height=0.6, zorder=2)
        ax.barh(y, nt, left=t, color=C["blue"], height=0.6, zorder=2)
        ax.text(t + nt + xmax * 0.012, y, f"{unidad} {miles(t + nt)}".strip(), va="center", fontsize=8.3,
                fontweight="bold", color=C["ink"])
        if nt > xmax * 0.09:
            ax.text(t + nt / 2, y, f"{miles(nt)}", va="center", ha="center", fontsize=7.4, color="white")
    ax.set_yticks(range(n))
    ax.set_yticklabels([f[0] for f in filas][::-1], fontsize=8.2)
    ax.set_xlim(0, xmax)
    ax.xaxis.set_major_formatter(fmt_miles())
    ax.grid(axis="x", color="#ebe9e3", lw=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.bar(0, 0, color=C["aqua"], label=tlab)
    ax.bar(0, 0, color=C["blue"], label=nlab)
    ax.legend(loc="lower right", fontsize=7.8, ncol=1, handlelength=1.0, borderaxespad=0.2)
    for (x, y, txt) in notas:
        ax.text(x, y, txt, fontsize=7.6, color=C["ink2"], va="center", ha="left", linespacing=1.25)
    save(fig, nombre)


barras("p2_barras_rp",
       [("Ricolandia", 80000, 720000), ("Pobrelandia a TCm (÷ 3)", 50000, 250000),
        ("Pobrelandia a PPA (÷ 1,8)", 50000, 450000)],
       "transable: soja", "no transable: lavados", 1010000, [])
barras("p2_barras_ns",
       [("Los del Norte", 25000, 375000), ("Los del Sur a TCm (÷ 300)", 10000, 10000),
        ("Los del Sur a PPA (÷ 37,5)", 10000, 150000)],
       "transable: termos", "no transable: consultas", 505000, [], unidad="")

# ---------------------------------------------------------------- cocientes a TCm vs a PPA
casos = [("Norte / Sur (TP2, ej. 10)", 20.0, 2.5),
         ("EEUU / Ucrania 2020, per cápita (parcial 2024)", 64317 / 3752, 64317 / 15717),
         ("EEUU / Rusia 2020, per cápita (parcial 2024)", 64317 / 10108, 64317 / 31491),
         ("Norte Unidos / Argensur (parcial 2022)", 92000 / 17500, 92000 / 23000),
         ("Dolar City / Ciudad Pesos (parcial 2023)", 51000 / 18500, 51000 / 42500),
         ("Ricolandia / Pobrelandia (TP2, ej. 9)", 800000 / 300000, 800000 / 500000)]
fig, ax = new_fig(6.5, 2.1)
n = len(casos)
for k, (lab, tcm, ppa) in enumerate(casos):
    y = n - 1 - k
    ax.plot([ppa, tcm], [y, y], color=C["rule"], lw=4, solid_capstyle="round", zorder=1)
    ax.annotate("", xy=(ppa * 1.04, y), xytext=(tcm / 1.04, y),
                arrowprops=dict(arrowstyle="-|>", color=C["ink3"], lw=1.0, mutation_scale=8, shrinkA=0, shrinkB=0))
    ax.plot(tcm, y, "o", ms=8, color=C["orange"], mec="white", mew=1.2, zorder=3)
    ax.plot(ppa, y, "o", ms=8, color=C["blue"], mec="white", mew=1.2, zorder=3)
    ax.text(tcm * 1.08, y, coma(tcm, 2), va="center", ha="left", fontsize=7.8, color=C["orange"], fontweight="bold")
    ax.text(ppa / 1.08, y, coma(ppa, 2), va="center", ha="right", fontsize=7.8, color=C["blue"], fontweight="bold")
ax.set_xscale("log")
ax.set_xlim(0.7, 40)
ax.set_xticks([1, 2, 5, 10, 20])
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:g}×"))
ax.xaxis.set_minor_formatter(plt.NullFormatter())
ax.set_yticks(range(n))
ax.set_yticklabels([c[0] for c in casos][::-1], fontsize=7.9)
ax.tick_params(axis="y", length=0)
ax.spines["left"].set_visible(False)
ax.axvline(1, color=C["ink3"], lw=0.8, ls=(0, (2, 2)))
ax.grid(axis="x", color="#ebe9e3", lw=0.8)
ax.set_axisbelow(True)
ax.set_xlabel("¿Cuántas veces más grande es el país rico? (escala logarítmica)", fontsize=8.3)
ax.plot([], [], "o", color=C["orange"], label="a tipo de cambio de mercado")
ax.plot([], [], "o", color=C["blue"], label="a PPA")
ax.legend(loc="lower right", fontsize=7.8, handletextpad=0.3, borderaxespad=0.2)
save(fig, "p2_cocientes")
print("ok")
