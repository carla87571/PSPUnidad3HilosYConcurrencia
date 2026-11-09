# 4_EjerciciosPracticos: Taller de Hilos en Python

Este directorio contiene las soluciones completas y pedagógicas a los **8 ejercicios prácticos** sobre concurrencia con la librería `threading` de Python.

---

## 📑 Lista de Ejercicios y Archivos

| # | Archivo | Tema Principal | Conceptos Clave |
| :---: | :--- | :--- | :--- |
| **1** | [`1_HiloQueCuenta.py`](file:///home/carla3/ANTIGRAVITY/hilos/4_EjerciciosPracticos/1_HiloQueCuenta.py) | Hilo que cuenta del 1 al 5 | Creación con `Thread(target=...)`, `.start()` y `.join()`. |
| **2** | [`2_MultiplesHilosConRetardo.py`](file:///home/carla3/ANTIGRAVITY/hilos/4_EjerciciosPracticos/2_MultiplesHilosConRetardo.py) | Múltiples hilos con `time.sleep(1)` | Concurrencia real: 3 hilos durmiendo 1s tardan ~1s en total, no 3s. |
| **3** | [`3_HiloConArgumento.py`](file:///home/carla3/ANTIGRAVITY/hilos/4_EjerciciosPracticos/3_HiloConArgumento.py) | Hilo con argumento | Paso de tupla con la coma final obligatoria: `args=("Ana",)`. |
| **4** | [`4_HiloQueSaluda.py`](file:///home/carla3/ANTIGRAVITY/hilos/4_EjerciciosPracticos/4_HiloQueSaluda.py) | Las 3 líneas mágicas | Estructura canónica fundamental de un hilo en Python. |
| **5** | [`5_DosHilosEnParalelo.py`](file:///home/carla3/ANTIGRAVITY/hilos/4_EjerciciosPracticos/5_DosHilosEnParalelo.py) | Dos hilos en paralelo | Observación del entremezclado de prints por el scheduler del SO. |
| **6** | [`6_HiloConNombre.py`](file:///home/carla3/ANTIGRAVITY/hilos/4_EjerciciosPracticos/6_HiloConNombre.py) | Hilo con nombre | Asignación de `name="MiHilo"` y consulta con `threading.current_thread().name`. |
| **7** | [`7_EsperandoConJoin.py`](file:///home/carla3/ANTIGRAVITY/hilos/4_EjerciciosPracticos/7_EsperandoConJoin.py) | Esperando con `join()` | Demostración del orden exacto de salida garantizado por `join()`. |
| **8** | [`8_VariosHilosNombreArgumentos.py`](file:///home/carla3/ANTIGRAVITY/hilos/4_EjerciciosPracticos/8_VariosHilosNombreArgumentos.py) | Varios hilos en bucle + Timer | List comprehension, dos bucles (`start`/`join`) y Timer periódico con `daemon=True`. |

---

## 🚀 Cómo Ejecutarlos

Puedes colocarte dentro de la carpeta y ejecutar cualquiera de los archivos con `python3`:

```bash
cd 4_EjerciciosPracticos

python3 1_HiloQueCuenta.py
python3 2_MultiplesHilosConRetardo.py
python3 3_HiloConArgumento.py
python3 4_HiloQueSaluda.py
python3 5_DosHilosEnParalelo.py
python3 6_HiloConNombre.py
python3 7_EsperandoConJoin.py
python3 8_VariosHilosNombreArgumentos.py
```

