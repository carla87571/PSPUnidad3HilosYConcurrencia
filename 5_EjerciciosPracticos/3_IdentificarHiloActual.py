"""
=============================================================================
BOLETÍN UD03 — AVANZADO: ACTIVIDAD 03
EJERCICIO 3: Identificar el hilo actual (.name, .ident, .daemon)
=============================================================================

ENUNCIADO:
Crea una función que muestre threading.current_thread().name,
threading.current_thread().ident y threading.current_thread().daemon.
Ejecútala desde el hilo principal y desde un hilo secundario.

💡 PISTA PEDAGÓGICA:
Para ejecutar la misma función desde ambos sitios:
1. Llámala directamente como una función normal: funcion_inspeccion()
   (será ejecutada por el hilo principal).
2. Pásala como target a threading.Thread(target=funcion_inspeccion)
   (será ejecutada por el nuevo hilo secundario).
=============================================================================
"""

import threading


def mostrar_informacion_hilo():
    """
    Inspecciona las propiedades del hilo que está ejecutando este código
    en este preciso instante (actúa como un espejo con current_thread).
    """
    hilo_actual = threading.current_thread()

    print(f"  • Nombre (.name)      : {hilo_actual.name}")
    print(f"  • ID numérico (.ident): {hilo_actual.ident}")
    print(f"  • ¿Es Daemon? (.daemon): {hilo_actual.daemon}")
    print("-" * 50)


def main():
    print("=" * 60)
    print("EJERCICIO 3: INTROSPECCIÓN CON threading.current_thread()")
    print("=" * 60)

    # 1. Ejecución directa desde el HILO PRINCIPAL
    print("\n1️⃣  EJECUCIÓN DESDE EL HILO PRINCIPAL:")
    mostrar_informacion_hilo()

    # 2. Ejecución desde un HILO SECUNDARIO
    print("2️⃣  EJECUCIÓN DESDE UN HILO SECUNDARIO (Worker-Auditor):")
    hilo_secundario = threading.Thread(
        target=mostrar_informacion_hilo,
        name="Worker-Auditor",
        daemon=True
    )
    hilo_secundario.start()
    hilo_secundario.join()

    print("✅ Comparación completada con éxito.")
    print("=" * 60)


if __name__ == "__main__":
    main()

