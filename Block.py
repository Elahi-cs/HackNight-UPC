
import pygame
from pygame.rect import Rect
from  settings import Settings

class Block(Rect):

    def __init__(self, x, y, width_block, height_block, color):
        super().__init__(x,y,width_block, height_block)

        self.color = color
    
    def movement_block(self, dif_x, dif_y):
        
        if self.x + dif_x < 0:
            self.x = 1400 
        else:
            self.x += dif_x
        self.y += dif_y
        #Scroll constante


    def blitme(self, screen):
        pygame.draw.rect(screen, self.color, self)

