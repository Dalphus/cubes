import pygame, sys, math
from Camera import Player
from Terrain import TerrainGenerator
from Draw import Render
from Input import InputManager as im
from GUI import *
from Cursor import Cursor

class __main__:
    
    def __init__(self,w,h):
        #pygame shit
        pygame.init()
        window = pygame.display.set_mode((w,h))
        clock = pygame.time.Clock()
        font = pygame.font.SysFont('Courier', 20)

        #variables +other cool stuff
        im.__init__()
        paused = False
        p1 = Player((-1,1,0))
        terrain = TerrainGenerator()
        render = Render()
        cursor = Cursor((4,2,0))

        #debug menu
        debug = Menu()
        b1 = Button(pygame.Rect(100,100,120,50),terrain.test,"test",font)
        b3 = Button(pygame.Rect(100,160,120,50),terrain.clear,"clear",font)
        debug.add_buttons(b1,b3)
        
        #game loop
        while True:
            dt = clock.tick()/200
            if dt == 0: dt = 0.01
            
            #input shenanigans
            im.manage_input()
            for e in im.keydown():
                if e.key == pygame.K_ESCAPE:
                    paused = not paused
                    pygame.event.set_grab(not paused)
                    #pygame.mouse.set_visible(paused)
                    print("Paused:",paused)
                elif e.key == pygame.K_RETURN:
                    terrain.test()
            
            #temporary gibberish
            if not paused:
                pygame.mouse.set_pos(256,256)
                pygame.event.clear(pygame.MOUSEMOTION)
                p1.update(dt)

                render.cubes(terrain.cube_list,p1)
                render.octree(terrain.map,p1)
                render.draw()

                cursor.update()
                render.cursor(cursor,p1)
            else:
                debug.update()

            window.blit(Render.world_surface,(0,0))
            if paused:
                window.blit(debug.menu_surface,(0,0))

            #print out fps
            fps = font.render(str(int(clock.get_fps())),True,(0,255,0))
            window.blit(fps,(20,20))
            
            pygame.display.flip()


__main__(512,512)