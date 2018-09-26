import pygame, sys, math
from Terrain import TerrainGenerator
from Draw import Render
from Input import InputManager as im
  
class World:
    def __init__(self,width,height):
        self.w = width
        self.h = height
        self.window = pygame.Surface((width,height))
                
        #terrain generation maybe
        self.terrain = TerrainGenerator()
        self.terrain.pillars()
        self.terrain.hideFaces()
    
    def update(self,player,dt):
        #keep mouse in center of screen
        pygame.mouse.set_pos(256,256)
        pygame.event.clear(pygame.MOUSEMOTION)

        #update cubes in terrain
        for cube in self.terrain.cube_list:
            cube.relative_faces(player.pos())
        
        #graphics
        self.window.fill((255,255,255))
        Render.render(self.window,self.terrain.cube_list,player)
        pygame.draw.circle(self.window,(0,0,0),(self.w//2,self.h//2),3)

        return self.window
