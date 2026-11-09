"""
=============================================================================
EJERCICIO 4: Hilo que saluda (Las tres líneas mágicas)
ENUNCIADO:
Crea un hilo que ejecute una función que imprima "Hola desde un hilo".
Usa threading.Thread, start() y join().
=============================================================================
"""

import threading


def saludar():
    """Función básica a ejecutar por el hilo."""
    print("¡Hola desde un hilo!")


def main():
    print("=" * 55)
    print("EJERCICIO 4: HILO QUE SALUDA (3 LÍNEAS MÁGICAS)")
    print("=" * 55)

    # Línea 1: Crear el hilo (sin ejecutar aún la función)
    hilo = threading.Thread(target=saludar)

    # Línea 2: Lanzar el hilo (pasa a estado ejecutable)
    hilo.start()

    # Línea 3: Esperar a que el hilo termine
    hilo.join()

    print("=" * 55)


if __name__ == "__main__":
    main()

