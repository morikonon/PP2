import pygame
import os

pygame.init()

window_size = (1000, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Музыкальный плеер")

music_dir = "/Users/muhameddaniar/Documents/kbtu/2semester/PP2/lab7/music"
songs = os.listdir(music_dir)
current_song_index = 0

pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))

font = pygame.font.Font(None, 36)
start_text = font.render("Start", True, pygame.Color("black"))
stop_text = font.render("Stop", True, pygame.Color("black"))
next_text = font.render("Next", True, pygame.Color("black"))
prev_text = font.render("Previous", True, pygame.Color("black"))

start_button_rect = start_text.get_rect(center=(window_size[0] // 4, window_size[1] // 2))
stop_button_rect = stop_text.get_rect(center=(window_size[0] * 2 // 4, window_size[1] // 2))
next_button_rect = next_text.get_rect(center=(window_size[0] * 3 // 4, window_size[1] // 2))
prev_button_rect = prev_text.get_rect(center=(window_size[0] // 4, window_size[1] * 3 // 4))

running = True
is_playing = False
while running:
    screen.fill((255, 255, 255))

    screen.blit(start_text, start_button_rect)
    screen.blit(stop_text, stop_button_rect)
    screen.blit(next_text, next_button_rect)
    screen.blit(prev_text, prev_button_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_pos) and not is_playing:
                pygame.mixer.music.play()
                is_playing = True
            elif stop_button_rect.collidepoint(mouse_pos) and is_playing:
                pygame.mixer.music.stop()
                is_playing = False
            elif next_button_rect.collidepoint(mouse_pos):
                current_song_index = (current_song_index + 1) % len(songs)
                pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
                pygame.mixer.music.play()
                is_playing = True
            elif prev_button_rect.collidepoint(mouse_pos):
                current_song_index = (current_song_index - 1) % len(songs)
                pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
                pygame.mixer.music.play()
                is_playing = True

    pygame.display.flip()

pygame.quit()