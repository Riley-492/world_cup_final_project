import pygame
import sys
from background import Background
from player_one import Car1
from player_two import Car2
from ball import Ball


class WorldCup:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.background = Background(self.screen_rect.width, self.screen_rect.height)
        self.car1 = Car1((128, 378))
        self.car2 = Car2((1088, 378))
        self.ball = Ball((633, 375))
        self.game_objects = pygame.sprite.Group()
        if pygame.sprite.collide_rect(self.car1, self.ball):
            print("boink") # make this a method and check for events and have it 'bounce off'
        self.game_objects.add(self.background, self.car1, self.car2, self.ball)

        pygame.display.set_caption('World Cup')

    def run_game(self):
        clock = pygame.time.Clock()

        while True:
            self.check_events()
            self.car1.update()
            self.car2.update()
            self.ball.update()
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

    def update_screen(self):
        self.game_objects.draw(self.screen)

        pygame.display.flip()

    def check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.car1.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.car1.moving_down = True
        elif event.key == pygame.K_RIGHT:
            self.car1.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.car1.moving_left = True
        elif event.key == pygame.K_w:
            self.car2.moving_up = True
        elif event.key == pygame.K_s:
            self.car2.moving_down = True
        elif event.key == pygame.K_d:
            self.car2.moving_right = True
        elif event.key == pygame.K_a:
            self.car2.moving_left = True

    def check_keyup_events(self, event):
        if event.key == pygame.K_SPACE:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.car1.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.car1.moving_down = False
        elif event.key == pygame.K_RIGHT:
            self.car1.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.car1.moving_left = False
        elif event.key == pygame.K_w:
            self.car2.moving_up = False
        elif event.key == pygame.K_s:
            self.car2.moving_down = False
        elif event.key == pygame.K_d:
            self.car2.moving_right = False
        elif event.key == pygame.K_a:
            self.car2.moving_left = False


if __name__ == '__main__':
    ai = WorldCup()
    ai.run_game()
