import pygame


class Background:

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game()
        self.image = pygame.surface.Surface((0, 0)) # screen_height, screen_width
        self.image.blit(pygame.image.load("images/fans.png"), (0, 0))


        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def draw(self):
        for y in range(0, 960, 64):
            for x in range(0, 640, 64):
                self.image.blit(pygame.image.load("images/fans.png"), (x, y))

