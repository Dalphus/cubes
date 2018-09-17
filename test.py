import pygame, sys

window = pygame.display.set_mode((512,512))
pos = (0,0)
pygame.mouse.get_rel()
paused = True

while True:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                paused = not paused
                pygame.event.set_grab(not paused)
        elif e.type == pygame.MOUSEMOTION:
            dx,dy = e.rel
            pos = (pos[0]+dx,pos[1]+dy)
    
    if not paused:
        pygame.mouse.set_pos(256,256)
        pygame.event.clear(pygame.MOUSEMOTION)
    
        
    window.fill((255,255,255))
    pygame.draw.circle(window,(255,0,0),pos,5)
    pygame.display.flip()
    
                


    
