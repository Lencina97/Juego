class Personaje:
    def __init__(self, nombre, clase, vida=100, ataque=300, mana=200):
        self.nombre = nombre
        self.clase = clase
        self.vida = vida
        self.ataque = ataque
        self.mana = mana


# El nombre es un atributo que hay que insertar algun valor
class Heroe(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, clase="Heroe")
        self.vida *= 4
        self.ataque += 300


class Tanque(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, clase="Tanque")
        self.vida += 130
        self.ataque *= 3
        self.mana -= 150


class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, clase="Mago")
        self.vida *= 3
        self.ataque += 300

    def regeneracion(self, vida):
        vida *= 2


class Asesino(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, clase="Asesino")
        self.vida *= 2
        self.ataque *= 5


class Enemigo(Personaje):
    def __init__(self):
        super().__init__(nombre="Enemigo", clase="Enemigo")
        self.vida *= 2


# jugador = Mago("Brian")
# print(jugador.nombre)

# def mostrar_datos(clase):
#    personaje_uno = clase()
#    print(f"Nombre = {personaje_uno.nombre}")
#    print(f"Vida = {personaje_uno.vida}")
#    print(f"Ataque = {personaje_uno.ataque}")
#    print(f"Maná = {personaje_uno.mana}")
#
#
# mostrar_datos(Heroe)
#
#
# mostrar_datos(Mago)
#
#
# mostrar_datos(Tanque)
#
#
# mostrar_datos(Asesino)
