import sys
import pygame

from settings import Settings
from player import Player

class TriColor:

    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width,
                 self.settings.screen_height)
                )

        pygame.display.set_caption("3-Color")

        self.player = Player(self.screen, 0, 0)

        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

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
        elif event.key == pygame.K_a:
            self.player.move_left()
        elif event.key == pygame.K_d:
            self.player.move_right()
        elif event.key == pygame.K_w:
            self.player.jump()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_a:
            self.player.stop_moving_left()
        elif event.key == pygame.K_d:
            self.player.stop_moving_right()
        elif event.key == pygame.K_w:
            self.player.stop_jumping()

    def _update_screen(self):
        self.screen.fill(self.settings.background_color)
        self.player.move()
        self.player.blitme()

        pygame.display.flip()
        dt = self.clock.tick(60) / 1000
        

if __name__=='__main__':
    game = TriColor()
    game.run_game()


