import pygame
from pygame.sprite import Sprite
import random


class Ball(Sprite):

    def __init__(self, position, velocity):
        super().__init__()
        self.velocity = velocity
        self.image = pygame.image.load("images/ball.png")
        self.rect = self.image.get_rect()
        self.rect.center = position

    def update(self, car1, car2):
        self.rect.x = self.rect.x + self.velocity[0]
        self.rect.y = self.rect.y + self.velocity[1]
        if self.rect.bottom >= 656:
            self.velocity[1] *= -1
            self.rect.bottom = 655
        if self.rect.top <= 128:
            self.velocity[1] *= -1
            self.rect.top = 128
        if self.rect.left <= 0:
            self.velocity[0] *= -1
            self.rect.left = 0
        if self.rect.right >= 1280:
            self.velocity[0] *= -1
            self.rect.right = 1280
        if self.rect.left <= 96 and self.rect.bottom <= 440 and self.rect.top >= 280:
            print(True)
        if self.rect.right >= 1184 and self.rect.bottom <= 440 and self.rect.top >= 280:
            print(True)
        for car in [car1, car2]:
            if car.rect.collidepoint(self.rect.midbottom):
                self.velocity[1] *= -1
                self.rect.bottom = car.rect.top
            if car.rect.collidepoint(self.rect.midright):
                self.velocity[0] *= -1
                self.rect.right = car.rect.left
            if car.rect.collidepoint(self.rect.midtop):
                self.velocity[1] *= -1
                self.rect.top = car.rect.bottom
            if car.rect.collidepoint(self.rect.midleft):
                self.velocity[0] *= -1
                self.rect.left = car.rect.right

    def draw(self):
        self.image.blit(self.image, self.rect)
