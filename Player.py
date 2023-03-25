import pygame
from  settings import Settings
from pygame.rect import Rect

class Player(Rect):
    """A class to move the player"""

    def __init__(self, screen, x, y):
        super().__init__(x, y, 50, 80)
        self.vel = [10.0,1.0]
        self.screen = screen
        self.moving = [False, False] #[0] IZQ, [1] DERECHA
    
    def movemet_player(self):
        self.vel[1] +=  0.5
        self.keys = pygame.key.get_pressed()

        self.moving[0] = self.keys[pygame.K_a]
        self.moving[1] = self.keys[pygame.K_d]
        
        if self.keys[pygame.K_w]:
            self.vel[1] = -10
        
        #if self.keys[pygame.K_s]:
        #    self.bottomright[1] += self.vel[1]
            
        if self.keys[pygame.K_a]:
            self.x -= self.vel[0]
        if self.keys[pygame.K_d]:
            self.x += self.vel[0]
    
        self.y += self.vel[1]

    def blitme(self):
        pygame.draw.rect(self.screen, (0, 0, 255), self)