from OpenGL.GL import *
from OpenGL.GLU import *

# Aqui tendremos funciones para reusarlas
class GLUtils:

    @staticmethod
    def InitOntho(left, right, top, bottom):
        # Configuramos la matriz de proyeccion sobre la que
        # aplicaremos las posteriores configuraciones
        glMatrixMode(GL_PROJECTION)

        # No es necesario pero es una buena practica
        # aplicar la matriz identidad
        glLoadIdentity()

        # Inicializamos la matriz de la vista ortogonal 2D
        gluOrtho2D(left, right, top, bottom)

    def PrepareRender():
        # Limpiamos el buffer de bits y el de profundidad
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Inicializamos la matriz GL_MODELVIEW
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    @staticmethod
    def DrawPoint(points, size):
        # Configuramos el radio de los puntos
        glPointSize(size)

        # Indicamos que vamos a pintar, en este caso puntos
        glBegin(GL_POINTS)
        glColor3f(0, 255, 255)
        
        for point in points:
            glVertex2f(point.x, point.y)

        glEnd()
    
    @staticmethod
    def MapValue(currMin, currMax, newMin, newMax, value):
        mapFactor = (newMax - newMin) / (currMax - currMin)
        return value * mapFactor
