"""
=============================================================================
EJEMPLO DE LA VIDA REAL: Servidor Seguro con Monitor Daemon y Sesión Timer
ARCHIVO: 3_EjemploVidaReal_MonitorYExpiracionSesion.py
TEMA: Aplicación práctica de Hilos Daemon y threading.Timer
=============================================================================

ESCENARIO DEL MUNDO REAL:
Imagina el backend de una aplicación bancaria o un panel de administración:

1. COMPONENTE DAEMON (Monitor de Salud del Servidor):
   - Un servicio de fondo (Heartbeat) que cada 0.8s verifica el estado del servidor.
   - Debe ser DAEMON (daemon=True): si el servidor se apaga o el administrador presiona
     detener, el monitor debe morir al instante sin bloquear el apagado del servidor.

2. COMPONENTE TIMER (Control de Sesión de Usuario con Auto-Logout):
   - Por seguridad bancaria, si el usuario permanece inactivo más de 2 segundos,
     un threading.Timer expira la sesión automáticamente.
   - Si el usuario realiza una acción (ej. transferir dinero o consultar saldo),
     el Timer anterior se CANCELA (.cancel()) y se reinicia el reloj de inactividad.
   - Si el usuario se marcha de la pantalla, el Timer se dispara y cierra la sesión.
=============================================================================
"""

import threading
import time
from typing import Optional


class GestorSesionBancaria:
    """Gestiona la sesión del usuario bancario utilizando threading.Timer."""

    def __init__(self, tiempo_inactividad: float = 2.0):
        self.tiempo_inactividad = tiempo_inactividad
        self.timer_inactividad: Optional[threading.Timer] = None
        self.sesion_activa = False

    def iniciar_sesion(self, usuario: str):
        self.usuario = usuario
        self.sesion_activa = True
        print(f"\n🔐 [Seguridad] Sesión iniciada para '{usuario}'.")
        self._reiniciar_temporizador()

    def _cerrar_sesion_por_timeout(self):
        """Función que dispara el Timer si expira el tiempo."""
        self.sesion_activa = False
        print(f"\n  🛑 [TIMER DISPARADO] ¡Tiempo de inactividad agotado!")
        print(f"  🔒 [Seguridad] La sesión de '{self.usuario}' fue CERRADA automáticamente por seguridad.\n")

    def _reiniciar_temporizador(self):
        """Cancela el timer anterior si existía y arranca uno nuevo."""
        if self.timer_inactividad is not None:
            self.timer_inactividad.cancel()  # Cancela el disparo previo

        # Creamos un nuevo Timer diferido
        self.timer_inactividad = threading.Timer(
            self.tiempo_inactividad,
            self._cerrar_sesion_por_timeout
        )
        self.timer_inactividad.daemon = True  # Para que no impida apagar el programa
        self.timer_inactividad.start()
        print(f"  ⏳ [Timer] Temporizador de inactividad armado ({self.tiempo_inactividad}s).")

    def registrar_actividad(self, accion: str):
        """Simula una interacción del usuario (clic, consulta, transferencia)."""
        if not self.sesion_activa:
            print(f"  ❌ Acción rechazada ('{accion}'): La sesión está cerrada.")
            return

        print(f"  👉 [Usuario Activo] Realizando acción: '{accion}'...")
        # El usuario demostró actividad, reiniciamos el reloj de seguridad:
        self._reiniciar_temporizador()


def monitor_salud_servidor():
    """
    Hilo DAEMON de fondo: Simula un vigilante de salud del servidor (Heartbeat).
    Al ser daemon=True, morirá automáticamente cuando el programa principal termine.
    """
    pulsos = 1
    while True:
        time.sleep(0.7)
        print(f"       💚 [Daemon Heartbeat #{pulsos}] Servidor operativo y seguro.")
        pulsos += 1


def main():
    print("=" * 70)
    print(" SERVICIO DE SEGURIDAD: MONITOR DAEMON + SESIONES CON TIMER")
    print("=" * 70)

    # 1. Arrancamos el monitor en segundo plano como DAEMON
    hilo_monitor = threading.Thread(
        target=monitor_salud_servidor,
        name="Monitor-Salud",
        daemon=True  # Muere en cuanto main() finalice
    )
    hilo_monitor.start()
    print("🚀 [Servidor] Monitor de salud iniciado como hilo DAEMON en segundo plano.")

    # 2. Creamos el gestor de sesión con un límite de inactividad de 1.8s
    banco = GestorSesionBancaria(tiempo_inactividad=1.8)
    banco.iniciar_sesion("carlos_mendoza")

    # 3. Simulamos interacción activa del usuario dentro del límite de tiempo
    time.sleep(0.9)
    banco.registrar_actividad("Consultar Saldo en Cuenta")

    time.sleep(1.0)
    banco.registrar_actividad("Transferir 150 USD a Proveedor")

    # 4. Ahora el usuario se va y deja la sesión desatendida (esperamos 2.5s)
    print("\n💤 [Simulación] El usuario se alejó del teclado y no toca la aplicación...")
    time.sleep(2.5)  # Supera los 1.8s del timer, por lo que el Timer disparará el logout

    # 5. Intento de realizar una acción tras el auto-logout
    banco.registrar_actividad("Intentar Retiro de Dinero")

    # 6. Apagado del sistema principal
    print("\n" + "=" * 70)
    print("🛑 [Servidor] Apagando el servidor principal...")
    print("   Observa cómo el hilo 'Monitor-Salud' (Daemon) muere de inmediato")
    print("   sin necesidad de join() y sin dejar procesos colgados.")
    print("=" * 70)


if __name__ == "__main__":
    main()

