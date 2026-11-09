

"""
=============================================================================
EJEMPLO DE LA VIDA REAL: Descarga Concurrente de Archivos
ARCHIVO: 2_HilosEjemplo1.py
TEMA: Uso de argumentos (args), múltiples hilos concurrentes y memoria compartida
=============================================================================

SITUACIÓN DEL MUNDO REAL:
Imagina una aplicación como WhatsApp, Spotify o un navegador web.
Cuando recibes varias fotos o descargas varias canciones a la vez:
- Si lo hicieras de forma SECUENCIAL (un solo hilo):
    Descarga 1 (2 seg) + Descarga 2 (2 seg) + Descarga 3 (2 seg) = 6 segundos.
    ¡La aplicación se congelaría y el usuario no podría hacer nada!

- Con HILOS (Concurrencia con threading):
    Lanzamos un hilo trabajador (worker) para cada archivo.
    Todas las descargas ocurren al mismo tiempo.
    ¡Tiempo total aproximado: solo 2 segundos!

CONCEPTOS DE LAS DIAPOSITIVAS APLICADOS AQUÍ:
- args / kwargs: Cómo pasar parámetros a cada hilo (Diapositiva 31).
- Workers: Hilos de trabajo realizando tareas I/O (Diapositiva 33).
- Memoria compartida: Los hilos guardan el resultado en un diccionario común (Diapositiva 34).
- start() y join(): Coordinación del flujo (Diapositiva 35).
=============================================================================
"""

import threading
import time
import random

# Memoria compartida donde los hilos guardarán el estado de cada descarga
descargas_completadas = {}


def descargar_archivo(nombre_archivo: str, tamano_mb: int, tiempo_segundos: float):
    """
    Simula la descarga de un archivo a través de la red (Operación I/O).
    Recibe argumentos específicos para cada hilo.
    """
    nombre_hilo = threading.current_thread().name
    print(f"  ⬇️  [{nombre_hilo}] Iniciando descarga de '{nombre_archivo}' ({tamano_mb} MB)...")

    # Simulamos el tiempo de espera de red con sleep
    time.sleep(tiempo_segundos)

    # Guardamos el resultado en la memoria compartida (diccionario)
    descargas_completadas[nombre_archivo] = {
        "tamano": f"{tamano_mb} MB",
        "hilo_responsable": nombre_hilo,
        "estado": "Completado exitosamente"
    }

    print(f"  ✅ [{nombre_hilo}] Finalizó la descarga de '{nombre_archivo}' en {tiempo_segundos:.1f}s.")


def simulacion_secuencial(archivos):
    """Descarga los archivos uno tras otro, sin hilos."""
    print("\n" + "-" * 60)
    print("1. ENFOQUE SECUENCIAL (Sin hilos - Tradicional)")
    print("-" * 60)
    inicio = time.time()

    for nombre, tamano, duracion in archivos:
        print(f"  ⏳ Descargando '{nombre}'...")
        time.sleep(duracion)
        print(f"  ✔️ '{nombre}' listo.")

    tiempo_total = time.time() - inicio
    print(f"⏱️  Tiempo total secuencial: {tiempo_total:.2f} segundos.")
    return tiempo_total


def simulacion_con_hilos(archivos):
    """Descarga los archivos concurrentemente usando hilos."""
    print("\n" + "-" * 60)
    print("2. ENFOQUE CONCURRENTE (Con Hilos - threading.Thread)")
    print("-" * 60)
    descargas_completadas.clear()
    inicio = time.time()

    lista_hilos = []

    # 1. Crear y arrancar un hilo por cada archivo
    for i, (nombre, tamano, duracion) in enumerate(archivos, start=1):
        # Usamos 'args' para pasarle una tupla con los argumentos a la función
        # Usamos 'name' para nombrar a cada hilo como en la diapositiva 33 (worker-1, etc.)
        hilo = threading.Thread(
            target=descargar_archivo,
            args=(nombre, tamano, duracion),
            name=f"Worker-{i}"
        )
        lista_hilos.append(hilo)
        hilo.start()  # ¡Lanza el hilo a trabajar inmediatamente!

    print(f"  🚀 [Hilo Principal] Se han lanzado {len(lista_hilos)} hilos en paralelo.")
    print("  💬 [Hilo Principal] La aplicación no se congela, sigue respondiendo al usuario.")

    # 2. Esperar a que todos los hilos terminen usando join()
    for hilo in lista_hilos:
        hilo.join()

    tiempo_total = time.time() - inicio
    print(f"⏱️  Tiempo total con hilos: {tiempo_total:.2f} segundos.")
    return tiempo_total


def main():
    print("=" * 60)
    print(" SIMULADOR DE DESCARGAS: SECUENCIAL VS MULTI-HILOS")
    print("=" * 60)

    # Lista de archivos a descargar: (nombre, tamaño en MB, segundos simulados)
    archivos_a_descargar = [
        ("reporte_anual.pdf", 15, 2.0),
        ("foto_perfil.png", 5, 1.5),
        ("video_tutorial.mp4", 50, 2.5),
    ]

    print("Archivos pendientes:")
    for arch, mb, dur in archivos_a_descargar:
        print(f" • {arch:<20} | {mb:>3} MB | tiempo de red: {dur}s")

    # Ejecutamos secuencialmente
    t_secuencial = simulacion_secuencial(archivos_a_descargar)

    # Ejecutamos con hilos
    t_hilos = simulacion_con_hilos(archivos_a_descargar)

    # Mostramos los resultados finales y memoria compartida
    print("\n" + "=" * 60)
    print(" RESUMEN Y RESULTADOS FINALES")
    print("=" * 60)
    print(f"• Tiempo sin hilos (secuencial) : {t_secuencial:.2f} segundos")
    print(f"• Tiempo con hilos (concurrente): {t_hilos:.2f} segundos")
    mejora = (t_secuencial / t_hilos)
    print(f"• ¡Fue aproximadamente {mejora:.1f} veces más rápido gracias a los hilos!")

    print("\n📦 Estado de la Memoria Compartida (Resultados recopilados):")
    for archivo, info in descargas_completadas.items():
        print(f" - {archivo}: procesado por [{info['hilo_responsable']}] ({info['tamano']})")
    print("=" * 60)


if __name__ == "__main__":
    main()

