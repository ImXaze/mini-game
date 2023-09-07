import pygame
from pygame.locals import *

pygame.init()

# Set the dimensions of the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Load the background image
background = pygame.image.load('background.jpg')

# Load the exit button image
exit_button = pygame.image.load('exit_button.png')

# Set the position of the exit button
exit_button_pos = (10, 10)

def draw_ui(ply):
    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the player
    ply.draw(screen)

    # Draw the exit button
    screen.blit(exit_button, exit_button_pos)

    # Update the display
    pygame.display.flip()

def check_exit_button(event):
    if event.type == MOUSEBUTTONDOWN:
        if exit_button.get_rect().collidepoint(pygame.mouse.get_pos()):
            pygame.quit()
            sys.exit()

while True:
    for event in pygame.event.get():
        check_exit_button(event)

    draw_ui(ply)