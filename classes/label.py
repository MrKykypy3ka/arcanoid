import pygame
from classes.area import Area

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self,scr, shift_x=0, shift_y=0):
        self.fill(scr)
        scr.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))