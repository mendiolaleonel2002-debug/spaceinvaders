import pygame
from pygame import mixer
import os

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