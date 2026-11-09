"""
=============================================================================
TEMA: Temporizadores con threading.Timer
DIAPOSITIVAS: 4, 5 y 6 (Bloque 01)
=============================================================================

¿QUÉ ES UN TIMER? (Diapositiva 4):
----------------------------------
threading.Timer(retardo, funcion) ejecuta la funcion UNA SOLA VEZ después de
retardo segundos, SIN BLOQUEAR el resto del programa.

PUNTOS CLAVE (Diapositivas 4 y 6):
1. NO BLOQUEA: Un Timer es internamente una subclase de Thread.
2. DISPARO ÚNICO: Se ejecuta una sola vez. Si quieres que se repita periódicamente,
   la función debe reprogramarse a sí misma.
3. CANCELACIÓN: t.cancel() anula el disparo antes de que ocurra.

USOS TÍPICOS (Diapositiva 5):
- ⏰ Aviso o recordatorio diferido.
- 🛑 Timeout de operaciones.
- 🔒 Cierre de sesión por inactividad (auto-logout).
- 🧹 Tareas de limpieza diferida.

⚠️ EL TIMER Y EL DAEMON (Diapositiva 5):
Por defecto, el Timer hereda el modo no-daemon. Si el programa termina antes
de que el Timer dispare, Python esperará a que se cumpla el retardo.
Para evitar que alargue el programa innecesariamente:
    t.daemon = True  (antes de llamar a start())
=============================================================================
"""

import threading
import time


def aviso_recordatorio(mensaje: str):
    """Función que será disparada por el Timer tras el retardo."""
    print(f"\n  🔔 [DISPARO DEL TIMER]: {mensaje} (Hora: {time.strftime('%H:%M:%S')})")


def demo_disparo_diferido():
    print("\n" + "=" * 65)
    print("1. DISPARO DIFERIDO: threading.Timer(retardo, funcion)")
    print("=" * 65)
    print("Programamos un aviso para dentro de 1.5 segundos.")
    print("El hilo principal continuará trabajando de inmediato sin bloquearse:")

    # 1. Creamos el Timer: (segundos de retardo, función a ejecutar, args opcionales)
    temporizador = threading.Timer(1.5, aviso_recordatorio, args=("¡Reunión en 5 minutos!",))

    # 2. Lo arrancamos con .start() (NO bloquea)
    temporizador.start()

    print(f"🚀 [MainThread] Timer iniciado a las {time.strftime('%H:%M:%S')}.")
    print("💬 [MainThread] El hilo principal sigue respondiendo al usuario...")

    # Esperamos 2 segundos para dar tiempo a que el Timer dispare
    time.sleep(2.0)
    print("📢 [MainThread] Continuamos después del disparo.")


def demo_cancelacion_timer():
    print("\n" + "=" * 65)
    print("2. CANCELACIÓN DEL TIMER: t.cancel() (Diapositiva 4)")
    print("=" * 65)
    print("Programamos un aviso para dentro de 3 segundos.")
    print("Pero el usuario realiza una acción al segundo 1 y CANCELAMOS el aviso:")

    t_cancelable = threading.Timer(3.0, aviso_recordatorio, args=("¡Este mensaje NUNCA saldrá!",))
    t_cancelable.start()
    print("⏳ Timer de 3 segundos programado...")

    time.sleep(1.0)
    print("🛑 [MainThread] Se detectó actividad. Cancelando el Timer ahora con t.cancel()...")
    t_cancelable.cancel()

    # Esperamos más tiempo para demostrar que nunca se disparará
    time.sleep(2.5)
    print("✅ Comprobado: El mensaje del Timer nunca se mostró porque fue cancelado.")


def demo_timer_periodico():
    print("\n" + "=" * 65)
    print("3. TIMER PERIÓDICO (Reprogramarse a sí mismo - Diapositiva 6)")
    print("=" * 65)
    print("Dado que el Timer ejecuta una sola vez, ¿cómo repetirlo cada X tiempo?")
    print("Hacemos que la función cree y arranque un nuevo Timer al terminar:")

    contador = 0
    max_repeticiones = 3

    def tarea_recurrente():
        nonlocal contador
        contador += 1
        print(f"  ⏰ [Ping Recurrente #{contador}] Latido del sistema a las {time.strftime('%H:%M:%S')}")

        if contador < max_repeticiones:
            # Reprogramamos el siguiente disparo en 0.6 segundos
            nuevo_timer = threading.Timer(0.6, tarea_recurrente)
            nuevo_timer.daemon = True  # Para que no bloquee la salida del programa
            nuevo_timer.start()
        else:
            print("  🏁 [Ping Recurrente] Se alcanzó el número máximo de repeticiones.")

    # Arrancamos el primer ciclo
    t_inicial = threading.Timer(0.6, tarea_recurrente)
    t_inicial.daemon = True
    t_inicial.start()

    # Dejamos correr la demostración
    time.sleep(2.2)


if __name__ == "__main__":
    demo_disparo_diferido()
    demo_cancelacion_timer()
    demo_timer_periodico()

