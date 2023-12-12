import pygame
import random
import time

pygame.init()
pygame.mixer.init()

WIDTH = 632
HEIGHT = 700
size = (WIDTH, HEIGHT)
pygame.display.set_caption("Breakout")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
game_font = pygame.font.Font("fontgame.ttf", 35)
end_text = f"Game over"

FPS = 75
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
velocity = 2

brick_width = 40
brick_height = 11
x_gap = 4
y_gap = 4
x_gap_init = 10
y_gap_init = 120
wall_width = 10
dist_top = 20

velocity_yellow = 3
velocity_green = 4
velocity_orange = 5
velocity_red = 6

ball = pygame.Rect(WIDTH / 2 - 6, 450, 12, 10)
paddle = pygame.Rect(WIDTH / 2 - 28, 650, 55, 16)
p_speed = 10
ballx = 0
bally = 0
lives = 5
brick_collision = False
cooldown_timer = 0


def ballmove():
    global ballx, bally
    ball.x += ballx
    ball.y += bally
    if ball.top <= 20 or ball.bottom >= HEIGHT:
        bally = -bally
    if ball.right >= WIDTH - 10 or ball.left <= 10:
        ballx = -ballx
    if ball.colliderect(paddle):
        if bally > 0:
            relative_collision_position = (ball.x + ball.width / 2 - paddle.left) / paddle.width * 2 - 1
            ballx = ballx * relative_collision_position
            bally = -bally
    # ballx = max(-5, min(5, ballx))
    # bally = max(-5, min(5, bally))


def draw_wall():
    pygame.draw.line(screen, GREY, [0, 0], [WIDTH, 0], 40)

    pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
    pygame.draw.line(screen, GREY, [WIDTH - (wall_width / 2) - 1, 0], [WIDTH - (wall_width / 2) - 1, HEIGHT],
                     wall_width)

    pygame.draw.line(screen, BLUE, [0, 657], [(wall_width - 1), 657], 35)
    pygame.draw.line(screen, BLUE, [WIDTH, 657], [(WIDTH - wall_width), 657], 35)


def return_brick_list(list_bricks):
    for i in range(8):
        for j in range(14):
            brick_x = x_gap_init + (j * (x_gap + brick_width))
            brick_y = y_gap_init + (i * (y_gap + brick_height))
            brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
            list_bricks.append(brick_rect)
    return list_bricks


def draw_list_brick2(list_bricks):
    for i in list_bricks:
        if i.y == 120 or i.y == 135:
            pygame.draw.rect(screen, RED, i)
        elif i.y == 150 or i.y == 165:
            pygame.draw.rect(screen, ORANGE, i)
        elif i.y == 180 or i.y == 195:
            pygame.draw.rect(screen, GREEN, i)
        elif i.y == 210 or i.y == 225:
            pygame.draw.rect(screen, YELLOW, i)


def main(score, balls):
    global ballx, bally, lives, end_text, brick_collision, cooldown_timer, ball_started, event
    step = 0
    run = True
    moving_left = False
    moving_right = False
    game_over = False
    list_bricks = []
    list_bricks = return_brick_list(list_bricks)

    while run:
        print(bally)
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
                        ballx = velocity * random.choice((1, -1))
                        bally = velocity

                    if event.key == pygame.K_LEFT:
                        ballx = velocity * random.choice((1, -1))
                        bally = velocity
        if moving_left:
            paddle.left -= p_speed
        if moving_right:
            paddle.right += p_speed

        if paddle.x < 10:
            paddle.x = 10
        elif paddle.x + 55 > WIDTH - 10:
            paddle.x = WIDTH - 55 - 10

        if not brick_collision:
            if cooldown_timer <= 0:
                hit_index = ball.collidelist(list_bricks)
                if hit_index != -1:
                    y_hit_index = list_bricks[hit_index].y
                    if (y_hit_index == 210 or y_hit_index == 225) and (bally != velocity_green
                                                                       and bally != velocity_orange
                                                                       and bally != velocity_red

                                                                       and bally != -velocity_green
                                                                       and bally != -velocity_orange
                                                                       and bally != -velocity_red):
                        if bally < 0:
                            bally = -velocity_yellow
                        else:
                            bally = velocity_yellow
                        if ballx < 0:
                            ballx = -velocity_yellow
                        else:
                            ballx = velocity_yellow
                    elif (y_hit_index == 180 or y_hit_index == 195) and (bally != velocity_orange
                                                                         and bally != velocity_red
                                                                         and bally != -velocity_orange
                                                                         and bally != -velocity_red):
                        if bally < 0:
                            bally = -velocity_green
                        else:
                            bally = velocity_green
                        if ballx < 0:
                            ballx = -velocity_green
                        else:
                            ballx = velocity_green
                    elif (y_hit_index == 150 or y_hit_index == 165) and (bally != velocity_red
                                                                         and bally != -velocity_red):
                        if bally < 0:
                            bally = -velocity_orange
                        else:
                            bally = velocity_orange
                        if ballx < 0:
                            ballx = -velocity_orange
                        else:
                            ballx = velocity_orange
                    elif (y_hit_index == 120 or y_hit_index == 135):
                        if bally < 0:
                            bally = -velocity_red
                        else:
                            bally = velocity_red
                        if ballx < 0:
                            ballx = -velocity_red
                        else:
                            ballx = velocity_red
                    list_bricks.pop(hit_index)
                    bally *= -1
                    score += 1
                    brick_collision = True
                    cooldown_timer = 1
        screen.fill(bg)
        ballmove()
        draw_wall()
        draw_list_brick2(list_bricks)
        # lives and game over system
        if ball.y > paddle.y:
            lives -= 1
            if lives < 1:
                run = False
            else:
                ball.x = WIDTH // 2 - 6
                ball.y = 450
                paddle.x = WIDTH // 2 - 28
                paddle.y = 650
                ballx = 0
                bally = 0
                ball_started = False

        pygame.draw.rect(screen, BLUE, paddle)
        pygame.draw.rect(screen, WHITE, ball)
        live_text = game_font.render(f"{lives}", False, (255, 255, 255))
        screen.blit(live_text, (450, 25))
        score_text = game_font.render(f"{score}", False, WHITE)
        screen.blit(score_text, (100, 25))
        pygame.display.update()
        clock.tick(FPS)

        if brick_collision:
            if score == 112:
                run = False
            cooldown_timer -= clock.get_time() / 1000
            if cooldown_timer <= 0:
                brick_collision = False

    screen.fill((0, 0, 0))

    if lives < 1:
        end_text = f"Game over"
        end_text_formated = game_font.render(end_text, False, (255, 255, 255))
        screen.blit(end_text_formated, (150, 300))
        pygame.display.update()
        time.sleep(4)
    if score == 112:
        end_text = f"Victory"
        end_text_formated = game_font.render(end_text, False, (255, 255, 255))
        screen.blit(end_text_formated, (150, 300))
        pygame.display.update()
        time.sleep(4)

main(score, balls)
