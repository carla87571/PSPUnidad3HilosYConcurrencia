"""
=============================================================================
EJERCICIO 2: Múltiples hilos con retardo
ENUNCIADO:
Crea 3 hilos que impriman su número (1, 2, 3) y luego duerman 1 segundo
con time.sleep(1). Lánzalos todos y espera a que terminen.
=============================================================================
"""

import threading
import time


def tarea_con_retardo(numero: int):
    """Imprime el número asignado, espera 1 segundo y avisa al terminar."""
    print(f"  🟢 Hilo #{numero} iniciando...")
    time.sleep(1.0)
    print(f"  🏁 Hilo #{numero} completado tras 1 segundo.")


def main():
    print("=" * 55)
    print("EJERCICIO 2: MÚLTIPLES HILOS CON RETARDO")
    print("=" * 55)

    tiempo_inicio = time.time()

    # 1. Creamos los 3 hilos (usando list comprehension)
    hilos = [
        threading.Thread(target=tarea_con_retardo, args=(num,))
        for num in range(1, 4)
    ]

    # 2. Bucle para lanzar todos (start)
    print("🚀 [MainThread] Lanzando los 3 hilos en paralelo...")
    for h in hilos:
        h.start()

    # 3. Bucle para esperar a todos (join)
    print("⏳ [MainThread] Esperando a que todos finalicen...")
    for h in hilos:
        h.join()

    tiempo_total = time.time() - tiempo_inicio
    print(f"\n⏱️ Tiempo total transcurrido: {tiempo_total:.2f} segundos.")
    print("💡 Nota: Aunque los 3 hilos durmieron 1 segundo cada uno,")
    print("   como corrieron al mismo tiempo, el tiempo total fue ~1s, no 3s.")
    print("=" * 55)


if __name__ == "__main__":
    main()


"""
¿Y por qué con el if?

El if __name__ == "__main__": es un candado de seguridad:

Le dice a Python: «Presiona el botón START solo si yo misma abrí este archivo desde la terminal. Si otro archivo solo quería leer mi receta (usando import), no la arranques».

En resumen:

def main(): 
→
→ Diseña la máquina.
if __name__ == "__main__": main() 
→
→ Enciende la máquina.
"""


"""
# Hace exactamente lo mismo que el código de tu archivo:
hilos = []
for num in range(1, 4):
    h = threading.Thread(target=tarea_con_retardo, args=(num,))
    hilos.append(h)
"""