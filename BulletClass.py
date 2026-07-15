import pygame

class Bullet:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
    
    def move(self, speed):
        self.y += speed
    
    def collision(self, obj):
        offset = (int(self.x - obj.x - 30), int(self.y - obj.y - 20))
        return self.mask.overlap(obj.mask, (offset))
