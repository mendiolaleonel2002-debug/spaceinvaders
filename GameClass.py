import pygame
import os
import sys
import turtle

BULLET_IMAGE = pygame.image.load(os.path.join('img', 'bullet_image.png'))

class Game:

    def __init__(self,font, FPS, lives, window, screen_width, screen_height, bullets = 0, clock = pygame.time.Clock() ):
        self.font =font
        self.HEIGTH = screen_height
        self.WIDTH = screen_width
        self.FPS = FPS
        self.lives = lives
        self.level  = 1
        self.count = 0
        self.window = window
        self.clock = clock
        self.bullets = bullets #aqui
        self.bullet_img = BULLET_IMAGE
        registros = self.leer_registros("puntajes.txt")
        if len(registros) > 0:
            self.jugador, self.max_pun = registros[0] 
        else:
            self.max_pun = 0   

    def escape(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                return False
    def over(self):
        if self.lives <= 0:
            self.count = 0
            while True:
                self.clock.tick(self.FPS)
                lost_label = self.font.render("GAME OVER", 1, (255, 255, 255))
                self.window.blit(lost_label,((self.WIDTH-lost_label.get_width())/2,(self.HEIGTH-lost_label.get_height())/2))
                pygame.display.update()
                self.count += 1
                if self.count == self.FPS * 3:
                    break
            return True #aquí
        else:
            return False
    
    def reload_bullet(self,bullet):
        self.bullets = bullet
    def draw_HUD(self):
        offset = 0
        lives_label = self.font.render(f'Lives: {self.lives}', 1, (255,255,255))
        level_label = self.font.render(f'Level: {self.level}', 1, (255,255,255))
        self.window.blit(lives_label,(10,10))
        self.window.blit(level_label,(self.WIDTH-level_label.get_width()-10, 10))  
        for i in range(self.bullets):
            offset += self.bullet_img.get_width()
            self.window.blit(self.bullet_img, (self.WIDTH-offset, self.HEIGTH-50)) 
    def leer_registros(self, nombre_archivo):
        registros = []
        try:
            with open(nombre_archivo, 'r') as file:
                for line in file:
                    nombre, puntuacion = line.strip().split(",")
                    registros.append((nombre, int(puntuacion)))
                    print(puntuacion)
        except FileNotFoundError:
            print("El archivo no existe")
        
        registros_ordenados = sorted(registros, key = lambda x:x[1], reverse= True)[:5]
        return registros_ordenados