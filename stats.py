from pygame.sprite import Sprite


class Stats(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.settings = ai_game.settings
        # self.reset_stats()

        self.game_active = True

    # def reset_stats(self):
