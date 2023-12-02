import pygame

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
wall_width = 16

paddle = pygame.Rect(WIDTH / 2 - 28, 670, 55, 16)
p_speed = 10


def draw_wall():
    pygame.draw.line(screen, GREY, [0, 19], [WIDTH, 19], 40)
    pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
    pygame.draw.line(screen, GREY, [WIDTH - (wall_width / 2) - 1, 0], [WIDTH - (wall_width / 2) - 1, HEIGHT],
                     wall_width)

    pygame.draw.line(screen, BLUE, [0, 300], [(wall_width - 1), 300], wall_width)
    pygame.draw.line(screen, BLUE, [WIDTH, 300], [(WIDTH - wall_width), 300], wall_width)


def main(score, balls):
    step = 0
    run = True
    moving_left = False
    moving_right = False
    paddle_x = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moving_left = True
                elif event.key == pygame.K_RIGHT:
                    moving_right = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moving_left = False
                elif event.key == pygame.K_RIGHT:
                    moving_right = False

        if moving_left:
            paddle.left -= p_speed/2
            paddle_x += -12.5
        if moving_right:
            paddle.right += p_speed/2
            paddle_x += 12.5

        if paddle_x < -500:
            moving_left = False
        elif paddle_x > 500:
            moving_right = False

        screen.fill(bg)
        draw_wall()
        pygame.draw.rect(screen, (255, 255, 255), paddle)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


main(score, balls)
