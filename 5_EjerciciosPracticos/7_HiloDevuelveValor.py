"""
=============================================================================
BOLETÍN UD03 — AVANZADO: ACTIVIDAD 07
EJERCICIO 7: Hilo que devuelve un valor (Memoria compartida)
=============================================================================

ENUNCIADO:
Usa una variable compartida para que un hilo devuelva un resultado al principal.

💡 PISTA PEDAGÓGICA:
Los hilos en Python creados con threading.Thread NO tienen soporte para devolver
valores con 'return' (el método join() siempre retorna None y descarta los valores).
La forma canónica de obtener un resultado es aprovechar la MEMORIA COMPARTIDA:
1. Pasamos una lista vacía como contenedor mutable (o una variable compartida).
2. El hilo calcula el dato y lo deposita con lista.append(resultado).
3. Tras llamar a hilo.join(), el hilo principal lee el resultado de la lista de forma segura.
=============================================================================
"""

import threading
import time


def calcular_cuadrado(numero: int, contenedor_resultado: list):
    """
    Realiza una operación pesada y deposita el resultado en el contenedor.
    """
    print(f"  ⚙️  [Hilo-Worker] Calculando el cuadrado de {numero}...")
    time.sleep(1.0)
    resultado = numero ** 2

    # Guardamos en la memoria compartida
    contenedor_resultado.append(resultado)
    print(f"  ✅ [Hilo-Worker] Cálculo listo: {numero}^2 = {resultado}. Guardado en contenedor.")


def main():
    print("=" * 60)
    print("EJERCICIO 7: DEVOLVER UN VALOR USANDO MEMORIA COMPARTIDA")
    print("=" * 60)

    numero_a_calcular = 15

    # 1. Creamos la estructura compartida (lista que actuará de buzón)
    buzon_resultados = []

    print(f"📥 Contenedor antes del hilo: {buzon_resultados}")

    # 2. Creamos el hilo pasándole el número y el contenedor por referencia
    hilo = threading.Thread(
        target=calcular_cuadrado,
        args=(numero_a_calcular, buzon_resultados),
        name="Worker-Calculador"
    )

    # 3. Lanzamos el hilo
    hilo.start()
    print("🚀 [MainThread] Hilo de cálculo lanzado. Esperando con join()...\n")

    # 4. Esperamos a que el hilo termine obligatoriamente antes de leer
    hilo.join()

    # 5. Leemos el resultado depositado por el hilo
    print("\n" + "=" * 60)
    print(f"📦 [MainThread] Contenedor después de join(): {buzon_resultados}")

    if buzon_resultados:
        valor_final = buzon_resultados[0]
        print(f"🎉 [MainThread] ¡Resultado recuperado con éxito!: {valor_final}")
    print("=" * 60)


if __name__ == "__main__":
    main()
