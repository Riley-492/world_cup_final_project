import pygame
from pygame.sprite import Sprite
import time


class Ball(Sprite):

    def __init__(self, position, velocity):
        super().__init__()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.position = position
        self.velocity = velocity
        self.image = pygame.image.load("images/ball.png")
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.score1 = 0
        self.score2 = 0

    def update(self, car1, car2):

        self.rect.x = self.rect.x + self.velocity[0]
        self.rect.y = self.rect.y + self.velocity[1]
        if self.rect.bottom >= 656:
            self.velocity[1] *= -1
            self.rect.bottom = 655
        if self.rect.top <= 128:
            self.velocity[1] *= -1
            self.rect.top = 128
        if self.rect.left <= 96:
            self.velocity[0] *= -1
            self.rect.left = 96
        if self.rect.right >= 1184:
            self.velocity[0] *= -1
            self.rect.right = 1184

        # Score!!!
        if self.rect.left <= 97 and self.rect.bottom <= 440 and self.rect.top >= 280:
            self.score1 += 1
            time.sleep(1.5)
            self.velocity[0] *= -1
            self.rect.left = 633
            self.rect.top = 375

        if self.rect.right >= 1184 and self.rect.bottom <= 440 and self.rect.top >= 280:
            self.score2 += 1
            time.sleep(1.5)
            self.velocity[0] *= -1
            self.rect.right = 633
            self.rect.top = 375

        # Ball collision with cars(players)
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

    def update_score(self):
        font = pygame.font.SysFont("Times", 46)
        msg = font.render(f"{self.score1} - Score -  {self.score2}", True, [30, 30, 30])
        self.screen.blit(msg, (517, 16))

    def draw(self):
        self.image.blit(self.image, self.rect)
