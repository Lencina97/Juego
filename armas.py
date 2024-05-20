from personajes import Armas

espada_larga = Armas("Excalibur", 15)
espada_bastarda = Armas("Fauces del Dragón", 23)
espada_corta = Armas("Destello Aurora", 10)

armas_para_heroe = []


def armas_heroe(arma):
    arma = armas_para_heroe.append(arma)
    return armas_para_heroe


armas_heroe(espada_bastarda)
armas_heroe(espada_corta)
armas_heroe(espada_larga)


def imprimir_armas(lista):
    for arma in lista:
        print(f"Nombre:{arma.nombre}, Ataque: +{arma.bonus_ataque}")


# imprimir_armas(armas_para_heroe)

espada_ancha = Armas("Rugido del León", 22)
espada_elfica = Armas("Lagrima de Estrellas", 16)

armas_heroe(espada_ancha)
armas_heroe(espada_elfica)
##imprimir_armas(armas_para_heroe)
