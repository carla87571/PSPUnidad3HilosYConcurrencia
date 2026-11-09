"""
=============================================================================
EJERCICIO 6: Hilo con nombre
ENUNCIADO:
Crea una función que imprima f"Soy {threading.current_thread().name}".
Lánzala en un hilo con name="MiHilo".
=============================================================================
"""

import threading


def identificar_hilo():
    """Imprime el nombre del hilo en ejecución usando current_thread()."""
    nombre_actual = threading.current_thread().name
    print(f"👉 Soy {nombre_actual}")


def main():
    print("=" * 55)
    print("EJERCICIO 6: HILO CON NOMBRE PERSONALIZADO")
    print("=" * 55)

    # Creamos el hilo asignando el parámetro name="MiHilo"
    hilo = threading.Thread(
        target=identificar_hilo,
        name="MiHilo"
    )

    print(f"📋 Nombre asignado antes de arrancar: '{hilo.name}'")

    hilo.start()
    hilo.join()

    print("=" * 55)


if __name__ == "__main__":
    main()

