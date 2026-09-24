# Guía para escribir secciones de los PDFs de Economía III

Todo el material se arma con `build.py`: fragmentos HTML en `docs/<doc>/` + gráficos SVG
generados con matplotlib en `figs/out/`. La hoja de estilos compartida es `assets/style.css`.

## Documentos

| doc | archivo final (`../pdf/`) | qué es |
|---|---|---|
| `teoria` | `1_Manual_de_teoria_Temas_1_a_3.pdf` | manual de teoría mejorado y completado |
| `practica` | `2_Practica_resuelta_1er_parcial.pdf` | práctica resuelta (TP1–TP4 + extras) mejorada |
| `parciales` | `3_Parciales_resueltos.pdf` | todos los parciales resueltos (clave + justificación) |
| `pasoapaso` | `4_Paso_a_paso_ejercicios.pdf` | cómo se resuelve cada ejercicio, paso por paso |

Material de origen (texto extraído y PDFs originales, sólo lectura):
`/tmp/claude-0/-home-user-ivan/b89bf22b-71b1-56f0-8ba3-a95a3e223b5f/scratchpad/src/`
`teoria.pdf`/`teoria.txt` (46 págs.), `practica.pdf`/`practica.txt` (59 págs.). Las páginas del .txt
están separadas por `=====PAGE=====`. Las tablas salen desordenadas en el .txt: para leerlas bien,
rasterizá la página (`python3 -c "import pymupdf; pymupdf.open('practica.pdf')[12].get_pixmap(dpi=90).save('/tmp/.../p13.png')"`)
y mirala con Read. Clave de los parciales: `src/CLAVE_PARCIALES.md`. Números: `src/lib/calculos_parciales.py`.

## Cómo previsualizar tu parte (aislado, no pisa a nadie)

```bash
cd /home/user/ivan/economia3/src
python3 figs/<tu_script>.py            # (correr desde figs/: cd figs && python3 x.py)
python3 build.py --preview <tu-nombre> docs/teoria/20-tema2.html
# -> _build/preview_<tu-nombre>.pdf y _build/preview_<tu-nombre>/p-01.png, p-02.png ...
```
Mirá TODAS las PNG con Read (son livianas, 60 dpi). Buscá: fórmulas rotas (texto rojo de KaTeX),
tablas o fórmulas que se salen del margen, rótulos de gráficos pisados, páginas con medio espacio en
blanco por un bloque que no entra, cajas partidas feo. El comando también imprime `katexErrors`,
`overflow` e imágenes faltantes: tienen que quedar en cero.

## Reglas de archivos
- Escribí SOLO tus fragmentos asignados y tus scripts de gráficos `figs/<prefijo>_*.py`
  (que guardan `figs/out/<prefijo>_*.svg`). No toques `style.css`, `build.py`, `econ_style.py`,
  los `manifest.json` ni archivos de otros.
- Si necesitás un estilo extra, poné un `<style>` al principio de tu fragmento con clases que
  empiecen con tu prefijo (ej. `.t2-escala`). Usá las variables de color de `style.css`.
- Rutas en el HTML relativas a `src/`: `<img src="figs/out/t2_idh_escala.svg">`.

## Reglas de contenido
1. Español rioplatense con voseo ("calculá", "fijate"), tono directo de apunte de estudio.
2. **No perder nada** del original: cada definición, dato, ejemplo, lista, cita bibliográfica con
   capítulo/páginas y comentario de la cátedra tiene que seguir estando. Podés reordenar, reescribir
   más claro, partir en cajas, convertir en tablas o gráficos.
3. **Completar**: agregá lo que haga falta para resolver los parciales reales (`CLAVE_PARCIALES.md`)
   y lo que un alumno necesitaría y no está (intuiciones, pasos intermedios, casos límite, lectura
   de gráficos, trampas). Cada tema/TP con al menos una caja "Así lo preguntan en el parcial" que cite
   la pregunta real (parcial y año) y su respuesta.
4. **Gráficos**: todo modelo lleva su gráfico; todo procedimiento su diagrama de pasos. Nada de datos
   inventados: los datos reales salen del manual, la práctica o los parciales (citá la fuente en el
   pie). Si un gráfico es ilustrativo (formas funcionales), decí "esquemático" en el pie.
5. **Cuentas**: verificá cada número con Python antes de escribirlo. Si el original tenía un error,
   corregilo (en silencio o con una nota breve "corregido").
6. Matemática con KaTeX: en línea `\( ... \)`, en bloque `\[ ... \]`. **Nunca** uses `$` como
   delimitador (el `$` se usa para pesos). Coma decimal dentro de fórmulas: `0{,}993` (con llaves,
   si no KaTeX mete un espacio). Macros disponibles: `\kt` = k̃, `\yt` = ỹ.
   Fuera de fórmulas: coma decimal y punto de miles (0,993 · 75.000).
7. Nunca copies nombres, DNI o LU que aparezcan en fotos de exámenes.
8. Cada figura con `<figcaption><b>Figura N.</b> …</figcaption>` que diga qué mirar.

## Estructura recomendada de un tema / TP
1. `.chapter-head` (kicker + título + qué vas a poder hacer).
2. Caja `summary` "En 30 segundos" (5–7 viñetas con lo esencial).
3. Desarrollo: definiciones (`box def`), fórmulas (`formula-card`), gráficos, ejemplos (`box example`
   con `calc`), intuición (`box intuition`), tablas comparativas, errores típicos (`box warn`), trucos
   (`box tip`), preguntas de parcial (`box exam`).
4. Cierre: `check` "Autoevaluación" con 3–6 preguntas y sus respuestas (breves) + `box biblio`.

## Componentes (copiar y pegar)

```html
<section class="tema-2">  <!-- tema-1 violeta · tema-2 azul · tema-3 verde agua: fija el color de acento -->

<div class="chapter-head">
  <div class="kicker">Tema 2 · Indicadores del bienestar</div>
  <h2><span class="num">2.4</span>El Índice de Desarrollo Humano</h2>
  <p>Qué vas a poder hacer: …</p>
</div>

<h3>Subtítulo</h3>          <!-- h2 y h3 entran solos al índice; data-toc="no" para excluir -->
<h4>Sub-subtítulo</h4>      <!-- no entra al índice -->

<div class="box def"><div class="box-title">Definición</div><p>…</p></div>
<div class="box formula"><div class="box-title">Fórmula</div><p>…</p></div>
<div class="box warn"><div class="box-title">Error típico</div><p>…</p></div>
<div class="box exam"><div class="box-title">Así lo preguntan en el parcial</div><p>…</p></div>
<div class="box example"><div class="box-title">Ejemplo numérico</div> … </div>
<div class="box tip"><div class="box-title">Truco</div><p>…</p></div>
<div class="box intuition"><div class="box-title">La intuición</div><p>…</p></div>
<div class="box summary"><div class="box-title">En 30 segundos</div><ul><li>…</li></ul></div>
<div class="box biblio"><div class="box-title">Bibliografía</div><p>…</p></div>

<div class="formula-card">
  <div class="fc-label">Estado estacionario</div>
  \[ k^* = \left(\frac{sA}{n+\delta}\right)^{\frac{1}{1-\alpha}} \]
  <div class="fc-legend"><span>\(s\): ahorro</span><span>\(n\): población</span></div>
</div>

<div class="calc">\[\begin{aligned} k^* &= (0{,}65/0{,}13)^{7/4} = 16{,}718 \\ y^* &= 8{,}359 \end{aligned}\]</div>

<figure class="w80"><img src="figs/out/t3a_solow.svg">
  <figcaption><b>Figura 3.2.</b> Qué mirar…</figcaption></figure>   <!-- w50/w60/w70/w80 o sin clase = 100% -->

<ol class="steps">
  <li><span class="step-title">Identificá los datos</span> …</li>
  <li><span class="step-title">Plantear</span> …</li>
</ol>

<div class="recipe"><div class="recipe-title">Receta: calcular el IDH</div><ol><li>…</li></ol></div>

<div class="statement"><div class="statement-title">Enunciado · Parcial 2023 · Ej. 1 a) <span class="pts">5 ptos</span></div><p>…</p></div>
<ul class="mcq">
  <li class="wrong"><span class="opt">i)</span><span>texto de la opción<span class="why">por qué no</span></span></li>
  <li class="correct"><span class="opt">iii)</span><span>texto<span class="why">por qué sí</span></span></li>
</ul>
<div class="answer"><div class="answer-body"><span class="answer-label">Respuesta</span>iii) …</div></div>
<div class="answer caution"><div class="answer-body"><span class="answer-label">Respuesta (con aclaración)</span>…</div></div>

<div class="grid-2"> …dos columnas… </div>   <div class="grid-3"> … </div>
<div class="card blue"><div class="card-title">Título</div><p>…</p></div>  <!-- blue orange aqua violet yellow red green -->
<div class="flow"><div class="node"><b>Paso</b>detalle</div><div class="arrow">→</div><div class="node">…</div></div>
<div class="versus"><div class="card blue">…</div><div class="vs">vs</div><div class="card orange">…</div></div>
<div class="check"><div class="check-title">Autoevaluación</div><ol><li>…</li></ol></div>
<span class="tag">etiqueta</span> <span class="tag orange">…</span> <span class="pts">5 ptos</span> <mark>resaltado</mark>

<table> <thead><tr><th>…</th><th class="num">…</th></tr></thead>
        <tbody><tr><td>…</td><td class="num">…</td></tr><tr class="total">…</tr></tbody></table>
<!-- td.ok = celda correcta en verde; table.compact = más apretada -->

<div class="page-break"></div>   <!-- salto de página forzado (usar poco) -->
</section>
```

Mermaid también está disponible (`<div class="mermaid">flowchart LR ...</div>`) si el manifest
tiene `"mermaid": true` (los cuatro lo tienen), pero preferí `.flow`/tarjetas o un SVG propio:
se ven más prolijos.

## Gráficos (matplotlib → SVG)

```python
# figs/t3a_solow.py   (correr con: cd figs && python3 t3a_solow.py)
import sys; sys.path.insert(0, "../lib")
from econ_style import *          # C (colores), LW, new_fig, econ_axes, data_axes, label_curve,
                                  # vguide, hguide, point, arrow, save, np, plt
k = np.linspace(0.001, 12, 400)
fig, ax = new_fig(6.0, 3.6)
ax.plot(k, k**0.35, color=C["blue"], lw=LW)
econ_axes(ax, r"$k$", r"$y$", xlim=(0, 12), ylim=(0, 2.6))   # ejes de pizarrón con flecha
label_curve(ax, 12, 12**0.35, r"$f(k)$", C["blue"], dx=4)       # rótulo directo, sin leyenda
save(fig, "t3a_solow")            # -> figs/out/t3a_solow.svg
```
- Colores por rol, en este orden fijo: `blue` (curva principal / producción / país 1), `orange`
  (ahorro-inversión / país 2), `aqua` (depreciación / país 3). Con más de 3 series agregá estilo de
  línea o marcador. `red` y `green` sólo para "mal/bien". Tinta: `ink`, `ink2`, `ink3`.
- Estática comparativa: situación inicial en color, la nueva en el mismo color con línea discontinua
  `ls="--"` o en el siguiente color, con flecha que muestre el desplazamiento.
- Ejes con datos reales: `data_axes(ax, xlabel, ylabel)` (grilla horizontal tenue, sin doble eje nunca).
- Tamaños: ancho 5,5–6,5 in para figuras a página completa; 3–3,4 in para las de `grid-2`.
- Texto matemático con `r"$...$"` (mathtext); coma decimal en números de ejes: usá
  `ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, p: f"{v:.2f}".replace(".", ",")))`.
- Mirá cada SVG renderizado en el preview: rótulos que se pisan = arreglar antes de seguir.
