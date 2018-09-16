import pygame, sys, math
import Terrain, Draw, Player
pygame.init()

  
class __main__:
    
    def __init__(self):
        #screen variables
        w,h = 512,512

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
        
        #game loop
        while True:
            #time since last call, in millis maybe
            dt = clock.tick()/200
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); sys.exit()

            for a in world.cube_list:
                a.relative_faces(steve.pos())
            
            #outsourcing graphics to Render object
            window.fill((255,255,255))
            Render.render(window,world.cube_list,steve)
            pygame.draw.circle(window,(0,0,0),(256,256),3)

            #print out fps
            fps = font.render(str(int(clock.get_fps())),True,(0,255,0))
            #fps = font.render(str((int(steve.x),int(steve.y),int(steve.z))),True,(0,255,0))
            window.blit(fps,(20,20))
    
            pygame.display.flip()
            steve.update(world,pygame.key.get_pressed(),dt)
__main__()

