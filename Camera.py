import pygame, math
from Terrain import Cube
from InputManager import InputManager

class Player:
    def __init__(self,im,position=(0,0,0),rotation=(0,0)):
        self.x,self.y,self.z = position
        self.yaw,self.pitch = rotation
        self.get_input = im

        self.movement = [0,0,0,0,0,0]
        self.keys = [pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d,pygame.K_SPACE,pygame.K_LSHIFT]
    
    def update(self,world,dt):
        s,c = math.sin(self.yaw),math.cos(self.yaw)
        #detecting and storing keypresses
        for e in self.get_input.keydown():
            for i in range(0,6):
                if e.key == self.keys[i]:
                    self.movement[i] = 1
                    break
        for e in self.get_input.keyup():
            for i in range(0,6):
                if e.key == self.keys[i]:
                    self.movement[i] = 0
                    break
        #mouse movement
        for e in self.get_input.mousemotion():
            self.mouse_event(e,dt)

        #wasd movement relative to camera angle     
        dx,dy,dz = (0,0,0)
        if self.movement[0]:
            dz += dt*c
            dx += dt*s
        if self.movement[1]:
            dz -= dt*c
            dx -= dt*s
        if self.movement[2]:
            dz += dt*s
            dx -= dt*c
        if self.movement[3]:
            dz -= dt*s
            dx += dt*c
        #up/down
        if self.movement[4]: dy += dt
        if self.movement[5]: dy -= dt

        if 0 < self.x+dx < len(world.map_data[0])-1 and 0 < self.y+dy < len(world.map_data)-1 and 0 < self.z+dz < len(world.map_data[0][0])-1:
            if dx and type(world.map_data[int(self.y)][int(self.x+(dx/abs(dx))*.3)][int(self.z)]) != Cube: self.x += dx
            if dy and type(world.map_data[int(self.y+(dy/abs(dy))*1.5)][int(self.x)][int(self.z)]) != Cube: self.y += dy
            if dz and type(world.map_data[int(self.y)][int(self.x)][int(self.z+(dz/abs(dz))*.3)]) != Cube: self.z += dz
        else:
            self.x += dx; self.y += dy; self.z += dz
    
    def mouse_event(self,event,dt):
        #looking around
        dx,dy = event.rel
        self.yaw += dx/(dt*250)
        if -math.pi/2+.2 < self.pitch-dy/(dt*250) < math.pi/2-.2:
            self.pitch -= dy/(dt*250)
            
    def pos(self):
        return (self.x,self.y,self.z)
