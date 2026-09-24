"""Parciales resueltos · Cómo usar este documento.
Figura 0.1 — mapa de calor temas × exámenes (cantidad de incisos, contados sobre CLAVE_PARCIALES.md).
Figura 0.2 — valor esperado de responder al azar según las opciones que quedan.
Correr desde figs/:  python3 x1_intro.py
"""
import sys; sys.path.insert(0, "../lib")
from econ_style import *
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle


def coma(v, d=2):
    return f"{v:.{d}f}".replace(".", ",").replace("-", "−")


# --------------------------------------------------------------------------------------------
# Figura 0.1 — mapa de calor
# Cada inciso se cuenta en el tema que evalúa (ver la lista en el pie de la figura del HTML).
#            P1 P2 P3 P4 P5 P6 P7 P8 P9
ROWS = [
    ("Tema 1", "Sen y las libertades",      [1, 1, 0, 1, 1, 0, 0, 1, 1]),
    ("Tema 1", "Crecimiento vs desarrollo", [0, 0, 0, 1, 1, 0, 0, 0, 1]),
    ("Tema 2", "PBI, TC de mercado y PPA",  [4, 5, 0, 1, 1, 2, 2, 0, 0]),
    ("Tema 2", "Tasas de crecimiento",      [0, 0, 0, 0, 0, 2, 2, 0, 0]),
    ("Tema 2", "Índice Big Mac",            [0, 0, 0, 0, 0, 0, 0, 2, 0]),
    ("Tema 2", "IDH",                       [0, 1, 2, 0, 0, 1, 1, 1, 0]),
    ("Tema 2", "IDH-D y pérdida",           [0, 4, 2, 0, 0, 1, 1, 1, 0]),
    ("Tema 2", "IDG",                       [0, 0, 1, 0, 0, 1, 1, 0, 1]),
    ("Tema 2", "IPS",                       [1, 1, 0, 0, 0, 0, 0, 0, 0]),
    ("Tema 3", "Harrod-Domar",              [0, 1, 0, 0, 0, 0, 0, 0, 0]),
    ("Tema 3", "Solow sin tecnología",      [5, 3, 0, 0, 0, 0, 0, 0, 0]),
    ("Tema 3", "Solow con tecnología",      [0, 1, 0, 1, 1, 3, 3, 3, 1]),
    ("Tema 3", "Romer",                     [0, 0, 0, 0, 0, 0, 0, 0, 0]),
]
COLS = [("P1", "2022"), ("P2", "2023"), ("P3", "s/f"), ("P4", "2024 T"), ("P5", "2024 T"),
        ("P6", "2024 P"), ("P7", "2024 P"), ("P8", "2025 P"), ("P9", "2025 T")]

M = np.array([r[2] for r in ROWS])
nr, nc = M.shape
assert M.sum() == 73, M.sum()

cmap = LinearSegmentedColormap.from_list("azul", ["#dcebfb", "#8dbbec", C["blue"], "#184f95", "#0e2f5a"])
vmax = 5
TIPO = ["mixto", "mixto", "práctico", "teórico", "teórico", "práctico", "práctico", "práctico",
        "teórico"]
ANIO = ["2022", "2023", "s/fecha", "2024", "2024", "2024", "2024", "2025", "2025"]

# unidades: x = ancho de celda (0,43 in), y = alto de fila (0,26 in)
CW, RH = 0.43, 0.26
XL, XR = -5.2, nc + 1.9
YB, YT = -0.9, nr + 1.75
fig = plt.figure(figsize=((XR - XL) * CW, (YT - YB) * RH))
ax = fig.add_axes([0, 0, 1, 1])
gap = 0.07
for i in range(nr):
    for j in range(nc):
        v = M[i, j]
        y = nr - 1 - i
        fc = "#f4f3ef" if v == 0 else cmap((v - 1) / (vmax - 1))
        ax.add_patch(Rectangle((j + gap / 2, y + gap), 1 - gap, 1 - 2 * gap, fc=fc, ec="none"))
        if v:
            ax.text(j + 0.5, y + 0.5, str(v), ha="center", va="center", fontsize=9.5, fontweight="bold",
                    color="white" if v >= 3 else C["ink"])
# columna de totales por tema (barra + número)
tot_r = M.sum(axis=1)
xt = nc + 0.3
for i, t in enumerate(tot_r):
    y = nr - 1 - i
    w = t / tot_r.max() * 1.05
    if t:
        ax.add_patch(Rectangle((xt, y + 0.25), w, 0.5, fc=C["ink3"], ec="none"))
    ax.text(xt + w + 0.08, y + 0.5, str(t), ha="left", va="center", fontsize=8.8, color=C["ink"],
            fontweight="bold")
ax.text(xt, nr + 0.2, "Total", ha="left", va="bottom", fontsize=8.6, color=C["ink"], fontweight="bold")
# Romer: sólo como distractor
ax.text(0.15, 0.5, "no se evalúa: sólo aparece como opción trampa (P5, pregunta 3 c)", ha="left",
        va="center", fontsize=7.8, style="italic", color=C["ink2"])
# totales por examen
tot_c = M.sum(axis=0)
ax.plot([0, nc], [-0.02, -0.02], color=C["ink2"], lw=0.8)
for j, t in enumerate(tot_c):
    ax.text(j + 0.5, -0.45, str(t), ha="center", va="center", fontsize=8.8, fontweight="bold", color=C["ink"])
ax.text(-0.18, -0.45, "Incisos por examen", ha="right", va="center", fontsize=8.4, color=C["ink"],
        fontweight="bold")
# encabezados de columna: P, año, tipo
for j, (p, a) in enumerate(COLS):
    ax.text(j + 0.5, nr + 1.05, p, ha="center", va="bottom", fontsize=9.5, fontweight="bold", color=C["ink"])
    ax.text(j + 0.5, nr + 0.62, ANIO[j], ha="center", va="bottom", fontsize=7.4, color=C["ink2"])
    t = TIPO[j].replace(" + ", "+")
    ax.text(j + 0.5, nr + 0.2, t, ha="center", va="bottom", fontsize=6.2, color=C["ink3"])
# rótulos de fila + separadores y bandas de tema
prev = None
for i, (tema, lab, _) in enumerate(ROWS):
    y = nr - 1 - i
    ax.text(-0.18, y + 0.5, lab, ha="right", va="center", fontsize=8.8, color=C["ink"])
    if tema != prev and i > 0:
        ax.plot([XL + 0.35, nc + 1.75], [y + 1, y + 1], color=C["ink3"], lw=0.8)
    prev = tema
bands = {"Tema 1": (0, 2), "Tema 2": (2, 9), "Tema 3": (9, 13)}
colors_t = {"Tema 1": C["violet"], "Tema 2": C["blue"], "Tema 3": C["aqua"]}
for tema, (a, b) in bands.items():
    y0, y1 = nr - b, nr - a
    ax.add_patch(Rectangle((XL + 0.35, y0 + 0.1), 0.09, y1 - y0 - 0.2, fc=colors_t[tema], ec="none"))
    ax.text(XL + 0.26, (y0 + y1) / 2, tema.replace("Tema ", "T"), rotation=90, ha="right", va="center",
            fontsize=7.6, color=C["ink2"], fontweight="bold")
ax.set_xlim(XL, XR)
ax.set_ylim(YB, YT)
ax.axis("off")
fig.savefig(OUT / "x1_mapa_calor.svg", format="svg", metadata={"Date": None}, bbox_inches=None)
plt.close(fig)

# --------------------------------------------------------------------------------------------
# Figura 0.2 — valor esperado de responder al azar
m = np.array([5, 4, 3, 2])
mm = np.linspace(2, 5, 200)
ev_t = lambda k: 10 / k - 5 * (k - 1) / k          # teórica: +10 / −5
ev_p = lambda k: 5 / k - 2.5 * (k - 1) / k         # práctica, inciso de 5 ptos: +5 / −2,5

fig, ax = new_fig(6.0, 3.1)
Y0, Y1 = -2.85, 3.45
ax.axhspan(0, Y1, color=C["green_bg"], zorder=0)
ax.axhspan(Y0, 0, color=C["red_bg"], zorder=0)
ax.axhline(0, color=C["ink2"], lw=1.0, zorder=2)
ax.plot(mm, ev_t(mm), color=C["blue"], lw=LW, zorder=3)
ax.plot(mm, ev_p(mm), color=C["orange"], lw=LW, ls="--", zorder=3)
ax.plot(m, ev_t(m), "o", ms=7, color=C["blue"], mec="white", mew=1.5, zorder=4)
ax.plot(m, ev_p(m), "s", ms=6, color=C["orange"], mec="white", mew=1.4, zorder=4)
lab_t = {5: "−2", 4: "−1,25", 2: "+2,5"}
lab_p = {5: "−1", 4: "−0,63", 2: "+1,25"}
for k, t in lab_t.items():
    off = (0, -11) if k != 2 else (-15, 4)
    ax.annotate(t, (k, ev_t(k)), xytext=off, textcoords="offset points", ha="center", va="center",
                fontsize=8.8, fontweight="bold", color=C["ink"])
for k, t in lab_p.items():
    off = (0, 10) if k != 2 else (12, -13)
    ax.annotate(t, (k, ev_p(k)), xytext=off, textcoords="offset points", ha="center", va="center",
                fontsize=8.2, color=C["ink2"])
# punto de equilibrio
ax.plot([3], [0], "o", ms=11, mfc="white", mec=C["ink"], mew=1.8, zorder=5)
ax.annotate("punto de equilibrio: con 3 opciones\nen pie, arriesgar vale 0 en promedio", (3, 0),
            xytext=(4.35, 2.35), fontsize=8.4, ha="center", va="center", color=C["ink"], fontweight="bold",
            arrowprops=dict(arrowstyle="-|>", color=C["ink2"], lw=1.0, mutation_scale=8, shrinkA=4, shrinkB=7))
ax.text(3.0, Y1 - 0.2, "conviene arriesgar", fontsize=8.2, color=C["green"], fontweight="bold", va="top",
        ha="center")
ax.text(1.85, Y0 + 0.2, "conviene dejar en blanco", fontsize=8.2, color=C["red"], fontweight="bold", ha="right",
        va="bottom")
ax.annotate("teórica (+10 / −5)", (2.35, ev_t(2.35)), xytext=(-8, 8), textcoords="offset points", ha="right",
            va="bottom", fontsize=8.6, fontweight="bold", color=C["blue"])
ax.text(5.2, 0.22, "práctica, inciso de 5 ptos (+5 / −2,5)", ha="left", va="bottom", fontsize=8.2,
        fontweight="bold", color=C["orange"])
ax.set_xlim(5.3, 1.75)
ax.set_ylim(Y0, Y1)
ax.set_xticks([5, 4, 3, 2])
ax.set_xticklabels(["5 opciones", "4", "3", "2"])
ax.set_yticks([-2, -1, 0, 1, 2, 3])
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:+.0f}".replace("+0", "0").replace("-", "−")))
data_axes(ax, "opciones que siguen en pie cuando elegís al azar  (descartar = moverse a la derecha)",
          "puntos esperados")
ax.xaxis.label.set_size(8.4)
ax.xaxis.label.set_color(C["ink2"])
save(fig, "x1_valor_esperado")
