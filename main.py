import pygame
from pygame import mixer
import os
from GameClass import Game
from PlayerClass import Player
from EnemyClass import Enemy
from BulletClass import Bullet
from DrawingClass import Drawing

#Background
BACKGROUND = pygame.image.load(os.path.join('img','background.png'))
ICON_IMAGE = pygame.image.load(os.path.join('img','title_icon.png'))
TITLE = 'Space Invaders Hybridge'

#Player:
    #Images
PLAYER_IMAGE = pygame.image.load(os.path.join('img','player_image.png'))
BULLET_IMAGE = pygame.image.load(os.path.join('img','bullet_image.png'))

pygame.init()

#Game Window
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON_IMAGE)

try:
    mixer.music.load('sounds/background_song1.mp3')
except:
    print("No se pudo cargar el sonido de fondo")
    pass

def main():
    puntaje = 0
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    try:
        mixer.music.play(-1)
    except:
        pass

    font = pygame.font.SysFont('cosmicsans', 50)
    game = Game(font, FPS, WIN, WIDTH, HEIGHT, clock)

    player_x = ((WIDTH)-(PLAYER_IMAGE.get_width())) / 2
    player_y = 480
    player = Player(x = player_x, y = player_y, x_speed = 5, y_speed= 4)


    enemy_init = Enemy(speed= 4)
    enemy_wave = 4
    enemies = enemy_init.create(enemy_wave)


    draw = Drawing(WIN)
    draw.drawing(game, player, enemies, FPS=60, puntos=0)

    while run:
        clock.tick(FPS)

        if game.over():
            if puntaje > game.max_pun:
                sound = pygame.mixer.Sound("sounds/ganar.mp3")
                sound.play()
                pantalla = PantallaNombre(puntaje)


                pygame.quit()
            else:
                menu_principal()
                run = False

    

            










