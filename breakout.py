import pygame
import random


pygame.init()
pygame.mixer.init()

WIDTH = 500
HEIGHT = 700
size = (WIDTH, HEIGHT)
pygame.display.set_caption("Breakout")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60
bg = (0, 0, 0)

WHITE = (255, 255, 255)
GREY = (212, 210, 212)
BLACK = (0, 0, 0)
BLUE = (0, 97, 148)

RED = (162, 8, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)

score = 0
balls = 1
velocity = 4

brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 10

ball = pygame.Rect(WIDTH / 2 - 6, 600, 15, 10)
paddle = pygame.Rect(WIDTH / 2 - 28, 650, 55, 16)
p_speed = 10
ballx = 0
bally = 0


def ballmove():
    global ballx, bally
    ball.x += ballx
    ball.y += bally
    if ball.top <= 20 or ball.bottom >= HEIGHT:
        bally *= -1
    if ball.right >= WIDTH - 10 or ball.left <= 10:
        ballx *= -1
    if ball.colliderect(paddle):
        if ball.right >= paddle.left and ball.left <= paddle.right:
            if ball.bottom >= paddle.top >= ball.top:
                bally *= -1
                ball.y = paddle.top - ball.height
            elif ball.top <= paddle.bottom <= ball.bottom:
                bally *= -1
                ball.y = paddle.bottom
            else:
                ballx *= -1


def draw_wall():
    pygame.draw.line(screen, GREY, [0, 0], [WIDTH, 0], 40)

    pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
    pygame.draw.line(screen, GREY, [WIDTH - (wall_width / 2) - 1, 0], [WIDTH - (wall_width / 2) - 1, HEIGHT],
                     wall_width)

    pygame.draw.line(screen, BLUE, [0, 657], [(wall_width - 1), 657], 35)
    pygame.draw.line(screen, BLUE, [WIDTH, 657], [(WIDTH - wall_width), 657], 35)


def main(score, balls):
    global ballx, bally
    step = 0
    run = True
    moving_left = False
    moving_right = False
    paddle_x = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moving_left = True
                elif event.key == pygame.K_RIGHT:
                    moving_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moving_left = False
                elif event.key == pygame.K_RIGHT:
                    moving_right = False
            if ballx == 0 and bally == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        ballx = 7 * random.choice((1, -1))
                        bally = 7 * random.choice((1, -1))

                    if event.key == pygame.K_LEFT:
                        ballx = 7 * random.choice((1, -1))
                        bally = 7 * random.choice((1, -1))

        if moving_left:
            paddle.left -= p_speed / 2
        if moving_right:
            paddle.right += p_speed / 2

        if paddle.x < 10:
            paddle.x = 10
        elif paddle.x + 55 > WIDTH - 10:
            paddle.x = WIDTH - 55 - 10


        screen.fill(bg)
        ballmove()
        draw_wall()
        pygame.draw.rect(screen, BLUE, paddle)
        pygame.draw.rect(screen, WHITE, ball)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


main(score, balls)
