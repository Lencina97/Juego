from crear_personaje import mostrar_estadisticas
from luchar import luchar
from caminar import caminar
from armas import armas_para_heroe, imprimir_armas


def acciones(jugador):
    while True:
        deseo = input(
            f"""¿Qué deseas hacer? \n 1)Luchar \n 2)Correr\n 3)Caminar \n 4)Mostrar estadisticas\n 5)Mostrar Armas"""
        )
        if deseo == "1":
            print("Antes de Luchar, elige tu arma")
            if jugador.clase == "Heroe":
                imprimir_armas(armas_para_heroe)
                deseo = input(" ")
                indice = int(deseo)
                arma = armas_para_heroe[indice]
                jugador.equipar_arma(arma)
                mostrar_estadisticas(jugador)
            luchar(jugador)
        elif deseo == "2":
            print("Corriendo")
            break
        elif deseo == "3":
            caminar(jugador)
        elif deseo == "4":
            mostrar_estadisticas(jugador)
        elif deseo == "5":
            imprimir_armas(armas_para_heroe)
        else:
            print("Intenta con otra opcion")
    # return jugador
