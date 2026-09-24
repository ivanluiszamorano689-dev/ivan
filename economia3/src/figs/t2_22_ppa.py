"""Tema 2.2: transables vs no transables, PPA en el mundo, factor PPA/TCm, Big Mac."""
from t2_util import *

SUB, SOB = C["orange"], C["blue"]   # subvaluada (factor < 1) / sobrevaluada (factor > 1)

# ---------------------------------------------------------------- Figura 2.3
# Datos: Parcial 2023, Ej. 3 (Dolar City / Ciudad Pesos). TCm = 2.500/100 = 25.
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.7, 2.75), gridspec_kw=dict(width_ratios=[1, 1.25]))
fig.subplots_adjust(wspace=0.32)
x = np.array([0, 1])
w = 0.34
dc = [100, 200]
cp = [2500 / 25, 2000 / 25]
b1 = a1.bar(x - w / 2 - 0.01, dc, w, color=C["blue"], label="Dolar City")
b2 = a1.bar(x + w / 2 + 0.01, cp, w, color=C["orange"], label="Ciudad Pesos")
for b, t in zip(b1, ["100", "200"]):
    a1.annotate(t, (b.get_x() + b.get_width() / 2, b.get_height()), xytext=(0, 3), textcoords="offset points",
                ha="center", fontsize=8.3)
for b, t in zip(b2, ["100", "80"]):
    a1.annotate(t, (b.get_x() + b.get_width() / 2, b.get_height()), xytext=(0, 3), textcoords="offset points",
                ha="center", fontsize=8.3)
a1.set_xticks(x)
a1.set_xticklabels(["Pendrive\n(transable)", "Corte de pelo\n(no transable)"], fontsize=8.4)
a1.set_ylim(0, 300)
a1.set_xlim(-0.55, 1.55)
a1.set_yticks([0, 100, 200])
data_axes(a1, "", "US\\$ al TC de mercado")
a1.yaxis.label.set_size(8.4)
a1.tick_params(axis="x", length=0)
a1.legend(loc="upper left", fontsize=7.8, handlelength=1.0, borderaxespad=0.1)
a1.annotate("mismo precio:\nun solo precio", (0, 150), ha="center", fontsize=7.4, color=C["ink2"])
a1.annotate("60 % más barato\nen el país pobre", (1.0, 238), ha="center", fontsize=7.4, color=C["red"],
            fontweight="bold")
a1.set_title("Precio de cada bien en US\$ (CP: \$ ÷ 25)", fontsize=8.6, pad=6)

labels = ["CP a TC de mercado\n(\\$25 por US\\$)", "CP a TC de PPA\n(\\$10,88 por US\\$)", "Dolar City"]
vals = [18500, 42500, 51000]
bars = a2.barh([2, 1, 0], vals, color=[C["orange"], C["orange"], C["blue"]], height=0.6)
bars[0].set_alpha(0.45)
bars[0].set_hatch("////")
bars[0].set_edgecolor(C["orange"])
a2.set_yticks([2, 1, 0])
a2.set_yticklabels(labels, fontsize=8.2)
a2.set_xlim(0, 62000)
a2.set_xticks([0, 20000, 40000, 60000])
a2.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: fmt(v, 0)))
clean_hbar(a2, "PBI en US$")
a2.xaxis.label.set_size(8.4)
hbar_labels(a2, bars, ["US\\$" + fmt(v) for v in vals], size=8.3)
a2.set_title("PBI de Ciudad Pesos (CP) en US\$", fontsize=8.6, pad=6)
a2.annotate("Brecha DC/CP:\n2,76 veces a TCm\n1,2 veces a PPA", xy=(0.99, 0.97), xycoords="axes fraction",
            ha="right", va="top", fontsize=7.8, color=C["ink"], fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc=C["gray_bg"], ec="none"))
save(fig, "t2_transables")

# ---------------------------------------------------------------- Figura 2.4
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.7, 2.35), gridspec_kw=dict(width_ratios=[1, 1]))
fig.subplots_adjust(wspace=0.45)
paises = ["China", "EEUU"]
ppa = [19.5, 14.6]
tcm = [16.5, 26.0]
y = np.array([1, 0])
h = 0.36
bp = a1.barh(y + h / 2 + 0.01, ppa, h, color=C["blue"], label="a PPA")
bt = a1.barh(y - h / 2 - 0.01, tcm, h, color=C["orange"], label="a TC de mercado")
a1.set_yticks(y)
a1.set_yticklabels(paises, fontsize=9)
a1.set_xlim(0, 33)
a1.set_xticks([0, 10, 20, 30])
clean_hbar(a1, "% del PBI mundial")
a1.xaxis.label.set_size(8.4)
hbar_labels(a1, bp, [fmt(v, 1) + " %" for v in ppa], size=8.2)
hbar_labels(a1, bt, [fmt(v, 1) + " %" for v in tcm], size=8.2)
for bb in list(bp) + list(bt):
    a1.annotate("PPA" if bb in list(bp) else "TCm", (0, bb.get_y() + bb.get_height() / 2), xytext=(4, 0),
                textcoords="offset points", va="center", fontsize=7.6, color="white", fontweight="bold")
a1.set_title("Participación en la economía mundial", fontsize=8.8, pad=6)

fac = {"Argentina": 0.46, "China": 0.47, "Suiza": 1.12}
names = list(fac)[::-1]
vals = [fac[n] for n in names]
bars = a2.barh(range(len(names)), vals, color=[SOB if v > 1 else SUB for v in vals], height=0.55)
a2.set_yticks(range(len(names)))
a2.set_yticklabels(names, fontsize=9)
a2.set_xlim(0, 1.95)
a2.set_xticks([0, 0.5, 1.0, 1.5])
a2.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: fmt(v, 1)))
clean_hbar(a2, r"factor $TC_{PPA}\,/\,TC_m$")
a2.xaxis.label.set_size(8.6)
a2.axvline(1, color=C["ink"], lw=1.1, ls=(0, (3, 2)))
a2.set_ylim(-0.5, 2.85)
a2.annotate("1 = PPA igual a TCm", (1.03, 2.55), ha="left", fontsize=7.4, color=C["ink2"], annotation_clip=False)
for b, v in zip(bars, vals):
    yy = b.get_y() + b.get_height() / 2
    a2.annotate(fmt(v, 2), (v, yy), xytext=(4, 0), textcoords="offset points", va="center", fontsize=8.3,
                fontweight="bold")
    a2.annotate(f"PBI(PPA) = {fmt(1 / v, 1)} × PBI(TCm)", (v, yy), xytext=(28, 0),
                textcoords="offset points", va="center", fontsize=7.3, color=C["ink2"],
                bbox=dict(boxstyle="square,pad=0.15", fc="white", ec="none"))
a2.set_title("Factor de conversión PPA / TCm (2025)", fontsize=8.8, pad=6)
save(fig, "t2_ppa_mundo")

# ---------------------------------------------------------------- Figura 2.5
# Datos: Parcial 2025, Ej. 2 (índice Big Mac, julio de 2024). BM en EEUU = US$5,69.
bm_us = 5.69
bm = {"Emiratos Árabes": (18, 3.67), "Australia": (7.75, 1.53), "Azerbaiyán": (6.15, 1.70), "Bahrein": (1.7, 0.38)}
rows = []
for p, (pl, tc) in bm.items():
    usd = pl / tc
    tcppa = pl / bm_us
    rows.append((p, usd, tcppa, tc, 100 * (tcppa / tc - 1)))
rows.sort(key=lambda r: r[4], reverse=True)       # la más subvaluada abajo
names = [r[0] for r in rows]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.7, 2.35), sharey=True, gridspec_kw=dict(width_ratios=[1, 1.1]))
fig.subplots_adjust(wspace=0.12)
yy = np.arange(len(rows))
bars = a1.barh(yy, [r[1] for r in rows], color=C["ink3"], height=0.55)
a1.axvline(bm_us, color=C["ink"], lw=1.2, ls=(0, (3, 2)))
a1.annotate("EEUU: US\\$5,69", (bm_us - 0.08, 3.42), ha="right", fontsize=7.6, color=C["ink"], annotation_clip=False)
a1.set_yticks(yy)
a1.set_yticklabels(names, fontsize=8.8)
a1.set_xlim(0, 7.2)
a1.set_xticks([0, 2, 4, 6])
clean_hbar(a1, "precio del Big Mac en US$ = P local / TCm")
a1.xaxis.label.set_size(8.2)
hbar_labels(a1, bars, ["US\\$" + fmt(r[1], 2) for r in rows], size=8.0, inside=True)
a1.set_ylim(-0.6, 3.75)

vals = [r[4] for r in rows]
bars = a2.barh(yy, vals, color=[SUB if v < 0 else SOB for v in vals], height=0.55)
a2.axvline(0, color=C["ink"], lw=1.0)
a2.set_xlim(-48, 22)
a2.set_xticks([-40, -20, 0, 20])
a2.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: ("+" if v > 0 else "") + fmt(v, 0) + " %"))
clean_hbar(a2, r"$\dfrac{TC_{PPA}}{TC_m}-1$,  con  $TC_{PPA}=\dfrac{P_{local}}{5{,}69}$")
a2.xaxis.label.set_size(8.6)
for b, r in zip(bars, rows):
    a2.annotate(fmt(r[4], 1) + " %", (r[4], b.get_y() + b.get_height() / 2), xytext=(-4, 0),
                textcoords="offset points", ha="right", va="center", fontsize=8.0, fontweight="bold")
    a2.annotate(f"PPA {fmt(r[2], 3)} vs TCm {fmt(r[3], 2)}", (0, b.get_y() + b.get_height() / 2), xytext=(5, 0),
                textcoords="offset points", ha="left", va="center", fontsize=7.2, color=C["ink2"])
a2.annotate("← subvaluada", (-47, 3.45), ha="left", fontsize=7.6, color=SUB, fontweight="bold",
            annotation_clip=False)
a2.annotate("sobrevaluada →", (21, 3.45), ha="right", fontsize=7.6, color=SOB, fontweight="bold",
            annotation_clip=False)
save(fig, "t2_bigmac")
