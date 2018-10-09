import pygame, sys, math
from Camera import Player
from Terrain import TerrainGenerator
from Draw import Render
from Input import InputManager as im

class __main__:
    
    def __init__(self,w,h):
        #pygame shit
        window = pygame.display.set_mode((w,h))
        clock = pygame.time.Clock()
        pygame.init()

        #variables +other cool stuff
        im.__init__()
        Render.__init__()
        paused = False
        font = pygame.font.SysFont('Courier', 20)
        p1 = Player((0,1,0))
        terrain = TerrainGenerator()
        terrain.flat()
        
        #game loop
        while True:
            dt = clock.tick()/200

            #input shenanigans
            im.manage_input()
            for e in im.keydown():
                if e.key == pygame.K_ESCAPE:
                    paused = not paused
                    pygame.event.set_grab(not paused)
                    #pygame.mouse.set_visible(paused)
                    print("Paused:",paused)
                    #im.keydown().remove(e)
            
            #temporary gibberish
            if not paused:
                pygame.mouse.set_pos(256,256)
                pygame.event.clear(pygame.MOUSEMOTION)
                p1.update(dt)
                Render.update(terrain.cube_list,p1)
            else:
                pass
            window.blit(Render.world_surface,(0,0))

            #print out fps
            fps = font.render(str(int(clock.get_fps())),True,(0,255,0))
            window.blit(fps,(20,20))
    
            pygame.display.flip()

__main__(512,512)

