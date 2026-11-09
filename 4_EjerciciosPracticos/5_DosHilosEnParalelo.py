"""
=============================================================================
EJERCICIO 5: Dos hilos en paralelo
ENUNCIADO:
Crea dos funciones hilo_a() y hilo_b(), cada una con un bucle que imprima
su nombre 3 veces. Lanza los dos hilos y observa cómo se entremezclan los mensajes.
=============================================================================
"""

import threading
import time


def hilo_a():
    """Imprime el nombre del Hilo A 3 veces."""
    for i in range(1, 4):
        print(f"🔵 [Hilo A] - Mensaje #{i}")
        time.sleep(0.2)


def hilo_b():
    """Imprime el nombre del Hilo B 3 veces."""
    for i in range(1, 4):
        print(f"    🟠 [Hilo B] - Mensaje #{i}")
        time.sleep(0.2)


def main():
    print("=" * 55)
    print("EJERCICIO 5: DOS HILOS EN PARALELO (ENTREMEZCLADO)")
    print("=" * 55)

    # 1. Crear ambos hilos
    thread_a = threading.Thread(target=hilo_a)
    thread_b = threading.Thread(target=hilo_b)

    # 2. Lanzar ambos hilos simultáneamente
    print("🚀 [MainThread] Lanzando Hilo A y Hilo B al mismo tiempo...\n")
    thread_a.start()
    thread_b.start()

    # 3. Esperar a que ambos concluyan
    thread_a.join()
    thread_b.join()

    print("\n✅ [MainThread] Ambos hilos han terminado.")
    print("💡 Observa cómo las salidas de [Hilo A] e [Hilo B] se intercalan.")
    print("=" * 55)


if __name__ == "__main__":
    main()

