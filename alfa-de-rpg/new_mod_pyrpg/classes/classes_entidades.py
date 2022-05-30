from prettytable import *

from classes_habilidad import habilidades_classes


tabla = PrettyTable()
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
        self.escudo_max = escudo
        self.escudo_act = escudo
        self.dinero = 0

    def mostrar_items(self):
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
                
            
ab={
    "nombre":"goblin_boss",
    "vida": 15,
    "ataque": 4,
    "defensa": 0.75,
    "planta": 23,
    "peso": 10,
    "coin_max":50,
    "coin_min":48,
    "habilidad":"veneno_2"
    
}     
goblinboss=Boss(ab)

goblinboss.habilidad.calc_acierto()
goblinboss.habilidad.calc_probalilidad()
goblinboss.habilidad.calc_turnos()