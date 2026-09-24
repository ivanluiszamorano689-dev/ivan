"""§0 · Plan de los 60 minutos del parcial (línea de tiempo)."""
from s0_util import *

fig, ax, H = canvas(6.6, 2.6)
x0, x1 = 3.0, 97.0
u = (x1 - x0) / 60.0          # unidades de dibujo por minuto
yb = H - 9.0                  # centro de la barra
bh = 4.2

segs = [
    (0, 4, "gray", "1 · Leer todo", "Clasificá cada ejercicio con el mapa (§1\u00a0a\u00a0§4) y pasá los % a decimales al margen."),
    (4, 12, "violet", "2 · Teóricas", "≈ 2 min cada una. Primero las seguras; a las dudosas poneles «?» y seguí."),
    (12, 20, "aqua", "3 · Lo seguro", "Incisos de una sola cuenta: TCm, IDH con índices dados, crecimiento de un año."),
    (20, 50, "blue", "4 · Cuentas", "Solow, TC PPA, IDH-D, tasas medias, Big Mac, gráfico. Regla: 0,6 min por punto."),
    (50, 56, "orange", "5 · Controles", "Pasá cada resultado por su control (§0\u00a0d). Dudosas: decidí con el valor esperado."),
    (56, 60, "gray", "6 · Repaso", "¿Marcaste la opción que calculaste? Redondeo pedido, rótulos del gráfico."),
]

# barra
for a, b, col, *_ in segs:
    rbox(ax, x0 + a * u + 0.15, yb - bh / 2, (b - a) * u - 0.3, bh, col, fill="solid", lw=0, r=0.8)
    if b - a >= 6:
        txt(ax, x0 + (a + b) / 2 * u, yb, f"{b - a} min", size=7.4, color="white", weight="bold")
# escala de minutos
for m in range(0, 61, 5):
    xm = x0 + m * u
    ax.plot([xm, xm], [yb + bh / 2 + 0.4, yb + bh / 2 + 1.3], color=C["ink3"], lw=0.8)
    txt(ax, xm, yb + bh / 2 + 2.9, f"{m}'", size=7.2, color=C["ink2"])

# tarjetas
n = len(segs)
gap = 1.4
cw = (x1 - x0 - gap * (n - 1)) / n
ctop = yb - bh / 2 - 5.2
ch = ctop - 1.0
for i, (a, b, col, title, body) in enumerate(segs):
    cx = x0 + i * (cw + gap)
    rbox(ax, cx, 1.0, cw, ch, col, fill="bg", lw=1.0, r=1.2)
    txt(ax, cx + 1.1, ctop - 1.9, title, size=7.8, weight="bold", color=DARK[col], ha="left")
    txt(ax, cx + 1.1, ctop - 3.9, f"{a}–{b} min", size=6.8, color=C["ink3"], ha="left")
    txt(ax, cx + 1.1, ctop - 5.6, body, size=6.9, ha="left", va="top", n=17, ls=1.22)
    # conector segmento -> tarjeta
    sx = x0 + (a + b) / 2 * u
    mx = cx + cw / 2
    ym = yb - bh / 2 - 2.6
    ax.plot([sx, sx, mx, mx], [yb - bh / 2 - 0.2, ym, ym, ctop + 0.2], color=MID[col], lw=0.9, zorder=1)
save(fig, "s0_plan60")
