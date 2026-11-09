"""
=============================================================================
EJERCICIO 1: Hilo que cuenta
ENUNCIADO:
Crea un hilo que ejecute una función que cuente del 1 al 5 imprimiendo cada
número. Lánzalo con start() y espera con join().
=============================================================================
"""

import threading
import time


def contar_uno_al_cinco():
    """Cuenta del 1 al 5 con una breve pausa entre cada número."""
    print("👉 [Hilo] Iniciando conteo:")
    for i in range(1, 6):
        print(f"   Número: {i}")
        time.sleep(0.3)
    print("👉 [Hilo] Conteo finalizado.")


def main():
    print("=" * 55)
    print("EJERCICIO 1: HILO QUE CUENTA (1 al 5)")
    print("=" * 55)

    # 1. Crear el hilo con target apuntando a la función (sin paréntesis)
    hilo = threading.Thread(target=contar_uno_al_cinco)

    # 2. Lanzar el hilo con start()
    print("🚀 [MainThread] Lanzando el hilo...")
    hilo.start()

    # 3. Esperar a que termine con join()
    print("⏳ [MainThread] Esperando a que el hilo termine con join()...")
    hilo.join()

    print("✅ [MainThread] El hilo terminó correctamente. Fin del programa.")
    print("=" * 55)


if __name__ == "__main__":
    main()

