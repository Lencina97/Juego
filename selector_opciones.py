def imprimir_lista(lista, indice=1):
    for item in lista:
        print(f"{indice}){item.__name__.capitalize()}")
        indice += 1


def seleccion_opciones(lista):
    while True:
        print("Elige una opcion:")
        imprimir_lista(lista)
        opcion = int(input("Elige una opción: ")) - 1
        if opcion < len(lista):
            lista = lista[opcion]
            if callable(lista):
                lista()

            return lista()

        else:
            print("Eso no es una opción")
