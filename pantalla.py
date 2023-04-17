import pygame
from linea import Linea

ANCHO = 500
ALTO = 500
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

class Pantalla:
    def __init__(self):
        self.dimensiones = (ANCHO, ALTO)
        self.pantalla = pygame.display.set_mode(self.dimensiones)
        self.linea_boton = pygame.Rect(10, 10, 100, 25)
        self.linea_boton_color = (92, 102, 119)
        self.linea = None

    def ejecutar(self):
        pygame.init()
        pygame.display.set_caption("Graficador")

        ejecutando = True
        while ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.linea_boton.collidepoint(evento.pos):
                        self.linea = Linea(self.pantalla)
                        self.linea.dibujar()

            self.pantalla.fill(BLANCO)
            pygame.draw.rect(self.pantalla, self.linea_boton_color, self.linea_boton, border_radius=5)
            fuente = pygame.font.SysFont(None, 24)
            texto = fuente.render("Linea", True, BLANCO)
            # Calcular posición vertical
            x = self.linea_boton.centerx - texto.get_width() // 2
            y = self.linea_boton.centery - texto.get_height() // 2
            self.pantalla.blit(texto, (x, y))

            if self.linea:
                self.linea.dibujar()

            pygame.display.flip()
            

        pygame.quit()

