import sys
import pygame as pg
from pygame.locals import *
from res.Point import Point
from res.Line import Line
import json

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

    def ReadFile(self):
        with open('lines.json', 'r') as file:
            # Cargamos los datos
            data = json.load(file)
            for dataLine in data:
                # Por cada linea creamos un objeto linea
                line = Line()
                for point in dataLine:
                    # Cojemos los puntos del archivo y los cargamos
                    # en la nueva linea
                    line.points.append(Point(point[0], point[1]))
                # Guardamos las lineas creadas en el array de lineas
                self.lines.append(line)
        print("Fichero cargado correctamente")


    def WriteFiles(self):
        data = []
        # Vamos a crear el json
        for line in self.lines:
            # Aqui vamos a guardar los puntos
            points = []
            for point in line.points:
                
                # No podemos guardar directamente el point ya que 
                # es un objeto, por lo que guardaremos cojuntamente
                # la posicion X e Y
                points.append([point.x, point.y])

            data.append(points)
        # Guardamos los datos en el json
        with open('lines.json', 'w') as file:
            json.dump(data, file)
        print("Fichero guardado correctamente")
