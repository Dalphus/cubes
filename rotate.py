import pygame, sys, math

window = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
    
    window.fill((255,255,255))

    pos = pygame.mouse.get_pos()    
    pygame.draw.circle(window,(255,0,0),pos,5)
    print(pos)
    
    pygame.display.flip()
    clock.tick(30)
