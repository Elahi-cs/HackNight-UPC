import pygame
from Environment import Environment
from settings import Settings


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#player  = Player(screen, 640,360)
environment = Environment(screen, 20)
environment.generate_blocks(360)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # fill the screen with a color to wipe away anything from last frame
    environment.cambio_fondo()
    environment.movement_blocks()
    environment.blitall(screen)
    #player.movemet_player()
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()