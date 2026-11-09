"""
=============================================================================
TEMA: Hilos Daemon vs Hilos No-Daemon (Normales)
DIAPOSITIVAS: 1, 2 y 3 (Bloque 01)
=============================================================================

¿QUÉ ES UN HILO DAEMON? (Diapositiva 1):
----------------------------------------
Un hilo daemon se ejecuta en segundo plano y SE MATA AUTOMÁTICAMENTE cuando
el programa principal termina.
Los hilos NO-daemon (por defecto), en cambio, IMPIDEN que el programa salga
hasta que ellos hayan completado su labor.

ANALOGÍA DE LA ALARMA DE INCENDIOS (Diapositiva 1):
- Quieres la alarma encendida mientras el edificio esté en pie.
- Si el edificio desaparece o se demuele (termina el programa), la alarma
  no tiene sentido y muere con él.
- Esa es la filosofía del daemon: tareas auxiliares de fondo prescindibles
  (reloj, latido/heartbeat, monitoreo, limpieza de archivos temporales).

CADA UNO TIENE SU SITIO (Diapositiva 3):
- HILO NORMAL + join(): Para tareas CRÍTICAS que deben completarse sí o sí
  (escribir en disco, guardar transacciones, procesar pagos).
- HILO DAEMON: Para servicios de fondo PRESCINDIBLES (da igual que se corten en seco).

⚠️ ADVERTENCIA (Diapositiva 3):
Un daemon cortado en seco se detiene a mitad de camino. Nunca escribas
archivos críticos desde un hilo daemon porque podrían quedar corruptos.

ESPERAS LIMITADAS CON TIMEOUT (Diapositivas 2 y 6):
- h.join(timeout=2): El hilo principal espera como máximo 2 segundos. Si el hilo
  no ha terminado, el principal continúa sin quedarse congelado para siempre.
=============================================================================
"""

import threading
import time


def trabajador_con_pasos(nombre: str, total_pasos: int, retardo: float = 0.4):
    """Simula una tarea dividida en varios pasos."""
    es_daemon = threading.current_thread().daemon
    tipo = "😈 DAEMON" if es_daemon else "🛡️ NO-DAEMON (Normal)"

    print(f"  [{nombre} - {tipo}] -> Iniciando ({total_pasos} pasos)...")
    for paso in range(1, total_pasos + 1):
        time.sleep(retardo)
        print(f"  [{nombre}] -> Completado paso {paso}/{total_pasos}")
    print(f"  [{nombre}] -> 🎉 ¡Trabajo completado exitosamente!")


def demo_hilo_no_daemon():
    print("\n" + "=" * 65)
    print("1. HILO NO-DAEMON (El programa está obligado a esperar)")
    print("=" * 65)
    print("Lanzamos un hilo normal (daemon=False) con 4 pasos (1.6s).")
    print("El intérprete de Python esperará obligatoriamente a que termine.")

    h1 = threading.Thread(
        target=trabajador_con_pasos,
        args=("Worker-Normal", 4, 0.4),
        daemon=False  # Por defecto es False
    )
    h1.start()
    h1.join()
    print("📢 [MainThread] 'Worker-Normal' terminó y podemos continuar.\n")


def demo_join_con_timeout():
    print("=" * 65)
    print("2. JOIN CON TIMEOUT: h.join(timeout=1.0) (Diapositivas 2 y 6)")
    print("=" * 65)
    print("Un hilo tardará 3 segundos (6 pasos de 0.5s).")
    print("No queremos esperar tanto, así que usamos un timeout de 1.0s:")

    h2 = threading.Thread(
        target=trabajador_con_pasos,
        args=("Worker-Lento", 6, 0.5),
        daemon=True
    )
    h2.start()

    print("⏳ [MainThread] Esperando como máximo 1.0 segundo...")
    h2.join(timeout=1.0)

    # Verificamos si el hilo sigue vivo
    if h2.is_alive():
        print(f"⚠️ [MainThread] ¡Se acabó el tiempo de espera! (is_alive = {h2.is_alive()})")
        print("   El hilo principal continúa su camino sin quedarse congelado.")
    else:
        print("✅ [MainThread] El hilo completó su tarea dentro del límite.")


def demo_muerte_del_daemon():
    print("\n" + "=" * 65)
    print("3. CÓMO MUERE UN DAEMON CUANDO EL PROGRAMA SALE (Diapositiva 2)")
    print("=" * 65)
    print("Lanzamos un hilo con daemon=True en un bucle infinito que cuenta.")
    print("El MainThread solo esperará 1.2 segundos y finalizará el script.")
    print("¡Observa cómo el daemon es cortado en seco en el momento en que")
    print("el programa principal termina!\n")

    def reloj_infinito():
        segundo = 1
        while True:
            time.sleep(0.4)
            print(f"     ⏰ [Reloj-Daemon] Tic-tac #{segundo}...")
            segundo += 1

    h_daemon = threading.Thread(target=reloj_infinito, name="Reloj-Daemon", daemon=True)
    h_daemon.start()

    time.sleep(1.3)
    print("\n🛑 [MainThread] El programa principal ha llegado al final de su ejecución.")
    print("🛑 [MainThread] Al apagarse el programa, Python mata a 'Reloj-Daemon' de inmediato.")


if __name__ == "__main__":
    demo_hilo_no_daemon()
    demo_join_con_timeout()
    demo_muerte_del_daemon()
