"""
=============================================================================
TEMA: Propiedades de un Hilo
DIAPOSITIVA: 5
=============================================================================

PROPIEDADES FUNDAMENTALES (Diapositiva 5):
-----------------------------------------
1. .name        -> Nombre legible del hilo (por defecto "Thread-1", o tu propio nombre).
2. .ident       -> Identificador numérico único asignado por el SO (None antes de start()).
3. .daemon      -> Booleano (True si es hilo demonio de fondo, False por defecto).
4. .is_alive()  -> Método que devuelve True si el hilo está activo/ejecutándose.
5. threading.current_thread() -> Devuelve el objeto Thread que ejecuta el código actual.

En este script veremos cómo cambian estas propiedades a lo largo del ciclo de vida:
ANTES de start()  ->  DURANTE la ejecución  ->  DESPUÉS de join()
=============================================================================
"""

import threading
import time


def funcion_trabajador():
    """
    Función que se ejecuta dentro del hilo secundario.
    Utiliza threading.current_thread() para auto-inspeccionarse.
    """
    # 'current_thread()' nos da acceso al hilo que está corriendo ahora mismo
    yo_mismo = threading.current_thread()

    print("\n   [Dentro del hilo secundario]:")
    print(f"   -> Objeto: {yo_mismo}")
    print(f"   -> Nombre (.name): '{yo_mismo.name}'")
    print(f"   -> ID del hilo (.ident): {yo_mismo.ident}")
    print(f"   -> ¿Es daemon? (.daemon): {yo_mismo.daemon}")
    print(f"   -> ¿Está vivo dentro de sí mismo? (.is_alive()): {yo_mismo.is_alive()}")

    # Simulamos trabajo
    time.sleep(1.2)
    print("   -> [Dentro del hilo secundario]: ¡Trabajo finalizado!")



def main():
    print("=" * 65)
    print(" INSPECCIÓN DE PROPIEDADES DE UN HILO (Diapositiva 5)")
    print("=" * 65)

    # 0. Inspeccionamos primero el hilo principal (MainThread)
    hilo_principal = threading.current_thread()
    print("\n📌 0. HILO PRINCIPAL DEL PROGRAMA:")
    print(f"   • Nombre (.name): '{hilo_principal.name}'")
    print(f"   • ID (.ident): {hilo_principal.ident}")
    print(f"   • ¿Es daemon? (.daemon): {hilo_principal.daemon}")
    print(f"   • ¿Está vivo? (.is_alive()): {hilo_principal.is_alive()}")

    # 1. Creamos un hilo secundario con nombre personalizado
    hilo = threading.Thread(target=funcion_trabajador, name="Worker-Procesador")

    print("\n📌 1. ESTADO DEL HILO ANTES DE start():")
    print(f"   • Nombre (.name)      : '{hilo.name}'")
    print(f"   • ID (.ident)         : {hilo.ident} (¡Aún es None porque el SO no lo ha lanzado!)")
    print(f"   • ¿Es daemon? (.daemon): {hilo.daemon}")
    print(f"   • ¿Está vivo? (.is_alive()): {hilo.is_alive()} (Aún no ha arrancado)")

    # 2. Lanzamos el hilo
    print("\n📌 2. LANZANDO EL HILO CON start():")
    hilo.start()

    print(f"   • ID numérico asignado (.ident): {hilo.ident} (¡Ya tiene ID!)")
    print(f"   • ¿Está vivo ahora? (.is_alive()): {hilo.is_alive()}")

    # 3. Esperamos a que termine con join()
    print("\n📌 3. ESPERANDO CON join():")
    hilo.join()

    print("\n📌 4. ESTADO DEL HILO DESPUÉS DE TERMINAR (POST-join):")
    print(f"   • ¿Está vivo? (.is_alive()): {hilo.is_alive()} (Ya finalizó su ejecución)")
    print(f"   • ID conservado (.ident)   : {hilo.ident} (Mantiene su registro para depuración)")
    print(f"   • Nombre (.name)          : '{hilo.name}'")

    print("\n" + "=" * 65)
    print(" TABLA RESUMEN DE PROPIEDADES")
    print("=" * 65)
    print(" Propiedad        | Antes de start() | En ejecución | Terminado")
    print(" -----------------|------------------|--------------|----------")
    print(f" .name            | {hilo.name:<16} | {hilo.name:<12} | {hilo.name}")
    print(f" .ident           | None             | Número ID    | {hilo.ident}")
    print(f" .is_alive()      | False            | True         | False")
    print(f" .daemon          | False            | False        | False")
    print("=" * 65)


if __name__ == "__main__":
    main()

