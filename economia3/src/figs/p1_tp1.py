"""Diagramas y gráficos del TP1 (práctica). Correr desde figs/: python3 p1_tp1.py"""
from p1_util import *  # noqa: F401,F403
from econ_style import econ_axes, data_axes, save, LW, new_fig, label_curve, vguide  # noqa: E402
from matplotlib.patches import Ellipse, Rectangle, Wedge  # noqa: E402

INK, INK2, INK3 = C["ink"], C["ink2"], C["ink3"]

# ============================================================== TP1.1 La cadena de Sen
fig, ax, W, H = canvas(6.8, 3.75, W=100)
# banda superior: libertad
box(ax, 1, H - 8.6, 98, 7.6, fc=C["violet_bg"], ec=C["violet"], lw=1.1, ls="--")
ax.text(50, H - 2.6, "LIBERTAD (supracapacidad): el marco de derechos que hace posible elegir", ha="center",
        va="center", fontsize=8.6, fontweight="bold", color="#3a2d86")
ax.text(50, H - 6.3, "Ej. de la cátedra: el Estado garantiza el derecho a estudiar → poder estudiar de verdad (capacidad) "
        "→ estudiar (funcionamiento)", ha="center", va="center", fontsize=7.3, color="#3a2d86")
cols = [
    ("Bienes y recursos", "ingreso, bienes\nprimarios (Rawls)", "lo que la persona TIENE", C["blue"], C["blue_bg"]),
    ("Factores de conversión", "edad · género · salud ·\ndiscapacidad · entorno ·\nservicios públicos",
     "cambian de persona a persona", INK2, C["gray_bg"]),
    ("Capacidades", "conjunto de capacidad =\nel MENÚ: lo que la persona\nPUEDE ser o hacer", "acá evalúa Sen el desarrollo",
     C["aqua"], C["aqua_bg"]),
    ("Funcionamientos", "lo que efectivamente\nES o HACE = el PLATO\nelegido", "lo que ELIGE y logra (agencia)", C["orange"],
     C["orange_bg"]),
]
xs = [1, 26.3, 51.6, 76.9]
bw = 22.1
ytop, bh = 23.8, 16.5
for (tit, txt, pie, ec, fc), x in zip(cols, xs):
    box(ax, x, ytop, bw, bh, fc=fc, ec=ec, lw=1.8 if tit == "Capacidades" else 1.3)
    ax.text(x + bw / 2, ytop + bh - 1.6, tit, ha="center", va="top", fontsize=9.2, fontweight="bold", color=INK)
    ax.text(x + bw / 2, ytop + bh - 5.4, txt, ha="center", va="top", fontsize=7.9, color=INK, linespacing=1.3)
    ax.text(x + bw / 2, ytop - 1.0, pie, ha="center", va="top", fontsize=7.4, color=INK2, style="italic")
for i in range(3):
    arr(ax, xs[i] + bw + 0.4, ytop + bh / 2, xs[i + 1] - 0.4, ytop + bh / 2, lw=1.6, ms=11)
# fila Añelo
ax.text(1, 17.2, "EN AÑELO (ej. 2)", ha="left", va="center", fontsize=7.8, fontweight="bold", color=INK2)
anelo = [
    "renta hidrocarburífera;\nsalario petrolero que cobra\nuna minoría",
    "+60 % de adultos sin\nsecundario, informalidad,\nsin gas ni cloacas → BAJA",
    "menú estrecho: sin empleo\ncalificado, sin crédito\nbarato ni vivienda",
    "morosidad, crédito caro\n(billeteras), traslado diario,\nsin protección social",
]
for t, x, (_, _, _, ec, fc) in zip(anelo, xs, cols):
    box(ax, x, 1.2, bw, 13.8, fc="white", ec=ec, lw=1.0, ls=(0, (4, 2)), text=t, size=7.7, linespacing=1.3)
for i in range(3):
    arr(ax, xs[i] + bw + 0.4, 8.1, xs[i + 1] - 0.4, 8.1, lw=1.1, ms=9, color=INK3)
save(fig, "p1_cadena_sen")

# ============================================================== TP1.2 Añelo en números
filas = [
    ("Mayores de 18 años sin secundario completo", 60, "más del 60 %", C["aqua"]),
    ("Camas por cada 100 personas que llegan a diario\n(menos de 10.000 camas para 35.000 personas)", 10000 / 35000 * 100,
     "menos de 29", C["blue"]),
    ("Empresas regularizadas (310 de 490)", 310 / 490 * 100, "63 %", C["violet"]),
    ("Complejos habitacionales habilitados (38 de 238)", 38 / 238 * 100, "16 %", C["violet"]),
    ("Deudores jóvenes con crédito de billeteras digitales", 36, "36 %", C["violet"]),
]
fig, ax = plt.subplots(figsize=(6.6, 2.55))
fig.subplots_adjust(left=0.47, right=0.97, top=0.86, bottom=0.08)
for i, (lab, v, txt, col) in enumerate(filas):
    y = len(filas) - 1 - i
    ax.barh(y, 100, height=0.52, color="#f0efec", zorder=1)
    ax.barh(y, v, height=0.52, color=col, zorder=2)
    ax.text(-2, y, lab, ha="right", va="center", fontsize=8.2, color=INK, linespacing=1.15)
    ax.text(v + 1.5, y, txt, ha="left", va="center", fontsize=8.4, color=INK, fontweight="bold", zorder=3)
ax.set_xlim(0, 100)
ax.set_ylim(-0.6, len(filas) - 0.4)
ax.axis("off")
for v in (0, 50, 100):
    ax.text(v, -0.62, f"{v} %", ha="center", va="top", fontsize=7.4, color=INK3)
from matplotlib.patches import Patch  # noqa: E402
ax.legend(handles=[Patch(color=C["aqua"], label="capacidad (educación)"),
                   Patch(color=C["blue"], label="infraestructura"),
                   Patch(color=C["violet"], label="informalidad")],
          loc="lower right", bbox_to_anchor=(1.0, 0.97), ncol=3, fontsize=7.6, handlelength=1.0, handleheight=0.8,
          columnspacing=1.3, handletextpad=0.5, labelcolor=INK2)
save(fig, "p1_anelo_numeros")

# ============================================================== TP1.3 Tasa de conversión (esquemático)
r = np.linspace(0, 10, 300)
alta = 3.2 * (1 - np.exp(-r / 3.0))
baja = 1.25 * (1 - np.exp(-r / 3.0))
fig, ax = new_fig(3.35, 2.75)
ax.plot(r, alta, color=C["blue"], lw=LW)
ax.plot(r, baja, color=C["orange"], lw=LW)
econ_axes(ax, "recursos", "capacidades", xlim=(0, 10.5), ylim=(0, 3.4))
r0, r1 = 3.0, 6.0
f = lambda x, a: a * (1 - np.exp(-x / 3.0))  # noqa: E731
for a, col in ((3.2, C["blue"]), (1.25, C["orange"])):
    ax.plot([r0, r1], [f(r0, a), f(r0, a)], color=INK3, lw=0.8, ls=(0, (2, 2)))
    ax.annotate("", xy=(r1, f(r1, a)), xytext=(r1, f(r0, a)),
                arrowprops=dict(arrowstyle="-|>", color=col, lw=1.4, mutation_scale=9))
vguide(ax, r0, f(r0, 3.2), r"$R_0$", size=8.5)
vguide(ax, r1, f(r1, 3.2), r"$R_1$", size=8.5)
ax.text(r1 + 0.25, (f(r0, 3.2) + f(r1, 3.2)) / 2, "mucha\nexpansión", fontsize=7.6, color=C["blue"], va="center")
ax.text(r1 + 0.25, (f(r0, 1.25) + f(r1, 1.25)) / 2 - 0.05, "poca", fontsize=7.6, color=C["orange"], va="center")
label_curve(ax, 10.3, 3.2 * (1 - np.exp(-10.3 / 3)), "conversión alta", C["blue"], dx=-2, dy=9, ha="right", size=8.2)
label_curve(ax, 10.3, 1.25 * (1 - np.exp(-10.3 / 3)), "conversión baja (Añelo)", C["orange"], dx=-2, dy=9,
            ha="right", size=8.2)
save(fig, "p1_conversion")

# ============================================================== TP1.4 Las cinco libertades se refuerzan
fig, ax, W, H = canvas(4.3, 3.3, W=100)
cx, cy, R = 50, H / 2 - 0.3, 29
orden = ["pol", "eco", "soc", "tra", "seg"]
nombres = {"pol": "Libertades\npolíticas", "eco": "Servicios\neconómicos", "soc": "Oportunidades\nsociales",
           "tra": "Garantías de\ntransparencia", "seg": "Seguridad\nprotectora"}
pos = {}
for i, k in enumerate(orden):
    ang = np.pi / 2 + i * 2 * np.pi / 5
    pos[k] = (cx + R * 1.28 * np.cos(ang), cy + R * np.sin(ang))
for i, a in enumerate(orden):
    for b in orden[i + 1:]:
        ax.plot([pos[a][0], pos[b][0]], [pos[a][1], pos[b][1]], color=C["rule"], lw=1.0, zorder=0)
bwid, bhei = 25, 11
for k in orden:
    col, bg, ink, _ = LIB[k]
    x, y = pos[k]
    box(ax, x - bwid / 2, y - bhei / 2, bwid, bhei, fc=bg, ec=col, lw=1.6, text=nombres[k], size=7.9,
        color=ink, weight="bold", linespacing=1.15)
    # flecha hacia el centro
    dx, dy = cx - x, cy - y
    d = np.hypot(dx, dy)
    ux, uy = dx / d, dy / d
    t0 = min(13.6 / max(abs(ux), 1e-6), 6.4 / max(abs(uy), 1e-6))
    t1 = d - min(15.0 / max(abs(ux), 1e-6), 7.2 / max(abs(uy), 1e-6))
    arr(ax, x + ux * t0, y + uy * t0, x + ux * t1, y + uy * t1, color=col, lw=1.5, ms=10)
box(ax, cx - 14, cy - 6.2, 28, 12.4, fc="white", ec=INK, lw=1.4, r=3,
    text="EXPANSIÓN DE\nLA LIBERTAD REAL\n= el desarrollo", size=7.6, weight="bold", linespacing=1.2)

save(fig, "p1_libertades_red")

# ============================================================== TP1.5 Criterio de decisión: ¿qué institución falla o funciona?
fig, ax, W, H = canvas(6.7, 4.8, W=100)
box(ax, 2, H - 7.0, 96, 6.0, fc=C["gray_bg"], ec=INK, lw=1.3,
    text="Leé la noticia y preguntate: ¿QUÉ INSTITUCIÓN FALLA O FUNCIONA?   (no: ¿de qué tema habla?)",
    size=8.8, weight="bold")
preg = [
    ("¿Hay información ocultada, corrupción, conflicto de\nintereses o un pedido de rendición de cuentas /\nacceso a la información?",
     "tra", "informe HLB · caminos de Colón · internet"),
    ("¿Se juega quién gobierna y cómo: elecciones, votos,\noposición, prensa, reclamo público, acceso a la\njusticia?",
     "pol", "ONPE · guerra civil en Yemen"),
    ("¿Es ayuda ante una crisis (ad hoc: hambruna,\ncatástrofe, guerra) o una red fija para el que cayó\n(desempleo, indigencia, vivienda)?",
     "seg", "Sudán · Ibrahim (Yemen) · hacinamiento"),
    ("¿Es acceso a salud o a educación: escuelas,\nhospitales, clínicas, vacunas?", "soc",
     "Belice · vacunas en Yemen · escuela"),
    ("¿Es crédito, financiamiento, precios, tarifas,\ningresos o funcionamiento de los mercados?", "eco",
     "deuda ganadera · leña y tarifas sociales"),
]
qx, qw, qh = 2, 50, 8.0
rx, rw = 63, 35
y = H - 10.0
for i, (q, k, ej) in enumerate(preg):
    col, bg, ink, nom = LIB[k]
    yb = y - qh
    box(ax, qx, yb, qw, qh, fc="white", ec=INK2, lw=1.1, text=q, size=7.6, ha="left", pad_x=2.2, linespacing=1.2)
    ax.text(qx - 0.2, yb + qh - 0.2, str(i + 1), ha="center", va="center", fontsize=7.5, fontweight="bold",
            color="white", bbox=dict(boxstyle="circle,pad=0.25", fc=INK2, ec="none"), zorder=5)
    box(ax, rx, yb + 0.3, rw, qh - 0.6, fc=bg, ec=col, lw=1.6)
    ax.text(rx + 2, yb + qh - 1.3, nom.upper(), ha="left", va="top", fontsize=8.0, fontweight="bold", color=ink)
    ax.text(rx + 2, yb + qh - 4.4, ej, ha="left", va="top", fontsize=7.1, color=INK2, linespacing=1.15)
    arr(ax, qx + qw + 0.4, yb + qh / 2, rx - 0.4, yb + qh / 2, color=col, lw=1.6, ms=10)
    ax.text((qx + qw + rx) / 2, yb + qh / 2 + 0.8, "Sí", ha="center", va="bottom", fontsize=8, fontweight="bold",
            color=ink)
    arr(ax, qx + 8, yb - 0.15, qx + 8, yb - 2.5, color=INK3, lw=1.2, ms=8)
    ax.text(qx + 9.2, yb - 1.3, "No", ha="left", va="center", fontsize=7.4, color=INK2, fontweight="bold")
    y = yb - 2.7
arr(ax, 10, H - 7.15, 10, H - 9.85, color=INK3, lw=1.2, ms=8)
box(ax, qx, y - 5.8, 96, 5.8, fc="white", ec=INK3, lw=1.0, ls=(0, (4, 2)),
    text="¿Caen dos? Nombrá la PRINCIPAL (la institución cuyo fallo explica la noticia) y mencioná la secundaria: suma puntos.",
    size=7.9, color=INK)
save(fig, "p1_flujo_libertades")

# ============================================================== TP1.6 Marcos y Sofía: mismo funcionamiento, distinto conjunto
fig, (a1, a2) = plt.subplots(1, 2, figsize=(5.6, 2.45))
fig.subplots_adjust(wspace=0.36)
for ax_, rad, tit in ((a1, 0.13, "Marcos: un menú de un solo plato"), (a2, 0.86, "Sofía: menú amplio, y eligió")):
    econ_axes(ax_, "seguir\nestudiando", "trabajo regulado", xlim=(0, 1.08), ylim=(0, 1.08))
    ax_.add_patch(Wedge((0, 0), rad, 0, 90, fc=C["aqua_bg"], ec=C["aqua"], lw=1.4))
    ax_.plot([0.035], [0.035], "o", ms=7.5, color=C["orange"], mec="white", mew=1.4, zorder=5, clip_on=False)
    ax_.set_title(tit, fontsize=8.6, loc="left", pad=20)
a1.annotate("conjunto de capacidad\n(casi vacío: faltaba\ningreso para la\ncanasta básica)", (0.08, 0.1),
            xytext=(0.3, 0.55), fontsize=7.6, color="#0f6e4c",
            arrowprops=dict(arrowstyle="-", color=C["aqua"], lw=0.8))
a1.annotate("funcionamiento\nobservado: fuera de\nla escuela y del\nempleo regulado", (0.04, 0.04), xytext=(0.42, 0.08),
            fontsize=7.6, color="#a8431b", arrowprops=dict(arrowstyle="-", color=C["orange"], lw=0.8))
a2.text(0.36, 0.14, "conjunto de\ncapacidad: podía\nestudiar, podía\ntrabajar", fontsize=7.6, color="#0f6e4c")
a2.annotate("mismo funcionamiento:\neligió arte y\nvoluntariado", (0.04, 0.04), xytext=(0.45, 0.86), fontsize=7.6,
            color="#a8431b", arrowprops=dict(arrowstyle="-", color=C["orange"], lw=0.8))
save(fig, "p1_marcos_sofia")

# ============================================================== TP1.7 Regla: ¿capacidad o funcionamiento?
fig, ax, W, H = canvas(6.7, 2.95, W=100)
box(ax, 1, 21, 32, 21, fc="white", ec=INK2, lw=1.2, size=8.0, linespacing=1.3,
    text="1. ¿El enunciado muestra que\nhabía ALTERNATIVAS y la persona\neligió (o podría elegir)?\n“decidió”, “prefirió”, “rechazó”,\n“podría haberse postulado”")
box(ax, 38, 2, 27, 17, fc="white", ec=INK2, lw=1.2, size=8.0, linespacing=1.3,
    text="2. Es un hecho ya realizado.\n¿Fue FORZADO por falta de\nalternativas (ingreso,\ncobertura, distancia)?")
res = [
    (30.5, "CAPACIDAD  (el menú)", "Lucía cuida a sus hijos · no fue a votar\n· Beyoncé ayuna · Paula · Joaquín",
     C["blue"], C["blue_bg"], "#184f95"),
    (15.5, "FUNCIONAMIENTO  (el plato)", "Mariela y Víctor se recibieron ·\ntransportista · Carlos (sobrepeso)",
     C["orange"], C["orange_bg"], "#a8431b"),
    (0.5, "FUNCIONAMIENTO por\nPRIVACIÓN de capacidad", "Jorge · Manuel · niño de 30 km ·\ntrabajo no registrado  (decilo: suma)",
     C["red"], C["red_bg"], "#a82b2a"),
]
for y0, t, ej, col, bg, ink in res:
    box(ax, 70, y0, 29, 13.2, fc=bg, ec=col, lw=1.6)
    ax.text(71.8, y0 + 12.2, t, ha="left", va="top", fontsize=8.0, fontweight="bold", color=ink, linespacing=1.15)
    ax.text(71.8, y0 + (5.6 if "\n" in t else 7.9), ej, ha="left", va="top", fontsize=6.9, color=INK2, linespacing=1.2)
arr(ax, 33.4, 37, 69.6, 37, color=C["blue"], lw=1.6)
ax.text(51, 37.8, "Sí", ha="center", va="bottom", fontsize=8.2, fontweight="bold", color="#184f95")
arr(ax, 17, 20.6, 17, 10.5, color=INK3, lw=1.3)
arr(ax, 17, 10.5, 37.6, 10.5, color=INK3, lw=1.3)
ax.text(18.2, 15.5, "No: describe un\nlogro o un estado", ha="left", va="center", fontsize=7.4, color=INK2)
arr(ax, 65.4, 14, 69.6, 21, color=C["orange"], lw=1.5)
ax.text(67.6, 14.2, "No", ha="left", va="center", fontsize=7.8, fontweight="bold", color="#a8431b")
arr(ax, 65.4, 7, 69.6, 7, color=C["red"], lw=1.5)
ax.text(67.5, 7.8, "Sí", ha="center", va="bottom", fontsize=7.8, fontweight="bold", color="#a82b2a")
save(fig, "p1_regla_cap_func")

# ============================================================== TP1.8 CAF: las cinco privaciones por libertad
priv = [
    ("Población en hacinamiento", 29.4, "29,4 %", ["seg"]),
    ("Jóvenes de 13 a 19 años que no asisten a la escuela", 21.9, "21,9 %", ["soc"]),
    ("Población rural sin seguro médico", 47.0, "47 %", ["soc"]),
    ("Población rural sin acceso a internet", 50.0, "más de la mitad", ["tra", "eco"]),
    ("Usa leña, carbón o kerosene para cocinar", 11.6, "11,6 %", ["eco"]),
]
fig, ax = plt.subplots(figsize=(6.6, 2.45))
fig.subplots_adjust(left=0.45, right=0.95, top=0.84, bottom=0.04)
for i, (lab, v, txt, libs) in enumerate(priv):
    y = len(priv) - 1 - i
    col = LIB[libs[0]][0]
    ax.barh(y, v, height=0.56, color=col, zorder=2)
    if len(libs) > 1:
        ax.barh(y, v, height=0.56, color="none", edgecolor=LIB[libs[1]][0], hatch="////", lw=0, zorder=3)
    ax.text(-1.5, y, lab, ha="right", va="center", fontsize=8.2, color=INK)
    ax.text(v + 1.2, y, txt, ha="left", va="center", fontsize=8.3, color=INK, fontweight="bold")
ax.set_xlim(0, 70)
ax.set_ylim(-0.55, len(priv) - 0.1)
ax.axis("off")
from matplotlib.patches import Patch  # noqa: E402
ax.legend(handles=[Patch(color=LIB[k][0], label=LIB[k][3]) for k in ("seg", "soc", "tra", "eco")],
          loc="lower right", bbox_to_anchor=(1.0, 0.95), ncol=4, fontsize=7.5, handlelength=1.0, handleheight=0.8,
          columnspacing=1.2, handletextpad=0.45, labelcolor=INK2)
save(fig, "p1_caf_privaciones")
print("ok")
