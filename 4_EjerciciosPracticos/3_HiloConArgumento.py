"""
=============================================================================
EJERCICIO 3: Hilo con argumento
ENUNCIADO:
Crea una función que reciba un nombre como argumento e imprima "Hola, {nombre}".
Lanza un hilo pasándole el argumento con args=("Ana",).

💡 PISTA DE LAS DIAPOSITIVAS:
Recuerda la coma final de la tupla: args=("Ana",).
Sin la coma, ("Ana") es interpretado por Python como un simple string y no una tupla.
Al desempaquetarlo, pasa 3 caracteres ('A', 'n', 'a') como argumentos independientes,
provocando: TypeError: la función esperaba 1 argumento pero recibió 3.
=============================================================================
"""

import threading


def saludar_persona(nombre: str):
    """Función que recibe un único parámetro de texto."""
    print(f"👋 Hola, {nombre}")


def main():
    print("=" * 55)
    print("EJERCICIO 3: HILO CON ARGUMENTO Y LA COMA FINAL")
    print("=" * 55)

    # Creamos el hilo usando args con la coma al final de la tupla: ("Ana",)
    hilo = threading.Thread(
        target=saludar_persona,
        args=("Ana",)  # <-- ¡COMA FINAL OBLIGATORIA PARA TUPLA DE 1 ELEMENTO!
    )

    print("🚀 [MainThread] Lanzando hilo con args=('Ana',)...")
    hilo.start()

    print("⏳ [MainThread] Esperando a que termine...")
    hilo.join()

    print("✅ [MainThread] Saludo completado con éxito.")
    print("=" * 55)


if __name__ == "__main__":
    main()

