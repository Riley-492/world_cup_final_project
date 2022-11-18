import pygame
import sys
from background import Background

class WorldCup:

    def __init__(self):

        pygame.init()
        #self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.background = Background(self.screen_rect.width, self.screen_rect.height)
        self.game_objects = pygame.sprite.Group()
        self.game_objects.add(self.background)
        pygame.display.set_caption('World Cup')
        self.bg_image = pygame.image.load("images/bg_green.png")
        self.bg_image_rect = self.bg_image.get_rect()
        self.num_tiles = self.screen_rect.width // self.bg_image_rect.width
        self.fans = pygame.image.load("images/fans.png")
        self.fans_rect = self.fans.get_rect()


    def run_game(self):
        clock = pygame.time.Clock()

        while True:
            self.check_events()
            self.update_screen()
            clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def check_keyup_events(self, event):
        if event.key == pygame.K_SPACE:
            sys.exit()

    def update_screen(self):
        self.game_objects.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    ai = WorldCup()
    ai.run_game()
