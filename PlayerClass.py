import pygame
import sys
import os
from ShipClass import Ship
from BulletClass import Bullet

PLAYER_IMG = pygame.image.load(os.path.joni('img', 'player_img.png'))
BULLET_IMG = pygame.image.load(os.path.joni('img', 'bullet_img.png'))

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = PLAYER_IMG
        self.bullet_img = BULLET_IMG
        self.max_health = health


    
        
        
        
