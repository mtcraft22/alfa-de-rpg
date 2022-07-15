from prettytable import *

from classes.classes_habilidad import habilidades_classes


tabla = PrettyTable()
tabla_habilidades = PrettyTable()
lista_enemigos = []

class Entidades:
    def __init__(self, nombre, ataque, defensa, vida):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida_max = vida
        self.vida_act = vida
        self.habilidades = []
        self.estado = "Normal"

    def atacar(self, destino):
       destino.vida_act -=self.ataque - destino.defensa

    '''def cambio_estado(self, destino, estado):
        destino.estado = estado'''


class Jugador(Entidades):
    def __init__(self, escudo, nombre, ataque, defensa, vida):
        super().__init__(nombre, ataque, defensa, vida)
        self.mochila = []
        self.mana_max = escudo
        self.mana_act = escudo
        self.dinero = 0
        for i in habilidades_classes:
            self.habilidades.append(i)
    def mostrar_habilidades(self):
        id = 0
        tabla_habilidades.clear()
        tabla_habilidades.field_names = ["id", "Nombre", "Puntos de afectación"]
        for a in self.habilidades:
            id += 1
            tabla_habilidades.add_row([f"{id}", f"{a.nombre}", f"{a.paralisis}"])
        print(tabla_habilidades)
    def mostrar_item(self):
        id = 0
        tabla.clear()
        tabla.field_names = ["id", "Nombre", "Puntos de afectación"]
        for i in self.Items_ala_venta:
            id += 1
            tabla.add_row([f"{id}", f"{i.nombre}", f"{i.suma}"])
        print(tabla)


class Enemigos(Entidades):
    def __init__(self, a):
        nombre = a["nombre"]
        vida= a["vida"]
        ataque = a["ataque"]
        defensa = a["defensa"]
        super().__init__(nombre, ataque, defensa, vida)
        self.planta_minima = a["planta"]
        self.peso = a["peso"]
        self.max_coin = a["coin_max"]
        self.min_coin = a["coin_min"]
        lista_enemigos.append(self)

class Boss(Enemigos):
    def __init__(self, a):
        super().__init__(a)
        self.habilidad = a["habilidad"]
        for i in habilidades_classes:
            if self.habilidad == i.nombre:
                self.habilidad = i
                
            
