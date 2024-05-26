from personajes import *

jugador = ""


def seleccion_clase():

    while True:
        clase = input(
            f"""Selecciona tu personaje: \n 1)Héroe\n 2)Mago\n 3)Tanque\n 4) Asesino\n"""
        )

        if clase == "1":
            clase = Heroe(jugador)
            break
        elif clase == "2":
            clase = Mago(jugador)
            break
        elif clase == "3":
            clase = Tanque(jugador)
            break
        elif clase == "4":
            clase = Asesino(jugador)
            break
        else:
            print("Esa no es ninguna clase, intenta de nuevo")
    jugador = clase
    print(
        f"""Bienvenido, seras un gran {jugador.clase}\n
          Estas son tus estadisticas(por ahora): \n"""
    )
    mostrar_estadisticas(jugador)
    return jugador


def mostrar_estadisticas(jugador):
    return print(
        f"""
            Nombre = {jugador.nombre} \n 
            Clase = {jugador.clase} \n 
            Vida = {jugador.vida} \n 
            Ataque = {jugador.ataque} \n 
            Maná = {jugador.mana}"""
    )
