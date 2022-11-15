import sys
import pygame
from time import sleep
from settings import Settings

Green = pygame.image.load("images/bg_green.png")


class WorldCup:

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


    def run_game(self):
        clock = pygame.time.Clock()
        self.update_screen()
        clock.tick(60)

    def update_screen(self):
        screen.fillGreen
        pygame.display.flip()

if __name__ == '__main__':
    ai = WorldCup()
    ai.run_game()
