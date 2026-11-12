# 5_EjerciciosPracticos: Boletín UD03 — Avanzado (Hilos en Python)

Este directorio contiene las soluciones pedagógicas completas a las **Actividades no evaluables 02 (Boletín UD03 — Avanzado)** sobre la librería `threading` y conceptos avanzados de concurrencia en Python.

---

## 📑 Lista de Ejercicios y Conceptos Aplicados

| # | Archivo | Concepto Clave | Descripción |
| :---: | :--- | :--- | :--- |
| **1** | [`1_JoinConTimeout.py`](file:///home/carla3/ANTIGRAVITY/hilos/5_EjerciciosPracticos/1_JoinConTimeout.py) | `h.join(timeout=2)` e `is_alive()` | Espera con límite de tiempo sin congelar el programa principal. |
| **2** | [`2_ListarHilosActivos.py`](file:///home/carla3/ANTIGRAVITY/hilos/5_EjerciciosPracticos/2_ListarHilosActivos.py) | `threading.enumerate()` | Inspecciona e itera sobre todos los hilos actualmente vivos en el proceso. |
| **3** | [`3_IdentificarHiloActual.py`](file:///home/carla3/ANTIGRAVITY/hilos/5_EjerciciosPracticos/3_IdentificarHiloActual.py) | `current_thread()` introspección | Consulta `.name`, `.ident` y `.daemon` desde el hilo principal y un secundario. |
| **4** | [`4_CarreraMensajes.py`](file:///home/carla3/ANTIGRAVITY/hilos/5_EjerciciosPracticos/4_CarreraMensajes.py) | Scheduler del Sistema Operativo | 5 hilos imprimiendo 10 veces para evidenciar el orden impredecible de CPU. |
| **5** | [`5_SimularDescargaProgreso.py`](file:///home/carla3/ANTIGRAVITY/hilos/5_EjerciciosPracticos/5_SimularDescargaProgreso.py) | Progreso con saltos de 25% | Simulación de descarga con `range(0, 101, 25)` y barra visual en consola. |
| **6** | [`6_DetenerHiloBandera.py`](file:///home/carla3/ANTIGRAVITY/hilos/5_EjerciciosPracticos/6_DetenerHiloBandera.py) | Bandera booleana de parada | Detención limpia de un bucle infinito mediante `ejecutando = False` al presionar Enter. |
| **7** | [`7_HiloDevuelveValor.py`](file:///home/carla3/ANTIGRAVITY/hilos/5_EjerciciosPracticos/7_HiloDevuelveValor.py) | Memoria compartida | Retorno de datos de un hilo al hilo principal usando una lista como contenedor mutable. |
| **8** | [`8_TimerConRepeticion.py`](file:///home/carla3/ANTIGRAVITY/hilos/5_EjerciciosPracticos/8_TimerConRepeticion.py) | Timer periódico recurrente | Reprogramación automática con `threading.Timer` y modo `daemon=True`. |
| **9** | [`9_PoolHilosManual.py`](file:///home/carla3/ANTIGRAVITY/hilos/5_EjerciciosPracticos/9_PoolHilosManual.py) | Pool manual con `queue.Queue` | 2 trabajadores consumiendo tareas concurrentemente con `cola.get()`, `task_done()` y `join()`. |

---

## 🚀 Cómo Ejecutar los Ejercicios

Puedes colocarte dentro de la carpeta y ejecutar cada ejercicio con `python3`:

```bash
cd 5_EjerciciosPracticos

python3 1_JoinConTimeout.py
python3 2_ListarHilosActivos.py
python3 3_IdentificarHiloActual.py
python3 4_CarreraMensajes.py
python3 5_SimularDescargaProgreso.py
python3 6_DetenerHiloBandera.py
python3 7_HiloDevuelveValor.py
python3 8_TimerConRepeticion.py
python3 9_PoolHilosManual.py
```
