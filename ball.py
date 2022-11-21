import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    MAX_VEL = 5

    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("images/ball.png")
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def draw(self):
        self.image.blit(self.image, self.rect)
