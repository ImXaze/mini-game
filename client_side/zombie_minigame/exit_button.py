import pygame
from pygame.locals import *

def exit_game():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()

def create_exit_button():
    exit_button = pygame.image.load('exit_button.png')
    exit_button_rect = exit_button.get_rect()
    exit_button_rect.topleft = (10, 10)
    return exit_button, exit_button_rect

def check_exit_button_click(event, exit_button_rect):
    if event.type == MOUSEBUTTONDOWN:
        if exit_button_rect.collidepoint(event.pos):
            exit_game()

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    exit_button, exit_button_rect = create_exit_button()

    while True:
        for event in pygame.event.get():
            check_exit_button_click(event, exit_button_rect)

        screen.blit(exit_button, exit_button_rect.topleft)
        pygame.display.update()

if __name__ == "__main__":
    main()