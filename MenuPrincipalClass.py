import pygame
import sys
import os
from pygame import mixer
# Inicializar Pygame
pygame.init()

class MenuPrincipal:
    # Definir colores
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    ROJO = (255, 0, 0)

    # Configurar la ventana
    ANCHO = 800
    ALTO = 600
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Space Invaders")
    try:
        mixer.music.load('sounds/background_song.mp3')
        
    except:
        print("No se pudo cargar el sonido")
        pass
    try:
        mixer.music.play(-1)
    except:
        pass

    # Directorio de imágenes
    DIR_IMAGENES = "img"
    def __init__(self, init_game_mtd, init_score_mtd, init_about_mtd):
        self.init_game_mtd = init_game_mtd
        self.init_score_mtd = init_score_mtd
        self.init_about_mtd = init_about_mtd
    # Función para cargar imágenes
    def cargar_imagen(self, nombre_archivo):
        ruta = os.path.join(self.DIR_IMAGENES, nombre_archivo)
        return pygame.image.load(ruta).convert_alpha()

    # Función para mostrar texto en la pantalla
    def mostrar_texto(self,texto, font, color, superficie, x, y):
        texto_objeto = font.render(texto, True, color)
        rectangulo_texto = texto_objeto.get_rect()
        rectangulo_texto.center = (x, y)
        superficie.blit(texto_objeto, rectangulo_texto)
        return rectangulo_texto

    # Función para el menú principal
    def menu_principal(self):
        opciones = ["Iniciar juego", "Puntajes", "Acerca de"]
        opcion_seleccionada = 0
        selector_rect = pygame.Rect(0, 0, 300, 50)

        # Cargar imagen de fondo
        fondo = self.cargar_imagen("menu_fondo.jpg")
        fondo = pygame.transform.scale(fondo, (self.ANCHO, self.ALTO))

        # Cargar imagen entre el subtítulo y las opciones del menú
        imagen = self.cargar_imagen("hybridge.gif")
        imagen = pygame.transform.scale(imagen, (80, 80))

        while True:
            self.ventana.blit(fondo, (0, 0))
            self.mostrar_texto("Space Invaders", pygame.font.Font(None, 64), self.BLANCO, self.ventana, self.ANCHO // 2, self.ALTO // 4)

            self.mostrar_texto("Hybridge", pygame.font.Font(None, 36), self.BLANCO, self.ventana, (self.ANCHO // 2), self.ALTO // 4 + 40)

            # Mostrar imagen debajo del subtítulo
            self.ventana.blit(imagen, (self.ANCHO // 2 - 40, self.ALTO // 4 + 60))


            # Mostrar opciones del menú y calcular rectángulos de texto
            rectangulos_texto = []
            for i, opcion in enumerate(opciones):
                rect_texto = self.mostrar_texto(opcion, pygame.font.Font(None, 32), self.BLANCO, self.ventana, self.ANCHO // 2, self.ALTO // 4 + 90 * (i + 1) + 100)
                rectangulos_texto.append(rect_texto)

            # Calcular la posición del rectángulo selector
            selector_rect.centerx = self.ANCHO // 2
            selector_rect.centery = rectangulos_texto[opcion_seleccionada].centery - 10

            # Dibujar rectángulo selector
            pygame.draw.rect(self.ventana, self.ROJO, selector_rect, 2)

            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        print("("+str(opcion_seleccionada)+ "-1)" + "%" + str(len(opciones)) + "=" + str((opcion_seleccionada - 1) % len(opciones)))
                        opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)
                    elif evento.key == pygame.K_DOWN:
                        print("("+str(opcion_seleccionada)+ "+1)" + "%" + str(len(opciones)) + "=" + str((opcion_seleccionada + 1) % len(opciones)))
                        opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
                    elif evento.key == pygame.K_RETURN:
                        opcion_elegida = opciones[opcion_seleccionada]
                
                        if(opcion_elegida.lower() == "iniciar juego"):
                            print("opción iniciar juego")
                            
                            self.init_game_mtd()
                            pygame.quit()
                        elif(opcion_elegida.lower() == "puntajes"):
                            print("opción puntaje")
                            self.init_score_mtd()
                            pygame.quit()
                        elif(opcion_elegida.lower() == "acerca de"):
                            print("opción acerca de")
                            self.init_about_mtd()
                            pygame.quit()
                        else:
                            print("otro")
