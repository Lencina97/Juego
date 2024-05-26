from personajes import *


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


# luchar(jugador)
