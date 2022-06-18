import math




# esta parte esta echa por alejandro garcia, esta adaptada a mis nesecidades


def draw_hp_bar(v_max, v_act, nombre,color_a,color_b,color_c, scale=1):
    print(f"{nombre} [", end="")
    color = color_a.clear
    p = v_act / v_max
    if p <= 0.2:
        color = color_c.color
    elif p <= 0.5 and p > 0.2:
        color = color_b.color
    elif p > 0.5:
        color = color_a.color
    for i in range(max(math.ceil(v_act / scale), 0)):
        print(color + "█", end=color_a.clear)
    for i in range(max(math.floor((v_max - v_act) / scale), 0)):
        print(" ", end="")
    print("] ", end="")
    print(f"{v_act}/{v_max} PS\n")


