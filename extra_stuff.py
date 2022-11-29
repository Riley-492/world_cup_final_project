from rect import *

rect = Rect(100, 50, 50, 50)
v = [2, 2]

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    rect.move_ip(v)

    if rect.left < 0:
        v[0] *= -1
    if rect.right > width:
        v[0] *= -1
    if rect.top < 0:
        v[1] *= -1
    if rect.bottom > height:
        v[1] *= -1

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    pygame.display.flip()

pygame.quit()



class Ball(Sprite):

    def __init__(self, boundaries, player_one, player_two):
        super().__init__()
        self.image = pygame.image.load("images/ball.png")#
        self.rect = self.image.get_rect(center=(633, 375))#
        self.pos = pygame. math.Vector2(self.rect.topleft)#
        self.direction = pygame.math.Vector2(1, 1)#
        self.speed = 4#
        self.old_rect = self.rect.copy()
        self.boundaries = boundaries
        self.player_one = player_one
        self.player_two = player_two

    def collision(self, direction):
        collision_sprites = pygame.sprite.spritecollide(self, self.boundaries, False)
        if collision_sprites:
            if direction == 'horizontal':
                for sprite in collision_sprites:
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.pos.x = self.rect.x
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.pos.x = self.rect.x
            if direction == 'vertical':
                for sprite in collision_sprites:
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.pos.y = self.rect.y
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.pos.y = self.rect.y

    def update(self, dt):

        self.old_rect = self.rect.copy()

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.collision('horizontal')
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self .pos.y)
        self.collision('vertical')



