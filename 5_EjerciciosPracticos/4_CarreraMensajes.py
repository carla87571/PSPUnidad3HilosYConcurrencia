"""
=============================================================================
BOLETÍN UD03 — AVANZADO: ACTIVIDAD 04
EJERCICIO 4: Carrera de mensajes (Concurrencia impredecible)
=============================================================================

ENUNCIADO:
Crea 5 hilos, cada uno imprime su nombre 10 veces. Observa el orden impredecible.

💡 PISTA PEDAGÓGICA:
Usa una lista por comprensión para crear los 5 hilos. Lanza todos con un bucle:
    for h in hilos: h.start()
y espera con:
    for h in hilos: h.join()
El orden exacto de los prints en consola lo decide el planificador (scheduler)
del Sistema Operativo según el reparto de CPU, por lo que cambiará entre ejecuciones.
=============================================================================
"""

import threading


def imprimir_repeticiones():
    """Cada hilo imprime su nombre 10 veces seguidas."""
    nombre = threading.current_thread().name
    for i in range(1, 11):
        print(f"[{nombre}] -> iteración {i}/10")


def main():
    print("=" * 60)
    print("EJERCICIO 4: CARRERA DE MENSAJES (PLANIFICADOR DEL SO)")
    print("=" * 60)

    # 1. Crear 5 hilos usando lista por comprensión
    hilos = [
        threading.Thread(
            target=imprimir_repeticiones,
            name=f"Corredor-{i}"
        )
        for i in range(1, 6)
    ]

    print("🚀 [MainThread] Disparando los 5 corredores a la vez:\n")

    # 2. Bucle 1: Iniciar todos los hilos
    for h in hilos:
        h.start()

    # 3. Bucle 2: Esperar a todos los hilos
    for h in hilos:
        h.join()

    print("\n" + "=" * 60)
    print("🏁 [MainThread] ¡Todos los hilos completaron sus 10 impresiones!")
    print("💡 Observa cómo las líneas de Corredor-1 a Corredor-5 se entremezclan.")
    print("=" * 60)


if __name__ == "__main__":
    main()
