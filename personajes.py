class Personaje:
    def __init__(
        self,
        clase,
        vida=100,
        ataque=300,
        mana=200,
    ):
        self.clase = clase
        self.vida = vida
        self.ataque = ataque
        self.mana = mana

    def equipar_arma(self, bonus_ataque):
        self.ataque += bonus_ataque


class Armas:
    def __init__(self, nombre, bonus_ataque):
        self.nombre = nombre
        self.bonus_ataque = bonus_ataque


# El nombre es un atributo que hay que insertar algun valor
class Heroe(Personaje, Armas):
    def __init__(self):
        super().__init__(
            clase="Heroe",
        )
        self.vida *= 4
        self.ataque += 300


class Tanque(Personaje):
    def __init__(self):
        super().__init__(clase="Tanque")
        self.vida += 130
        self.ataque *= 3
        self.mana -= 150


class Mago(Personaje):
    def __init__(self):
        super().__init__(clase="Mago")
        self.vida *= 3
        self.ataque += 300

    def regeneracion(self, vida):
        vida *= 2


class Asesino(Personaje):
    def __init__(self):
        super().__init__(clase="Asesino")
        self.vida *= 2
        self.ataque *= 5


class Enemigo(Personaje):
    def __init__(self):
        super().__init__(clase="Enemigo")
        self.vida *= 2


clases = [Heroe, Mago, Tanque, Asesino]

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
