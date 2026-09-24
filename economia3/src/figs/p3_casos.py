"""TP3 Parte C: IDH de Argentina 1996-2021 (esquemático), IPS de República Dominicana 2021-2023,
Bután (FNB y comparación con Perú). Datos: práctica resuelta, TP3 Parte C y Parte A-B.
Correr desde figs/: python3 p3_casos.py"""
from p3_util import *  # noqa: F403
from matplotlib.lines import Line2D

# ------------------------------------------------------------------ 1) Argentina 1996-2021 (esquemático)
fig, ax = new_fig(6.6, 3.1)
t = np.linspace(1996, 2021, 300)
u = (t - 1996) / 25
edu = 0.92 + 0.07 * (1 - np.exp(-2.6 * u)) / (1 - np.exp(-2.6))
sal = 0.81 + 0.085 * u
ing_x = [1996, 2006, 2011, 2016, 2021]
ing_y = [0.655, 0.655, 0.695, 0.695, 0.635]
ing = np.interp(t, ing_x, ing_y)
ax.plot(t, edu, color=C["orange"], lw=LW)
ax.plot(t, sal, color=C["blue"], lw=LW)
ax.plot(t, ing, color=C["aqua"], lw=LW)
ax.plot([1996, 2023], [0.655, 0.655], color=C["aqua"], lw=0.9, ls=(0, (2, 3)))
ax.text(2021.6, 0.659, "nivel 1996", fontsize=7, color=C["ink3"], va="bottom")
for x, y, c, m in [(1996, 0.92, C["orange"], "s"), (2021, 0.99, C["orange"], "s"), (1996, 0.81, C["blue"], "o"),
                   (2021, 0.895, C["blue"], "o")] + [(x, y, C["aqua"], "^") for x, y in zip(ing_x, ing_y)]:
    ax.plot(x, y, m, ms=7, color=c, mec="white", mew=1.2, zorder=4)
lbl = [(1996, 0.92, "≈0,92", -8, 0, "right"), (2021, 0.99, "≈0,99", 0, 8, "center"),
       (1996, 0.81, "≈0,81", -8, 0, "right"), (2021, 0.895, "0,895", 0, 8, "center"),
       (1996, 0.655, "≈0,655", -8, 0, "right"), (2011, 0.695, "≈0,695", 0, 8, "center"),
       (2016, 0.695, "≈0,695", 0, 8, "center"), (2021, 0.635, "≈0,635", 0, -10, "center")]
for x, y, s, dx, dy, ha in lbl:
    ax.annotate(s, (x, y), xytext=(dx, dy), textcoords="offset points", ha=ha, va="center", fontsize=7.4,
                color=C["ink"], fontweight="bold")
ax.text(2010.5, 0.95, "Educación: la más alta; mejora y se frena cerca del tope", fontsize=7.8, color=C["ink"], ha="center", va="top")
ax.text(2012, 0.83, "Salud: sube pareja, sin retrocesos", fontsize=7.8, color=C["ink"], ha="center", va="top")
ax.text(2003.5, 0.615, "Ingreso: estancado, sube y cae por debajo de 1996", fontsize=7.8, color=C["ink"], ha="center", va="center")
for nm, y, c in (("educación", 0.99, C["orange"]), ("salud", 0.895, C["blue"]), ("ingreso", 0.635, C["aqua"])):
    ax.text(2023.2, y, nm, color=c, fontsize=8.6, fontweight="bold", va="center")
ax.set_xlim(1993, 2026.5)
ax.set_ylim(0.58, 1.02)
ax.set_xticks([1996, 2001, 2006, 2011, 2016, 2021])
ax.yaxis.set_major_formatter(fmt_coma(2))
ax.set_yticks([0.6, 0.7, 0.8, 0.9, 1.0])
data_axes(ax, "", "índice de dimensión")
ax.yaxis.label.set_size(8.2)
ax.text(0.0, 1.03, "ESQUEMÁTICO · los puntos son los valores (aproximados) que da la práctica; las líneas siguen la forma descripta",
        transform=ax.transAxes, fontsize=7.2, color=C["ink3"], ha="left", va="bottom")
save(fig, "p3_arg_1996_2021")

# ------------------------------------------------------------------ 2) IPS República Dominicana
D = [("Sociedad inclusiva", 48.46, 49.17, 62.17, "O"), ("Educación básica", 74.46, 74.31, 78.68, "F"),
     ("Libertad y elección", 57.57, 57.41, 60.17, "O"), ("Salud", 58.50, 57.28, 59.02, "F"),
     ("Vivienda", 88.16, 87.72, 87.89, "N"), ("Agua y saneamiento", 87.27, 87.28, 85.17, "N"),
     ("Seguridad", 57.26, 57.75, 54.25, "N"), ("Información y comunic.", 79.41, 80.72, 74.45, "F"),
     ("Nutrición y atención médica", 90.27, 86.60, 84.13, "N"), ("Derechos y voz", 82.88, 85.73, 71.47, "O"),
     ("Calidad medioambiental", 68.88, 60.28, 56.16, "F"), ("Educación avanzada", 55.36, 52.92, 40.90, "O")]
DC = {"N": C["blue"], "F": C["orange"], "O": C["aqua"]}
DM = {"N": "o", "F": "s", "O": "^"}
fig, (a1, a2) = new_fig(6.7, 4.1, ncols=2, sharey=True, gridspec_kw=dict(width_ratios=[1.45, 1]))
fig.subplots_adjust(wspace=0.06)
n = len(D)
for i, (nm, v1, v2, v3, d) in enumerate(D):
    y = n - 1 - i
    up = v3 > v1
    col = C["green"] if up else C["red"]
    a1.annotate("", xy=(v3, y), xytext=(v1, y), arrowprops=dict(arrowstyle="-|>", color=col, lw=1.6, mutation_scale=9,
                shrinkA=3, shrinkB=2))
    a1.plot(v1, y, "o", ms=6, mfc="white", mec=C["ink2"], mew=1.2, zorder=3)
    a1.plot(v2, y, "o", ms=2.8, color=C["ink3"], zorder=3)
    a1.plot(v3, y, "o", ms=6.5, color=C["ink"], mec="white", mew=1, zorder=4)
    a1.text(v3 + (1.3 if up else -1.3), y + 0.02, coma(v3, 1), ha="left" if up else "right", va="center", fontsize=7,
            color=C["ink"])
    a1.plot(22.5, y, DM[d], ms=6, color=DC[d], clip_on=False, zorder=5)
    v = 100 * (v3 / v1 - 1)
    a2.barh(y, v, 0.62, color=col, zorder=2)
    a2.text(v + (0.8 if v >= 0 else -0.8), y, coma(v, 1, signo=True) + " %", ha="left" if v >= 0 else "right",
            va="center", fontsize=7.4, fontweight="bold", color=C["ink"])
a1.set_yticks(range(n))
a1.set_yticklabels([d[0] for d in D][::-1], fontsize=8)
a1.tick_params(axis="y", length=0, pad=14)
a1.set_xlim(25, 100)
a1.set_xticks([30, 40, 50, 60, 70, 80, 90, 100])
a1.grid(axis="x", color=GRID, lw=0.8)
a1.set_axisbelow(True)
a1.spines["left"].set_visible(False)
a1.set_title("Nivel: 2021 (○) → 2023 (●)", fontsize=8.8, pad=6)
a1.set_xlabel("puntaje (0 a 100)", fontsize=8)
a2.axvline(0, color=C["ink2"], lw=0.9)
a2.set_xlim(-38, 40)
a2.set_xticks([-30, -15, 0, 15, 30])
a2.xaxis.set_major_formatter(fmt_pct(signo=False))
a2.grid(axis="x", color=GRID, lw=0.8)
a2.set_axisbelow(True)
a2.spines["left"].set_visible(False)
a2.tick_params(axis="y", length=0)
a2.set_title("Variación 2021-2023", fontsize=8.8, pad=6)
a2.set_xlabel("variación porcentual", fontsize=8)
a1.set_ylim(-0.7, n - 0.3)
hs = [Line2D([], [], marker=DM[k], ls="", color=DC[k], ms=6, label=l) for k, l in
      (("N", "Necesidades humanas básicas"), ("F", "Fundamentos del bienestar"), ("O", "Oportunidades"))]
hs += [Line2D([], [], marker="o", ls="", color=C["ink3"], ms=3, label="2022")]
fig.legend(handles=hs, loc="lower center", bbox_to_anchor=(0.5, -0.07), ncol=4, fontsize=7.6, handletextpad=0.3,
           columnspacing=1.2)
save(fig, "p3_ips_rd")

# ------------------------------------------------------------------ 3) IPS RD: promedio por dimensión
fig, ax = new_fig(3.25, 2.5)
yrs = [2021, 2022, 2023]
series = [("Necesidades", "N"), ("Fundamentos", "F"), ("Oportunidades", "O")]
off = {"N": 0, "F": -1.4, "O": 0}
for nm, k in series:
    vals = [np.mean([d[1 + j] for d in D if d[4] == k]) for j in range(3)]
    ax.plot(yrs, vals, color=DC[k], lw=LW, marker=DM[k], ms=5.5, mec="white", mew=1)
    ax.text(2023.08, vals[-1] + off[k], f"{nm} {coma(vals[-1], 1)}", fontsize=7.2, va="center", color=C["ink"])
    ax.text(2020.92, vals[0] + off[k], coma(vals[0], 1), fontsize=7.2, va="center", ha="right", color=C["ink2"])
tot = [np.mean([d[1 + j] for d in D]) for j in range(3)]
ax.plot(yrs, tot, color=C["ink"], lw=1.4, ls=(0, (4, 2)), marker="o", ms=3.5)
ax.text(2023.08, tot[-1] + 1.3, f"Promedio {coma(tot[-1], 2)}", fontsize=7.2, va="center", color=C["ink"],
        fontweight="bold")
ax.text(2020.92, tot[0] + 1.3, coma(tot[0], 2), fontsize=7.2, va="center", ha="right", color=C["ink"], fontweight="bold")
ax.set_xlim(2020.4, 2024.75)
ax.set_xticks(yrs)
ax.set_ylim(55, 84)
data_axes(ax)
ax.tick_params(labelsize=7.6)
save(fig, "p3_ips_dim")

# ------------------------------------------------------------------ 4) Bután frente a Perú
fig, ax = new_fig(3.35, 2.55)
grp = ["salud", "educación", "ingreso", "IDH", "IDH-D"]
but = [0.815, 0.560, 0.745, 0.698, 0.478]
per = [0.888, 0.754, 0.750, 0.795, 0.633]
x = np.arange(len(grp))
w = 0.38
ax.bar(x - w / 2, per, w * 0.94, color=C["blue"], zorder=2, label="Perú")
ax.bar(x + w / 2, but, w * 0.94, color=C["orange"], zorder=2, label="Bután")
for xi, a, b in zip(x, per, but):
    ax.text(xi - w / 2, a - 0.02, coma(a), ha="center", va="top", fontsize=6.6, color="white", rotation=90,
            fontweight="bold")
    ax.text(xi + w / 2, b - 0.02, coma(b), ha="center", va="top", fontsize=6.6, color="white", rotation=90,
            fontweight="bold")
ax.axvline(2.5, color=C["rule"], lw=0.9)
ax.set_xticks(x)
ax.set_xticklabels(grp, fontsize=7.6)
ax.set_ylim(0, 1.05)
ax.yaxis.set_major_formatter(fmt_coma(1))
ax.tick_params(axis="y", labelsize=7.4)
data_axes(ax)
ax.legend(loc="upper right", fontsize=7.4, ncol=2, handlelength=1, borderaxespad=0.1, columnspacing=0.8)
save(fig, "p3_butan_peru")

# ------------------------------------------------------------------ 5) Felicidad Nacional Bruta: pilares y dominios
fig, ax = lienzo(6.7, 3.0, 10, 4.45)
pil = ["Buen gobierno", "Desarrollo socioeconómico\nsostenible y equitativo", "Preservación y\npromoción de la cultura",
       "Conservación\ndel ambiente"]
ax.text(0.05, 4.25, "4 PILARES", fontsize=7.6, fontweight="bold", color=C["ink2"], va="center")
for k, p in enumerate(pil):
    caja(ax, 1.25 + k * 2.5, 3.72, 2.3, 0.62, p, fc=C["violet_bg"], ec=C["violet"], size=7.6, weight="bold")
ax.text(0.05, 3.18, "9 DOMINIOS (igual peso, 33 indicadores)", fontsize=7.6, fontweight="bold", color=C["ink2"],
        va="center")
dom = [("Nivel de vida", "idh", "IDH: ingreso\nIPS: vivienda, agua"), ("Salud", "idh", "IDH: salud\nIPS: salud y bienestar"),
       ("Educación", "idh", "IDH: educación\nIPS: conocim. básicos"),
       ("Buen gobierno", "ips", "IPS: derechos\npersonales"), ("Diversidad y resiliencia\necológica", "ips",
                                                              "IPS: calidad\nmedioambiental"),
       ("Bienestar\npsicológico", "fnb", "sólo FNB"), ("Uso del tiempo", "fnb", "sólo FNB"),
       ("Diversidad y resiliencia\ncultural", "fnb", "sólo FNB"), ("Vitalidad\ncomunitaria", "fnb", "sólo FNB")]
sty = {"idh": (C["blue_bg"], C["blue"]), "ips": (C["aqua_bg"], C["aqua"]), "fnb": ("#ffffff", C["ink3"])}
for k, (nm, tipo, nota) in enumerate(dom):
    col = k % 5 if k < 5 else (k - 5)
    row = 0 if k < 5 else 1
    xw = 1.92
    x0 = 1.0 + col * 2.0 if row == 0 else 1.0 + col * 2.0 + 1.0
    y = 2.35 if row == 0 else 0.85
    fc, ec = sty[tipo]
    caja(ax, x0, y, xw, 1.18, "", fc=fc, ec=ec, size=7.6, lw=1.3)
    ax.text(x0, y + 0.2, nm, ha="center", va="center", fontsize=7.6, fontweight="bold", linespacing=1.1)
    ax.text(x0, y - 0.33, nota, ha="center", va="center", fontsize=6.6, color=C["ink2"], linespacing=1.1)
save(fig, "p3_butan_fnb")
