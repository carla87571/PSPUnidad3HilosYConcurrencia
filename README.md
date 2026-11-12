# PSP Unidad 3: Programación de Servicios y Procesos - Hilos y Concurrencia en Python

Repositorio educativo con explicaciones teóricas, analogías pedagógicas, ejemplos del mundo real y ejercicios prácticos sobre el módulo `threading` en Python.

---

## 🗂️ Estructura del Repositorio

El proyecto se encuentra organizado en 5 bloques temáticos:

### 1. [`1_HilosVsProcesos/`](./1_HilosVsProcesos)
* **Conceptos clave:** Diferencias entre procesos e hilos (memoria compartida, costo de creación, aislamiento, condiciones de carrera).
* **Analogía:** Cocinas de restaurantes independientes (procesos) vs cocineros en la misma cocina (hilos).
* **Archivos:**
  * `1_tuPrimerHilo.py`: Demostración pedagógica del mismo PID y memoria compartida.
  * `2_HilosEjemplo1.py`: Caso real (Descarga concurrente de archivos reduciendo el tiempo de 6.0s a 2.5s).
  * `diapositivas/`: 7 diapositivas explicativas (Bloque 31 a 37).

### 2. [`2_hilosPropiedadesYArgumentos/`](./2_hilosPropiedadesYArgumentos)
* **Conceptos clave:** Ciclo de vida del hilo, errores típicos (`target=fn` vs `target=fn()`), propiedades (`.ident`, `.name`, `.is_alive()`), argumentos con `args` (tupla) y `kwargs` (diccionario), y el truco de la coma `args=("Ana",)`.
* **Archivos:**
  * `1_ErroresComunesYCicloDeVida.py`: Errores de principiante y segundo start.
  * `2_PropiedadesDelHilo.py`: Inspección de propiedades en sus 3 fases.
  * `3_ArgumentosArgsYKwargs.py`: Paso de argumentos posicionales y nombrados.
  * `4_VariosHilosYNombres.py`: Patrón de 2 fases (lanzar todos / esperar a todos).
  * `5_EjemploVidaReal_NotificacionesYProcesamiento.py`: Servicio multicanal (Email, SMS, Push, Analítica).
  * `diapositivas/`: 9 diapositivas explicativas (Bloque 1 a 9).

### 3. [`3_HilosDaemonYTimer/`](./3_HilosDaemonYTimer)
* **Conceptos clave:** Hilos daemon (servicios de fondo prescindibles que mueren con el programa principal), temporizadores `threading.Timer`, avisos diferidos y cancelación con `t.cancel()`.
* **Archivos:**
  * `1_HilosDaemonVsNoDaemon.py`: Comparativa de comportamiento y timeout con `join()`.
  * `2_TemporizadorTimer.py`: Disparo diferido, cancelación y timer periódico.
  * `3_EjemploVidaReal_MonitorYExpiracionSesion.py`: Monitor de servidor (*heartbeat*) y auto-logout bancario.
  * `diapositivas/`: 7 diapositivas explicativas (Bloque 1 a 7).

### 4. [`4_EjerciciosPracticos/`](./4_EjerciciosPracticos)
* **Taller de 8 ejercicios prácticos:**
  1. `1_HiloQueCuenta.py`: Conteo del 1 al 5 con `start()` y `join()`.
  2. `2_MultiplesHilosConRetardo.py`: 3 hilos concurrentes con `time.sleep(1)`.
  3. `3_HiloConArgumento.py`: Hilo con tupla y coma final `args=("Ana",)`.
  4. `4_HiloQueSaluda.py`: Las tres líneas mágicas canónicas.
  5. `5_DosHilosEnParalelo.py`: Intercalado de mensajes entre dos hilos.
  6. `6_HiloConNombre.py`: Uso de `name="MiHilo"` y `current_thread().name`.
  7. `7_EsperandoConJoin.py`: Garantía del orden secuencial con `join()`.
  8. `8_VariosHilosNombreArgumentos.py`: Lista por comprensión, bucles de control y Timer recurrente.

### 5. [`5_EjerciciosPracticos/`](./5_EjerciciosPracticos)
* **Boletín Avanzado de 9 actividades:**
  1. `1_JoinConTimeout.py`: Join con límite de tiempo e inspección con `is_alive()`.
  2. `2_ListarHilosActivos.py`: Listar hilos vivos con `threading.enumerate()`.
  3. `3_IdentificarHiloActual.py`: Introspección con `threading.current_thread()`.
  4. `4_CarreraMensajes.py`: Intercalado y scheduler de CPU con 5 hilos.
  5. `5_SimularDescargaProgreso.py`: Progreso porcentual en pasos de 25%.
  6. `6_DetenerHiloBandera.py`: Parada limpia de un hilo con bandera booleana (`ejecutando`).
  7. `7_HiloDevuelveValor.py`: Devolución de valores usando memoria compartida.
  8. `8_TimerConRepeticion.py`: Timer periódico recurrente con `daemon=True`.
  9. `9_PoolHilosManual.py`: Pool manual de trabajadores con `queue.Queue`.

---

## 🛠️ Requisitos y Ejecución

* **Python:** Versión 3.8 o superior.
* Sin librerías externas necesarias (utiliza la librería estándar `threading`).

Para ejecutar cualquier script:
```bash
python3 1_HilosVsProcesos/1_tuPrimerHilo.py
python3 2_hilosPropiedadesYArgumentos/5_EjemploVidaReal_NotificacionesYProcesamiento.py
python3 3_HilosDaemonYTimer/3_EjemploVidaReal_MonitorYExpiracionSesion.py
python3 4_EjerciciosPracticos/1_HiloQueCuenta.py
```

