import time
import random
import pickle
import os
import saves_managment  
import declaaraciones
import lista_enemigos_por_nivel
import pintar_pantalla
import indicar_acion
from classes.classes_objetos import lista_items as productos
if len(saves_managment.lista_ficheros)!=0:
    os.chdir("./saves")
    Cargado=open(saves_managment.selecionpartida(),"rb")
    Jugador_info=pickle.load(Cargado)
    declaaraciones.J.dinero=Jugador_info.dinero
    declaaraciones.J.mochila=Jugador_info.mochila
    os.chdir("./..")
else:
    print("No se cargo nigun fichero")
def combate():
    
    ene = random.choice(lista_enemigos_por_nivel.sacar_lista_nivel(declaaraciones.com.piso))
    declaaraciones.mochila_es.Items_ala_venta=declaaraciones.J.mochila 
    while declaaraciones.J.vida_act > 0 and ene.vida_act > 0:
        
        pintar_pantalla.actualizar_pantalla(declaaraciones.com, ene, declaaraciones.J, f" {declaaraciones.J.mochila}")
        acion = indicar_acion.preguntar_acion(declaaraciones.com.aciones)
        if acion == 0:
            declaaraciones.J.atacar(ene)
            pintar_pantalla.actualizar_pantalla(declaaraciones.com, ene, declaaraciones.J,
                                                f" Inflingistes {declaaraciones.J.ataque - ene.defensa} de daño ")
            time.sleep(0.5)
            ene.atacar(declaaraciones.J)
            pintar_pantalla.actualizar_pantalla(declaaraciones.com, ene, declaaraciones.J,
                                                f" Te hicieron {ene.ataque - declaaraciones.J.defensa} de daño ")
        elif acion == 2:
           
            pintar_pantalla.actualizar_pantalla(declaaraciones.mochila_es,None, declaaraciones.J,"Mi mochila")
            item_us=indicar_acion.preguntar_acion(declaaraciones.mochila_es.aciones, "Introduce ID de producto a usar o enter para salir ")
            if type(item_us) != int:
                continue
            try:
                declaaraciones.J.mochila[item_us].usar(declaaraciones.J)
                pintar_pantalla.actualizar_pantalla(declaaraciones.mochila_es,None, declaaraciones.J,f"Usastes {declaaraciones.J.mochila[item_us].nombre}")
                declaaraciones.J.mochila.pop(item_us)
            except IndexError:
                pintar_pantalla.actualizar_pantalla(declaaraciones.mochila_es,None, declaaraciones.J,"Introduce un valor correcto:")
            
            while item_us> len(declaaraciones.J.mochila):
                pintar_pantalla.actualizar_pantalla(declaaraciones.mochila_es,None, declaaraciones.J,"Mi mochila")
                item_us=indicar_acion.preguntar_acion(declaaraciones.mochila_es.aciones, "Introduce ID de producto a usar o enter para salir ")
                if type(item_us) != int:
                    break
                try:
                    declaaraciones.J.mochila[item_us].usar(declaaraciones.J)
                    pintar_pantalla.actualizar_pantalla(declaaraciones.mochila_es,None, declaaraciones.J,f"Usastes {declaaraciones.J.mochila[item_us].nombre}")
                    declaaraciones.J.mochila.pop(item_us)
                except IndexError:
                    pintar_pantalla.actualizar_pantalla(declaaraciones.mochila_es,None, declaaraciones.J,"Introduce un valor correcto:")  
            continue
        elif acion == 3:
           
            pintar_pantalla.actualizar_pantalla(declaaraciones.habilidades,None, declaaraciones.J,"Mi mochila")
            item_us=indicar_acion.preguntar_acion(declaaraciones.habilidades.aciones, "Introduce ID de producto a usar o enter para salir ")
            if type(item_us) != int:
                continue
            try:
                declaaraciones.J.mochila[item_us].usar(declaaraciones.J)
                pintar_pantalla.actualizar_pantalla(declaaraciones.habilidades,None, declaaraciones.J,f"Usastes {declaaraciones.J.mochila[item_us].nombre}")
                declaaraciones.J.mochila.pop(item_us)
            except IndexError:
                pintar_pantalla.actualizar_pantalla(declaaraciones.habilidades,None, declaaraciones.J,"Introduce un valor correcto:")
            
            while item_us> len(declaaraciones.J.mochila):
                pintar_pantalla.actualizar_pantalla(declaaraciones.habilidades,None, declaaraciones.J,"Mi mochila")
                item_us=indicar_acion.preguntar_acion(declaaraciones.habilidades.aciones, "Introduce ID de producto a usar o enter para salir ")
                if type(item_us) != int:
                    break
                try:
                    declaaraciones.J.mochila[item_us].usar(declaaraciones.J)
                    pintar_pantalla.actualizar_pantalla(declaaraciones.habilidades,None, declaaraciones.J,f"Usastes {declaaraciones.J.mochila[item_us].nombre}")
                    declaaraciones.J.mochila.pop(item_us)
                except IndexError:
                    pintar_pantalla.actualizar_pantalla(declaaraciones.habilidades,None, declaaraciones.J,"Introduce un valor correcto:")  
            continue    
    pintar_pantalla.actualizar_pantalla(declaaraciones.final, ene, declaaraciones.J,
                                        f" final combate, llendo al hub ")
    
    if declaaraciones.J.vida_act <= 0:
        declaaraciones.J.vida_act = declaaraciones.J.vida_max/2
        ene.vida_act = ene.vida_max
    elif ene.vida_act <= 0:
        pasta = random.randint(ene.min_coin, ene.max_coin)
        declaaraciones.J.dinero += pasta
        ene.vida_act = ene.vida_max
        pintar_pantalla.actualizar_pantalla(declaaraciones.final, ene, declaaraciones.J,f"Recivistes {pasta} coin/s ")
        time.sleep(0.5)
    
    selecionar()

def comprar():
    pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, "Bienvenido al baludaque")
    acion = indicar_acion.preguntar_acion(declaaraciones.tienda.aciones)
    if acion == 0:
        pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, "¿Que desea comprar?")
        item= indicar_acion.preguntar_acion(declaaraciones.tienda.aciones,"Introduce la id del item: ")
        if declaaraciones.J.dinero>= productos[item].coste:
            declaaraciones.J.mochila.append(productos[item])
            nombres=[]
            nombres.append(productos[item].nombre)
            declaaraciones.J.dinero -= productos[item].coste
            pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, f"compraste {productos[item].nombre}")
            if declaaraciones.tienda.tangaciones > 0:
                declaaraciones.tienda.tangaciones -= 1
                pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, f"Como has comprado te descuento un robo robos pendientes {declaaraciones.tienda.tangaciones}")
            print("Su mochila: ", nombres)
            input("sal")
            comprar()
        else:
            pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, f"No me robes !cara dura¡")

    if acion == 2:
        item = indicar_acion.preguntar_acion(declaaraciones.tienda.aciones,"Introduce la id del item: ")
        declaaraciones.J.mochila.append(productos[item])
        nombres=[]
        nombres.append(productos[item].nombre)
        pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, f"ahora incrementaré un 25% los precios por tonto, cuidado que lo pagaras")
        declaaraciones.tienda.tangaciones +=1
        if declaaraciones.tienda.tangaciones > 5 and declaaraciones.tienda.tangaciones <= 10:
            pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, f"Me daras toda la pasta por cometer acciones poco licitas")
            declaaraciones.J.dinero = 0
        elif declaaraciones.tienda.tangaciones >= 10:
            pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, f"Me daras toda la mochila por cometer acciones poco licitas")
            declaaraciones.J.mochila.clear()
        for i in declaaraciones.tienda.Items_ala_venta:
            i.coste *=1.25
        print("Su mochila: ", nombres)
        input("sal")
        comprar()
        
    if acion == 3:
        selecionar()


def selecionar():
    pintar_pantalla.actualizar_pantalla(declaaraciones.Hub, None, None, None)
    acion = indicar_acion.preguntar_acion(declaaraciones.Hub.aciones)
    if acion == 0:
        comprar()
    if acion == 1:
        combate()
    if acion == 3:
        os.chdir("./saves")
        id=0
        for i in saves_managment.lista_ficheros:
            id +=1
            print(f"{id}. {i}")
        
        try:
            fichero=int(input("Indique numero del archivo a sobreescribir o Enter para archivo nuevo "))
        except:
            fichero=input("Indique nombre de nuevo archivo ")
        if type(fichero)==int:
            
            fichero_sel=saves_managment.lista_ficheros[fichero-1]
            data=open(f"{fichero_sel}","wb")
            pickle.dump(declaaraciones.J,data)
             
        else:
            data=open(f"{fichero}.prpg","x")
            with open(f"{fichero}.prpg","wb") as data:
                pickle.dump(declaaraciones.J, data)
        os.chdir("./..")
combate()