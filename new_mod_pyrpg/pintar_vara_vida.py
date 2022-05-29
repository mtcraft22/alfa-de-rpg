import math

import colores_e_estilos


# esta parte esta echa por alejandro garcia, esta adaptada a mis nesecidades


def draw_hp_bar(v_max, v_act, nombre, scale=1):
    print(f"{nombre} [", end="")
    color = colores_e_estilos.verde.clear
    p = v_act / v_max
    if p <= 0.2:
        color = colores_e_estilos.rojo.color
    elif p <= 0.5 and p > 0.2:
        color = colores_e_estilos.amarillo.color
    elif p > 0.5:
        color = colores_e_estilos.verde.color
    for i in range(max(math.ceil(v_act / scale), 0)):
        print(color + "█", end=colores_e_estilos.verde.clear)
    for i in range(max(math.floor((v_max - v_act) / scale), 0)):
        print(" ", end="")
    print("] ", end="")
    print(f"{v_act}/{v_max} PS\n")


