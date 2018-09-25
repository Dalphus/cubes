import pygame
from Input import InputManager as im

window = pygame.display.set_mode((512,512))
clock = pygame.time.Clock()
im.__init__()

x = False

while True:
    im.manage_input()
    _keydown = im.keydown()

    x = len(_keydown)
    if x: print(im.keydown())
    
    for e in _keydown:
        if e.key == pygame.K_ESCAPE:
            print("test")
            _keydown.remove(e)

    if x: print(im.keydown(),'\n')
        
    window.fill((255,255,255))
    pygame.display.flip()
    
    clock.tick(1)
        
