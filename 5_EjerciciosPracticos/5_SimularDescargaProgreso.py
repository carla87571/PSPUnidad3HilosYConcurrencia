"""
=============================================================================
BOLETÍN UD03 — AVANZADO: ACTIVIDAD 05
EJERCICIO 5: Simular descarga con progreso porcentual
=============================================================================

ENUNCIADO:
Crea un hilo que descargue (simulado con sleep) y muestre progreso cada 25%.

💡 PISTA PEDAGÓGICA:
Dentro de la función, itera con range(0, 101, 25) (generará 0, 25, 50, 75, 100).
Usa time.sleep(0.5) en cada salto para simular el retardo de la red e imprime
el porcentaje alcanzado. El hilo principal espera con join() antes de confirmar
la descarga completa.
=============================================================================
"""

import threading
import time


def simular_descarga(archivo: str):
    """Descarga un archivo simulando un reporte de progreso cada 25%."""
    print(f"  ⬇️  Iniciando descarga de '{archivo}'...")

    for porcentaje in range(0, 101, 25):
        time.sleep(0.5)  # Simula el retardo de descarga
        barra = "█" * (porcentaje // 10) + "░" * (10 - (porcentaje // 10))
        print(f"  [{barra}] {porcentaje}% descargado")

    print(f"  ✅ Descarga finalizada: '{archivo}' guardado en disco.")


def main():
    print("=" * 60)
    print("EJERCICIO 5: SIMULACIÓN DE DESCARGA CON PROGRESO CADA 25%")
    print("=" * 60)

    nombre_archivo = "instalador_actualizacion.zip"

    # 1. Crear el hilo con argumento
    hilo_descarga = threading.Thread(
        target=simular_descarga,
        args=(nombre_archivo,),
        name="Worker-Descarga"
    )

    # 2. Iniciar el hilo
    hilo_descarga.start()
    print("💬 [MainThread] La descarga avanza en segundo plano sin congelar la app...\n")

    # 3. Esperar a que la descarga concluya
    hilo_descarga.join()

    print("\n" + "=" * 60)
    print("🎉 [MainThread] Archivo listo para ser utilizado por el programa.")
    print("=" * 60)


if __name__ == "__main__":
    main()

