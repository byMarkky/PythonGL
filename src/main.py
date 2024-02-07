import sys
import math
import pygame as pg
sys.path.append('..')   # Nos movemos un direcctorio arriba
from res.App import App
from res.GLUtils import *
from res.Point import Point
from OpenGL.GL import *
from OpenGL.GLU import *


class GLApp(App):
    def Init(self):
        self.ortoWidth, self.ortoHeight = 1, 1
        self.points = []

    def Setup(self):
        # Los vectores suelen venir normalizados entre -1 y 1
        # asi que para mapear valores tenemos que dibujar en 
        # un espacio normalizado entre 0 y 1
        GLUtils.InitOntho(0, self.ortoWidth, self.ortoHeight, 0)

    def Inputs(self):
        for event in self.events:
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()

                # Pasamos los puntos normalizados
                self.points.append(
                    Point(GLUtils.MapValue(0, self.anchoPatalla, 0, self.ortoWidth, x),
                          GLUtils.MapValue(0, self.altoPantalla, 0, self.ortoHeight, y))
                )
                #print(x, y)

    def Render(self):
        GLUtils.PrepareRender()
        GLUtils.DrawPoint(self.points, 5)

        


if __name__ == '__main__':
    app = GLApp("OpenGL en Python", 900, 600, 60)
    app.Run()