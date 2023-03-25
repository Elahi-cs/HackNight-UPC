import pygame
from  settings import Settings
from pygame.rect import Rect

class Player(Rect):
    """A class to move the player"""

    def __init__(self, screen, x, y):
        self.width = 50
        self.height = 80
        super().__init__(x, y, self.width, self.height)
        self.settings = Settings()
        self.horizontal_speed = self.settings.horizontal_speed
        self.vertical_speed = self.settings.vertical_speed
        self.screen = screen
        self.moving_left = False
        self.moving_right = False
        self.jumping = False
        self.color = self.settings.player_color

    def move_left(self):
        self.moving_left = True

    def move_right(self):
        self.moving_right = True

    def jump(self):
        self.jumping = True

    def stop_moving_left(self):
        self.moving_left = False

    def stop_moving_right(self):
        self.moving_right = False

    def stop_jumping(self):
        self.jumping = False
    
    def move(self):
        self.vertical_speed += self.settings.gravity 

        if self.jumping:
            self.vertical_speed = -10
        
        if self.moving_left:
            self.x -= int(self.horizontal_speed)
        if self.moving_right:
            self.x += int(self.horizontal_speed)
    
        self.y += int(self.vertical_speed)

        self._check_boundaries()


    def _check_boundaries(self):
        if self.x > self.settings.screen_width:
            self.x = self.settings.screen_width
        elif self.x < 0:
            self.x = 0

        if self.y > self.settings.screen_height:
            self.y = self.settings.screen_height
        elif self.y < 0:
            self.y = 0

    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self)
