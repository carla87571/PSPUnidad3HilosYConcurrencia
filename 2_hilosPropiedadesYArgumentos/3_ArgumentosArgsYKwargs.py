"""
=============================================================================
TEMA: Pasar Argumentos a Hilos: args y kwargs
DIAPOSITIVAS: 6, 7 y 9
=============================================================================

¿POR QUÉ PASAR ARGUMENTOS? (Diapositiva 6)
Sin argumentos, todos los hilos harían exactamente lo mismo.
Con 'args' y 'kwargs', cada hilo recibe datos propios y hace su versión del trabajo.

FORMAS DE PASAR ARGUMENTOS (Diapositiva 7):
1. args= (Tupla): Pasa argumentos posicionales en el orden en que los recibe la función.
   Ej: args=("Ana", "lavar platos")

2. kwargs= (Diccionario): Pasa argumentos por nombre clave (clave-valor).
   Ej: kwargs={"nombre": "Bob", "tarea": "fregar suelo"}

⚠️ EL TRUCO DE LA COMA (Diapositivas 7 y 9):
Si tu función solo recibe UN argumento:
❌ args=("Ana")   -> Python lo evalúa como un simple STRING. Al desempaquetarlo,
                      pasa 'A', 'n', 'a' como 3 argumentos separados -> TypeError!
✅ args=("Ana",)  -> Con la COMA final, Python sabe que es una TUPLA de un elemento.
=============================================================================
"""

import threading
import time


def tarea_hogar(persona: str, quehacer: str, duracion: float = 1.0):
    """Función de ejemplo que recibe varios parámetros."""
    hilo_actual = threading.current_thread().name
    print(f"  🧹 [{hilo_actual}] {persona} comenzó a {quehacer}...")
    time.sleep(duracion)
    print(f"  ✨ [{hilo_actual}] {persona} terminó de {quehacer}.")


def saludar_un_argumento(nombre: str):
    """Función que solo acepta UN parámetro posicional."""
    print(f"  👋 ¡Hola, {nombre}!")


def demo_args_posicionales():
    print("\n" + "=" * 65)
    print("1. PASAR ARGUMENTOS POSICIONALES CON 'args' (Tupla)")
    print("=" * 65)

    # args espera una TUPLA con los valores ordenados: (persona, quehacer, duracion)
    h1 = threading.Thread(
        target=tarea_hogar,
        args=("Ana", "lavar los platos", 1.2),
        name="Hilo-Ana"
    )
    h1.start()
    h1.join()


def demo_kwargs_nombrados():
    print("\n" + "=" * 65)
    print("2. PASAR ARGUMENTOS CON NOMBRE CON 'kwargs' (Diccionario)")
    print("=" * 65)

    # kwargs espera un DICCIONARIO donde las claves coinciden con los parámetros
    h2 = threading.Thread(
        target=tarea_hogar,
        kwargs={"persona": "Bob", "quehacer": "fregar el suelo", "duracion": 1.0},
        name="Hilo-Bob"
    )
    h2.start()
    h2.join()


def demo_combinar_args_y_kwargs():
    print("\n" + "=" * 65)
    print("3. COMBINAR 'args' Y 'kwargs' SIMULTÁNEAMENTE")
    print("=" * 65)

    # Podemos pasar los primeros posicionales y los opcionales por clave
    h3 = threading.Thread(
        target=tarea_hogar,
        args=("Carlos", "cocinar el almuerzo"),  # persona, quehacer
        kwargs={"duracion": 1.5},                # duracion
        name="Hilo-Carlos"
    )
    h3.start()
    h3.join()


def demo_trampa_de_la_coma():
    print("\n" + "=" * 65)
    print("4. LA TRAMPA DE LA COMA: args=('Ana',) vs args=('Ana')")
    print("=" * 65)

    print("❌ CASO ERRÓNEO: args=('Ana')  [Sin coma]")
    try:
        # Python ve ("Ana") como un string ("Ana"), no como una tupla.
        # Al desempaquetar el string para pasar los argumentos, pasa len("Ana") = 3 argumentos: 'A', 'n', 'a'
        h_error = threading.Thread(
            target=saludar_un_argumento,
            args=("Ana")  # <-- FALTA LA COMA
        )
        h_error.start()
        h_error.join()
    except TypeError as e:
        print(f"   ⚠️ ERROR CAPTURADO: {e}")
        print("   Explicación: Python intentó llamar a saludar('A', 'n', 'a'),")
        print("   pero la función solo esperaba 1 argumento.")

    print("\n✅ CASO CORRECTO: args=('Ana',)  [Con coma final]")
    h_bien = threading.Thread(
        target=saludar_un_argumento,
        args=("Ana",)  # <-- TUPLA VÁLIDA DE 1 ELEMENTO
    )
    h_bien.start()
    h_bien.join()
    print("   ¡Funcionó a la perfección gracias a la coma!")


if __name__ == "__main__":
    demo_args_posicionales()
    demo_kwargs_nombrados()
    demo_combinar_args_y_kwargs()
    demo_trampa_de_la_coma()

