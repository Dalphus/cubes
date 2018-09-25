import pygame, sys, math
from World import World
from Input import InputManager as im

class __main__:
    
    def __init__(self,w,h):
        #pygame shit
        window = pygame.display.set_mode((w,h))
        clock = pygame.time.Clock()
        pygame.init()

        #variables +other cool stuff
        im.__init__()
        paused = True
        font = pygame.font.SysFont('Courier', 20)
        dim1 = World(window)
        
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
            
            if not paused:
                dim1.update(dt)
            else:
                pass

            #print out fps
            fps = font.render(str(int(clock.get_fps())),True,(0,255,0))
            window.blit(fps,(20,20))
    
            pygame.display.flip()

__main__(512,512)

