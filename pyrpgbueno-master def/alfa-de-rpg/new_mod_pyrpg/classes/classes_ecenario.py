from prettytable import *


tabla = PrettyTable()


class Escenarios:
    def __init__(self, nombre, aciones):
        self.nombre = nombre
        self.aciones = aciones


class Combate(Escenarios):
    def __init__(self, nombre, aciones):
        super().__init__(nombre, aciones)
        self.piso = 1

class Tienda(Escenarios):
    def __init__(self, items, nombre, aciones):
        super().__init__(nombre, aciones)
        self.Items_ala_venta = items
        self.tangaciones=0

    def mostrar_items(self):
        id = 0
        tabla.clear()
        tabla.field_names = ["id", "Nombre", "Coste", "Puntos de afectación"]
        for i in self.Items_ala_venta:
            id += 1
            tabla.add_row([f"{id}",f"{i.nombre}",f"{i.coste}",f"{i.suma}"])
        print(tabla)





