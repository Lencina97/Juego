clientes = {}


def agregar_clientes(clientes):
    nombre = input("Ingrese el nombre del cliente: ")
    edad = input("Ingrese la edad del cliente: ")
    email = input("Ingrese el email del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    cliente = {"Nombre ": nombre, "Edad ": edad, "Email": email, "Telefono": telefono}
    clientes.append(cliente)


agregar_clientes(clientes)

print(clientes)
