"""TP2 Parte B: índice Big Mac — barras divergentes de sub/sobrevaluación.
Correr desde figs/:  python3 p2_bigmac.py"""
from p2_util import *  # noqa: F403

# (país, precio local, TCm) — datos de la práctica (TP2, ej. 7 y 8) y del parcial 2025 (ej. 2)
bm2021 = dict(us=4.89, datos=[("Argentina", 320, 85.37), ("Australia", 6.48, 1.30), ("Chile", 2940, 719.43),
                              ("China", 22.40, 6.48), ("Colombia", 12950, 3460.50), ("Costa Rica", 2350, 613.77),
                              ("Guatemala", 25, 7.80), ("India", 2.59 * 73.39, 73.39), ("Israel", 5.35 * 3.18, 3.18),
                              ("Japón", 3.74 * 104.30, 104.30), ("México", 54, 54 / 2.68), ("Noruega", 52, 52 / 6.09),
                              ("Uruguay", 204, 204 / 4.80)])
bm2025 = dict(us=5.79, datos=[("Argentina", 7300, 1050), ("Australia", 7.75, 1.591), ("Canadá", 7.81, 1.439),
                              ("Chile", 4490, 987.25), ("China", 25.50, 7.248), ("Costa Rica", 2990, 506.625),
                              ("Dinamarca", 39, 7.108), ("Japón", 480, 154.355), ("Corea del Sur", 5500, 1431.2),
                              ("México", 95, 20.647), ("Noruega", 75, 11.237), ("Pakistán", 1050, 1050 / 3.765),
                              ("Qatar", 15, 3.641), ("Arabia Saudita", 19, 3.751)])
bm2024 = dict(us=5.69, datos=[("Emiratos Árabes", 18, 3.67), ("Australia", 7.75, 1.53), ("Azerbaiyán", 6.15, 1.70),
                              ("Bahrein", 1.7, 0.38)])


def divergente(nombre, bm, w=6.4, h=None, xlim=(-58, 36), titulo=None, marcar=("Argentina",), step=10, dec=2):
    filas = []
    for p, pl, tc in bm["datos"]:
        ppa = pl / bm["us"]
        filas.append((p, 100 * (ppa / tc - 1), pl / tc))
    filas.sort(key=lambda f: f[1])
    n = len(filas)
    h = h or 0.9 + 0.25 * n
    fig, ax = new_fig(w, h)
    for i, (p, v, usd) in enumerate(filas):
        col = C["blue"] if v > 0 else C["orange"]
        ax.barh(i, v, color=col, height=0.66, zorder=2)
        txt = coma(v, 1, signo=True) + "%"
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
divergente("p2_bigmac_2024jul", bm2024, w=4.2, xlim=(-48, 12), marcar=("Australia", "Bahrein"), h=1.75)
print("ok")
