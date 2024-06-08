from crear_personaje import seleccion_clase
import os
from selector_opciones import seleccion_opciones


def aventura():
    print("Bienvenido Aventurero, por favor elige tu clase: ")
    seleccion_clase()


def configuracion():
    print("Te la creiste we")


def salir():
    exit()


items = [aventura, configuracion, salir]


def limpiar_consola():
    os.system("cls")


def seleccion_opcion():
    seleccion_opciones(items)
