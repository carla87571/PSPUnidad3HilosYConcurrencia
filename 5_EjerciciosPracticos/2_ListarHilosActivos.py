"""
=============================================================================
BOLETÍN UD03 — AVANZADO: ACTIVIDAD 02
EJERCICIO 2: Listar hilos activos con threading.enumerate()
=============================================================================

ENUNCIADO:
Crea 3 hilos que hagan tareas distintas. Usa threading.enumerate() para listar
todos los hilos activos y muestra sus nombres.

💡 PISTA PEDAGÓGICA:
threading.enumerate() devuelve una lista de todos los objetos Thread que están
actualmente vivos (activos) en el proceso. Al iterar sobre ella y consultar .name,
verás a tus 3 hilos trabajadores y también al hilo principal ('MainThread').
=============================================================================
"""

import threading
import time


def tarea_descarga():
    """Tarea 1: Simula descargar un archivo."""
    time.sleep(1.5)


def tarea_calculo():
    """Tarea 2: Simula un cálculo matemático."""
    time.sleep(1.5)


def tarea_red():
    """Tarea 3: Simula escuchar una petición de red."""
    time.sleep(1.5)


def main():
    print("=" * 60)
    print("EJERCICIO 2: LISTAR HILOS ACTIVOS CON threading.enumerate()")
    print("=" * 60)

    # 1. Crear 3 hilos con tareas y nombres distintos
    h1 = threading.Thread(target=tarea_descarga, name="Worker-Descargas")
    h2 = threading.Thread(target=tarea_calculo, name="Worker-Calculos")
    h3 = threading.Thread(target=tarea_red, name="Worker-Red")

    # 2. Lanzar los 3 hilos
    h1.start()
    h2.start()
    h3.start()

    print("🚀 [MainThread] Se han lanzado los 3 hilos de trabajo.")
    print("\n📋 Consultando hilos vivos con threading.enumerate():\n")

    # 3. Listar todos los hilos activos usando threading.enumerate()
    hilos_activos = threading.enumerate()

    for idx, hilo in enumerate(hilos_activos, start=1):
        es_principal = "⭐ (Hilo Principal)" if hilo is threading.main_thread() else "🧵 (Hilo Trabajador)"
        print(f"   {idx}. Nombre: {hilo.name:<20} | ID: {hilo.ident} {es_principal}")

    print(f"\n📊 Total de hilos activos en este instante: {len(hilos_activos)}")

    # 4. Esperar a que terminen
    h1.join()
    h2.join()
    h3.join()

    print("\n✅ [MainThread] Todos los hilos concluyeron sus tareas.")
    print("=" * 60)


if __name__ == "__main__":
    main()
