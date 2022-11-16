import pygame


class Crowd:

    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((1024, 640))
        self.image.blit(pygame.image.load("images/bg_green.png"), (0, 0))
        self.image.blit(pygame.image.load("images/fans.png"), (0, 0))

        self.image.blit(pygame.image.load("images/bg_green.png"), (128, 0))
        self.image.blit(pygame.image.load("images/fans.png"), (128, 0))

        self.rect = self.image.get_rect()

    def move(self, coordinate):
        self.rect.center = coordinate

    def draw(self):
        self.image.blit(self.image, self.rect)
