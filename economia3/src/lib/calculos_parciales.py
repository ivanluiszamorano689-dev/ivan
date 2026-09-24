#!/usr/bin/env python3
"""Clave numérica de todos los parciales resueltos.

Cada bloque reproduce las cuentas de un ejercicio con los datos del enunciado.
Correr `python3 calculos_parciales.py` imprime todos los resultados; los
documentos (parciales resueltos y paso a paso) citan estos números.
"""
from math import log, exp


def r(x, n=4):
    return round(x, n)


def idx(x, lo, hi):
    return (x - lo) / (hi - lo)


def idx_ingreso(gni, lo=100, hi=75000):
    return (log(gni) - log(lo)) / (log(hi) - log(lo))


def gmean(*xs):
    p = 1.0
    for x in xs:
        p *= x
    return p ** (1 / len(xs))


def nivel_dh(v):
    if v >= 0.800:
        return "muy alto"
    if v >= 0.700:
        return "alto"
    if v >= 0.550:
        return "medio"
    return "bajo"


def solow_sin_tec(s, n, d, A, a):
    k = (s * A / (n + d)) ** (1 / (1 - a))
    y = A * k ** a
    return k, y


def solow_con_tec(s, n, g, d, a):
    k = (s / (n + g + d)) ** (1 / (1 - a))
    y = k ** a
    return k, y


out = {}

# ---------------------------------------------------------------- 2022 Tema A
k, y = solow_sin_tec(0.26, 0.04, 0.09, 5 / 2, 3 / 7)
k2, y2 = solow_sin_tec(0.26, 0.04, 0.045, 5 / 2, 3 / 7)
out["2022_ej1"] = dict(sA=0.26 * 2.5, n_d=0.13, k=r(k, 3), y=r(y, 3), k_delta_mitad=r(k2, 3), y_delta_mitad=r(y2, 3),
                       CA="0,65/k^(4/7)", CD_inicial=0.13, CD_nueva=0.085, check_y=r(k * 0.13 / 0.26, 3))
TCm = 12000 / 300
PBI_A = 50 * 12000 + 800 * 125
PBI_A_precios_NU = 50 * 300 + 800 * 10
PBI_NU = 200 * 300 + 3200 * 10
out["2022_ej2"] = dict(TCm=TCm, PBI_Argensur_pesos=PBI_A, PBI_Argensur_USD_TCm=PBI_A / TCm,
                       TCppa=r(PBI_A / PBI_A_precios_NU, 2), PBI_Argensur_USD_PPA=r(PBI_A / (PBI_A / PBI_A_precios_NU), 1),
                       PBI_NU=PBI_NU,
                       canasta_NU_USD=16 * 10 + 1 * 300, canasta_NU_en_pesos=16 * 125 + 1 * 12000,
                       TCppa_canasta=r((16 * 125 + 12000) / (16 * 10 + 300), 2))

# ---------------------------------------------------------------- 2023
A, a = 1.5, 5 / 6
k, y = solow_sin_tec(0.19, 0.045, 0.13, A, a)
alpha_c = log(20.5 / 1.5) / log(30.7)
A_c = 20.5 / 30.7 ** a
out["2023_ej1"] = dict(sA=0.19 * 1.5, n_d=0.175, k=r(k, 3), y=r(y, 3), y_sin_A=r(k ** a, 3),
                       FA="0,285 k^(5/6)", FD="0,175 k", CA="0,285/k^(1/6)", CD=0.175,
                       alpha_c=r(alpha_c, 4), A_si_fuera_A=r(A_c, 4), v_k_sobre_y=r(30.7 / 20.5, 4),
                       HD_umbral_percapita=r(0.19 / 0.175, 4), HD_umbral_total=r(0.19 / 0.13, 4))
Ivida, Iedu, Iing = 0.993, 0.925, 0.936
Ivida_aj = Ivida * (1 - 0.027)
A_edu = 1 - 0.896 / Iedu
gni = 100 * 750 ** Iing
idhd = gmean(Ivida_aj, 0.896, 0.776)
idh = gmean(Ivida, Iedu, Iing)
out["2023_ej2"] = dict(Ivida_aj=r(Ivida_aj, 3), A_edu_pct=r(100 * A_edu, 2), INB_implicito=round(gni),
                       IDHD=r(idhd, 3), IDH=r(idh, 3), perdida_pct=r(100 * (1 - idhd / idh), 2),
                       A_ing_implicito_pct=r(100 * (1 - 0.776 / Iing), 2))
TCm = 2500 / 100
PBI_CP = 25 * 2500 + 200 * 2000
PBI_CP_precios_DC = 25 * 100 + 200 * 200
PBI_DC = 30 * 100 + 240 * 200
tcppa = PBI_CP / PBI_CP_precios_DC
out["2023_ej3"] = dict(TCm=TCm, PBI_CP_pesos=PBI_CP, PBI_CP_USD_TCm=PBI_CP / TCm, PBI_DC_USD=PBI_DC,
                       TCppa=r(tcppa, 2), PBI_CP_USD_PPA=r(PBI_CP / tcppa, 1), cociente_PPA=r(PBI_DC / (PBI_CP / tcppa), 3),
                       cociente_TCm=r(PBI_DC / (PBI_CP / TCm), 3))

# ------------------------------------------------ 2024 práctico (Barbados/Guyana y Barbados/Jamaica)
barb = gmean(0.886, 0.766, 0.727)


def pais(le, eys, mys, gni, As, Ae, Ai):
    iv, ie, ii = idx(le, 20, 85), (eys / 18 + mys / 15) / 2, idx_ingreso(gni)
    h = gmean(iv, ie, ii)
    hd = gmean(iv * (1 - As / 100), ie * (1 - Ae / 100), ii * (1 - Ai / 100))
    return dict(Ivida=r(iv, 4), Iedu=r(ie, 4), Iing=r(ii, 4), IDH=r(h, 4), nivel=nivel_dh(h),
                Ivida_aj=r(iv * (1 - As / 100), 4), Iedu_aj=r(ie * (1 - Ae / 100), 4), Iing_aj=r(ii * (1 - Ai / 100), 4),
                IDHD=r(hd, 4), perdida_pct=r(100 * (1 - hd / h), 2))


out["2024_barbados_IDH"] = dict(IDH=r(barb, 4), nivel=nivel_dh(barb))
out["2024_guyana"] = pais(65.7, 12.5, 8.6, 22465, 15.8, 10.4, 25.1)
out["2024_jamaica"] = pais(70.5, 13.4, 9.2, 8834, 8.7, 6.5, 32.0)


def g(x1, x0, t=1):
    return 100 * ((x1 / x0) ** (1 / t) - 1)


ucr = {2018: 3097, 2019: 3661, 2020: 3752, 2021: 4828, 2022: 4576, 2023: 5181}
ucr_ppa = {2018: 12709, 2019: 14381, 2020: 15717, 2021: 18040, 2022: 16080, 2023: 18007}
rus = {2018: 11212, 2019: 11448, 2020: 10108, 2021: 12522, 2022: 15445, 2023: 13817}
rus_ppa = {2018: 28629, 2019: 30964, 2020: 31491, 2021: 38938, 2022: 40958, 2023: 44104}
usa = {2018: 63201, 2019: 65548, 2020: 64317, 2021: 71056, 2022: 77247, 2023: 81695}
out["2024_ucrania_ej2"] = dict(a_crec_2020_2021=r(g(ucr[2021], ucr[2020]), 2), b_ucr_media=r(g(ucr[2023], ucr[2018], 5), 2),
                               b_usa_media=r(g(usa[2023], usa[2018], 5), 2), c_veces_TCm_2020=r(usa[2020] / ucr[2020], 2),
                               d_veces_PPA_2020=r(usa[2020] / ucr_ppa[2020], 2))
out["2024_rusia_ej2"] = dict(a_crec_2020_2021=r(g(rus[2021], rus[2020]), 2), b_rus_media=r(g(rus[2023], rus[2018], 5), 2),
                             b_usa_media=r(g(usa[2023], usa[2018], 5), 2), c_veces_TCm_2020=r(usa[2020] / rus[2020], 2),
                             d_veces_PPA_2020=r(usa[2020] / rus_ppa[2020], 2),
                             distractores=dict(rus_2019_2020=r(g(rus[2020], rus[2019]), 2), rus_2018_2019=r(g(rus[2019], rus[2018]), 2),
                                               rus_2021_2022=r(g(rus[2022], rus[2021]), 2)))
k, y = solow_con_tec(0.20, 0.10, 0.25, 0.05, 0.5)
out["2024_guyana_ej3"] = dict(ngd=0.40, k=r(k, 4), y=r(y, 4), CA="0,2 k^(-0,5) = 0,2/k^(0,5)", CD=0.40)
k, y = solow_con_tec(0.15, 0.08, 0.17, 0.05, 0.5)
out["2024_jamaica_ej3"] = dict(ngd=0.30, k=r(k, 4), y=r(y, 4), CA="0,15/k^(0,5)", CD=0.30)

# ---------------------------------------------------------------- 2025
k1, y1 = solow_con_tec(0.15, 0.06, 0.25, 0.04, 0.4)
k2, y2 = solow_con_tec(0.10, 0.06, 0.25, 0.04, 0.4)
k3, y3 = solow_con_tec(0.135, 0.06, 0.25, 0.04, 0.4)
out["2025_ej1"] = dict(alpha=0.4, ngd=0.35, a_k=r(k1, 4), a_y=r(y1, 4), b_k=r(k2, 4), b_y=r(y2, 4),
                       b_alt_s_13_5=dict(k=r(k3, 4), y=r(y3, 4)),
                       tasa_en_k_b_con_s_a=r(0.15 * k2 ** (-0.6) - 0.35, 4),
                       tasa_en_k_a_con_s_b=r(0.10 * k1 ** (-0.6) - 0.35, 4))
bm_us = 5.69
bm = {"Emiratos Árabes": (18, 3.67), "Australia": (7.75, 1.53), "Azerbaiyán": (6.15, 1.70), "Bahrein": (1.7, 0.38)}
out["2025_ej2"] = {p: dict(precio_USD=r(pl / tc, 2), TCppa=r(pl / bm_us, 4), sobre_infra_pct=r(100 * (pl / bm_us / tc - 1), 2))
                   for p, (pl, tc) in bm.items()}
yem = gmean(0.6738, 0.3595, 0.3891)
yemd = gmean(0.6738 * (1 - 0.267), 0.3595 * (1 - 0.461), 0.3891 * (1 - 0.218))
out["2025_ej3"] = dict(IDH=r(yem, 4), nivel=nivel_dh(yem), vida_aj=r(0.6738 * 0.733, 4), edu_aj=r(0.3595 * 0.539, 4),
                       ing_aj=r(0.3891 * 0.782, 4), IDHD=r(yemd, 4), perdida_pct=r(100 * (1 - yemd / yem), 2))

# --------------------------------------------------------- Namibia / Honduras
nam = pais(63.7, 12.6, 7.0, 9357, 22.1, 25.0, 0)
hon = pais(76.3, 10.1, 6.6, 5308, 13.3, 23.3, 0)
for p, iaj in ((nam, 0.318), (hon, 0.373)):
    p["Iing_aj"] = iaj
    p["A_ing_implicito_pct"] = r(100 * (1 - iaj / p["Iing"]), 2)
    hd = gmean(p["Ivida_aj"], p["Iedu_aj"], iaj)
    p["IDHD"] = r(hd, 4)
    p["perdida_pct"] = r(100 * (1 - hd / p["IDH"]), 2)
out["namibia"] = nam
out["honduras"] = hon
sal = {}
for nombre, tmm, tna in (("Namibia", 195, 65), ("Honduras", 63.6, 72.9)):
    gf = ((10 / tmm) * (1 / tna)) ** 0.5
    sal[nombre] = dict(indice_salud_mujeres=r(gf, 4), salud_referencia=r((gf + 1) / 2, 4))
out["idg_salud"] = sal

if __name__ == "__main__":
    import json
    print(json.dumps(out, ensure_ascii=False, indent=1))
