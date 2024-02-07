import sys
import math
import pygame as pg
sys.path.append('..')   # Nos movemos un direcctorio arriba
from res.App import App
from res.GLUtils import *
from res.Point import Point
from res.Line import Line
from OpenGL.GL import *
from OpenGL.GLU import *


class GLApp(App):
    def Init(self):
        self.ortoWidth, self.ortoHeight = 1, 1
        self.currentLine = None
        self.lines = []
        self.mouseDown = False

    def Setup(self):
        # Los vectores suelen venir normalizados entre -1 y 1
        # asi que para mapear valores tenemos que dibujar en 
        # un espacio normalizado entre 0 y 1
        GLUtils.InitOntho(0, self.ortoWidth, self.ortoHeight, 0)

    def Inputs(self):
        for event in self.events:
            if event.type == pg.MOUSEBUTTONDOWN:
                self.mouseDown = True

                # Cuando apretemos el boton del raton creamos una nueva linea
                self.currentLine = Line()

                # Guardamos la linea en nuestro array de lineas
                self.lines.append(self.currentLine)

            elif event.type == pg.MOUSEBUTTONUP:
                self.mouseDown = False
            elif event.type == pg.MOUSEMOTION and self.mouseDown:
                x, y = pg.mouse.get_pos()
                
                currPoint = Point(GLUtils.MapValue(0, self.anchoPatalla, 0, self.ortoWidth, x),
                            GLUtils.MapValue(0, self.altoPantalla, 0, self.ortoHeight, y))
                
                # Pasamos los puntos normalizados
                self.currentLine.points.append(currPoint)
                #print(x, y)

    def Render(self):
        GLUtils.PrepareRender()
        #GLUtils.DrawPoint(self.points, 5) # Asi podemos ver los puntos de la lineas
        GLUtils.DrawLine(self.lines, 1)

        


if __name__ == '__main__':
    app = GLApp("OpenGL en Python", 900, 600, 60)
    app.Run()