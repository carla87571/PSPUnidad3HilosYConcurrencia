"""
=============================================================================
TEMA: Tu Primer Hilo en Python (Módulo threading)
DIAPOSITIVAS: 31 a la 37
=============================================================================

¿QUÉ ES UN HILO? (Diapositiva 32)
----------------------------------
Un hilo (thread) es la unidad más pequeña de ejecución: una tarea que vive
DENTRO de un proceso y COMPARTE SU MEMORIA con los demás hilos de ese proceso.

ANALOGÍA DE LOS CHEFS (Diapositiva 36):
- PROCESOS = Cocinas de restaurantes diferentes. Cada una con sus fogones,
  su nevera y sus ingredientes propios. Si una se quema, la de al lado ni
  se entera (alto aislamiento, pero abrir un restaurante es lento y costoso).
- HILOS = Cocineros dentro de la misma cocina. Comparten encimera, nevera e
  ingredientes (memoria compartida). Contratar a un cocinero más es barato
  y rápido, pero si uno tira el aceite caliente, todos lo sufren.

LAS TRES LÍNEAS MÁGICAS (Diapositiva 35):
1. hilo = threading.Thread(target=funcion)  -> Crea el hilo
2. hilo.start()                            -> Lo lanza (empieza a ejecutarse)
3. hilo.join()                             -> Espera a que termine
=============================================================================
"""

import os
import threading
import time

# Variable compartida (como la nevera o despensa de la cocina, Diapositiva 33)
ingredientes_compartidos = ["Harina", "Huevos", "Leche"]


def tarea_saludar():
    """
    Función que ejecutará nuestro hilo secundario (worker).
    """
    nombre_hilo = threading.current_thread().name
    pid_actual = os.getpid()

    print(f"\n[Hilo Secundario: '{nombre_hilo}'] -> ¡Hola desde un hilo!")
    print(f"[Hilo Secundario: '{nombre_hilo}'] -> Mi PID es: {pid_actual}")
    print(f"[Hilo Secundario: '{nombre_hilo}'] -> Accediendo a la nevera compartida...")

    # Simulamos un pequeño trabajo
    time.sleep(1)

    # Modificamos la memoria compartida (agregamos un ingrediente)
    ingredientes_compartidos.append("Chocolate")
    print(f"[Hilo Secundario: '{nombre_hilo}'] -> ¡Añadí Chocolate a la despensa!")
    print(f"[Hilo Secundario: '{nombre_hilo}'] -> Tarea completada.\n")


def main():
    print("=" * 60)
    print(" DEMOSTRACIÓN PEDAGÓGICA: TU PRIMER HILO")
    print("=" * 60)

    # 1. Información del hilo principal y proceso
    hilo_principal = threading.current_thread().name
    pid_proceso = os.getpid()

    print(f"[Hilo Principal: '{hilo_principal}'] -> PID del proceso: {pid_proceso}")
    print(f"[Hilo Principal: '{hilo_principal}'] -> Ingredientes iniciales: {ingredientes_compartidos}")

    print("\n--- PASO 1: Crear el hilo (threading.Thread) ---")
    # Creamos el objeto Thread indicando la función objetivo (target)
    # y asignándole un nombre descriptivo
    hilo = threading.Thread(target=tarea_saludar, name="Cocinero-1")

    print(f"Estado antes de start(): ¿Está vivo?: {hilo.is_alive()}")

    print("\n--- PASO 2: Lanzar el hilo (hilo.start()) ---")
    # start() le dice al Sistema Operativo que comience a ejecutar la tarea en paralelo
    hilo.start()
    print(f"Estado después de start(): ¿Está vivo?: {hilo.is_alive()}")
    print(f"[Hilo Principal: '{hilo_principal}'] -> Sigo ejecutándome mientras Cocinero-1 trabaja...")

    print("\n--- PASO 3: Esperar a que termine (hilo.join()) ---")
    # join() pausa el hilo principal hasta que 'hilo' haya terminado su labor
    hilo.join()
    print(f"[Hilo Principal: '{hilo_principal}'] -> 'Cocinero-1' ha terminado (join completado).")

    # 2. Comprobación de Memoria Compartida (Diapositiva 33 y 34)
    print("\n" + "=" * 60)
    print(" COMPROBACIÓN DE CONCEPTOS CLAVE")
    print("=" * 60)
    print(f"1. Memoria Compartida: Los ingredientes ahora son: {ingredientes_compartidos}")
    print("   -> El hilo secundario modificó la lista y el hilo principal la ve al instante.")
    print(f"2. Mismo Proceso: Ambos hilos compartieron el mismo PID ({pid_proceso}).")
    print("   -> Viven dentro de la misma casa / proceso.")
    print("=" * 60)


if __name__ == "__main__":
    main()

