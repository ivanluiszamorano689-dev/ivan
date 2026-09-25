# Cómo retomar este trabajo en una sesión nueva

Rama: `claude/brave-hawking-do0b0t` (repo `ivanluiszamorano689-dev/ivan`). Todo lo necesario está acá; la sesión
anterior no hace falta.

## Estado (25/09/2026)
Los 4 PDFs de `economia3/pdf/` compilan sin errores (0 KaTeX, 0 imágenes faltantes, 0 desbordes):
teoría 102 págs. · práctica 97 · parciales 73 · paso a paso 104.

| Documento | Revisión que tuvo |
|---|---|
| Parciales resueltos | Redacción + revisor adversarial por bloque (completo). Faltó el editor final (no se miraron todas las páginas). |
| Paso a paso | Redacción + revisión parcial: §3 (índices) sin revisar. |
| Manual de teoría | Redacción; solo el Tema 2 tuvo revisor (quizás incompleto). Temas 1 y 3 + banco sin revisar. |
| Práctica resuelta | Redacción sin revisores (los redactores verificaron cuentas con Python). Bloque "Errores + Ejercicios extra" rehecho y verificado. |

## Pendiente, en orden de prioridad
1. Auditar números de la práctica: `docs/practica/10-tp1.html` … `40-tp4.html`.
2. Auditar teoría: `docs/teoria/10-tema1.html`, `30-tema3a.html`, `31-tema3b.html`, `90-banco.html`.
3. Auditar `docs/pasoapaso/30-indices.html`.
4. Revisión visual página por página de los 4 PDFs (saltos de página, gráficos).
5. Opcional: simulacro nuevo tipo parcial en la práctica.

## Fuentes de verdad
- `src/CLAVE_PARCIALES.md`: transcripción y respuestas de los 9 parciales, verificadas por dos agentes contra las fotos.
  No cambiar sin ver la foto. Decisiones ya tomadas: Namibia IDH 0,645 (la foto dice 0,646 por mal redondeo);
  Guyana IDH-D da 0,591 y se marca 0,593 (no afirmar de dónde sale la diferencia); P6 Ej.3 c = "Ninguna"
  (estrictamente, por el signo del exponente); P7 Ej.2 b = "Ninguna"; salud IDG Namibia/Honduras = Honduras;
  P5-3 = e (investigadores = Romer); Ranis-Stewart solo como complemento (no está en la bibliografía de la cátedra).
- `src/lib/calculos_parciales.py`: todas las cuentas de los parciales.
- Originales NO están en el repo: si hacen falta, volvé a subir `teoria.pdf` y `practica.pdf`. Las fotos de
  exámenes no se suben al repo (tienen datos personales); la clave ya tiene todo transcripto.

## Cómo compilar
```bash
cd economia3/src
npm install                                   # playwright-core
pip install pymupdf matplotlib numpy cairosvg
python3 build.py practica                     # o teoria / parciales / pasoapaso; --figs regenera gráficos
python3 build.py --preview prueba docs/practica/40-tp4.html   # vista previa aislada en _build/
```
Si Chromium no está en `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, exportá `CHROMIUM_PATH`.
Guía de componentes y reglas de estilo: `src/COMPONENTES.md`.

## Reglas para no gastar de más (aprendidas en la sesión anterior)
- Nada de workflows ni varios agentes en paralelo: con 8 agentes el gasto fue ~$3/min.
- Una tarea chica por sesión (un archivo o un documento) y cerrar la sesión al terminar.
- Auditar con texto (python + pymupdf / grep), no con imágenes. Mirar PNG solo al final y pocas.
- Sonnet alcanza para auditar cuentas; Opus para decisiones de contenido dudosas.
- Referencia: un revisor Opus costó $3–6 (equivalente API) por bloque de ~25 páginas.

## Pedido modelo para la sesión nueva
"Hacé checkout de la rama claude/brave-hawking-do0b0t y leé economia3/CONTINUAR.md. Auditá solo
economia3/src/docs/practica/40-tp4.html: recalculá con Python cada número, corregí solo errores reales,
recompilá la práctica, hacé commit y push. Sin workflows ni subagentes, sin mirar imágenes. Informe en 10 líneas."
