import pygame
from player_one import Car1
from pygame.sprite import Sprite
global x_speed, y_speed


class Ball(Sprite):

    def __init__(self, position, velocity, startdir):
        super().__init__()
        self.pos = pygame.math.Vector2(position)
        self.velocity = velocity
        self.dir = pygame.math.Vector2(startdir).normalize()
        self.image = pygame.image.load("images/ball.png")
        self.rect = self.image.get_rect(center=(round(self.pos.x), round(self.pos.y)))

    def reflect(self, nv):
        self.dir = self.dir.reflect(pygame.math.Vector2(nv))

    def update(self, car1, car2):
        self.pos += self.dir * 4
        self.rect.center = round(self.pos.x), round(self.pos.y)

        if self.rect.left <= 0:
            self.reflect((1, 0))
            self.rect.left = 0
        if self.rect.right >= 1280:
            self.reflect((-1, 0))
            self.rect.right = 1280
        if self.rect.top <= 128:
            self.reflect((0, 1))
            self.rect.top = 128
        if self.rect.bottom >= 656:
            self.reflect((0, -1))
            self.rect.bottom = 656
        if pygame.sprite.collide_rect(car1, self):
            self.reflect((0, -1))
            self.reflect((1, 0))
        if pygame.sprite.collide_rect(car2, self):
            self.reflect((0, -1))
            self.reflect((1, 0))
        if self.rect.left <= 96 and self.rect.bottom <= 440 and self.rect.top >= 280:
            self.reflect((-1, 0))
        if self.rect.right >= 1184 and self.rect.bottom <= 440 and self.rect.top >= 280:
            self.reflect((1, 0))

    def draw(self):
        self.image.blit(self.image, self.rect)
