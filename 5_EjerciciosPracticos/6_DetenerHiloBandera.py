"""
=============================================================================
BOLETÍN UD03 — AVANZADO: ACTIVIDAD 06
EJERCICIO 6: Detener hilo infinito con bandera (Flag)
=============================================================================

ENUNCIADO:
Crea un hilo infinito que se detenga cuando pulses Enter.

💡 PISTA PEDAGÓGICA:
Declara una variable booleana global 'ejecutando = True'. El hilo comprueba
la variable continuamente en un bucle:
    while ejecutando:
Desde el hilo principal, usa input("Presiona Enter para detener...") para pausar.
En cuanto el usuario pulsa Enter, el principal cambia ejecutando = False.
Al detectar el cambio de valor, el hilo secundario sale de su bucle y finaliza limpiamente.
=============================================================================
"""

import threading
import time

# Bandera de control global compartida en memoria
ejecutando = True


def tarea_continua():
    """Bucle que se ejecuta mientras la bandera 'ejecutando' sea True."""
    global ejecutando
    contador = 1

    print("  🟢 [Hilo-Infinito] Tarea en ejecución continua...")
    while ejecutando:
        print(f"     [Hilo-Infinito] Latido #{contador} (trabajando en segundo plano...)")
        contador += 1
        time.sleep(0.6)

    print("  🛑 [Hilo-Infinito] Bandera detectada como False. ¡Hilo detenido limpiamente!")


def main():
    global ejecutando
    print("=" * 60)
    print("EJERCICIO 6: DETENER HILO INFINITO CON BANDERA BOOLEANA")
    print("=" * 60)

    # 1. Crear y arrancar el hilo
    hilo = threading.Thread(target=tarea_continua, name="Hilo-Infinito")
    hilo.start()

    print("\n👉 [MainThread] El hilo está corriendo.")
    print("👉 [MainThread] Presiona [Enter] en tu teclado para detenerlo:\n")

    # 2. Esperar a que el usuario pulse Enter
    try:
        input()
    except EOFError:
        # Por si se ejecuta en un entorno sin terminal interactiva
        time.sleep(1.8)

    # 3. Cambiar la bandera para ordenar la parada
    print("\n🛑 [MainThread] Solicitando parada del hilo: ejecutando = False...")
    ejecutando = False

    # 4. Esperar a que el hilo confirme su salida con join()
    hilo.join()

    print("✅ [MainThread] Hilo sincronizado y programa finalizado sin fugas.")
    print("=" * 60)


if __name__ == "__main__":
    main()
