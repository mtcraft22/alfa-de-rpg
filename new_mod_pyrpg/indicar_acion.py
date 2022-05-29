import pintar_pantalla
import declaaraciones

def preguntar_acion(aciones, com="Introduce el numero coresponiente a la ación:"):
    try:
        acion = int(input(com))
        a_indice_lista = acion - 1
        return int(a_indice_lista)  # devuelve la posicion en lista de la acion selecionada
    except:
        return
   