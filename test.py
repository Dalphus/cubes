import pygame, sys

window = pygame.display.set_mode((512,512))
clock = pygame.time.Clock()
draw_circle = False

while True:

    #print(pygame.mouse.get_pos())
        
    window.fill((255,255,255))
    pygame.draw.circle(window,(255,0,0),(256,256),10)

    

    clock.tick(1)
    pygame.display.flip()
                


