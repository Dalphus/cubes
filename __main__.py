import pygame, sys, math
from Terrain import TerrainGenerator
from Camera import Player
from Draw import Render
from InputManager import InputManager
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
        get_input = InputManager()
        steve = Player(get_input,(5,5,5))
        font = pygame.font.SysFont('Courier', 20)
        paused = True
        
        #game loop
        while True:
            dt = clock.tick()/200

            #input shenanagins
            get_input.manage_input()
            
            for e in get_input.keydown():
                if e.key == pygame.K_ESCAPE:
                    paused = not paused
                    pygame.event.set_grab(not paused)
                    #pygame.mouse.set_visible(paused)
                    print(paused)

            if not paused:
                pygame.mouse.set_pos(256,256)
                pygame.event.clear(pygame.MOUSEMOTION)
                steve.update(world,dt)
            
            for cube in world.cube_list:
                cube.relative_faces(steve.pos())
            
            #graphics
            window.fill((255,255,255))
            Render.render(window,world.cube_list,steve)
            pygame.draw.circle(window,(0,0,0),(w//2,h//2),3)

            #print out fps
            fps = font.render(str(int(clock.get_fps())),True,(0,255,0))
            #fps = font.render(str((int(steve.x),int(steve.y),int(steve.z))),True,(0,255,0))
            window.blit(fps,(20,20))
    
            pygame.display.flip()

__main__(512,512)

