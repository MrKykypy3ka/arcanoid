import pygame
from classes.picture import Picture
from random import choice

class Ball(Picture):
    def __init__(self, filename, color, x=0, y=0, width=10, height=10, dx=1, dy=1, speed=3):
        Picture.__init__(self, filename=filename, x=x, y=y, width=width, height=height, color=color)
        self.dx = dx
        self.dy = dy
        self.speed = speed


    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))