import pygame
from pygame.sprite import Sprite

class Background(Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.surface.Surface((width, height)) # screen_height, screen_width

        self.bg_image = pygame.image.load("images/bg_green.png")
        self.bg_image_rect = self.bg_image.get_rect()
        self.num_tiles = width // self.bg_image_rect.width
        self.fans = pygame.image.load("images/fans.png")
        self.fans_rect = self.fans.get_rect()
        for y in range(self.num_tiles):
            for x in range(self.num_tiles):
                self.image.blit(self.bg_image, (x*self.bg_image_rect.width, y*self.bg_image_rect.height))

        self.fans_width = width // self.fans_rect.width

        for y in range(self.fans_width):
            for x in range(self.fans_width):
                self.image.blit(self.fans, (x*self.fans_rect.width, self.fans_rect.height))

        self.fans_up = pygame.image.load("images/fans_up.png")
        self.fans_up_rect = self.fans_up.get_rect()
        self.fans_up_width = width // self.fans_up_rect.width
        for y in range(656, 720, 64):
            for x in range(0, 1200, 128):
                self.image.blit(self.fans_up, (x, y))

        self.rect = self.image.get_rect()

    #def blitme(self):
    #    self.image.blit(self.image, self.rect)

    def draw(self):
        for y in range(0, 640, 64):
            for x in range(0, 640, 64):
                self.image.blit(pygame.image.load("images/bg_green.png"), (x, y))
                self.image.blit(pygame.image.load("images/fans.png"), (x, y))


