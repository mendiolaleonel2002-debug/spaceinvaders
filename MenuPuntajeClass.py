import pygame
import sys
import os

# Definir la clase MenuPuntajes
class MenuPuntajes:
    # Definir colores
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    GRIS = (200, 200, 200)
    ROJO = (255, 0, 0)

    # Configurar la ventana
    ANCHO = 800
    ALTO = 600
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Mejores Puntajes")
    def __init__(self, back_mtd):
        self.back_mtd = back_mtd
    # Función para cargar puntajes desde un archivo de texto
    def cargar_puntajes(self, archivo):
        puntajes = []
        try:
            with open(archivo, 'r') as file:
                for line in file:
                    nombre, puntaje = line.strip().split(',')
                    puntajes.append((nombre, int(puntaje)))
        except FileNotFoundError:
            print(f"No se encontró el archivo {archivo}")
        return sorted(puntajes, key=lambda x: x[1], reverse=True)[:5]

    # Función para cargar imágenes
    def cargar_imagen(self, nombre_archivo):
        ruta = os.path.join("img", nombre_archivo)
        return pygame.image.load(ruta).convert_alpha()

    # Función para mostrar texto en la pantalla
    def mostrar_texto(self, texto, font, color, superficie, x, y):
        texto_objeto = font.render(texto, True, color)
        rectangulo_texto = texto_objeto.get_rect()
        rectangulo_texto.center = (x, y)
        superficie.blit(texto_objeto, rectangulo_texto)

    # Función para dibujar un botón
    def dibujar_boton(self, texto, font, color, superficie, x, y, ancho, alto):
        pygame.draw.rect(superficie, color, (x, y, ancho, alto))
        self.mostrar_texto(texto, font, self.NEGRO, superficie, x + ancho / 2, y + alto / 2)

    # Función para mostrar los mejores puntajes en la pantalla
    def mostrar_puntajes(self, puntajes):
        self.ventana.fill(self.NEGRO)

        # Cargar imagen de fondo
        fondo = self.cargar_imagen("menu_fondo.jpg")
        fondo = pygame.transform.scale(fondo, (self.ANCHO, self.ALTO))
        self.ventana.blit(fondo, (0, 0))

        # Mostrar título
        self.mostrar_texto("Mejores Puntajes", pygame.font.Font(None, 48), self.BLANCO, self.ventana, self.ANCHO // 2, 50)

        # Mostrar subtítulo de juego
        self.mostrar_texto("Space Invaders Hybridge", pygame.font.Font(None, 36), self.BLANCO, self.ventana, self.ANCHO // 2, 120)

        if not puntajes:
            self.mostrar_texto("Aún no hay registros", pygame.font.Font(None, 36), self.ROJO, self.ventana, self.ANCHO // 2, self.ALTO // 2)
        else:
            # Mostrar puntajes
            y_offset = 250
            for i, (nombre, puntaje) in enumerate(puntajes, 1):
                color_texto = self.BLANCO if i == 1 else self.ROJO
                font_size = 42 if i == 1 else 36  # Tamaño de fuente más grande para el primer registro
                self.mostrar_texto(f"{i}. {nombre}: {puntaje}", pygame.font.Font(None, font_size), color_texto, self.ventana, self.ANCHO // 2, y_offset)
                y_offset += 60

        # Dibujar botón de volver atrás
        self.dibujar_boton("<", pygame.font.Font(None, 36), self.GRIS, self.ventana, 20, 20, 50, 50)

        pygame.display.update()

    # Función principal para ejecutar la pantalla de puntajes
    def ejecutar(self):
        puntajes = self.cargar_puntajes("puntajes.txt")  # Nombre del archivo de puntajes
        self.mostrar_puntajes(puntajes)

        # Loop principal
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # 1 es el botón izquierdo del mouse
                        x, y = event.pos
                        if 20 <= x <= 70 and 20 <= y <= 70:  # Coordenadas del botón de volver atrás
                            print("acción atrás")  # Imprimir "acción atrás" al hacer clic en el botón
                            self.back_mtd()
                            pygame.quit()

# Inicializar Pygame
pygame.init()
    