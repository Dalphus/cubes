import pygame, math
from Input import InputManager as im

class Player:
    def __init__(self,position=(0,0,0),rotation=(0,0)):
        self.x,self.y,self.z = position
        self.yaw,self.pitch = rotation

        self.movement = [0,0,0,0,0,0]
        self.keys = [pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d,\
                     pygame.K_SPACE,pygame.K_LSHIFT]
    
    def update(self,dt):
        s,c = math.sin(self.yaw),math.cos(self.yaw)
        #detecting and storing keypresses
        for e in im.keydown():
            for i in range(0,6):
                if e.key == self.keys[i]:
                    self.movement[i] = 1
                    break
        for e in im.keyup():
            for i in range(0,6):
                if e.key == self.keys[i]:
                    self.movement[i] = 0
                    break
        
        #mouse movement
        for e in im.mousemotion():
            dx,dy = e.rel
            self.yaw += dx/(dt*400)
            if -math.pi/2+.2 < self.pitch-dy/(dt*250) < math.pi/2-.2:
                self.pitch -= dy/(dt*400)

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

        self.x += dx; self.y += dy; self.z += dz
            
    def pos(self):
        return (self.x,self.y,self.z)
