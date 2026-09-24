"""Gráficos de los parciales 2025 (P8 práctico y P9 teórico).

Correr desde figs/:  python3 x3_2025.py   -> figs/out/x3_*.svg
Datos: enunciados del Primer Parcial 2025 y de la prueba teórica del 27/09/2025 (CLAVE_PARCIALES.md).
"""
import sys

sys.path.insert(0, "../lib")
from econ_style import *  # noqa: F401,F403


def fmt(v, dec):
    return f"{v:.{dec}f}".replace(".", ",")


# ------------------------------------------------------------------ datos P8 Ej. 1
S_A, S_B, NGD, ALPHA = 0.15, 0.10, 0.35, 0.4
EXP = ALPHA - 1                       # -0,6
KA = (S_A / NGD) ** (1 / (1 - ALPHA))   # 0,2436
KB = (S_B / NGD) ** (1 / (1 - ALPHA))   # 0,1239
CA_A_KB = S_A * KB ** EXP             # 0,525


def ca(s, k):
    return s * k ** EXP


# ------------------------------------------------------------------ P8.1  el gráfico tal como viene en la hoja
fig, ax = new_fig(3.0, 2.35)
XM, YM = 0.40, 0.75
k1 = np.linspace((S_A / 0.73) ** (1 / (1 - ALPHA)), XM, 300)
k2 = np.linspace(0.058, XM, 300)
ink = "#2b2b29"
ax.plot(k1, ca(S_A, k1), color=ink, lw=1.25)
ax.plot(k2, ca(S_B, k2), color=ink, lw=1.25)
ax.plot([0, XM], [NGD, NGD], color=ink, lw=1.25)
for kx in (KB, KA):
    ax.plot([kx, kx], [0, NGD], color=ink, lw=0.8, ls=(0, (2.5, 2.5)))
arrow(ax, KB, NGD, KB, CA_A_KB, color=ink, lw=1.0, both=True)
ax.set_xlim(0, XM + 0.005)
ax.set_ylim(0, YM)
ax.set_xticks([])
ax.set_yticks([])
ax.spines["left"].set_color(ink)
ax.spines["bottom"].set_color(ink)
ax.spines["left"].set_linewidth(0.9)
ax.spines["bottom"].set_linewidth(0.9)
save(fig, "x3_solow_hoja")

# ------------------------------------------------------------------ P8.2  el gráfico completado
fig, ax = new_fig(6.3, 3.75)
XM, YM = 0.46, 0.80
ka_ = np.linspace((S_A / YM) ** (1 / (1 - ALPHA)), XM, 400)
kb_ = np.linspace((S_B / YM) ** (1 / (1 - ALPHA)), XM, 400)
ax.plot(ka_, ca(S_A, ka_), color=C["orange"], lw=LW, zorder=3)
ax.plot(kb_, ca(S_B, kb_), color=C["orange"], lw=LW, ls=(0, (5, 3)), zorder=3)
ax.plot([0, XM], [NGD, NGD], color=C["aqua"], lw=LW, zorder=2)
econ_axes(ax, "", "", xlim=(0, XM), ylim=(0, YM))
ax.annotate(r"$\hat{k}$  (capital por unidad de trabajo efectivo)", (XM, 0), xytext=(0, -29),
            textcoords="offset points", fontsize=9.5, ha="right", va="top", color=C["ink"], annotation_clip=False)
ax.set_ylabel(r"$\gamma_{\hat{k}}$  (tasa de crecimiento de $\hat{k}$)", loc="top", rotation=0, fontsize=9.5,
              labelpad=-4)
ax.yaxis.set_label_coords(0.0, 1.03)
ax.yaxis.label.set_horizontalalignment("left")

# cortes y guías
vguide(ax, KB, NGD, r"$\hat{k}^*_b=0{,}124$", size=9.5)
vguide(ax, KA, NGD, r"$\hat{k}^*_a=0{,}244$", size=9.5)
hguide(ax, KB, CA_A_KB, r"$0{,}525$", size=9)
hguide(ax, 0.0, NGD, r"$0{,}35$", size=9)
point(ax, KB, NGD, color=C["ink"])
point(ax, KA, NGD, color=C["ink"])
ax.annotate("EE (b)", (KB, NGD), xytext=(-6, -13), textcoords="offset points", ha="right", fontsize=8.6,
            fontweight="bold", color=C["ink"])
ax.annotate("EE (a)", (KA, NGD), xytext=(6, -13), textcoords="offset points", ha="left", fontsize=8.6,
            fontweight="bold", color=C["ink"])

# flecha doble medida
arrow(ax, KB, NGD + 0.016, KB, CA_A_KB, color=C["ink"], lw=1.4, both=True)
ax.annotate(r"$\gamma_{\hat{k}} = 0{,}525-0{,}35 = +0{,}175 > 0$" + "\n(con " + r"$s=0{,}15$" + " en " +
            r"$\hat{k}=0{,}124$" + ")",
            (KB, (NGD + CA_A_KB) / 2), xytext=(0.215, 0.62), fontsize=8.8, color=C["ink"], va="center",
            ha="left", arrowprops=dict(arrowstyle="-", color=C["ink2"], lw=0.8, shrinkA=2, shrinkB=2))

# rótulos de curvas
label_curve(ax, 0.069, ca(S_A, 0.069), r"CA$_a=\dfrac{0{,}15}{\hat{k}^{\,0{,}6}}$  (inciso a)", C["orange"],
            dx=9, dy=2, size=9.2)
label_curve(ax, XM, ca(S_B, XM), r"CA$_b=\dfrac{0{,}10}{\hat{k}^{\,0{,}6}}$  (inciso b)", C["orange"],
            dx=-2, dy=-15, ha="right", size=9.2)
label_curve(ax, XM, NGD, r"CD $=n+g+\delta=0{,}35$", C["aqua"], dx=-2, dy=10, ha="right", size=9.2)

# desplazamiento de la curva de ahorro
kx = 0.395
arrow(ax, kx, ca(S_A, kx) - 0.008, kx, ca(S_B, kx) + 0.012, color=C["orange"], lw=1.3)
ax.text(kx + 0.006, (ca(S_A, kx) + ca(S_B, kx)) / 2 + 0.005, r"baja $s$", fontsize=8.4, color=C["orange"],
        ha="left", va="center", fontweight="bold")

# transición de a hacia b sobre el eje
arrow(ax, KA - 0.01, 0.07, KB + 0.012, 0.07, color=C["ink2"], lw=1.1)
ax.text((KA + KB) / 2, 0.085, "transición", fontsize=8, color=C["ink2"], ha="center", va="bottom")
save(fig, "x3_solow_completo")

# ------------------------------------------------------------------ P8.3  Big Mac: barras divergentes
US = 5.69
BM = [("Emiratos Árabes", 18, 3.67), ("Australia", 7.75, 1.53), ("Azerbaiyán", 6.15, 1.70), ("Bahrein", 1.7, 0.38)]
rows = []
for nom, p, tc in BM:
    ppa = p / US
    rows.append((nom, p / tc, ppa, (ppa / tc - 1) * 100))
rows.sort(key=lambda r: r[3])            # más infravaluada abajo -> se dibuja de abajo hacia arriba
fig, ax = new_fig(6.2, 2.5)
ys = np.arange(len(rows))
pregunta = {"Australia", "Bahrein"}
for y, (nom, pusd, ppa, sv) in zip(ys, rows):
    col = C["blue"]
    ax.barh(y, sv, height=0.56, color=col, zorder=3)
    ax.text(sv - 0.8, y, fmt(sv, 1).replace("-", "−") + " %", ha="right", va="center", fontsize=8.8, color=C["ink"],
            fontweight="bold")
    ax.text(1.2, y, f"US${fmt(pusd, 2)} el Big Mac", ha="left", va="center", fontsize=8.2, color=C["ink2"])
ax.axvline(0, color=C["ink"], lw=1.1, zorder=4)
ax.set_yticks(ys)
ax.set_yticklabels([r[0] + ("  ← inciso a)" if r[0] in pregunta else "") for r in rows], fontsize=8.8)
for lbl in ax.get_yticklabels():
    if "inciso" in lbl.get_text():
        lbl.set_fontweight("bold")
ax.set_xlim(-50, 22)
ax.set_xticks([-40, -30, -20, -10, 0, 10, 20])
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:+.0f} %".replace("+0", "0").replace("-", "−")))
ax.tick_params(axis="y", length=0)
ax.spines["left"].set_visible(False)
ax.grid(axis="x", color="#ebe9e3", lw=0.8)
ax.set_axisbelow(True)
ax.set_ylim(-0.6, len(rows) - 0.1)
ax.text(-49, len(rows) - 0.25, "← infravaluada: el Big Mac es más barato que en EEUU", fontsize=8.2,
        color=C["ink2"], ha="left", va="bottom")
ax.text(21.5, len(rows) - 0.25, "sobrevaluada →", fontsize=8.2, color=C["ink3"], ha="right", va="bottom")
ax.set_xlabel("infra/sobrevaloración frente al dólar = TC PPA / TCm − 1", fontsize=8.6)
save(fig, "x3_bigmac")

# ------------------------------------------------------------------ P8.4  Yemen: índices sin ajustar y ajustados
H, E, I = 0.6738, 0.3595, 0.3891
AH, AE, AI = 0.267, 0.461, 0.218
raw = [H, E, I, (H * E * I) ** (1 / 3)]
adj = [H * (1 - AH), E * (1 - AE), I * (1 - AI)]
adj.append((adj[0] * adj[1] * adj[2]) ** (1 / 3))
loss = [AH * 100, AE * 100, AI * 100, (1 - adj[3] / raw[3]) * 100]
cats = ["Salud", "Educación", "Ingreso", "IDH → IDH-D"]
fig, ax = new_fig(6.2, 2.55)
x = np.arange(4) + np.array([0, 0, 0, 0.35])
w = 0.34
ax.axvspan(x[3] - 0.5, x[3] + 0.5, color=C["gray_bg"], zorder=0)
b1 = ax.bar(x - w / 2, raw, w, color=C["blue"], zorder=3)
b2 = ax.bar(x + w / 2, adj, w, color=C["orange"], zorder=3)
for xi, r, a in zip(x, raw, adj):
    ax.text(xi - w / 2, r + 0.012, fmt(r, 3), ha="center", va="bottom", fontsize=8.4, color=C["ink"])
    ax.text(xi + w / 2, a + 0.012, fmt(a, 3), ha="center", va="bottom", fontsize=8.4, color=C["ink"])
trans = ax.get_xaxis_transform()
for xi, lo in zip(x, loss):
    ax.text(xi, -0.2, "pierde " + fmt(lo, 1) + " %", transform=trans, ha="center", va="top", fontsize=8.4,
            color=C["red"], fontweight="bold")
ax.plot([x[3] - 0.5, x[3] + 0.5], [0.550, 0.550], color=C["ink2"], lw=0.9, ls=(0, (4, 3)), zorder=2)
ax.text(x[3] + 0.47, 0.562, "corte bajo/medio: 0,550", fontsize=7.8, color=C["ink2"], ha="right", va="bottom")
ax.set_xticks(x)
ax.set_xticklabels(cats, fontsize=9)
ax.set_xlim(-0.5, x[3] + 0.5)
ax.set_ylim(0, 0.8)
data_axes(ax, "", "")
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: fmt(v, 1)))
ax.tick_params(axis="x", length=0)
ax.legend(handles=[b1, b2], labels=["índice sin ajustar", "ajustado por desigualdad"], loc="upper center", ncol=2,
          fontsize=8.4, handlelength=1.2, bbox_to_anchor=(0.5, 1.04))
save(fig, "x3_yemen")

# ------------------------------------------------------------------ P9.1  crecimiento per cápita de largo plazo
t = np.linspace(0, 10, 400)
g = 0.12
sin_tec = 1.55 - 0.85 * np.exp(-0.55 * t)
con_tec = 0.70 + g * t + 0.85 * (1 - np.exp(-0.55 * t)) - 0.0
mas_s = con_tec + 0.38 * (1 - np.exp(-0.55 * np.clip(t - 4.0, 0, None))) * (t > 4.0)
fig, ax = new_fig(5.6, 2.55)
ax.plot(t, sin_tec, color=C["orange"], lw=LW, zorder=3)
ax.plot(t, con_tec, color=C["blue"], lw=LW, zorder=3)
ax.plot(t[t >= 4.0], mas_s[t >= 4.0], color=C["blue"], lw=LW, ls=(0, (5, 3)), zorder=3)
econ_axes(ax, "tiempo", r"$\ln(y)$, producto per cápita (esc. log.)", xlim=(0, 10.6), ylim=(0.4, 3.2))
ax.yaxis.set_label_coords(0.0, 1.03)
ax.yaxis.label.set_horizontalalignment("left")
label_curve(ax, 10, sin_tec[-1], "sin progreso tecnológico:\nse estanca en el EE", C["orange"], dx=-2, dy=-16,
            ha="right", size=8.6)
label_curve(ax, 7.2, 0.70 + g * 7.2 + 0.85 * (1 - np.exp(-0.55 * 7.2)), "con progreso tecnológico:\ncrece a la tasa $g$",
            C["blue"], dx=8, dy=-18, ha="left", size=8.6)
label_curve(ax, 6.2, mas_s[np.searchsorted(t, 6.2)], "más ahorro: sube el NIVEL,\nno la pendiente", C["blue"],
            dx=-10, dy=14, ha="right", size=8.2, weight="normal")
ax.plot([4.0], [con_tec[np.searchsorted(t, 4.0)]], "o", ms=4, color=C["blue"], zorder=4)
ax.annotate(r"sube $s$", (4.0, con_tec[np.searchsorted(t, 4.0)]), xytext=(4, -14), textcoords="offset points",
            fontsize=8, color=C["ink2"])
save(fig, "x3_solow_largo_plazo")
print("ok", fmt(KA, 4), fmt(KB, 4), fmt(CA_A_KB, 3), [fmt(r[3], 2) for r in rows], fmt(adj[3], 4))
