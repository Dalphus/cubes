import pygame

class __main__:
    def __init__(self):
        world = pygame.display.set_mode((500,500))

        while True:
            world.fill((255,255,255))
            pygame.draw.polygon(world,(0,255,0),((50,50),(50,200),(50,50)))
            pygame.display.flip()
__main__()
