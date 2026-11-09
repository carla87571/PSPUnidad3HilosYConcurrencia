"""
=============================================================================
TEMA: Nombrar Hilos y Lanzar Varios a la Vez
DIAPOSITIVA: 8
=============================================================================

PATRÓN DE DOS FASES (Diapositiva 8):
1. FASE DE LANZAMIENTO:
   Creamos una lista de hilos y en un primer bucle llamamos a .start() en todos.
   ¡Esto permite que arranquen a trabajar de forma verdaderamente simultánea!

2. FASE DE REUNIÓN / ESPERA:
   En un segundo bucle independiente llamamos a .join() en cada uno.
   Esto asegura que el hilo principal espere a que TODOS los hilos concluyan.

⚠️ EL ORDEN DEL SCHEDULER DEL SISTEMA OPERATIVO:
- El orden en que los hilos imprimen en consola NO ESTÁ GARANTIZADO:
  lo decide el planificador (scheduler) del SO según la disponibilidad de la CPU.
- El mensaje final ("Todas las tareas terminadas"), sin embargo, SIEMPRE sale al final,
  garantizado por los .join().
=============================================================================
"""

import threading
import time
import random


def ejecutar_tarea(numero_tarea: int):
    """
    Función que ejecuta cada hilo trabajador.
    Recibe el número de tarea y consulta su propio nombre.
    """
    nombre_hilo = threading.current_thread().name
    print(f"  🟢 [{nombre_hilo}] -> Iniciando Tarea #{numero_tarea}...")

    # Simulamos duraciones ligeramente variables para evidenciar al scheduler del SO
    duracion = random.uniform(0.5, 1.5)
    time.sleep(duracion)

    print(f"  🏁 [{nombre_hilo}] -> ¡Tarea #{numero_tarea} completada en {duracion:.2f}s!")


def main():
    print("=" * 65)
    print(" GESTIÓN DE MÚLTIPLES HILOS Y NOMBRES (Diapositiva 8)")
    print("=" * 65)

    cantidad_hilos = 5

    # 1. Creación de los hilos utilizando List Comprehension
    # Asignamos a cada hilo un nombre descriptivo: 'hilo-1', 'hilo-2', etc.
    hilos = [
        threading.Thread(
            target=ejecutar_tarea,
            args=(i,),
            name=f"hilo-{i}"
        )
        for i in range(1, cantidad_hilos + 1)
    ]

    print(f"📦 Se han creado {len(hilos)} instancias de hilos.")

    # 2. BUCLE 1: Lanza todos los hilos
    print("\n🚀 BUCLE 1: Arrancando todos los hilos (start)...")
    for h in hilos:
        h.start()

    print("📢 [MainThread] Todos los hilos están corriendo a la vez.")
    print("📢 [MainThread] Nota cómo el orden de finalización puede variar según el SO.\n")

    # 3. BUCLE 2: Espera a todos los hilos
    print("⏳ BUCLE 2: Esperando a que todos finalicen (join)...")
    for h in hilos:
        h.join()

    # 4. Mensaje final garantizado
    print("\n" + "=" * 65)
    print("🎉 ¡TODAS LAS TAREAS TERMINADAS!")
    print("   El 'join()' garantizó que este mensaje siempre se imprima al final.")
    print("=" * 65)


if __name__ == "__main__":
    main()

