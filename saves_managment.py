
import os
import pickle
import indicar_acion

os.chdir("./saves")
lista_ficheros=[]
for i in os.listdir():
    lista_ficheros.append(i)
def create_save(nombre):
    open(f"{nombre}.prpg","x")
    lista_ficheros.clear()
    for i in os.listdir():
            lista_ficheros.append(i)
    
def selecionpartida():
    id=0
    for i in lista_ficheros:
        id +=1
        print(f"{id}. {i}")
    fichero=indicar_acion.preguntar_acion(lista_ficheros,"Selecione el fichero a cargar enter para continuar: ")
    return lista_ficheros[fichero]

os.chdir("./..")

