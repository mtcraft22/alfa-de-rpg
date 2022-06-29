import pygame, time
import cursores,botonespy

pygame.mixer.init()
# parametros de pantalla y variable run
pantalla = pygame.display.set_mode((300, 300), pygame.RESIZABLE|pygame.HWSURFACE|pygame.DOUBLEBUF)


run = True
# carga de imagenes de los botones
boton_a = pygame.image.load("goblin.png")
boton_b = pygame.image.load("goblin-fuerte.png")
# crearos los botones
#boton_logica_a = pygame_buttons.button(50, 200, boton_a, 1)
pygame.mouse.set_cursor(*cursores.default_metadata)
#boton_logica_b = pygame_buttons.button(100, 200, boton_b, 1)

#cargamos sonido
click= pygame.mixer.Sound("click.ogg")
# calulamos el delta time y limitamos los fps
relog = pygame.time.Clock()
fps_max = 60
prev_time = time.time()
vida = 8
vida_max = 20
boton_c =botonespy.botones((100,100),(150,200),"+1",6,[20,200,0])
boton_d =botonespy.botones((100,100),(50,200),"-1",6,[200,20,0])

while run:

    pantalla.fill((255, 255, 255))
    
    if vida>=vida_max :
        suma=-1
    else:
        suma=1
    if boton_c.mostrar(pantalla):
        vida +=suma
    if boton_d.mostrar(pantalla):
        vida -=1
    '''if boton_logica_a.draw(pantalla):
        click.play()
        vida += suma_a
    if boton_logica_b.draw(pantalla):
        vida -= suma_b
        click.play()'''
    # cordenadaas de inicio de dibujado de la vara de vida
    x = 50
    y = 100
    # dibujando la vara de vida
    for i in range(vida_max):
        pygame.draw.rect(pantalla, (255, 154, 0), (x, y, 5, 5))
        x += 5
    x = 50
    # representacion de la vida, dibujando rectagulos
    for i in range(vida):
        pygame.draw.rect(pantalla, (0, 255, 150), (x, y, 5, 5))
        x += 5
    relog.tick(60)
    now = time.time()
    dt = now - prev_time
    prev_time = now
    # obtenemos el valor a multiplicar por la velocidad de animacion del juego
    velocidad_delta_time = dt * fps_max
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

    pygame.display.flip()
