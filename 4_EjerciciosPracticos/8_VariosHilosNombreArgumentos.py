"""
=============================================================================
EJERCICIO 8: Varios hilos con nombre y argumentos (+ Bonus Timer Periódico)
ENUNCIADO:
1. Crea 3 hilos en un bucle, cada uno con name = "hilo-" + str(n) y que reciba
   su número como argumento para imprimir "hilo-N trabajando".
   Lanza todos y espera a todos.
   💡 Pista: Usa una lista por comprensión para crear los 3 hilos y luego dos
   bucles: for h in hilos: h.start() y for h in hilos: h.join().

2. Pista Adicional (Timer Periódico):
   Dentro de la función que ejecuta el Timer, crea otro threading.Timer(2.0, funcion).start()
   al final. Así la función se programa a sí misma de nuevo.
   Ojo: pon el Timer como daemon (t.daemon = True antes de t.start()) para que
   muera con el principal.
=============================================================================
"""

import threading
import time


# =============================================================================
# PARTE 1: Varios hilos con nombres y argumentos
# =============================================================================
def tarea_trabajador(n: int):
    """Recibe su número como argumento e imprime que está trabajando."""
    nombre_hilo = threading.current_thread().name
    print(f"  👉 [{nombre_hilo}] trabajando (argumento recibido: {n})")
    time.sleep(0.5)


def parte_1_multiples_hilos():
    print("\n" + "=" * 60)
    print("PARTE 1: 3 HILOS CON LIST COMPREHENSION, NOMBRES Y ARGS")
    print("=" * 60)

    # 1. Crear los 3 hilos con una lista por comprensión
    hilos = [
        threading.Thread(
            target=tarea_trabajador,
            args=(n,),
            name="hilo-" + str(n)
        )
        for n in range(1, 4)
    ]

    # 2. Bucle 1: Lanzar todos los hilos
    print("🚀 [MainThread] Bucle de inicio: lanzando todos los hilos...")
    for h in hilos:
        h.start()

    # 3. Bucle 2: Esperar a todos los hilos
    print("⏳ [MainThread] Bucle de espera: uniendo todos con join()...")
    for h in hilos:
        h.join()

    print("✅ [MainThread] Todos los hilos trabajadores concluyeron.")


# =============================================================================
# PARTE 2: Pista del Timer Periódico y Daemon
# =============================================================================
contador_timer = 0


def funcion_timer_recurrente():
    """
    Función que ejecuta el Timer y se reprograma a sí misma.
    Se configura como daemon para morir cuando el programa principal termine.
    """
    global contador_timer
    contador_timer += 1
    print(f"  ⏰ [Timer Periódico #{contador_timer}] Ejecutando a las {time.strftime('%H:%M:%S')}")

    # Pista: crea otro threading.Timer(2.0, funcion) al final para repetirse
    nuevo_timer = threading.Timer(1.0, funcion_timer_recurrente)
    nuevo_timer.daemon = True  # Ojo: como daemon para que muera con el principal
    nuevo_timer.start()


def parte_2_timer_periodico():
    print("\n" + "=" * 60)
    print("PARTE 2: TIMER PERIÓDICO REPROGRAMADO (DAEMON)")
    print("=" * 60)
    print("Iniciando Timer recurrente (se reprograma a sí mismo cada segundo)...")

    # Arrancamos el primer Timer como daemon
    t_inicial = threading.Timer(0.5, funcion_timer_recurrente)
    t_inicial.daemon = True
    t_inicial.start()

    # Dejamos correr al programa principal 3.2 segundos para ver los disparos
    print("💬 [MainThread] El programa principal realiza otras tareas durante 3.2s...")
    time.sleep(3.2)

    print("\n🛑 [MainThread] El programa principal ha llegado a su fin.")
    print("🛑 [MainThread] Como el Timer es daemon=True, se apagará automáticamente.")


def main():
    parte_1_multiples_hilos()
    parte_2_timer_periodico()
    print("\n" + "=" * 60)
    print("🎉 EJERCICIO 8 COMPLETADO EXITOSAMENTE")
    print("=" * 60)


if __name__ == "__main__":
    main()

