import pygame.font
from pygame.sprite import Sprite


class Button(Sprite):

    def __init__(self, msg):
        super().__init__()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.width = 200
        self.height = 50
        self.button_color = (0, 230, 0)
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('Times', 46)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_rect = self.msg.get_rect()
        self.msg_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg, self.msg_rect)
