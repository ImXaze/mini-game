import pygame
from player_model import ply
from controls import handle_input

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            handle_input(event, ply)

    # Game logic
    ply.update()

    # Draw everything
    screen.fill((0, 0, 0))
    ply.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(FPS)

pygame.quit()