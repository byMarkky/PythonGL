import sys
import pygame as pg
from pygame.locals import *

class App:
    def __init__(self, titulo, ancho, alto, maxFPS):
        pg.init()   # Inicializamos pygame
        self.titulo = titulo
        self.maxFPS = maxFPS
        self.anchoPatalla, self.altoPantalla = ancho, alto
        
        # Habilitamos el doble buffer
        self.display = pg.display.set_mode(
            (ancho, alto), DOUBLEBUF | OPENGL)
        self.clock = pg.time.Clock()
        
    def Run(self):
        self.Init()     # Iniciamos los miembros
        self.Setup()    # Iniciamos la configuracion

        while 1:
            self.events = pg.event.get()
            for event in self.events:
                if event.type == pg.QUIT:
                    sys.exit()
            
            # Calculamos los FPS
            self.deltaTime = self.clock.tick(self.maxFPS) / 1000
            self.Inputs()   # Frame inputs
            self.Update()   # Frame login
            self.Render()   # Frame drawing

            pg.display.flip()   # Cambiamos de buffer
            pg.display.set_caption(
                f"{self.titulo} ({self.clock.get_fps():.2f} fps)")
    
    def Init(self):
        pass

    def Setup(Setup):
        pass

    def Inputs(self):
        pass

    def Update(self):
        pass

    def Render(self):
        pass