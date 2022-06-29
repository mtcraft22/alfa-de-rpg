
import math
import pygame
pygame.init()
fuente=pygame.font.Font(None,20)
clicks= pygame.mixer.Sound("click.ogg")
class botones():
    def __init__(self, tam,pos,texto,relieve,colores):
        # configuracion base de los botones
        self.click=False
        self.ancho=tam[0]
        self.alto=tam[1]
        self.pos_y=pos[1]
        self.color_fontral_static=colores
        self.color_fondo=[]
        for i in colores:
            print(i)
            i-=30
            if i>=0:
                self.color_fondo.append(i)
            else:
                self.color_fondo.append(0)
            print(self.color_fondo)
        self.color_fontral=colores[0]
        self.pos=pos
        self.hover_color=[]
        for i in colores:
            print(i)
            i+=25
            if i<=255:
                self.hover_color.append(i)
            else:
                self.hover_color.append(255)
        print(self.hover_color)
        self.texto=texto
        self.relieve=relieve
        self.tam=math.ceil(self.alto/2)
        self.fuente=pygame.font.Font(None,self.tam)
        self.relieve_dinamico=relieve
    def mostrar(self,superficie):
        action=False
        self.rect_top=((self.pos[0],self.pos[1]-self.relieve_dinamico),(self.alto,self.ancho))
        self.rect_bottom=(self.pos,(self.alto,self.ancho))
        
        pygame.draw.rect(superficie,self.color_fondo,self.rect_bottom,border_radius=12)
        rect_frontal=pygame.draw.rect(superficie,self.color_fontral,self.rect_top,border_radius=12)
        
        render=self.fuente.render(self.texto,True,(255,255,255))
        render_rect=render.get_rect(center=rect_frontal.center)
        render_rect.center=rect_frontal.center
        superficie.blit(render,render_rect)
        mouse_pos =pygame.mouse.get_pos()
        if rect_frontal.collidepoint(mouse_pos) :
            self.color_fontral=self.hover_color
            if pygame.mouse.get_pressed()[0]and self.click==False:
                self.relieve_dinamico=0
                self.click=True
                action=True
                clicks.play()
        else:
            self.color_fontral=self.color_fontral_static
        if pygame.mouse.get_pressed()[0]==False:
            self.relieve_dinamico=self.relieve
            self.click=False
            
        return action  
        
            