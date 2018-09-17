import pygame, sys
pygame.init()

window = pygame.display.set_mode((512,512))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Courier', 20)
draw_circle = False

while True:
    clock.tick()
    filtered_input = [[],[]]
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            filtered_input[0].append(e)
        elif e.type == pygame.KEYUP:
            filtered_input[1].append(e)
        elif e.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    for e in filtered_input[0]:
        if e.key == pygame.K_a:
            draw_circle = True
    for e in filtered_input[1]:
        if e.key == pygame.K_a:
            draw_circle = False
        
    window.fill((255,255,255))
    if draw_circle:
        pygame.draw.circle(window,(255,0,0),(256,256),10)

    fps = font.render(str(int(clock.get_fps())),True,(0,255,0))
    window.blit(fps,(20,20))

    pygame.display.flip()
                


