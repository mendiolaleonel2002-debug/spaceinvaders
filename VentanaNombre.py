import pygame
import sys
import os
class PantallaNombre:
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    GRIS = (200, 200, 200)

    ANCHO = 800
    ALTO = 600

    def __init__(self, puntaje,finish_mtd):
        pygame.init()
        self.ventana = pygame.display.set_mode((self.ANCHO, self.ALTO))
        pygame.display.set_caption("Ingresar Nombre")
        self.fuente_titulo = pygame.font.Font(None, 30)
        self.fuente_subtitulo = pygame.font.Font(None, 36)
        self.fuente_input = pygame.font.Font(None, 36)
        self.texto_input = ""
        self.input_active = False
        self.fondo = self.cargar_imagen("menu_fondo.jpg")
        self.puntaje = puntaje
   


        titulo_texto = "Felicidades! Haz superado el máximo puntaje. Por favor, ingresa tu nombre:"
        titulo_render = self.fuente_titulo.render(titulo_texto, True, self.BLANCO)
        titulo_rect = titulo_render.get_rect(center=(self.ANCHO/2, 50))

        subtitulo_texto = "Space Invaders Hybridge"
        subtitulo_render = self.fuente_subtitulo.render(subtitulo_texto, True, self.BLANCO)
        subtitulo_rect = subtitulo_render.get_rect(center=(self.ANCHO/2, 100))

        input_box = pygame.Rect(200, 200, 400, 50)

        boton_aceptar = pygame.Rect(300, 300, 200, 50)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        self.input_active = not self.input_active
                    else:
                        self.input_active = False
                if event.type == pygame.KEYDOWN:
                    if self.input_active:
                        if event.key == pygame.K_RETURN:
                            nombre = self.texto_input.strip() if self.texto_input.strip() else "Jugador"
                            print("Texto ingresado:", nombre)
                            self.escribir_en_archivo("puntajes.txt", f"{nombre},{self.puntaje}")
                            finish_mtd()
                            pygame.quit()
                            return
                        elif event.key == pygame.K_BACKSPACE:
                            self.texto_input = self.texto_input[:-1]
                        else:
                            self.texto_input += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_aceptar.collidepoint(event.pos):
                        nombre = self.texto_input.strip() if self.texto_input.strip() else "Jugador"
                        print("Texto ingresado:", nombre)
                        self.escribir_en_archivo("puntajes.txt", f"{nombre},{self.puntaje}")
                        finish_mtd()
                        pygame.quit()
                        return

            self.ventana.blit(self.fondo, (0, 0))

            pygame.draw.rect(self.ventana, self.NEGRO, titulo_rect)
            self.ventana.blit(titulo_render, titulo_rect)

            pygame.draw.rect(self.ventana, self.NEGRO, subtitulo_rect)
            self.ventana.blit(subtitulo_render, subtitulo_rect)

            color_input = self.GRIS if not self.input_active else self.BLANCO
            pygame.draw.rect(self.ventana, color_input, input_box, 2)
            texto_superficie = self.fuente_input.render(self.texto_input, True, self.BLANCO)
            self.ventana.blit(texto_superficie, (input_box.x + 5, input_box.y + 5))

            pygame.draw.rect(self.ventana, self.GRIS, boton_aceptar)
            texto_boton = self.fuente_input.render("Aceptar", True, self.NEGRO)
            texto_boton_rect = texto_boton.get_rect(center=boton_aceptar.center)
            self.ventana.blit(texto_boton, texto_boton_rect)

            pygame.display.flip()

    
    def cargar_imagen(self, nombre_archivo):
        ruta = os.path.join("img", nombre_archivo)
        return pygame.transform.scale(pygame.image.load(ruta).convert(), (self.ANCHO, self.ALTO))

    def escribir_en_archivo(self, nombre_archivo, contenido):
        directorio_trabajo = os.getcwd()
        ruta = os.path.join(directorio_trabajo, nombre_archivo)

        try:
            with open(ruta, 'a') as archivo:
                archivo.write(contenido + '\n')

        except PermissionError:
            print(f"No tiene permisos para escribir en el directorio '{os.path.dirname(ruta)}'")
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")

def finish():
    print("Fin del programa")


    
                        


        

        

