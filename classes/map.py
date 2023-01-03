import pygame
from random import randint, choice, sample
from classes.brick import Brick


class Map():
    def __init__(self, scr, fcolor):
        start_x = 5
        start_y = 5
        count = 9
        self.bricks = []
        self.busters = []

        scr_width, scr_heidth = scr.get_size()

        max = 36
        count_brick = randint(max // 3, max)
        count_buster = randint(count_brick // 3 + 1, count_brick)
        arr_buster = sample(range(0, count_brick), count_buster)
        arr_brick = sample(range(0, max), count_brick)
        index = 0
        for j in range(4):
            y = start_y + (55 * j)
            x = start_x
            for i in range(count):
                if index in arr_brick:
                    if index in arr_buster:
                        buster = choice(['star', 'fast', 'slow', 'triple'])
                        d = Brick('images/brick.png', fcolor, x, y, 50, 50, buster=buster)
                    else:
                        d = Brick('images/brick.png', fcolor, x, y, 50, 50)
                    self.bricks.append(d)
                x = x + 55
                index += 1
            count = count - 1

    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))