import pygame
from classes.area import Area

class Picture(Area):
    def __init__(self, filename, color, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=color)
        self.image = pygame.image.load(filename)
        self.filename = filename

    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))