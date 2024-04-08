import pygame
import sys

pygame.init()
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
color = BLACK

width = 600
height = 600

screen = pygame.display.set_mode((width, height))
screen.fill(WHITE)
pygame.display.set_caption("Paint")

drawing = False
position = None
rad = 20
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            position = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            position = None
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                mouse_pos = event.pos
                pygame.draw.line(screen, color, position, mouse_pos, rad)
                position = mouse_pos

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_a]:
        color = BLUE
        rad = 20
    elif pressed_key[pygame.K_q]:
        color = RED
        rad = 20
    elif pressed_key[pygame.K_z]:
        color = GREEN
        rad = 20
    elif pressed_key[pygame.K_w]:
        color = WHITE
        rad = 40

    pygame.display.flip()

sys.exit()
pygame.quit()