import pygame, math
from Terrain import Cube

class Player:
    def __init__(self,position=(0,0,0),rotation=(0,0)):
        self.x,self.y,self.z = position
        self.yaw,self.pitch = rotation
    
    def update(self,world,key,dt):
        s,c = math.sin(self.yaw),math.cos(self.yaw)
        #wasd movement relative to camera angle
        dx,dy,dz = (0,0,0)
        if key[pygame.K_w]:
            dz += dt*c
            dx += dt*s
        if key[pygame.K_s]:
            dz -= dt*c
            dx -= dt*s
        if key[pygame.K_d]:
            dz -= dt*s
            dx += dt*c
        if key[pygame.K_a]:
            dz += dt*s
            dx -= dt*c
        #up/down
        if key[pygame.K_SPACE]: dy += dt
        if key[pygame.K_LSHIFT]: dy -= dt

        if 0 < self.x+dx < len(world.map_data[0])-1 and 0 < self.y+dy < len(world.map_data)-1 and 0 < self.z+dz < len(world.map_data[0][0])-1:
            if dx and type(world.map_data[int(self.y)][int(self.x+(dx/abs(dx))*.3)][int(self.z)]) != Cube: self.x += dx
            if dy and type(world.map_data[int(self.y+(dy/abs(dy))*1.5)][int(self.x)][int(self.z)]) != Cube: self.y += dy
            if dz and type(world.map_data[int(self.y)][int(self.x)][int(self.z+(dz/abs(dz))*.3)]) != Cube: self.z += dz
        else:
            self.x += dx; self.y += dy; self.z += dz
        
        #looking around
        mouse = pygame.mouse.get_rel()
        self.yaw += mouse[0]/(dt*250)
        if -math.pi/2+.2 < self.pitch-mouse[1]/(dt*250) < math.pi/2-.2:
            self.pitch -= mouse[1]/(dt*250)
            
    def pos(self):
        return (self.x,self.y,self.z)
