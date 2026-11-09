# Módulo 3: Hilos Daemon y Temporizadores (Timer) en Python

Este directorio contiene ejemplos pedagógicos paso a paso y un caso completo del mundo real basados en las diapositivas de la lección (**Diapositivas 1 a 7**).

---

## 📑 Resumen de las Diapositivas

| Diapositiva | Título / Tema Principal | Concepto Clave |
| :--- | :--- | :--- |
| **1.PNG** | *Hilos daemon: La idea en una frase* | Se ejecutan en segundo plano y **se matan automáticamente** cuando el programa principal termina.<br>Analogía: *alarma de incendios* (vive mientras el edificio esté vivo). |
| **2.PNG** | *Daemon en acción: con y sin daemon* | **Sin daemon:** el programa espera obligatoriamente.<br>**Con daemon:** el hilo muere al salir.<br>Uso de `h.join(timeout=3)` para esperas con tiempo límite. |
| **3.PNG** | *Cada uno tiene su sitio* | **Normal + join():** Tareas críticas (escribir archivos, transacciones).<br>**Daemon:** Tareas prescindibles (monitoreo, limpieza, heartbeat).<br>⚠️ Nunca escribas archivos críticos en un daemon: puede quedar a medias. |
| **4.PNG** | *Timer: avisos diferidos* | `threading.Timer(retardo, funcion)` ejecuta una función **una sola vez** tras el retardo sin bloquear.<br>Uso de `t.cancel()` para anular el disparo. |
| **5.PNG** | *Usos típicos del Timer* | Avisos, recordatorios, timeouts, expiración de sesión y limpieza.<br>⚠️ Para no alargar el programa: `t.daemon = True`. |
| **6.PNG** | *Mini-chequeo: daemons y Timer* | 1. No impide salida.<br>2. `join(timeout=2)` espera máximo 2s y continúa.<br>3. Dispara una sola vez (para repetir se reprograma a sí mismo). |
| **7.PNG** | *Resumen del bloque 01* | Repaso de: Hilos, ciclo básico (`start`/`join`), `args`/`kwargs`, Daemon y Timer. Adelanto del Bloque 02 (GIL y trazas). |

---

## 📂 Archivos Creados

### 1. `1_HilosDaemonVsNoDaemon.py` (Diapositivas 1, 2, 3 y 6)
- **Propósito:** Demostración pedagógica del comportamiento de hilos normales vs daemons.
- **Qué enseña:**
  - Cómo un hilo normal (`daemon=False`) obliga al intérprete a esperar.
  - Cómo un hilo daemon (`daemon=True`) muere instantáneamente al apagarse el programa principal.
  - Cómo utilizar `h.join(timeout=1.0)` para evitar bloqueos indefinidos.

### 2. `2_TemporizadorTimer.py` (Diapositivas 4, 5 y 6)
- **Propósito:** Control de eventos diferidos con `threading.Timer`.
- **Qué enseña:**
  - Disparo diferido sin bloquear el hilo principal.
  - Cancelación antes del disparo mediante `t.cancel()`.
  - Cómo crear un **Timer periódico** que se repite periódicamente reprogramándose a sí mismo.

### 3. `3_EjemploVidaReal_MonitorYExpiracionSesion.py` (Caso Práctico del Mundo Real)
- **Escenario:** Servidor seguro con dos componentes:
  1. **Monitor de salud en segundo plano (Daemon):** Un *heartbeat* que vigila el estado del servidor y muere solo cuando el servidor se apaga.
  2. **Expiración de sesión bancaria (Timer):** Un auto-logout que cierra la cuenta del usuario si no interactúa tras 1.8 segundos, reiniciándose (`.cancel()`) con cada acción activa del usuario.

---

## 🚀 Cómo Ejecutar los Ejemplos

```bash
cd 3_HilosDaemonYTimer

# 1. Comparar hilo Normal vs Daemon y timeout
python3 1_HilosDaemonVsNoDaemon.py

# 2. Dominar el uso de threading.Timer y su cancelación
python3 2_TemporizadorTimer.py

# 3. Probar el sistema de servidor seguro con monitor y auto-logout
python3 3_EjemploVidaReal_MonitorYExpiracionSesion.py
```

