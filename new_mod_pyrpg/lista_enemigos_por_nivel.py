import declaaraciones


def sacar_lista_nivel(nivel):
    listxnil = []
    for i in declaaraciones.lista_enemigos_completa:
        if i.planta_minima <= nivel:
            listxnil.append(i)
        else:
            continue
    return listxnil


