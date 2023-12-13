import pygame
import random
import time

pygame.init()
pygame.mixer.init()

# screen adjustments
WIDTH = 632
HEIGHT = 700
size = (WIDTH, HEIGHT)
pygame.display.set_caption("Breakout")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
game_font = pygame.font.Font("fontgame.ttf", 35)
FPS = 75

# colors
WHITE = (255, 255, 255)
GREY = (212, 210, 212)
BLACK = (0, 0, 0)
BLUE = (0, 97, 148)
RED = (162, 8, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)

# some parameters
score = 0
balls = 1
velocity = 2
brick_width = 40
brick_height = 11
x_gap = 4
y_gap = 4
x_gap_init = 10
y_gap_init = 120
speed_brick_yellow = 3
speed_brick_green = 4
speed_brick_orange = 5
speed_brick_red = 6
wall_width = 10
ball = pygame.Rect(WIDTH / 2 - 6, 450, 12, 10)
paddle = pygame.Rect(WIDTH / 2 - 28, 650, 55, 16)
p_speed = 10
ball_speed_x = 0
ball_speed_y = 0
lives = 5
brick_collision = False
cooldown_timer = 0

# sound effects
bounce_wall_sound_effect = pygame.mixer.Sound('assets/sound_collision_wall.wav')
bounce_table_sound_effect = pygame.mixer.Sound('assets/sound_collision_paddle.wav')
bounce_brick_sound_effect = pygame.mixer.Sound('assets/sound_collision_brick.wav')


# ball movement
def ball_move():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 20 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y
        bounce_wall_sound_effect.play()
    if ball.right >= WIDTH - 10 or ball.left <= 10:
        ball_speed_x = -ball_speed_x
        bounce_wall_sound_effect.play()
    if ball.colliderect(paddle):
        if ball_speed_y > 0:
            relative_collision_position = (ball.x + ball.width / 2 - paddle.left) / paddle.width * 2 - 1
            ball_speed_x = ball_speed_x * relative_collision_position
            ball_speed_y = -ball_speed_y
        bounce_table_sound_effect.play()


def draw_wall():
    pygame.draw.line(screen, GREY, [0, 0], [WIDTH, 0], 40)

    pygame.draw.line(screen, GREY, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT], wall_width)
    pygame.draw.line(screen, GREY, [WIDTH - (wall_width / 2) - 1, 0], [WIDTH - (wall_width / 2) - 1, HEIGHT],
                     wall_width)

    pygame.draw.line(screen, BLUE, [0, 657], [(wall_width - 1), 657], 35)
    pygame.draw.line(screen, BLUE, [WIDTH, 657], [(WIDTH - wall_width), 657], 35)

    pygame.draw.line(screen, RED, [(wall_width / 2) - 1, 120],
                     [(wall_width / 2) - 1, 146], wall_width)
    pygame.draw.line(screen, RED, [(WIDTH - wall_width / 2) - 1, 120],
                     [(WIDTH - wall_width / 2) - 1, 146], wall_width)

    pygame.draw.line(screen, ORANGE, [(wall_width / 2) - 1, 150],
                     [(wall_width / 2) - 1, 176], wall_width)
    pygame.draw.line(screen, ORANGE, [(WIDTH - wall_width / 2) - 1, 150],
                     [(WIDTH - wall_width / 2) - 1, 176], wall_width)

    pygame.draw.line(screen, GREEN, [(wall_width / 2) - 1, 180],
                     [(wall_width / 2) - 1, 206], wall_width)
    pygame.draw.line(screen, GREEN, [(WIDTH - wall_width / 2) - 1, 180],
                     [(WIDTH - wall_width / 2) - 1, 206], wall_width)

    pygame.draw.line(screen, YELLOW, [(wall_width / 2) - 1, 210],
                     [(wall_width / 2) - 1, 236], wall_width)
    pygame.draw.line(screen, YELLOW, [(WIDTH - wall_width / 2) - 1, 210],
                     [(WIDTH - wall_width / 2) - 1, 236], wall_width)


# add bricks on a list
def return_brick_list(list_bricks):
    for i in range(8):
        for j in range(14):
            brick_x = x_gap_init + (j * (x_gap + brick_width))
            brick_y = y_gap_init + (i * (y_gap + brick_height))
            brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
            list_bricks.append(brick_rect)
    return list_bricks


def draw_list_brick(list_bricks):
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
    global ball_speed_x, ball_speed_y, lives, brick_collision, cooldown_timer, ball_started, event
    run = True
    moving_left = False
    moving_right = False
    list_bricks = []
    list_bricks = return_brick_list(list_bricks)

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
            if ball_speed_x == 0 and ball_speed_y == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        ball_speed_x = velocity * random.choice((1, -1))
                        ball_speed_y = velocity
                    if event.key == pygame.K_LEFT:
                        ball_speed_x = velocity * random.choice((1, -1))
                        ball_speed_y = velocity

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
                    if (y_hit_index == 210 or y_hit_index == 225) and (ball_speed_y != speed_brick_green
                                                                       and ball_speed_y != speed_brick_orange
                                                                       and ball_speed_y != speed_brick_red

                                                                       and ball_speed_y != -speed_brick_green
                                                                       and ball_speed_y != -speed_brick_orange
                                                                       and ball_speed_y != -speed_brick_red):
                        if ball_speed_y < 0:
                            ball_speed_y = -speed_brick_yellow
                        else:
                            ball_speed_y = speed_brick_yellow
                        if ball_speed_x < 0:
                            ball_speed_x = -speed_brick_yellow
                        else:
                            ball_speed_x = speed_brick_yellow
                    elif (y_hit_index == 180 or y_hit_index == 195) and (ball_speed_y != speed_brick_orange
                                                                         and ball_speed_y != speed_brick_red
                                                                         and ball_speed_y != -speed_brick_orange
                                                                         and ball_speed_y != -speed_brick_red):
                        if ball_speed_y < 0:
                            ball_speed_y = -speed_brick_green
                        else:
                            ball_speed_y = speed_brick_green
                        if ball_speed_x < 0:
                            ball_speed_x = -speed_brick_green
                        else:
                            ball_speed_x = speed_brick_green
                    elif (y_hit_index == 150 or y_hit_index == 165) and (ball_speed_y != speed_brick_red
                                                                         and ball_speed_y != -speed_brick_red):
                        if ball_speed_y < 0:
                            ball_speed_y = -speed_brick_orange
                        else:
                            ball_speed_y = speed_brick_orange
                        if ball_speed_x < 0:
                            ball_speed_x = -speed_brick_orange
                        else:
                            ball_speed_x = speed_brick_orange
                    elif y_hit_index == 120 or y_hit_index == 135:
                        if ball_speed_y < 0:
                            ball_speed_y = -speed_brick_red
                        else:
                            ball_speed_y = speed_brick_red
                        if ball_speed_x < 0:
                            ball_speed_x = -speed_brick_red
                        else:
                            ball_speed_x = speed_brick_red
                    list_bricks.pop(hit_index)
                    ball_speed_y *= -1
                    bounce_brick_sound_effect.play()
                    score += 1
                    brick_collision = True
                    cooldown_timer = 1

        screen.fill(BLACK)
        ball_move()
        draw_wall()
        draw_list_brick(list_bricks)

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
                ball_speed_x = 0
                ball_speed_y = 0
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
        end_text_formatted = game_font.render(end_text, False, (255, 255, 255))
        screen.blit(end_text_formatted, (150, 300))
        pygame.display.update()
        time.sleep(4)
    if score == 112:
        end_text = f"Victory"
        end_text_formatted = game_font.render(end_text, False, (255, 255, 255))
        screen.blit(end_text_formatted, (150, 300))
        pygame.display.update()
        time.sleep(4)


main(score, balls)

