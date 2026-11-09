"""
=============================================================================
TEMA: Ciclo de Vida y Errores Comunes de Principiante
DIAPOSITIVAS: 1, 2 y 3
=============================================================================

1. LAS 3 FASES DEL HILO (Diapositiva 1):
   - Thread(target=saludar) -> Crea el hilo (NUEVO, existe pero no hace nada aún).
   - hilo.start()          -> Lo lanza (EJECUTABLE, el SO decide cuándo corre).
   - hilo.join()           -> Espera a que termine antes de continuar.

2. ERROR TÍPICO #1: Pasar target con paréntesis (Diapositiva 2):
   ❌ Thread(target=saludar()) -> Ejecuta la función INMEDIATAMENTE en el hilo principal.
   ✅ Thread(target=saludar)   -> Pasa la REFERENCIA a la función para que el nuevo
                                  hilo la ejecute al arrancar.

3. ERROR TÍPICO #2: Llamar a start() dos veces (Diapositiva 2):
   ⚠️ start() solo se puede invocar UNA VEZ por hilo.
   Una segunda llamada lanza: RuntimeError: threads can only be started once.
   Si necesitas repetir el trabajo, debes crear una nueva instancia de Thread.

4. HILO PRINCIPAL VS SECUNDARIOS (Diapositiva 3):
   El hilo principal NO espera a los secundarios automáticamente por arte de magia.
   Sin join(), el hilo principal puede imprimir su mensaje de despedida antes
   de que los hilos secundarios hayan terminado su trabajo.
=============================================================================
"""

import threading
import time


def tarea_saludar():
    nombre = threading.current_thread().name
    print(f"  👉 [Hilo: {nombre}] ¡Hola! Estoy ejecutándome en segundo plano.")
    time.sleep(1)
    print(f"  🏁 [Hilo: {nombre}] He completado mi tarea.")


def demo_error_parentesis():
    print("\n" + "=" * 65)
    print("DEMOSTRACIÓN 1: El error de los paréntesis en 'target'")
    print("=" * 65)

    print("\n❌ Caso Incorrecto: Thread(target=tarea_saludar())")
    print("   Observa cómo la función se ejecuta ANTES de que el hilo arranque:")
    # Al poner paréntesis, Python evalúa y ejecuta la función EN ESTE INSTANTE
    # en el hilo principal, y le pasa 'None' (lo que retorna saludar) al target.
    # hilo_malo = threading.Thread(target=tarea_saludar())  <-- Ejecutaría aquí mismo

    print("   (La función se ejecutaría en el MainThread y el hilo quedaría vacío)")

    print("\n✅ Caso Correcto: Thread(target=tarea_saludar)")
    # Pasamos solo el nombre de la función (su referencia en memoria)
    hilo_bueno = threading.Thread(target=tarea_saludar, name="Hilo-Correcto")
    print("   -> Hilo creado pero aún NO se ejecuta.")
    print("   -> Ahora llamamos a hilo_bueno.start():")
    hilo_bueno.start()
    hilo_bueno.join()


def demo_error_doble_start():
    print("\n" + "=" * 65)
    print("DEMOSTRACIÓN 2: Llamar a start() más de una vez")
    print("=" * 65)

    hilo = threading.Thread(target=tarea_saludar, name="Hilo-Unico")
    print("1. Primer llamada: hilo.start()")
    hilo.start()
    hilo.join()

    print("\n2. Segunda llamada al mismo objeto: hilo.start()")
    try:
        hilo.start()
    except RuntimeError as error:
        print(f"   ⚠️ ¡EXCEPCIÓN CAPTURADA con éxito!: {error}")
        print("   💡 REGLA DE ORO: Un hilo solo vive una vez. Para repetir la tarea,")
        print("      debes instanciar un nuevo threading.Thread(target=...).")


def demo_importancia_join():
    print("\n" + "=" * 65)
    print("DEMOSTRACIÓN 3: El hilo principal vs Hilos secundarios (Diapositiva 3)")
    print("=" * 65)

    def tarea_lenta():
        time.sleep(1.5)
        print("     [Hilo Lento] Terminé mi proceso tras 1.5s.")

    hilo_lento = threading.Thread(target=tarea_lenta, name="TrabajadorLento")
    hilo_lento.start()

    print("  [MainThread] Con 'join()', esperamos a que el hilo termine...")
    hilo_lento.join()
    print("  [MainThread] ¡Ahora sí es seguro continuar o cerrar la aplicación!")


if __name__ == "__main__":
    demo_error_parentesis()
    demo_error_doble_start()
    demo_importancia_join()

