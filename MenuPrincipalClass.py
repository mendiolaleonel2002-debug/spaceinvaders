from DrawingClass import WIDTH
import pygame
import sys
import os
from pygame import mixer

pygame.init()

class MenuPrincipal:
    BLANCO = (255, 255, 255)
    NEGRO = (0,0,0)
    ROJO = (255, 0, 0)

    WIDTH = 800
    HEIGHT = 600

    ventana = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders Hybridge")
    try:
        mixer.music.load('sounds/background_song.mp3')
    except:
        print("No se pudo cargar el archivo de audio")

    try:
        mixer.music.play(-1)
    except:
        pass

    DIR_IMAGES = "img"
    def __init__(self, init_game, init_score_mtd, init_about_mtd):
        self.init_game = init_game
        self.init_score_mtd = init_score_mtd
        self.init_about_mtd = init_about_mtd

        

        

    
    