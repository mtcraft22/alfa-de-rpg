import os  # importamos la libreria os para executar el comando color que nos permitira visualizar nuestros colores


'''classe para crear los colores requiere los valores rgb i true o 
false para decir si el color es para el fondo o pra el texto'''


class CreadorDeColor:
    os.system("color")

    def __init__(self, r, g, b, es_fondo):
        self.r = r
        self.g = g
        self.b = b
        self.es_fondo = es_fondo
        self.color = None
        self.clear = None

    def generate_color(self):
        if self.es_fondo:
            self.color = f"\033[48;2;{self.r};{self.g};{self.b}m"
            self.clear = "\033[49m"
        else:
            self.color = f"\033[38;2;{self.r};{self.g};{self.b}m"
            self.clear = "\033[38;2;255;255;255m"


rojo = CreadorDeColor(200, 23, 23, False)
rojo.generate_color()
amarillo = CreadorDeColor(255, 255, 0, False)
amarillo.generate_color()
verde = CreadorDeColor(23, 200, 23, False)
verde.generate_color()

'''
    aleatorio = CreadorDeColor(134, 34, 173, False)  # ejemplo de declaración de color (r , g , b , booleano)
    aleatorio.generate_color()  # método para generar el color
    print(aleatorio.color, "hola este es su color", aleatorio.clear)  # ejemplo de uso 
    
'''

