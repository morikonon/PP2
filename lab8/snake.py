import pygame
import sys
from pygame.locals import *
import random

pygame.init()

FPS = 10
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((600, 600))
screen.fill(WHITE)
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 40)

class SnakeSegment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Snake:
    def __init__(self):
        self.segments = []
        self.head = SnakeSegment(300, 300)
        self.segments.append(self.head)
        self.direction = "right"

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.direction != "right":
            self.direction = "left"
        elif keys[K_RIGHT] and self.direction != "left":
            self.direction = "right"
        elif keys[K_UP] and self.direction != "down":
            self.direction = "up"
        elif keys[K_DOWN] and self.direction != "up":
            self.direction = "down"

        dx, dy = 0, 0
        if self.direction == "left":
            dx = -20
        elif self.direction == "right":
            dx = 20
        elif self.direction == "up":
            dy = -20
        elif self.direction == "down":
            dy = 20

        new_head = SnakeSegment(self.head.rect.x + dx, self.head.rect.y + dy)
        self.segments.insert(0, new_head)
        self.head = new_head
        if len(self.segments) > 1:
            self.segments.pop()

    def draw(self, screen):
        for segment in self.segments:
            screen.blit(segment.image, segment.rect)

    def check_collision(self):
        if self.head.rect.left < 0 or self.head.rect.right > screen_width \
                or self.head.rect.top < 0 or self.head.rect.bottom > screen_height:
            return True
        return False


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        self.rect.topleft = (random.randint(0, screen_width - 20), random.randint(0, screen_height - 20))


snake = Snake()
apple = Apple()

clock = pygame.time.Clock()

score = 0
level = 1
speed = 10

def display_score():
    score_text = score_font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

def display_level():
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(level_text, (10, 40))

def check_level():
    global score, level, speed
    if score >= 3 and score % 3 == 0:
        level += 1
        speed += 1

def display_game_over():
    game_over_text = score_font.render("Game Over", True, BLACK)
    screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 20))

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    snake.move()
    if pygame.sprite.collide_rect(snake.head, apple):
        snake.segments.append(SnakeSegment(snake.segments[-1].rect.x, snake.segments[-1].rect.y))
        apple.respawn()
        score += 1
        check_level()

    if snake.check_collision():
        game_over = True

    screen.fill(WHITE)
    snake.draw(screen)
    screen.blit(apple.image, apple.rect)
    display_score()
    display_level()
    pygame.display.update()
    clock.tick(speed)

screen.fill(WHITE)
display_game_over()
pygame.display.update()
pygame.time.wait(2000)
pygame.quit()
sys.exit()