import pygame
from pygame.sprite import Sprite


class Background(Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.surface.Surface((width, height))  # screen_height, screen_width
        # Green Field
        self.bg_image = pygame.image.load("images/bg_green.png")
        self.bg_image_rect = self.bg_image.get_rect()
        self.num_tiles = width // self.bg_image_rect.width
        for y in range(self.num_tiles):
            for x in range(self.num_tiles):
                self.image.blit(self.bg_image, (x*self.bg_image_rect.width, y*self.bg_image_rect.height))

        # White Lines
        self.white_line = pygame.image.load('images/white_line.png')
        self.white_line_rect = self.white_line.get_rect()
        for y in range(128, 656, 64):
            for x in range(90, 102, 64):
                self.image.blit(self.white_line, (x, y))
        for y in range(128, 656, 64):
            for x in range(1184, 1194, 64):
                self.image.blit(self.white_line, (x, y))


        # Top fans
        self.fans = pygame.image.load("images/fans.png")
        self.fans_rect = self.fans.get_rect()
        self.fans_width = width // self.fans_rect.width
        # Received assistance from Noah Harding
        for y in range(self.fans_width):
            for x in range(self.fans_width):
                self.image.blit(self.fans, (x*self.fans_rect.width, self.fans_rect.height))

        # Fans bottom
        self.fans_up = pygame.image.load("images/fans_up.png")
        self.fans_up_rect = self.fans_up.get_rect()
        self.fans_up_width = width // self.fans_up_rect.width
        for y in range(656, 720, 64):
            for x in range(0, 1200, 128):
                self.image.blit(self.fans_up, (x, y))

        # Goal Left Side
        # Received assistance from Sean Miller
        self.left_side = pygame.image.load("images/left_side.png")
        self.left_side_rect = self.left_side.get_rect()
        self.left_side_width = width // self.left_side_rect.width
        for y in range(296, 488, 192):
            for x in range(0, 96, 96):
                self.image.blit(self.left_side, (x, y))

        # Goal Right Side
        self.right_side = pygame.image.load("images/right_side.png")
        self.right_side_rect = self.right_side.get_rect()
        self.right_side_width = width // self.right_side_rect.width
        for y in range(296, 488, 192):
            for x in range(1184, 1280, 96):
                self.image.blit(self.right_side, (x, y))

        self.rect = self.image.get_rect()
