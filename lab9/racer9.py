import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Функция для движения врага
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    # Функция для движения игрока
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sizes = [30 , 45, 60]
        self.size = random.choice(self.sizes)
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT - 40))
        self.points = self.calculate_points()

    # Функция для движения монеты
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT - 40))
            self.points = self.calculate_points()

    # Функция для расчета количества очков за монету
    def calculate_points(self):
        if self.size == 30:
            return 1
        elif self.size == 45:
            return 2
        elif self.size == 60:
            return 3
        else:
            return 0

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()  # Создаем группу для врагов
enemies.add(E1)  # Добавляем в нее объект врага
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5     
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):  # Используем метод spritecollideany для группы врагов
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Проверка столкновения игрока с монетой
    coin_collided = pygame.sprite.spritecollideany(P1, coins)
    if coin_collided:
        coins.remove(coin_collided)
        all_sprites.remove(coin_collided)
        SCORE += coin_collided.points


    if len(coins) < 2:
        coin = Coin()
        coins.add(coin)
        all_sprites.add(coin)

    score_text = font_small.render("Score: " + str(SCORE), False, BLACK)
    DISPLAYSURF.blit(score_text, (300, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)