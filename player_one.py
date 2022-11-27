import pygame
from player_two import Car2
from pygame.sprite import Sprite

class Car1(Sprite):
    """A class to manage the ship."""

    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load('images/car_black.png')
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_up and self.rect.top > 128:
            self.y -= 4
        if self.moving_down and self.rect.bottom < 656:
            self.y += 4
        if self.moving_right and self.rect.right < 1280:
            self.x += 4
        if self.moving_left and self.rect.left > 0:
            self.x -= 4

        # Update rect object from self.y.
        self.rect.y = self.y
        self.rect.x = self.x



    def draw(self):
        """Draw the ship at its current location."""
        self.image.blit(self.image, self.rect)
