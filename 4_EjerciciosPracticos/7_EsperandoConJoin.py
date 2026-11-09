"""
=============================================================================
EJERCICIO 7: Esperando con join()
ENUNCIADO:
Crea un hilo que imprima "Empezando", duerma 3 segundos y termine imprimiendo
"Terminado". En el programa principal, después de start(), espera con join() y
luego imprime "El programa terminó". Comprueba el orden de las tres salidas.
=============================================================================
"""

import threading
import time


def tarea_demorada():
    """Función que dura 3 segundos simulando un proceso."""
    print("Empezando")
    time.sleep(3.0)
    print("Terminado")


def main():
    print("=" * 55)
    print("EJERCICIO 7: CONTROL DEL ORDEN CON join()")
    print("=" * 55)

    hilo = threading.Thread(target=tarea_demorada)

    # 1. Lanzamos el hilo
    hilo.start()

    # 2. Esperamos con join() a que termine la función tarea_demorada
    hilo.join()

    # 3. Solo después del join() se imprime el mensaje final
    print("El programa terminó")
    print("=" * 55)


if __name__ == "__main__":
    main()

