from personajes import *

nombre = input("Escribe tu nombre: ").capitalize()
# clase = " "
# datos = [nombre, clase]


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
    acciones(jugador)


def caminar(jugador):
    respuesta = input("Encontraste una cueva, ¿quieres entrar? ").capitalize()
    if respuesta == "Si":
        respuesta_bar = input(
            "Es un bar, ¿quieres beber algo y recuperar vida? "
        ).capitalize()
        if respuesta_bar == "Si":
            jugador.vida = jugador.vida
            print(f"Vida recuperada al 100%")
            acciones(jugador)
        else:
            jugador.vida = round(jugador.vida - (jugador.vida / 30))
            print("El cantinero enloqueció, te atacó y te quitó vida")
            print(f"Vida = {jugador.vida}")
            acciones(jugador)
    else:
        print("Entonces seguimos nuestro camino")
        acciones(jugador)


def acciones(jugador):
    while True:
        deseo = input(
            f"""¿{jugador.nombre} el {jugador.clase} qué deseas hacer? \n
                      1)Luchar \n
                      2)Correr\n
                      3)Caminar \n
                      4)Mostrar estadisticas\n
                      """
        )
        if deseo == "1":
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


def seleccion_clase(nombre):
    while True:
        clase = input(
            f"""Selecciona tu personaje {nombre}: \n
                  1)Héroe\n
                  2)Mago\n
                  3)Tanque\n
                  4) Asesino\n"""
        )

        if clase == "1":
            clase = Heroe(nombre)
            break
        elif clase == "2":
            clase = Mago(nombre)
            break
        elif clase == "3":
            clase = Tanque(nombre)
            break
        elif clase == "4":
            clase = Asesino(nombre)
            break
        else:
            print("Esa no es ninguna clase, intenta de nuevo")
    jugador = clase
    print(
        f"""Bienvenido {jugador.nombre}, seras un gran {jugador.clase}\n
          Estas son tus estadisticas(por ahora): \n"""
    )
    mostrar_estadisticas(jugador)
    acciones(jugador)


def clases(clase, nombre):
    jugador = clase()
    nombre = jugador.nombre
    return


def mostrar_estadisticas(jugador):
    print(f"Nombre = {jugador.nombre}")
    print(f"Clase = {jugador.clase}")
    print(f"Vida = {jugador.vida}")
    print(f"Ataque = {jugador.ataque}")
    print(f"Maná = {jugador.mana}")


seleccion_clase(nombre)
