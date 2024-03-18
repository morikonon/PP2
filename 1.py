import pygame
import sys
from datetime import datetime
import math

pygame.init()

window_size = (700, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Mickey Clock")

mickey_image = pygame.image.load("mickey2.png")
mickey_rect = mickey_image.get_rect()

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = datetime.now()
    hours = current_time.hour
    minutes = current_time.minute
    seconds = current_time.second

    minute_angle = math.radians(minutes * 6)  
    second_angle = math.radians(seconds * 6)  

    minute_hand = pygame.transform.rotate(mickey_image, -math.degrees(minute_angle))
    second_hand = pygame.transform.rotate(mickey_image, -math.degrees(second_angle))

    screen.fill((255, 255, 255))  
    screen.blit(minute_hand, (window_size[0] // 2 - mickey_rect.width // 2, window_size[1] // 2 - mickey_rect.height // 2))
    screen.blit(second_hand, (window_size[0] // 2 - mickey_rect.width // 2, window_size[1] // 2 - mickey_rect.height // 2))

    pygame.display.flip()

    clock.tick(60)
