import random
import json
import os
habilidades_classes = []
lista_habilidades_json = []
os.chdir("./habilidades")
for i in os.listdir(os.getcwd()):
    lista_habilidades_json.append(i)

print(lista_habilidades_json)

class habilidades():
    def __init__(self,a):
        self.nombre = a["nombre"]
        self.config = a["config"]
        self.estados = a["estados"]
        self.aciones = a["aciones"]
        
        
       
    def ataca(self):
        self.ataca=[]
        for i in range(self.config["ataque"]["probabilidad"]):
            self.ataca.append(True)
        for i in range(100-self.config["ataque"]["probabilidad"]):
            self.ataca.append(False)
        return random.choice(self.ataca)
for i in os.listdir(f"{os.getcwd()}"):
    with open(f"{i}", "r",encoding="utf-8") as enem:
        habilidades_dic = json.loads(enem.read())
    habilidad_class = habilidades(habilidades_dic)
    print(habilidad_class.nombre,habilidad_class.ataca())
os.chdir("./..")
'''for i in range(100):
    print(i,"aaa\n")
    habilidad_class.calc_acierto()
    habilidad_class.calc_probalilidad()'''


