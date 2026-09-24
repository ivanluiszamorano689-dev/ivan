"""TP2 Parte B: índice Big Mac — barras divergentes de sub/sobrevaluación.
Correr desde figs/:  python3 p2_bigmac.py"""
from p2_util import *  # noqa: F403

# (país, precio en US$, sub/sobrevaluación %) tal como quedan en las tablas resueltas del TP2 (ej. 7 y 8)
# y del parcial 2025 (ej. 2). Todos verificados con precio local / TCm y TC PPA / TCm - 1.
bm2021 = dict(us=4.89, datos=[("Argentina", 3.75, -23.35), ("Australia", 4.98, 1.93), ("Chile", 4.09, -16.43),
                              ("China", 3.46, -29.31), ("Colombia", 3.74, -23.47), ("Costa Rica", 3.83, -21.70),
                              ("Guatemala", 3.21, -34.46), ("India", 2.59, -47.03), ("Israel", 5.35, 9.41),
                              ("Japón", 3.74, -23.52), ("México", 2.68, -45.19), ("Noruega", 6.09, 24.54),
                              ("Uruguay", 4.80, -1.84)])
bm2025 = dict(us=5.79, datos=[("Argentina", 6.952, 20.08), ("Australia", 4.870, -15.89), ("Canadá", 5.429, -6.23),
                              ("Chile", 4.548, -21.45), ("China", 3.518, -39.24), ("Costa Rica", 5.902, 1.93),
                              ("Dinamarca", 5.487, -5.24), ("Japón", 3.110, -46.29), ("Corea del Sur", 3.843, -33.63),
                              ("México", 4.601, -20.53), ("Noruega", 6.674, 15.27), ("Pakistán", 3.765, -34.97),
                              ("Qatar", 4.120, -28.85), ("Arabia Saudita", 5.066, -12.52)])
bm2024 = dict(us=5.69, datos=[("Emiratos Árabes", 18 / 3.67, 100 * (18 / 5.69 / 3.67 - 1)),
                              ("Australia", 7.75 / 1.53, 100 * (7.75 / 5.69 / 1.53 - 1)),
                              ("Azerbaiyán", 6.15 / 1.70, 100 * (6.15 / 5.69 / 1.70 - 1)),
                              ("Bahrein", 1.7 / 0.38, 100 * (1.7 / 5.69 / 0.38 - 1))])


def divergente(nombre, bm, w=6.4, h=None, xlim=(-58, 36), titulo=None, marcar=("Argentina",), step=10, dec=2, dsub=2):
    filas = []
    for p, usd, sub in bm["datos"]:
        filas.append((p, sub, usd))
    filas.sort(key=lambda f: f[1])
    n = len(filas)
    h = h or 0.75 + 0.205 * n
    fig, ax = new_fig(w, h)
    for i, (p, v, usd) in enumerate(filas):
        col = C["blue"] if v > 0 else C["orange"]
        ax.barh(i, v, color=col, height=0.66, zorder=2)
        txt = coma(v, dsub, signo=True) + "%"
        ax.text(v + (0.8 if v >= 0 else -0.8), i, txt, va="center", ha="left" if v >= 0 else "right",
                fontsize=7.6, color=C["ink"], fontweight="bold" if p in marcar else "normal")
        # nombre del país del lado opuesto a la barra
        ax.text(-0.9 if v >= 0 else 0.9, i, f"{p}  (US$ {coma(usd, dec)})", va="center",
                ha="right" if v >= 0 else "left", fontsize=7.6, color=C["ink"],
                fontweight="bold" if p in marcar else "normal")
    ax.axvline(0, color=C["ink"], lw=1.0, zorder=3)
    ax.set_ylim(-0.7, n - 0.3)
    ax.set_xlim(*xlim)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.xaxis.set_major_formatter(fmt_pct(0, signo=True))
    ax.set_xticks(np.arange(np.ceil(xlim[0] / step) * step, xlim[1] + 0.1, step))
    ax.grid(axis="x", color="#ebe9e3", lw=0.8)
    ax.set_axisbelow(True)
    ax.set_xlabel(f"(TC PPA − TCm) / TCm  ·  Big Mac en EEUU = US$ {coma(bm['us'], 2)}", fontsize=8.3)
    sub = "◀ moneda SUBvaluada (Big Mac más barata que en EEUU)" if xlim[1] > 20 else "◀ todas SUBvaluadas"
    ax.text(xlim[0], n - 0.1, sub, fontsize=7.6,
            color=C["orange"], fontweight="bold", va="bottom", ha="left")
    if xlim[1] > 20:
        ax.text(xlim[1], n - 0.1, "SOBREvaluada ▶", fontsize=7.6, color=C["blue"], fontweight="bold",
                va="bottom", ha="right")
    ax.set_ylim(-0.7, n + 0.5)
    save(fig, nombre)


divergente("p2_bigmac_2021", bm2021, xlim=(-60, 36))
divergente("p2_bigmac_2025", bm2025, xlim=(-60, 36), dec=3)
divergente("p2_bigmac_2024jul", bm2024, w=4.2, xlim=(-48, 12), marcar=("Australia", "Bahrein"), h=1.75, dsub=1)
print("ok")
