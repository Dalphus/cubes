import pygame, sys, math
from Terrain import TerrainGenerator
from Camera import Player
from Draw import Render
pygame.init()
  
class __main__:
    
    def __init__(self,w,h):
        #pygame shit
        window = pygame.display.set_mode((w,h))
        clock = pygame.time.Clock()

        #terrain generation maybe
        world = TerrainGenerator()
        world.pillars()
        world.hideFaces()

        #other shit idk
        steve = Player((5,5,5))
        font = pygame.font.SysFont('Courier', 20)
        paused = True
        
        #game loop
        while True:
            dt = clock.tick()/200

            #input shenanagins
            kb = pygame.key.get_pressed()
            if pygame.event.peek(pygame.QUIT):
                pygame.display.quit();pygame.quit();sys.exit()
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        paused = not paused
                        pygame.event.set_grab(not paused)
##                        pygame.mouse.set_visible(paused)
            if not paused:
                pygame.mouse.set_pos(256,256)
                pygame.mouse.get_rel()
            
            for cube in world.cube_list:
                cube.relative_faces(steve.pos())
            
            #graphics
            window.fill((255,255,255))
            Render.render(window,world.cube_list,steve)
            pygame.draw.circle(window,(0,0,0),(256,256),3)

            #print out fps
            fps = font.render(str(int(clock.get_fps())),True,(0,255,0))
            #fps = font.render(str((int(steve.x),int(steve.y),int(steve.z))),True,(0,255,0))
            window.blit(fps,(20,20))
    
            pygame.display.flip()
            steve.update(world,kb,dt)

__main__(512,512)

