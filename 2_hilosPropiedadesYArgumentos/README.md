# Módulo 2: Hilos - Propiedades y Argumentos en Python

Este directorio contiene ejemplos pedagógicos y casos del mundo real basados en las diapositivas del bloque (**Diapositivas 1 a 9**).

---

## 📑 Mapeo de Diapositivas

| Diapositiva | Título / Tema Principal | Concepto Clave |
| :--- | :--- | :--- |
| **1.PNG** | *Tu primer hilo: La idea en una frase* | Las 3 fases: `Thread(target=fn)` (crea), `start()` (lanza), `join()` (espera). |
| **2.PNG** | *El error típico de principiante* | ❌ `Thread(target=fn())` ejecuta de inmediato en el hilo principal.<br>✅ `Thread(target=fn)` pasa la referencia.<br>⚠️ `start()` solo se llama **una vez**. |
| **3.PNG** | *El hilo principal vs los secundarios* | `MainThread` no espera por arte de magia: sin `join()`, el último print puede salir desordenado. El intérprete espera a hilos no-daemon. |
| **4.PNG** | *join(): esperar a que termine* | Bloquea al hilo que lo llama (`MainThread`) hasta que el trabajador acaba su tarea. |
| **5.PNG** | *Propiedades de un hilo* | `.name`, `.ident`, `.daemon`, `.is_alive()` y `threading.current_thread()`. |
| **6.PNG** | *Hilos con argumentos: La idea en una frase* | Permite que cada hilo trabaje con datos propios y haga su versión de la tarea. |
| **7.PNG** | *Pasar argumentos: args y kwargs* | `args=` (tupla posicional), `kwargs=` (diccionario por clave).<br>⚠️ **Truco de la coma:** `args=("Ana",)`. |
| **8.PNG** | *Nombrar hilos y lanzar varios a la vez* | Patrón de 2 fases: 1º bucle lanza todos (`start()`), 2º bucle espera a todos (`join()`). El orden de ejecución lo define el scheduler del SO. |
| **9.PNG** | *Mini-chequeo: argumentos* | Respuestas del cuestionario de repaso. |

---

## 📂 Archivos Creados

### 1. `1_ErroresComunesYCicloDeVida.py` (Diapositivas 1, 2 y 3)
- Demuestra la diferencia entre pasar `target=fn` vs `target=fn()`.
- Captura pedagógicamente el error `RuntimeError: threads can only be started once`.
- Demuestra por qué `join()` es necesario para sincronizar el flujo con el `MainThread`.

### 2. `2_PropiedadesDelHilo.py` (Diapositiva 5)
- Inspecciona las propiedades del hilo antes de `start()`, durante su ejecución y después de `join()`.
- Muestra el uso de `threading.current_thread()`, `.ident`, `.name`, `.daemon` y `.is_alive()`.

### 3. `3_ArgumentosArgsYKwargs.py` (Diapositivas 6, 7 y 9)
- Enseña el uso de tuplas con `args` y diccionarios con `kwargs`.
- Reproduce y explica **la trampa de la coma** (`args=("Ana")` vs `args=("Ana",)`).

### 4. `4_VariosHilosYNombres.py` (Diapositiva 8)
- Implementa el patrón canónico de dos fases para múltiples hilos.
- Demuestra cómo el scheduler del Sistema Operativo puede alternar el orden de finalización, pero `join()` garantiza el cierre ordenado.

### 5. `5_EjemploVidaReal_NotificacionesYProcesamiento.py` (Caso Práctico Completo)
- **Escenario:** Servicio de notificaciones multicanal para una tienda online (Email, SMS, Push y Analítica).
- Combina `args`, `kwargs`, nombres de hilos, monitorización con `.is_alive()` y reducción del tiempo total de espera de 4.0s a solo 1.5s.

---

## 🚀 Cómo Ejecutar los Ejemplos

```bash
cd 2_hilosPropiedadesYArgumentos

# 1. Aprender el ciclo de vida y evitar errores comunes
python3 1_ErroresComunesYCicloDeVida.py

# 2. Inspeccionar propiedades (.ident, .name, .is_alive())
python3 2_PropiedadesDelHilo.py

# 3. Dominar args, kwargs y el truco de la coma
python3 3_ArgumentosArgsYKwargs.py

# 4. Lanzar múltiples hilos con el patrón de dos fases
python3 4_VariosHilosYNombres.py

# 5. Probar el sistema de notificaciones de la vida real
python3 5_EjemploVidaReal_NotificacionesYProcesamiento.py
```

