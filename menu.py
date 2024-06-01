from crear_personaje import seleccion_clase
import os

menu = ["1)Comenzar aventura", "2)Configuración", "3)Salir"]


def aventura():
    print("Bienvenido Aventurero, por favor elige tu clase: ")
    seleccion_clase()


def configuracion():
    print("Te la creiste we")


items = {1: aventura, 2: configuracion, 3: exit}


def limpiar_consola():
    os.system("cls")


def imprimir_menu(lista):
    for item in lista:
        print(item)


def seleccion_opcion():
    while True:
        imprimir_menu(menu)
        opcion = int(input("Elige una opción: "))
        if opcion in items:
            limpiar_consola()
            items[opcion]()

            break
        else:
            print("Elegi bien gato")
            break
