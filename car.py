import pygame
from pygame.sprite import Sprite


class Car(Sprite):
    def __init__(self, position, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self, other_car):
        if other_car.rect.collidepoint(self.rect.midright):
            self.moving_right = False
        if other_car.rect.collidepoint(self.rect.midleft):
            self.moving_left = False
        if other_car.rect.collidepoint(self.rect.midtop):
            self.moving_up = False
        if other_car.rect.collidepoint(self.rect.midbottom):
            self.moving_down = False

        # Received assistance from Rachel Huang
        if self.moving_up and self.rect.top > 128:
            self.y -= 5
        if self.moving_down and self.rect.bottom < 656:
            self.y += 5
        if self.moving_right and self.rect.right < 1280:
            self.x += 5
        if self.moving_left and self.rect.left > 0:
            self.x -= 5

        # Update rect object from self.y.
        self.rect.y = self.y
        self.rect.x = self.x

    def draw(self):
        """Draw the ship at its current location."""
        self.image.blit(self.image, self.rect)
