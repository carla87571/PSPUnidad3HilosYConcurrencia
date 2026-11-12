"""
=============================================================================
BOLETÍN UD03 — AVANZADO: ACTIVIDAD 09
EJERCICIO 9: Pool de hilos manual con cola de tareas (queue.Queue)
=============================================================================

ENUNCIADO:
Crea un "pool" manual con una cola de tareas. 2 hilos cogen tareas de la cola
y las ejecutan.

💡 PISTA PEDAGÓGICA:
- Usa queue.Queue: es una estructura de datos segura para hilos (thread-safe),
  por lo que varios hilos pueden insertar y extraer datos sin condiciones de carrera.
- Los trabajadores ejecutan un bucle continuo:
    while True:
        tarea = cola.get()        # Espera y saca una tarea de la cola
        procesar(tarea)
        cola.task_done()          # Avisa a la cola que la tarea terminó
- El hilo principal inserta las tareas con cola.put(tarea) y luego espera
  con cola.join() hasta que todas las tareas hayan llamado a task_done().
- Crea los workers con daemon=True para que se apaguen solos cuando el hilo principal
  termine tras el cola.join().
=============================================================================
"""

import queue
import threading
import time


def trabajador_pool(cola_tareas: queue.Queue):
    """
    Función que ejecuta cada hilo trabajador del pool en un bucle continuo.
    """
    nombre = threading.current_thread().name

    while True:
        # 1. Obtener la siguiente tarea de la cola (se bloquea si la cola está vacía)
        tarea = cola_tareas.get()

        print(f"  👷 [{nombre}] Tomó de la cola: '{tarea}'...")

        # 2. Simular el procesamiento de la tarea
        time.sleep(0.8)

        print(f"  ✅ [{nombre}] Finalizó con éxito: '{tarea}'")

        # 3. Notificar a la cola que esta tarea en particular ha sido completada
        cola_tareas.task_done()


def main():
    print("=" * 65)
    print("EJERCICIO 9: POOL MANUAL DE HILOS CON queue.Queue")
    print("=" * 65)

    # 1. Crear la cola thread-safe
    cola = queue.Queue()

    num_trabajadores = 2
    hilos_pool = []

    # 2. Crear y arrancar los 2 hilos del pool como DAEMON
    print(f"⚙️ Creando e iniciando pool de {num_trabajadores} trabajadores (daemon=True)...")
    for i in range(1, num_trabajadores + 1):
        worker = threading.Thread(
            target=trabajador_pool,
            args=(cola,),
            name=f"Worker-{i}",
            daemon=True  # Permite que mueran cuando el programa principal termine
        )
        worker.start()
        hilos_pool.append(worker)

    # 3. Enviar 6 tareas a la cola
    lista_tareas = [
        "Procesar Factura #101",
        "Generar PDF Reporte #102",
        "Enviar Email Bienvenida #103",
        "Comprimir Imagen #104",
        "Actualizar Base Datos #105",
        "Notificar SMS Usuario #106"
    ]

    print(f"\n📥 [MainThread] Insertando {len(lista_tareas)} tareas en la cola:")
    for tarea in lista_tareas:
        print(f"   + Encolando: '{tarea}'")
        cola.put(tarea)

    print("\n🚀 [MainThread] Todas las tareas han sido encoladas.")
    print("⏳ [MainThread] Esperando con cola.join() a que todas sean procesadas...\n")

    # 4. cola.join() bloquea al hilo principal hasta que cada tarea llame a task_done()
    cola.join()

    print("\n" + "=" * 65)
    print("🎉 [MainThread] ¡Todas las tareas de la cola han sido completadas!")
    print("🛑 [MainThread] Al finalizar main(), los workers daemon se apagan solos.")
    print("=" * 65)


if __name__ == "__main__":
    main()
