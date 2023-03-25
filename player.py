import pygame
from  settings import Settings
from pygame.rect import Rect

class Player(Rect):
    """A class to move the player"""

    def __init__(self, screen, x, y):
        self.width = 50
        self.height = 80
        super().__init__(x, y, self.width, self.height)
        self.horizontal_speed = 10.0
        self.vertical_speed = 1.0
        self.screen = screen
        self.moving_left = False
        self.moving_right = False
        self.jumping = False
        self.color = (0, 0, 255)
    
    def move_player(self):
        self.vertical_speed +=  0.5

        if self.jumping:
            self.vertical_speed = -10
        
        if self.moving_left:
            self.x -= self.horizontal_speed
        if self.moving_right:
            self.x += self.horizontal_speed
    
        self.y += self.vertical_speed

    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self)
