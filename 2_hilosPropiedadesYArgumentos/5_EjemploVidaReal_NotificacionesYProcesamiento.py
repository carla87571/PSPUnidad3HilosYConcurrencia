"""
=============================================================================
EJEMPLO DE LA VIDA REAL: Sistema de Notificaciones Multicanal (E-Commerce)
ARCHIVO: 5_EjemploVidaReal_NotificacionesYProcesamiento.py
=============================================================================

ESCENARIO DEL MUNDO REAL:
Una tienda online acaba de registrar una compra importante. Para completar la orden,
el sistema necesita ejecutar 4 tareas independientes de red (I/O):
  1. Enviar recibo por Correo Electrónico.
  2. Enviar código de seguimiento por SMS.
  3. Enviar notificación Push a la aplicación móvil.
  4. Registrar el evento en el sistema de Auditoría/Analítica.

Si se hiciera de forma SECUENCIAL:
  El cliente esperaría 1.2s + 0.8s + 0.5s + 1.5s = 4.0 segundos en pantalla.
  ¡Una experiencia lenta y frustrante!

CON HILOS (threading con propiedades y argumentos):
  - Creamos un hilo para cada canal con su propio nombre (name='Worker-Email', etc.).
  - Pasamos los datos del cliente con args (tupla) y opciones con kwargs (diccionario).
  - Se lanzan todos al mismo tiempo en paralelo.
  - El cliente espera únicamente el tiempo de la tarea más lenta (~1.5s).
  - Usamos join() para asegurar que todo se haya enviado antes de mostrar la confirmación.
=============================================================================
"""

import threading
import time
from typing import Dict, Any

# Memoria compartida para registrar el estatus final de cada notificación
# str: Sus claves serán textos (ej: "Email", "SMS")
#Any: Sus valores pueden ser cualquier cosa
# lo mismo que escribir registro_auditoria = {} (un diccionario vacío), pero con una etiqueta explicativa

registro_auditoria: Dict[str, Any] = {}


def enviar_notificacion(
    canal: str,
    destinatario: str,
    mensaje: str,
    duracion_red: float,
    prioridad_alta: bool = False
):
    """
    Simula el envío de una notificación a través de una API externa (Email, SMS, Push, etc.).
    Recibe argumentos posicionales (args) y argumentos por nombre (kwargs).
    """
    hilo = threading.current_thread()
    icono = "📧" if canal == "Email" else "📱" if canal == "SMS" else "🔔" if canal == "Push" else "📊"

    print(f"  {icono} [{hilo.name} | ID:{hilo.ident}] Enviando a {destinatario}...")

    # Simulamos el retardo de la llamada de red a la API externa
    time.sleep(duracion_red)

    # Guardamos en la memoria compartida
    registro_auditoria[canal] = {
        "destinatario": destinatario,
        "hilo": hilo.name,
        "id_hilo": hilo.ident,
        "tiempo": f"{duracion_red:.2f}s",
        "prioridad": "Alta" if prioridad_alta else "Normal",
        "estado": "Enviado exitosamente"
    }

    print(f"  ✅ {icono} [{hilo.name}] Notificación {canal} entregada con éxito.")


def main():
    print("=" * 70)
    print(" SIMULADOR REAL: SERVICIO DE NOTIFICACIONES MULTICANAL")
    print("=" * 70)

    pedido_id = "ORD-94821"
    cliente_email = "maria.garcia@email.com"
    cliente_telefono = "+34 612 345 678"

    print(f"Procesando confirmaciones para el pedido: {pedido_id}\n")

    # Definimos las tareas con sus argumentos posicionales (args) y nombrados (kwargs)
    configuraciones_envio = [
        {
            "name": "Worker-Email",
            "args": ("Email", cliente_email, f"Factura y Recibo del Pedido #{pedido_id}", 1.2),
            "kwargs": {"prioridad_alta": True}
        },
        {
            "name": "Worker-SMS",
            "args": ("SMS", cliente_telefono, f"Su pedido #{pedido_id} está en camino.", 0.8),
            "kwargs": {"prioridad_alta": True}
        },
        {
            "name": "Worker-Push",
            "args": ("Push", "Dispositivo-iOS-Maria", "¡Tu paquete ha salido del almacén!", 0.5),
            "kwargs": {"prioridad_alta": False}
        },
        {
            "name": "Worker-Analytics",
            "args": ("Analítica", "Servidor-Metricas", f"Evento checkout {pedido_id}", 1.5),
            "kwargs": {"prioridad_alta": False}
        }
    ]

    # 1. CREACIÓN DE HILOS CON PROPIEDADES (name, args, kwargs)
    hilos = []
    for config in configuraciones_envio:
        h = threading.Thread(
            target=enviar_notificacion,
            args=config["args"],
            kwargs=config["kwargs"],
            name=config["name"]
        )
        hilos.append(h)

    # 2. LANZAMIENTO SIMULTÁNEO (Fase 1: start)
    inicio_tiempo = time.time()
    print("🚀 [MainThread] Disparando todos los envíos concurrentemente...")

    for h in hilos:
        h.start()

    # Comprobación de que están activos (.is_alive())
    print("\n🔍 Comprobando estado en tiempo real:")
    for h in hilos:
        print(f"   • Hilo '{h.name}' (ID: {h.ident}) -> ¿Está activo?: {h.is_alive()}")
    print("-" * 70)

    # 3. ESPERA Y REUNIÓN DE RESULTADOS (Fase 2: join)
    for h in hilos:
        h.join()

    tiempo_total = time.time() - inicio_tiempo

    # 4. REPORTE FINAL DE LA OPERACIÓN
    print("-" * 70)
    print("\n" + "=" * 70)
    print(" 📋 REPORTE DE AUDITORÍA Y RENDIMIENTO")
    print("=" * 70)
    print(f"⏱️ Tiempo total transcurrido: {tiempo_total:.2f} segundos.")
    print("   (En modo secuencial habría tardado ~4.00 segundos).\n")

    print("Detalle de las notificaciones procesadas:")
    for canal, detalle in registro_auditoria.items():
        print(f" • [{canal:<9}] Enviado por {detalle['hilo']:<17} (ID: {detalle['id_hilo']}) en {detalle['tiempo']}")

    print("\n🎉 Todos los canales confirmaron entrega. Pedido completado con éxito.")
    print("=" * 70)


if __name__ == "__main__":
    main()

