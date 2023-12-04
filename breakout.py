import pygame
import random


pygame.init()
pygame.mixer.init()

WIDTH = 600
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

brick_width = 40
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 10
dist_top = 20

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


class Brick:
    def __int__(self, color, level, x, y):
        self.color = color
        self.level = level
        self.x = x
        self.y = y
    def imprimir(self):
        print(self.color)

def draw_wall():
    pygame.draw.line(screen, GREY, [0, 0], [WIDTH, 0], 40)

    pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
    pygame.draw.line(screen, GREY, [WIDTH - (wall_width / 2) - 1, 0], [WIDTH - (wall_width / 2) - 1, HEIGHT],
                     wall_width)

    pygame.draw.line(screen, BLUE, [0, 657], [(wall_width - 1), 657], 35)
    pygame.draw.line(screen, BLUE, [WIDTH, 657], [(WIDTH - wall_width), 657], 35)



def return_brick_list():
    list_bricks = []
    #for i in range(14):
'''
def return_brick_list():
    list_bricks = []

    for j in range(7):
        for i in range(13):
            brick = Brick()
            if j < 2:
                if i == 0:
                    brick.x = wall_width+1
                    brick.y = dist_top
                    brick.level = 1
                    brick.color = RED
                else:
                    brick.x = wall_width + 1
                    brick.y = dist_top + (brick_height*i) + y_gap
                    brick.level = 1
                    brick.color = ORANGE
            else:
                brick.x = wall_width + 1
                brick.y = dist_top + (brick_height * i) + y_gap
                brick.level = 1
                brick.color = BLUE
            #if 1 < j < 4:


            #if 3 < j < 6:


            #if 5 < j < 8:

        list_bricks.append(brick)
    list_bricks.append(brick)
    return list_bricks
'''
def draw_brick_list(list_bricks):
    #i=0
    #brick = pygame.Rect(list_bricks[i].x, list_bricks[i].y, brick_width, brick_height)
    #pygame.draw.rect(screen, list_bricks[i].color, brick)
    for i in list_bricks:
        brick = pygame.Rect(i.x, i.y, brick_width, brick_height)
        pygame.draw.rect(screen, i.color, brick)
      #i.imprimir()
    print(len(list_bricks))


def main(score, balls):
    global ballx, bally
    step = 0
    run = True
    moving_left = False
    moving_right = False
    list_bricks = return_brick_list()


    '''for i in range(14):
        for j in range(9):
            if i==0:
                if j == 0:
                    brick.x = '''



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
        draw_brick_list(list_bricks)
        pygame.draw.rect(screen, BLUE, paddle)
        pygame.draw.rect(screen, WHITE, ball)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


main(score, balls)
