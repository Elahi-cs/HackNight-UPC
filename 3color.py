import sys
import pygame

from settings import Settings

class TriColor:

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width,
                 self.settings.screen_height)
                )

        pygame.display.set_caption("3-Color")

    def run_game(self):
        while True:
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # Espai per canviar color fons
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        pass


if __name__=='__main__':
    game = TriColor()
    game.run_game()


