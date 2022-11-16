import sys
import pygame
from background import Crowd
TILE_SIZE = 64
WINDOW_SIZE = 15 * TILE_SIZE
pygame.init()

screen = pygame.display.set_mode((1024, 640))  # pygame.FULLSCREEN)
green = pygame.image.load("images/bg_green.png")

green_rect = green.get_rect()
screen_rect = screen.get_rect()

num_tiles = screen_rect.width // green_rect.width

crowd = Crowd()
crowd.move((576, 0))

def draw_background():
    # screen is square so same number of tiles in row and col
    for y in range(num_tiles):
        for x in range(num_tiles):
            screen.blit(green, (x * green_rect.width, y * green_rect.height))


clock = pygame.time.Clock()
coordinate = (0, 0)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_background()
    pygame.display.flip()
    clock.tick(60)



