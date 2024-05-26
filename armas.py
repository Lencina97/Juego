from personajes import Armas


def armas(nombre, bonus_ataque, lista):
    arma = Armas(nombre, bonus_ataque)
    arma = lista.append(arma)


armas_para_heroe = []


armas("Excalibur", 15, armas_para_heroe)
armas("Fauces del Dragón", 23, armas_para_heroe)
armas("Destello Aurora", 10, armas_para_heroe)


def imprimir_armas(lista):
    for arma in lista:
        print(f"Nombre:{arma.nombre}, Ataque: +{arma.bonus_ataque}")


# imprimir_armas(armas_para_heroe)

armas("Rugido del León", 22, armas_para_heroe)
armas("Lagrima de Estrellas", 16, armas_para_heroe)


##imprimir_armas(armas_para_heroe)

armas_para_mago = []


armas("El vaston de los Mil Destellos", 15, armas_para_mago)
armas("Varita del Vórtice Infinito", 25, armas_para_mago)
armas("Orbe de la clarividencia", 32, armas_para_mago)

"""print("Estas son las armas de Mago")
imprimir_armas(armas_para_mago)

print("Estas son las armas de Heroe")
imprimir_armas(armas_para_heroe)
"""


listado_de_armas = {1: armas_para_heroe, 2: armas_para_mago}


def filtrar_armas(listado_de_armas, elemento):
    lista = listado_de_armas[elemento]
    return lista


# lista_filtrada = filtrar_armas(listado_de_armas, 2)
# imprimir_armas(lista_filtrada)
# deseo = input("")
# indice = int(deseo)
# arma = lista_filtrada[indice]
