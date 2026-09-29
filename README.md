# ivan
Para pruebas de CLAUDE

## Cuentas Claras (`finanzas/`)

App web para anotar ingresos y gastos y llevar un presupuesto mensual, desde el celular o la compu.
Es un solo archivo HTML (`finanzas/index.html`), sin instalar nada.

En el celular usa una barra de pestañas abajo. En pantallas anchas (compu) pasa a un menú lateral con el contenido
en dos columnas. Atajos de teclado en la compu: `N` carga un movimiento, `←` / `→` cambian de mes.

**Qué hace**

- **Inicio:** saldo del mes (ingresos − gastos), estado del presupuesto, gastos por categoría y comparación de los últimos 6 meses.
- **Movimientos:** lista por día, con filtro por tipo, por categoría y búsqueda por nota.
- **Presupuesto:** tope mensual por categoría, cuánto queda, cuánto podés gastar por día y aviso cuando te acercás o te pasás.
- **Proyección:** créditos (lo que te deben) y deudas al cierre de cada mes, resultado devengado del mes y saldo
  proyectado de los próximos 12 meses con los fijos ajustados por la inflación mensual estimada.
- **Ajustes:** crear, renombrar y archivar categorías; exportar/importar una copia (`.json`) y exportar planilla (`.csv` para Excel).
- **Movimientos fijos:** sueldo, cuotas, servicios y todo lo que se repite cada mes. Cada mes aparecen en Inicio para
  anotarlos con un toque, con el saldo proyectado del mes. Admiten cuotas, montos por cada sábado del mes anterior y
  un aviso periódico para actualizar el monto (por ejemplo, ajuste trimestral por IPC).
- Al cargar un monto se pueden sumar varios: `1500+830`. Acepta `15.000`, `1.500,50`, etc.

**Dónde se guardan los datos**

Abierta como página normal, los datos quedan en el navegador del teléfono (`localStorage`).
Conviene exportar una copia cada tanto desde Ajustes.

**Cómo tenerla en el celu**

1. Publicar la carpeta `finanzas/` en cualquier hosting estático con HTTPS (por ejemplo GitHub Pages).
2. Abrir la dirección en el navegador del teléfono.
3. Menú → **Agregar a pantalla de inicio** (en iPhone, desde el botón Compartir en Safari).

Con HTTPS funciona sin conexión gracias a `sw.js`.
