import pygame
from Input import InputManager as im

window = pygame.display.set_mode((512,512))
clock = pygame.time.Clock()
im.__init__()

while True:
    im.manage_input()
    #print(im.keydown())
    #print(im.mbdown())
        
    window.fill((255,255,255))
    pygame.display.flip()
    
    clock.tick(1)
        
