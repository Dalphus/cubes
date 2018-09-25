import pygame, sys, math
from Terrain import TerrainGenerator
from Camera import Player
from Draw import Render
from Input import InputManager as im
  
class World:
    def __init__(self,_window):
        self.window = _window
        self.w,self.h = pygame.display.get_surface().get_size()
        
        #terrain generation maybe
        self.world = TerrainGenerator()
        self.world.pillars()
        self.world.hideFaces()

        #controlled camera, will probably move code somewhere else
        self.p1 = Player((5,5,5))
    
    def update(self,dt):
        #keep mouse in center of screen
        pygame.mouse.set_pos(256,256)
        pygame.event.clear(pygame.MOUSEMOTION)

        #update player (again, temporary)
        self.p1.update(self.world,dt)

        #update cubes in terrain
        for cube in self.world.cube_list:
            cube.relative_faces(self.p1.pos())
        
        #graphics
        self.window.fill((255,255,255))
        Render.render(self.window,self.world.cube_list,self.p1)
        pygame.draw.circle(self.window,(0,0,0),(self.w//2,self.h//2),3)
