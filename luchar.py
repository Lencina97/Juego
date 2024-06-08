from personajes import *
from armas import imprimir_armas


def luchar(jugador):
    oponente = Enemigo()

    while oponente.vida > 0:
        oponente.vida -= round(jugador.ataque / 15)
        jugador.vida -= round(oponente.ataque / 15)
        print(f"Tu oponente tiene {oponente.vida} de vida")
        print(f"Tienes {jugador.vida} de vida")
        if jugador.vida <= 0:
            print("Has muerto")
            break
        elif oponente.vida == 0:
            print("Enemigo derrotado")
    # return jugador


# if jugador.clase == "Heroe":
#                imprimir_armas(armas_para_heroe)
#                deseo = input(" ")
#                indice = int(deseo)
#                arma = armas_para_heroe[indice]
#                jugador.equipar_arma(arma)
#                mostrar_estadisticas(jugador)
#
# luchar(jugador)
