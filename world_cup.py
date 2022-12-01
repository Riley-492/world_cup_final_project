import pygame
import sys
from background import Background
from car import Car
from ball import Ball
from pygame import mixer

mixer.init()
# music from bensound.com
mixer.music.load('background_music.mp3')
mixer.music.set_volume(0.3)
mixer.music.play()


class WorldCup:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.background = Background(self.screen_rect.width, self.screen_rect.height)
        self.car1 = Car((136, 378), 'images/car_black.png')
        self.car2 = Car((1088, 378), 'images/car_blue.png')
        self.ball = Ball((633, 375), [1, 1.5])
        self.game_objects = pygame.sprite.Group()
        self.game_objects.add(self.background, self.car1, self.car2, self.ball)
        pygame.display.set_caption('World Cup')
        self.score1 = 0
        self.score2 = 0

    def run_game(self):
        clock = pygame.time.Clock()

        while True:
            self.check_events()
            self.car1.update(self.car2)
            self.car2.update(self.car1)
            self.ball.update(self.car1, self.car2)
            self.ball.update_score()
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

    def update_screen(self):
        self.game_objects.draw(self.screen)
        self.ball.update_score()
        pygame.display.flip()


if __name__ == '__main__':
    ai = WorldCup()
    ai.run_game()
