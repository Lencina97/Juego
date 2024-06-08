from personajes import clases
from acciones import mostrar_estadisticas, acciones
from selector_opciones import seleccion_opciones

#
##def imprimir_clases(clases, indice=1):
#   for clase in clases:
#       print(f"{indice}.{clase.__name__}")
#       indice += 1
#


def seleccion_clase():
    print("Selecciona un personaje: ")

    jugador = seleccion_opciones(clases)
    print(
        f"""Bienvenido, seras un gran {jugador.clase}\n
              Estas son tus estadisticas(por ahora): \n"""
    )
    mostrar_estadisticas(jugador)
    acciones(jugador)
