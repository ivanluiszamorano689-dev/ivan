"""Mapa de las 12 trampas que más se repiten en los parciales 2022-2025.

Correr desde figs/:  python3 x3_grilla.py   -> figs/out/x3_trampas_mapa.svg
Datos: clave de los parciales (CLAVE_PARCIALES.md); cada punto es un examen en el que la trampa
aparece en al menos un inciso (lista "Apareció en" de cada tarjeta de docs/parciales/90-grilla.html).
"""
import sys

sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403

EXAMS = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9"]
SUB = ["2022", "2023", "s/f", "2024", "2024", "2024", "2024", "2025", "2025"]
T1, T2, T3, TG = C["violet"], C["blue"], C["aqua"], C["orange"]
TRAPS = [
    ("1 · Sen no mide utilidad, felicidad ni PBI", T1, {"P1", "P2", "P4", "P5", "P9"}),
    ("2 · Palabras absolutas en CE y DH", T1, {"P2", "P4", "P5", "P9"}),
    ("3 · Sólo la tecnología da crecimiento per cápita", T3, {"P1", "P2", "P4", "P5", "P9"}),
    ("4 · “Curvas” (tasas) vs “funciones” (niveles)", T3, {"P1", "P2", "P6", "P7", "P8"}),
    ("5 · Olvidar A, invertir el cociente", T3, {"P1", "P2", "P7"}),
    ("6 · Leer mal los datos: α, g, “a” vs “un”", T3, {"P2", "P6", "P7", "P8"}),
    ("7 · TCm del transable, PPA de la canasta", T2, {"P1", "P2"}),
    ("8 · A TCm la brecha se agranda", T2, {"P1", "P2", "P4", "P5", "P6", "P7"}),
    ("9 · Tasas: período, fila, cantidad de períodos", T2, {"P6", "P7"}),
    ("10 · IDH-D: % y media geométrica", T2, {"P2", "P3", "P6", "P7", "P8"}),
    ("11 · Con qué índice se clasifica", T2, {"P3", "P6", "P7", "P8", "P9"}),
    ("12 · “Ninguna” y “n/a” también se marcan", TG, {"P1", "P2", "P5", "P6", "P7"}),
]

fig, ax = new_fig(6.4, 3.35)
n = len(TRAPS)
for i, (lbl, col, s) in enumerate(TRAPS):
    y = n - 1 - i
    if i % 2 == 0:
        ax.axhspan(y - 0.5, y + 0.5, color="#f7f6f2", zorder=0, lw=0)
    for j, e in enumerate(EXAMS):
        if e in s:
            ax.plot(j, y, "o", ms=8.2, color=col, mec="white", mew=1.0, zorder=3)
        else:
            ax.plot(j, y, "o", ms=3.0, color=C["rule"], zorder=2)
    ax.text(len(EXAMS) - 0.35, y, f"{len(s)}", ha="left", va="center", fontsize=8.6, fontweight="bold",
            color=C["ink"])
ax.set_yticks(range(n))
ax.set_yticklabels([t[0] for t in TRAPS][::-1], fontsize=8.9)
for tl, t in zip(ax.get_yticklabels(), TRAPS[::-1]):
    tl.set_color(C["ink"])
ax.set_xticks(range(len(EXAMS)))
ax.set_xticklabels([f"{e}\n{s}" for e, s in zip(EXAMS, SUB)], fontsize=8.6)
ax.xaxis.tick_top()
ax.tick_params(axis="both", length=0)
for sp in ax.spines.values():
    sp.set_visible(False)
ax.set_xlim(-0.6, len(EXAMS) + 0.1)
ax.set_ylim(-0.6, n - 0.4)
ax.text(len(EXAMS) - 0.35, n - 0.25, "exámenes", ha="left", va="bottom", fontsize=7.6, color=C["ink2"])
save(fig, "x3_trampas_mapa")
print("ok", [len(t[2]) for t in TRAPS])
