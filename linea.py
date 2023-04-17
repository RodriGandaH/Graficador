import random

ANCHO = 500
ALTO = 500
NEGRO = (0, 0, 0)

class Linea:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.color = NEGRO
        self.posicion_inicial = (random.randint(0, ANCHO), random.randint(0, ALTO))
        self.posicion_final = (random.randint(0, ANCHO), random.randint(0, ALTO))

    def dibujar(self):
        x0, y0 = self.posicion_inicial
        x1, y1 = self.posicion_final

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        if x0 < x1:
            sx = 1
        else:
            sx = -1

        if y0 < y1:
            sy = 1
        else:
            sy = -1

        err = dx - dy

        while True:
            self.pantalla.set_at((x0, y0), self.color)

            if x0 == x1 and y0 == y1:
                break

            e2 = 2 * err

            if e2 > -dy:
                err = err - dy
                x0 = x0 + sx

            if e2 < dx:
                err = err + dx
                y0 = y0 + sy
