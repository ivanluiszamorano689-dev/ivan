# Economía III — material para el 1er parcial

Material de estudio de Economía III (FCEJyS, UNSa) para el primer parcial (Temas 1 a 3).

## Los PDFs (carpeta `pdf/`)

| Archivo | Qué es |
|---|---|
| `1_Manual_de_teoria_Temas_1_a_3.pdf` | El manual de teoría mejorado y completado: gráficos de todos los modelos, diagramas de conceptos, fórmulas, ejemplos resueltos, errores típicos y las preguntas reales de parcial de cada tema. |
| `2_Practica_resuelta_1er_parcial.pdf` | La práctica resuelta (TP1 a TP4 y los ejercicios extra) mejorada: cada ejercicio va enunciado → pasos → cuentas → respuesta → gráfico. Suma un simulacro nuevo tipo parcial. |
| `3_Parciales_resueltos.pdf` | Los 9 exámenes reales del primer parcial (2022–2025), transcriptos y resueltos. Para cada opción dice por qué es o no es la correcta, y trae la grilla de respuestas. |
| `4_Paso_a_paso_ejercicios.pdf` | Cómo se resuelve cada ejercicio de parcial, cuenta por cuenta. Incluye la receta de cada tipo de ejercicio, el uso de la calculadora, los controles y qué error lleva a cada opción incorrecta. |

## Cómo se generan (carpeta `src/`)

- `docs/<documento>/`: el contenido. Cada documento tiene un `manifest.json` y sus fragmentos HTML.
- `figs/*.py`: los gráficos, hechos con matplotlib y guardados como SVG en `figs/out/`. El estilo común está en `lib/econ_style.py`.
- `assets/style.css`: el sistema de diseño compartido (cajas didácticas, pasos, opción múltiple, tablas). En `COMPONENTES.md` está la guía de componentes.
- `CLAVE_PARCIALES.md`: la transcripción y la clave de los 9 parciales. Dos verificaciones independientes la contrastaron con las fotos originales. `lib/calculos_parciales.py` reproduce todas las cuentas.
- `build.py`: arma cada documento. Ensambla portada, índice con números de página y fragmentos, y lo imprime a PDF con Chromium; la matemática se escribe con KaTeX.

```bash
cd src
npm install                 # playwright-core (usa el Chromium instalado)
pip install pymupdf matplotlib numpy
python3 build.py --figs     # regenera gráficos y los cuatro PDFs
python3 build.py teoria     # o uno solo
```
