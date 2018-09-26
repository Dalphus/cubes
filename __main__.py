import pygame, sys, math
from World import World
from Camera import Player
from Input import InputManager as im

class __main__:
    
    def __init__(self,w,h):
        #pygame shit
        window = pygame.display.set_mode((w,h))
        clock = pygame.time.Clock()
        pygame.init()

        #variables +other cool stuff
        im.__init__()
        paused = False
        font = pygame.font.SysFont('Courier', 20)
        dim1 = World(w,h)
        p1 = Player((-5,5,-5))
        
        #game loop
        while True:
            dt = clock.tick()/200

            #input shenanigans
            im.manage_input()
            _keydown = im.keydown()
            for e in _keydown:
                if e.key == pygame.K_ESCAPE:
                    paused = not paused
                    pygame.event.set_grab(not paused)
                    #pygame.mouse.set_visible(paused)
                    print("Paused:",paused)
                    _keydown.remove(e)

            window.fill((255,255,255))
            if not paused:
                p1.update(dim1.terrain,dt)
                world_surface = dim1.update(p1,dt)
            else:
                pass
            window.blit(world_surface,(0,0))

            #print out fps
            fps = font.render(str(int(clock.get_fps())),True,(0,255,0))
            window.blit(fps,(20,20))
    
            pygame.display.flip()

__main__(512,512)

