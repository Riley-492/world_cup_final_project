import pygame
import sys
from background import Background
from car import Car
from ball import Ball
from pygame import mixer
pygame.init()
mixer.init()
# music from bensound.com
mixer.music.load('background_music.mp3')
mixer.music.set_volume(0.3)
mixer.music.play()

font = pygame.font.SysFont("Times", 46)


class WorldCup:

    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.background = Background(self.screen_rect.width, self.screen_rect.height)
        self.car1 = Car((136, 378), 'images/car_black.png')
        self.car2 = Car((1088, 378), 'images/car_blue.png')
        self.ball = Ball((633, 375), [2, 3])
        self.game_objects = pygame.sprite.Group()
        self.game_objects.add(self.background, self.car1, self.car2, self.ball)
        pygame.display.set_caption('World Cup')
        self.score1 = 0
        self.score2 = 0

    def draw_clock(self, seconds):
        # Clock
        output_string = f"Time: {seconds}"
        text = font.render(output_string, True, [30, 30, 30])
        self.screen.blit(text, [10, 16])

    def run_game(self):
        clock = pygame.time.Clock()
        frame_index = 0

        while True:
            self.check_events()
            self.car1.update(self.car2)
            self.car2.update(self.car1)
            self.ball.update(self.car1, self.car2)
            self.ball.update_score()

            # Drawing the screen and its objects
            self.game_objects.draw(self.screen)
            self.draw_clock(frame_index//60)
            self.ball.update_score()
            pygame.display.flip()

            clock.tick(60)
            frame_index += 1

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
            self.car2.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.car2.moving_down = True
        elif event.key == pygame.K_RIGHT:
            self.car2.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.car2.moving_left = True
        elif event.key == pygame.K_w:
            self.car1.moving_up = True
        elif event.key == pygame.K_s:
            self.car1.moving_down = True
        elif event.key == pygame.K_d:
            self.car1.moving_right = True
        elif event.key == pygame.K_a:
            self.car1.moving_left = True

    def check_keyup_events(self, event):
        if event.key == pygame.K_SPACE:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.car2.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.car2.moving_down = False
        elif event.key == pygame.K_RIGHT:
            self.car2.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.car2.moving_left = False
        elif event.key == pygame.K_w:
            self.car1.moving_up = False
        elif event.key == pygame.K_s:
            self.car1.moving_down = False
        elif event.key == pygame.K_d:
            self.car1.moving_right = False
        elif event.key == pygame.K_a:
            self.car1.moving_left = False


if __name__ == '__main__':
    ai = WorldCup()
    ai.run_game()
