def caminar(jugador):
    respuesta = input("Encontraste una cueva, ¿quieres entrar? ").capitalize()
    if respuesta == "Si":
        respuesta_bar = input(
            "Es un bar, ¿quieres beber algo y recuperar vida? "
        ).capitalize()
        if respuesta_bar == "Si":
            jugador.vida = jugador.vida
            print(f"Vida recuperada al 100%")
            # acciones(jugador)
        else:
            jugador.vida = round(jugador.vida - (jugador.vida / 30))
            print("El cantinero enloqueció, te atacó y te quitó vida")
            print(f"Vida = {jugador.vida}")
            # acciones(jugador)
    else:
        print("Entonces seguimos nuestro camino")
    # return jugador
