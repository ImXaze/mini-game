import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Shared dependencies
from player_model import ply
from main import LocalPlayer, SetPos, GetPos

# Control constants
MOVE_SPEED = 5
ROTATE_SPEED = 2

def handle_controls():
    keys = pygame.key.get_pressed()

    # Player movement
    if keys[K_w]:
        ply.SetPos((ply.GetPos()[0], ply.GetPos()[1] - MOVE_SPEED))
    if keys[K_s]:
        ply.SetPos((ply.GetPos()[0], ply.GetPos()[1] + MOVE_SPEED))
    if keys[K_a]:
        ply.SetPos((ply.GetPos()[0] - MOVE_SPEED, ply.GetPos()[1]))
    if keys[K_d]:
        ply.SetPos((ply.GetPos()[0] + MOVE_SPEED, ply.GetPos()[1]))

    # Player rotation
    if keys[K_q]:
        ply.rotate(-ROTATE_SPEED)
    if keys[K_e]:
        ply.rotate(ROTATE_SPEED)

    # Exit game
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    handle_controls()

    pygame.display.update()