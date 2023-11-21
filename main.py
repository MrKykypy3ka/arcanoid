import pygame
import sys
from random import random, randint
from time import sleep
from classes.area import Area
from classes.label import Label
from classes.picture import Picture
from classes.map import Map
from classes.ball import Ball

def write_result(name, score):
    try:
        f = open('leader_board.txt', 'r+')
    except:
        f = open('leader_board.txt', 'w+')
    s = ''
    for line in f.readlines():
        player = line.split(',')
        if player[1] == name:
            player[2] = str(int(player[2]) + score) + '\n'
        s += ",".join(player)
    f.close()
    f = open('leader_board.txt', 'w')
    f.write(f'{s}')
    f.close()

def lose_or_win(balls, map):
    if len(balls) == 0:
        time_text = Label(2, 200, 50, 50, back)
        time_text.set_text('Вы проиграли:(', 60, (255, 0, 0))
        time_text.draw(scr, 10, 10)
        return True, False
    elif len(map) == 0:
        time_text = Label(20, 200, 0, 0, back)
        time_text.set_text('Вы выиграли!', 60, (0, 200, 0))
        time_text.draw(scr, 10, 10)
        return True, True
    return False, False

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top
    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

def move_platform(platform, move_right, move_left):
    if move_right:
        platform.rect.x += 5
    if move_left:
        platform.rect.x -= 5
    if -1 > platform.rect.x:
        platform.rect.x = 0
    elif platform.rect.x > 413:
        platform.rect.x = 412

def start(scr):
    scr.fill(back)
    ball_speed = 3
    dx = 1
    dy = -1

    platform_x = 200
    platform_y = 450
    score = 0
    move_right = False
    move_left = False
    game_over = False
    end = False

    balls = [Ball('images/ball.png', back, randint(50, 400), randint(200, 400), 30, 30, dx, dy, ball_speed)]
    platform = Picture('images/platform.png', back, platform_x, platform_y, 88, 22)
    lvl1 = Map(scr, back)

    label_score = Label(420, 480, 127, 60, back)
    label_score.set_text(f'Cчёт: {score}', 14, (0, 0, 255))
    label_score.draw(scr)

    while not game_over and not end:
        for ball in balls:
            ball.fill(scr)
        for m in lvl1.busters:
            m.fill(scr)
        platform.fill(scr)
        label_score.fill(scr)
        label_score.set_text(f'Cчёт: {score}', 14, (0, 0, 255))
        move_platform(platform, move_right, move_left)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_right = True
                if event.key == pygame.K_LEFT:
                    move_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    move_right = False
                if event.key == pygame.K_LEFT:
                    move_left = False
            if event.type == pygame.QUIT:
                return True, False
        for ball in balls:
            ball.rect.x += ball.speed * ball.dx
            ball.rect.y += ball.speed * ball.dy
            if ball.rect.y < 0:
                ball.dy = -ball.dy
            elif ball.rect.x > 470 or ball.rect.x < 0:
                ball.dx = -ball.dx
            elif ball.colliderect(platform.rect) and ball.dy > 0:
                ball.dx, ball.dy = detect_collision(ball.dx, ball.dy, ball.rect, platform.rect)
            for ball2 in balls:
                if ball.colliderect(ball2):
                    ball2.dx, ball2.dy = detect_collision(ball2.dx, ball2.dy, ball2.rect, ball.rect)
                    ball.dx, ball.dy = detect_collision(ball.dx, ball.dy, ball.rect, ball2.rect)
            if ball.rect.y > platform_y + 20:
                balls.remove(ball)
        for m in lvl1.bricks:
            m.draw(scr)
            for ball in balls:
                if m.colliderect(ball.rect):
                    if m.buster != 'None':
                        lvl1.busters.append(Picture('images/'+m.buster + '.png', back, m.x, m.y, 50, 15))
                    score += 10
                    lvl1.bricks.remove(m)
                    m.fill(scr)
                    ball.dx, ball.dy = detect_collision(ball.dx, ball.dy, ball.rect, m.rect)
        for m in lvl1.busters:
            m.rect.y += 2
            if platform.colliderect(m):
                if m.filename == 'images/fast.png':
                    for ball in balls:
                        ball.speed += 1
                elif m.filename  == 'images/slow.png':
                    for ball in balls:
                        ball.speed -= 1
                elif m.filename  == 'images/star.png':
                    score += 100
                elif m.filename == 'images/triple.png':
                    balls.append(Ball('images/ball.png', back, randint(50, 400), randint(200, 400), 30, 30, dx, dy, ball_speed))
                    balls.append(Ball('images/ball.png', back, randint(50, 400), randint(200, 400), 30, 30, dx, dy, ball_speed))
                lvl1.busters.remove(m)
        game_over, win = lose_or_win(balls, lvl1.bricks)
        platform.draw(scr)
        label_score.draw(scr)
        for ball in balls:
            ball.draw(scr)
        for m in lvl1.busters:
            m.draw(scr)
        pygame.display.update()
        clock.tick(60)
    if game_over:
        sleep(3)
        return score, win

def statistic(scr):
    try:
        f = open('leader_board.txt', 'r+')
    except:
        f = open('leader_board.txt', 'w+')
    arr = []
    i = 1
    for line in f.readlines():
        s = ((' ').join(line.split(',')).replace('\n', ''))
        arr.append(Label(100, 30*i, 0, 0, back))
        arr[i-1].set_text(s, 24, (0, 0, 255))
        i += 1
    exit = False
    while not exit:
        scr.fill(back)
        for board in arr:
            board.draw(scr)
            board.fill(scr)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        pygame.display.update()
        clock.tick(60)

def main(scr):
    exit = False
    stat = False

    new_game = Label(100, 100, 127, 60, back)
    new_game.set_text('Игра', 50, (0, 0, 255))

    settings = Label(100, 200, 200, 60, back)
    settings.set_text('Лидеры', 50, (0, 0, 255))

    end_game = Label(100, 300, 170, 60, back)
    end_game.set_text('Выход', 50, (0, 0, 255))

    name = Label(5, 5, 0, 0, back)
    name.set_text('Имя игрока: ', 20, (0, 0, 255))

    font = pygame.font.SysFont(None, 100)
    text = ""
    input_active = True

    while True:
        scr.fill(back)
        new_game.fill(scr)
        new_game.draw(scr)
        settings.fill(scr)
        settings.draw(scr)
        end_game.fill(scr)
        end_game.draw(scr)
        name.draw(scr)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                input_active = True
            elif event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if (x in range(100, 227)) and (y in range(100, 160)) or (x in range(100, 375)) and (
                        y in range(200, 260)) or (x in range(100, 270)) and (y in range(300, 360)):
                    pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                else:
                    pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if new_game.collidepoint(x, y):
                    score, win = start(scr)
                    if win:
                        write_result(text, score)
                elif settings.collidepoint(x, y):
                    statistic(scr)
                elif end_game.collidepoint(x, y):
                    sys.exit()
        name.set_text(f'Имя игрока: {text}', 20, (0, 0, 255))
        name.fill(scr)
        pygame.display.update()
        clock.tick(20)

if __name__ == "__main__":
    pygame.init()
    programIcon = pygame.image.load('images/ball.png')
    pygame.display.set_icon(programIcon)
    pygame.display.set_caption('Arcanoid')
    back = (200, 255, 255)
    scr = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()
    main(scr)

#  пробный комит