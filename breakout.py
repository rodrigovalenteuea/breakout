import pygame

pygame.init()
pygame.mixer.init()

WIDTH = 893
HEIGHT = 1000
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60

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

paddle_width = 54
paddle_height = 20

def draw_wall():

    pygame.draw.line(screen, GREY, [0, 19], [WIDTH, 19], 40)
    pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
    pygame.draw.line(screen, GREY, [WIDTH - (wall_width / 2) - 1, 0], [WIDTH - (wall_width / 2) - 1, HEIGHT], wall_width)

    pygame.draw.line(screen, BLUE, [0, 300], [(wall_width-1), 300], wall_width)
    pygame.draw.line(screen, BLUE, [WIDTH, 300], [(WIDTH-wall_width), 300], wall_width)

def main(score, balls):
    step = 0
    run = True
    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        draw_wall()
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

main(score, balls)
