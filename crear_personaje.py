from personajes import clases
from acciones import mostrar_estadisticas, acciones


def imprimir_clases(clases, indice=1):
    for clase in clases:
        print(f"{indice}.{clase.__name__}")
        indice += 1


def seleccion_clase():

    while True:
        print("Selecciona un personaje: ")
        imprimir_clases(clases)
        respuesta = int(input("")) - 1
        jugador = clases[respuesta]()
        break
    if respuesta > range(clases):
        print("Esa no es una opcion, intenta de nuevo")
    print(
        f"""Bienvenido, seras un gran {jugador.clase}\n
          Estas son tus estadisticas(por ahora): \n"""
    )
    mostrar_estadisticas(jugador)
    acciones(jugador)
