# Módulo 1: Hilos vs Procesos en Python

Este directorio contiene ejemplos prácticos y pedagógicos basados en las diapositivas de la lección (**Diapositivas 31 a 37**).

---

## 📑 Resumen de las Diapositivas

| Diapositiva | Título / Tema | Concepto Clave |
| :--- | :--- | :--- |
| **31.PNG** | *Lo que veremos en este bloque* | De proceso a hilo, `Thread`, `start`, `join`, argumentos (`args`, `kwargs`), hilos Daemon y Timer. |
| **32.PNG** | *De proceso a hilo* | Un hilo es la unidad más pequeña de ejecución que vive **dentro de un proceso** y **comparte su memoria**. |
| **33.PNG** | *Un proceso, varios hilos* | En un mismo proceso (PID común), conviven el hilo principal (`main`), hilos trabajadores (`workers`), y demonios con memoria compartida. |
| **34.PNG** | *Tabla: Hilos vs Procesos* | Memoria compartida vs aislada, creación rápida vs lenta, bajo aislamiento y peligro de condición de carrera (*race conditions*). |
| **35.PNG** | *Crear y lanzar un hilo* | Las **3 líneas mágicas**: `Thread(target=...)`, `.start()`, `.join()`. |
| **36.PNG** | *La analogía de los chefs* | **Procesos:** Restaurantes separados (aislados, fogones propios).<br>**Hilos:** Cocineros en la misma cocina (comparten nevera/memoria, baratos, riesgo si tocan el mismo ingrediente). |
| **37.PNG** | *Mini-chequeo* | 1. Vive dentro del proceso.<br>2. Más barato porque no copia recursos del SO.<br>3. Precio: bajo aislamiento. |

---

## 📂 Archivos Creados

### 1. `1_tuPrimerHilo.py`
- **Propósito:** Código pedagógico paso a paso.
- **Qué enseña:**
  - Las 3 líneas mágicas: creación con `threading.Thread`, ejecución con `.start()` y sincronización con `.join()`.
  - Demostración de que el hilo principal y el secundario comparten el **mismo PID** (`os.getpid()`).
  - Demostración de **memoria compartida** agregando un elemento a una lista común.

### 2. `2_HilosEjemplo1.py`
- **Propósito:** Ejemplo del mundo real fácil de entender (Descargador concurrente de archivos).
- **Qué enseña:**
  - Cómo pasar argumentos a cada hilo (`args=(nombre, tamano, duracion)`).
  - Comparativa en tiempo real entre la ejecución **secuencial** (6.0 segundos) vs **concurrente con hilos** (2.5 segundos).
  - Hilos trabajadores (`Worker-1`, `Worker-2`, `Worker-3`) operando en paralelo y depositando resultados en un diccionario compartido.

---

## 🚀 Cómo ejecutar los ejemplos

```bash
# Ejemplo 1: Tu primer hilo pedagógico
python3 1_tuPrimerHilo.py

# Ejemplo 2: Caso de la vida real (Descargas en paralelo)
python3 2_HilosEjemplo1.py
```

