import random
import json
import os
habilidades_classes = []
lista_habilidades_json = []
os.chdir("./../habilidades")
for i in os.listdir(os.getcwd()):
    lista_habilidades_json.append(i)

print(lista_habilidades_json)

class habilidades():
    def __init__(self,a):
        self.nombre = a["nombre"]
        self.probabilidad = a["probabilidad"]
        self.precisión = a["precision"]
        self.puntosafectados = a["puntosafectados"]
        self.turnos_max = a["turnos_max"]
        self.turnos_min = a["turnos_min"]
        habilidades_classes.append(self)
    def calc_turnos (self):
        a=random.randint(self.turnos_min, self.turnos_max)
        print(a)
        return a
    def calc_acierto(self):
        a=[]
        for i in range(self.precisión):
            a.append(True)
        for b in range(100-self.precisión):
            a.append(False)
        print("prob_arci",random.choice(a))
    def calc_probalilidad(self):
        p=[]
        for i in range(self.probabilidad):
            p.append(True)
        for b in range(100-self.probabilidad):
            p.append(False)
        print("prob_lan",random.choice(p))
for i in os.listdir(f"{os.getcwd()}"):
    with open(f"{i}", "r") as enem:
        habilidades_dic = json.loads(enem.read())
    habilidad_class = habilidades(habilidades_dic) 
print(habilidades_classes)
'''for i in range(100):
    print(i,"aaa\n")
    habilidad_class.calc_acierto()
    habilidad_class.calc_probalilidad()'''


