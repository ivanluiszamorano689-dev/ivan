# Cuentas Claras entre dos personas

Guía para usar la app en los celulares de las dos personas, con los mismos datos, sin depender de Claude.
Todo es gratis. Se hace una sola vez y lleva unos 15 minutos.

- **La app** se publica gratis en GitHub Pages.
- **Los datos** se guardan en Firebase, la base de datos gratuita de Google. No ocupa espacio de Google Drive.
- Cada persona entra con su email y su contraseña. Comparten un **hogar**: lo que carga uno lo ve el otro al instante.
- **Sin conexión:** la app sigue funcionando y sincroniza sola cuando vuelve internet.

## 1. Publicar la app

1. En GitHub, entrá al repositorio **ivan** → **Settings** → **Pages**.
2. En **Build and deployment**, elegí **Source: Deploy from a branch**.
3. En **Branch**, elegí `claude/relaxed-johnson-c30z8q` y la carpeta `/ (root)`. Tocá **Save**.
4. En uno o dos minutos la app queda en:
   **https://ivanluiszamorano689-dev.github.io/ivan/finanzas/**

El código queda a la vista de cualquiera, pero no incluye ningún dato tuyo. Los datos viven en Firebase y solo los ven los miembros del hogar.

## 2. Crear la base de datos en Firebase

1. Entrá a **console.firebase.google.com** con tu cuenta de Google y tocá **Crear proyecto**.
   Poné cualquier nombre, por ejemplo `cuentas-claras`. Google Analytics no hace falta. No pide tarjeta.
2. **Compilación → Authentication → Comenzar**. En **Método de acceso**, activá **Correo electrónico/contraseña** y guardá.
3. **Compilación → Firestore Database → Crear base de datos**:
   - si te pregunta la edición, elegí **Estándar**;
   - ubicación: **southamerica-east1 (São Paulo)**;
   - elegí **modo de producción**.
4. En la pestaña **Reglas** de Firestore, borrá todo, pegá estas reglas y tocá **Publicar**.
   También están en la app, con un botón para copiarlas.

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    function signedIn() { return request.auth != null; }
    match /usuarios/{uid} {
      allow read, write: if signedIn() && request.auth.uid == uid;
    }
    match /hogares/{hid} {
      allow read: if signedIn() && request.auth.uid in resource.data.miembros;
      allow create: if signedIn() && request.resource.data.miembros == [request.auth.uid];
      allow update: if signedIn() && (
        request.auth.uid in resource.data.miembros ||
        (request.resource.data.miembros == resource.data.miembros.concat([request.auth.uid])
          && request.resource.data.diff(resource.data).affectedKeys().hasOnly(['miembros', 'nombres'])
          && request.resource.data.nombres.diff(resource.data.nombres).affectedKeys().hasOnly([request.auth.uid])
          && resource.data.miembros.size() < 6));
      match /datos/{doc} {
        allow read, write: if signedIn()
          && request.auth.uid in get(/databases/$(database)/documents/hogares/$(hid)).data.miembros;
      }
    }
  }
}
```

5. Tocá el engranaje **⚙ → Configuración del proyecto**. Abajo, en **Tus apps**, tocá el ícono web **</>**.
   Poné un nombre, no marques Hosting y tocá **Registrar app**.
6. Copiá el bloque que empieza con `const firebaseConfig = {`.

## 3. Conectar la app y pasar tus datos

1. Abrí la app en el celu: **https://ivanluiszamorano689-dev.github.io/ivan/finanzas/**
2. **Ajustes → Importar copia** y elegí el archivo `cuentas-claras-copia-2026-09-29.json`. Tiene todo lo que cargaste hasta hoy.
3. **Ajustes → Configurar sincronización**, pegá el `firebaseConfig` y tocá **Guardar y conectar**.
4. **Entrar o crear cuenta**: poné tu nombre, tu email y una contraseña.
5. Tocá **Crear hogar con mis datos**. Lo que tenés en el celu pasa al hogar compartido.

## 4. Invitar a tu pareja

1. En **Ajustes**, tocá **Invitar** y mandale el link por WhatsApp.
2. Ella abre el link, pone su nombre, email y contraseña, y listo: ve y carga lo mismo que vos.

El link da acceso a tus cuentas. Mandáselo solo a ella.

## En el día a día

- **Como app:** en el navegador del celu elegí **Agregar a pantalla de inicio** (en iPhone, desde Compartir en Safari).
- **Quién cargó qué:** cada movimiento muestra quién lo cargó.
- **En la compu:** entrás a la misma dirección con la misma cuenta.
- **Para el Excel:** **Ajustes → Exportar gastos para el Excel** baja los gastos variables con las columnas de la hoja *Gastos variables*. Abrí el archivo y pegá las filas desde la fila 6.
- **Copia de seguridad:** cada tanto, **Ajustes → Exportar copia**.

## Límites del plan gratis de Firebase

El plan Spark da 1 GB de datos, 50.000 lecturas y 20.000 escrituras por día. Una pareja usa una mínima parte.
Si alguna vez se llegara al límite, la app deja de sincronizar hasta el día siguiente, pero no se pierde nada.
