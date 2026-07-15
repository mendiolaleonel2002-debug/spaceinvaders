import pygame
import os
import sys
import turtle

BULLET_IMAGE = pygame.image.load(os.path.join('img','bullet_image.png'))

class Game:
    def __init__(self, font, FPS, count, window, lives, screen_width, screen_height, bullets = 0, clock = pygame.time.Clock()):
        self.font = font
        self.window = window
        self.HEIGHT = screen_height
        self.WIDTH = screen_width
        self.bullets = bullets
        self.bullet_image = BULLET_IMAGE
        self.lives = lives
        self.FPS = FPS
        

    def escape(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                return False
    
    def over(self):
        if self.lives <=0:
            self.count = 0
            while True:
                self.clock.tick(self.FPS)
                lost_label = self.font.render('Game Over', 1, (255, 255, 255))
                self.window.blit(lost_label,((self.WIDTH-lost_label.get_width())/2,(self.HEIGTH-lost_label.get_height())/2))
                pygame.display.update()
                self.count +=1
                if self.count == self.FPS * 3:
                    break
            return True
        else:
            return False

                
                

        
        
        
