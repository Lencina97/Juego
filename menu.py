import os

from crear_personaje import seleccion_clase


menu = ["1)Comenzar aventura", "2)Configuración", "3)Salir"]


def aventura():
    print("Bienvenido Aventurero, por favor elige tu clase: ")
    seleccion_clase()


def configuracion():
    print("Te la creiste we")


items = {1: aventura, 2: configuracion, 3: exit}


def seleccion_opcion():

    while True:
        imprimir_menu(menu)
        opcion = int(input("Elige una opción: "))
        if opcion in items:
            items[opcion]()
            break
        else:
            print("Elegi bien gato")
            break


def imprimir_menu(lista):
    for item in lista:
        print(item)


if os.name == "nt":
    os.system("cls")
