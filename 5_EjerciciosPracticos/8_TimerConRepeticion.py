"""
=============================================================================
BOLETÍN UD03 — AVANZADO: ACTIVIDAD 08
EJERCICIO 8: Timer recurrente usando reprogramación (Recursividad diferida)
=============================================================================

ENUNCIADO:
El Timer normal solo se dispara una vez. Crea un timer que se repita cada 2
segundos usando recursividad.

💡 PISTA PEDAGÓGICA:
Dentro de la función que ejecuta el Timer, crea otro:
    t = threading.Timer(2.0, funcion)
    t.daemon = True
    t.start()
al final. Así la función se programa a sí misma de nuevo.
Ojo: para evitar que el programa se quede congelado e impida salir al usuario,
marca siempre el Timer como daemon (t.daemon = True antes de start()) para que
muera automáticamente cuando el programa principal termine.
=============================================================================
"""

import threading
import time

contador_disparos = 0
INTERVALO_SEGUNDOS = 2.0


def tarea_recurrente():
    """
    Función que ejecuta el trabajo periódico y se reprograma a sí misma.
    """
    global contador_disparos
    contador_disparos += 1
    hora_actual = time.strftime("%H:%M:%S")

    print(f"  ⏰ [Timer-Recurrente #{contador_disparos}] Disparo a las {hora_actual}")

    # REPROGRAMACIÓN: Creamos el siguiente Timer para dentro de 2.0 segundos
    siguiente_timer = threading.Timer(INTERVALO_SEGUNDOS, tarea_recurrente)

    # ⚠️ Clave: Marcado como DAEMON para que muera cuando el hilo principal finalice
    siguiente_timer.daemon = True
    siguiente_timer.start()


def main():
    print("=" * 60)
    print("EJERCICIO 8: TIMER RECURRENTE CADA 2 SEGUNDOS (DAEMON)")
    print("=" * 60)
    print(f"Iniciando el temporizador periódico (cada {INTERVALO_SEGUNDOS}s)...")

    # 1. Creamos y lanzamos el primer Timer
    primer_timer = threading.Timer(INTERVALO_SEGUNDOS, tarea_recurrente)
    primer_timer.daemon = True
    primer_timer.start()

    print(f"🚀 [MainThread] Temporizador programado a las {time.strftime('%H:%M:%S')}.")
    print("💬 [MainThread] El programa principal realiza otras tareas durante 7 segundos...\n")

    # 2. Dejamos correr al programa principal durante 7 segundos para ver varios disparos
    time.sleep(7.0)

    # 3. El programa principal termina
    print("\n" + "=" * 60)
    print("🛑 [MainThread] Fin del programa principal.")
    print("🛑 [MainThread] Como los Timers son daemon=True, mueren limpiamente")
    print("   sin dejar procesos colgados en el sistema.")
    print("=" * 60)


if __name__ == "__main__":
    main()
