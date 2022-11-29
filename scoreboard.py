import pygame
from pygame.sprite import Sprite
import pygame.font


class Scoreboard(Sprite):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('Times', 48)

    def show_score(self, x, y):
        self.score = self.font.render(f"Score: " + str(self.score), True, self.text_color)
        self.score.blit(self.score, (x, y))
