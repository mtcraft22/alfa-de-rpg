import random
import json
import os
enemigos_classes = []
lista_enemigos_json = []
os.chdir("./../habilidades")
for i in os.listdir(os.getcwd()):
    lista_enemigos_json.append(i)

print(lista_enemigos_json)

class habilidades():
    def __init__(self,a):
        self.nombre = a["nombre"]
        self.probabilidad = a["probabilidad"]
        self.precisión = a["precision"]
        self.puntosafectados = a["puntosafectados"]
        self.turnos_max = a["turnos_max"]
        self.turnos_min = a["turnos_min"]
    def calc_turnos (self):
        return random.randint(self.turnos_min, self.turnos_max)
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
        enemigos_dic = json.loads(enem.read())
    enemigo_class = habilidades(enemigos_dic) 

for i in range(100):
    print(i,"aaa\n")
    enemigo_class.calc_acierto()
    enemigo_class.calc_probalilidad()


