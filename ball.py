import pygame

class Ball:
    MAX_VEL = 5
    ball = pygame.image.load("images/ball_soccer2.png")

    def __init__(self, x, y):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):


    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1

