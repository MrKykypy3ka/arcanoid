import pygame

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = (255, 255, 255)
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def outline(self, scr, frame_color, thickness):
        pygame.draw.rect(scr, frame_color, self.rect, thickness)

    def fill(self, scr):
        pygame.draw.rect(scr, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

    def collidelist(self, rect):
        return self.rect.collidelist(rect)