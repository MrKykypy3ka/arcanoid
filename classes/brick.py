import pygame
from classes.picture import Picture
from random import choice

class Brick(Picture):
    def __init__(self, filename, color, x=0, y=0, width=10, height=10, buster="None"):
        Picture.__init__(self, filename=filename, x=x, y=y, width=width, height=height, color=color)
        self.buster = buster

    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))