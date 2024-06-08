from luchar import luchar
from caminar import caminar


def mostrar_estadisticas(jugador):
    return print(
        f"""
            Clase = {jugador.clase} \n
            Vida = {jugador.vida} \n
            Ataque = {jugador.ataque} \n
            Maná = {jugador.mana}"""
    )


def correr():
    print("Corriendo")
    exit


opciones = [luchar, correr, caminar, mostrar_estadisticas]


def mostrar_opciones(lista):
    for opcion in lista:
        print(opcion)


def acciones(jugador):
    while True:
        deseo = input(
            f"""¿Qué deseas hacer? \n 1)Luchar \n 2)Correr\n 3)Caminar \n 4)Mostrar estadisticas\n 5)Mostrar Armas"""
        )
        if deseo == "1":
            print("Antes de Luchar, elige tu arma")

            luchar(jugador)
        elif deseo == "2":
            print("Corriendo")
            break
        elif deseo == "3":
            caminar(jugador)
        elif deseo == "4":
            mostrar_estadisticas(jugador)

        else:
            print("Intenta con otra opcion")
