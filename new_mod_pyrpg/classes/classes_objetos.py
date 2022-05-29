import classes.classes_entidades
lista_items = []

class Item:
    def __init__(self, suma, coste, nombre):
        self.suma = suma
        self.coste = coste
        self.coste_inicial = coste
        self.nombre = nombre
        lista_items.append(self)

class Poción(Item):
    def __init__(self, suma, coste, nombre):
        super().__init__(suma, coste, nombre)

    def usar(self, entidad):
        entidad.vida_act += self.suma
        if entidad.vida_act > entidad.vida_max:
            entidad.vida_act =  entidad.vida_max

class Escudo(Item):
    def __init__(self, suma, coste, nombre):
        super().__init__(suma, coste, nombre)

    def usar(self, entidad):
        if type(entidad) == classes.classes_entidades.Jugador:
            entidad.escudo_act += self.suma
        else:
            raise TypeError("Esta entidad no tiene la carasteristica <escudo>")
