import pygame
import os
import random
from ShipClass import Ship

current_dir = os.path.dirname(__file__)

#Definir las rutas completas de las imagenes
BULLET_IMG = pygame.image.load(os.path.join('img', 'bullet_img.png'))
ENEMY_BLUE_IMAGE = pygame.image.load(os.path.join(current_dir, 'img', 'enemy_blue_image.png'))
ENEMY_GREEN_IMAGE = pygame.image.load(os.path.join(current_dir, 'img', 'enemy_green_image.png'))
ENEMY_PURPLE_IMAGE = pygame.image.load(os.path.join(current_dir, 'img', 'enemy_purple_image.png'))
SHOT_BLUE_IMAGE = pygame.image.load(os.path.join(current_dir, 'img', 'shot_blue_image.png'))
SHOT_GREEN_IMAGE = pygame.image.load(os.path.join(current_dir, 'img', 'shot_green_image.png'))
SHOT_PURPLE_IMAGE = pygame.image.load(os.path.join(current_dir, 'img', 'shot_purple_image.png'))

class Enemy(Ship):
    COLOR = {
        'blue': (ENEMY_BLUE_IMAGE, SHOT_BLUE_IMAGE),
        'green': (ENEMY_GREEN_IMAGE, SHOT_GREEN_IMAGE),
        'purple': (ENEMY_PURPLE_IMAGE, SHOT_PURPLE_IMAGE)
    }

    def __init__(self, speed, x=50, y=50, color='blue', health=100):
        super().__init__(x,y,health)
        self.ship_img, self.bullet_img = self.COLOR[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.speed = speed

    def move(self):
        self.y += self.speed

    def create(self, amount):
        enemies = []
        for i in range(amount):
            enemy = Enemy(x=random.randrange(20, WIDTH - ENEMY_BLUE_IMAGE.get_width() - 20),
                          y=random.randrange(-1000, -100),
                          color=random.choice(['blue', 'green', 'purple']),
                          speed=self.speed)
            enemies.append(enemy)
        return enemies

    def increase_speed(self):
        self.speed *= 1.02

def main():
    run = True
    clock = pygame.time.Clock()
    enemies = Enemy(1).create(5)

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for enemy in enemies:
            enemy.move()

        WIN.fill((0,0,0))
        for enemy in enemies:
            enemy.draw(WIN)
        pygame.display.update()

    pygame.quit()

WIDTH, HEIGHT = 800, 600