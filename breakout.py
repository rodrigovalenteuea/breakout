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

# colors
WHITE = (255, 255, 255)
GREY = (212, 210, 212)
BLACK = (0, 0, 0)
BLUE = (0, 97, 148)

RED = (162, 8, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)

# texts
score = 0
balls = 1
velocity = 4

brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16
paddle_size = 55


# paddle and ball
paddle = pygame.Rect(WIDTH / 2 - 28, 670, paddle_size, 16)
ball = pygame.Rect(WIDTH / 2, 670, 15, 10)

p_speed = 7
ballx = 0
bally = 0
balldirect = pygame.math.Vector2(1, 0)
still_playing = True


def ball_movement():
    global ballx, bally, still_playing
    ball.x += ballx * balldirect.x
    ball.y += bally * balldirect.y
    if ball.right >= WIDTH or ball.left <= 20:
        ballx *= -1
        bally *= -1
    if ball.top <= 40:
        bally *= -1
    if ball.colliderect(paddle):
        balldirect.x *= -1
        balldirect.y = ((paddle.centery - ball.x) / (paddle_size / 2)) * -1
        ballx += 0.25
        bally += 0.25



def draw_wall():
    pygame.draw.line(screen, GREY, [0, 19], [WIDTH, 19], 40)
    pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
    pygame.draw.line(screen, GREY, [WIDTH - (wall_width / 2) - 1, 0], [WIDTH - (wall_width / 2) - 1, HEIGHT],
                     wall_width)

    pygame.draw.line(screen, BLUE, [0, 300], [(wall_width - 1), 300], wall_width)
    pygame.draw.line(screen, BLUE, [WIDTH, 300], [(WIDTH - wall_width), 300], wall_width)


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
            if ballx == 0 or bally == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        ballx, bally = 10, 10

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

        ball_movement()
        screen.fill(bg)
        draw_wall()
        pygame.draw.rect(screen, (255, 255, 255), paddle)
        pygame.draw.rect(screen, (255, 255, 255), ball)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


main(score, balls)
