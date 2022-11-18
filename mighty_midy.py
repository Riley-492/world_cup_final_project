import pygame
import sys
from background import Background

TILE_SIZE = 64
WINDOW_SIZE = 10 * TILE_SIZE
pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
field = pygame.image.load("images/bg_green.png")
field_rect = field.get_rect()
screen_rect = screen.get_rect()

# add an island
background = Background()

num_tiles = screen_rect.width // field_rect.width

clock = pygame.time.Clock()
while True:

    # 1 check for user input (key press, mouse clicks,joystick)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            coordinate = pygame.mouse.get_pos()
            # draw a ship at the x,y coordinate of the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("")
        if event.type == pygame.QUIT:
            sys.exit()

    # update game objects

    # draw the screen
    background.draw()
    pygame.display.flip()
    clock.tick(60)