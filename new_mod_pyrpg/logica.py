import time
import random




import declaaraciones
import lista_enemigos_por_nivel
import pintar_pantalla
import indicar_acion
from classes.classes_objetos import lista_items as productos



def combate():
    ene = random.choice(lista_enemigos_por_nivel.sacar_lista_nivel(declaaraciones.com.piso))
    while declaaraciones.J.vida_act > 0 and ene.vida_act > 0:
        
        pintar_pantalla.actualizar_pantalla(declaaraciones.com, ene, declaaraciones.J, f" Inicio de combate")
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
            declaaraciones.J.mochila[item_us].usar(declaaraciones.J)
            pintar_pantalla.actualizar_pantalla(declaaraciones.mochila_es,None, declaaraciones.J,f"Usastes {declaaraciones.J.mochila[item_us].nombre}")
            declaaraciones.J.mochila.pop(item_us)
            
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
            declaaraciones.J.mochila.clear
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


combate()
