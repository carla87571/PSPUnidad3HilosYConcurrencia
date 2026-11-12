"""
=============================================================================
BOLETÍN UD03 — AVANZADO: ACTIVIDAD 01
EJERCICIO 1: Join con timeout
=============================================================================

ENUNCIADO:
Crea un hilo que duerma 5 segundos. En el hilo principal, usa join(timeout=2)
y comprueba con is_alive() si el hilo sigue ejecutándose después del timeout.

💡 PISTA PEDAGÓGICA:
h.join(2) devuelve None tanto cuando el hilo termina a tiempo como cuando expira
el timeout. La única forma segura de saber si el hilo sigue vivo después del timeout
es consultar el método booleano: h.is_alive() justo después del join.
=============================================================================
"""

import threading
import time


def tarea_larga():
    """Simula una tarea pesada que dura 5 segundos."""
    print("  ⏳ [Hilo Secundario] Comenzando tarea larga de 5 segundos...")
    time.sleep(5.0)
    print("  🏁 [Hilo Secundario] Tarea larga completada.")


def main():
    print("=" * 60)
    print("EJERCICIO 1: JOIN CON TIMEOUT Y COMPROBACIÓN DE is_alive()")
    print("=" * 60)

    # 1. Crear el hilo (lo marcamos como daemon para que no bloquee al salir)
    hilo = threading.Thread(target=tarea_larga, name="HiloLargo", daemon=True)

    # 2. Lanzar el hilo
    print("🚀 [MainThread] Lanzando el hilo secundario...")
    hilo.start()

    # 3. Esperar como máximo 2 segundos con timeout
    print("⏱️ [MainThread] Esperando con hilo.join(timeout=2)...")
    hilo.join(timeout=2)

    # 4. Comprobar con is_alive()
    if hilo.is_alive():
        print(f"\n⚠️ [MainThread] ¡TIMEOUT ALCANZADO!")
        print(f"   El hilo sigue ejecutándose: hilo.is_alive() == {hilo.is_alive()}")
        print("   El hilo principal continuó su camino sin congelarse.")
    else:
        print("\n✅ [MainThread] El hilo terminó antes del timeout.")

    print("=" * 60)


if __name__ == "__main__":
    main()
