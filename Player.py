import pygame, math

class Player:
    def __init__(self,position=(0,0,0),rotation=(0,0)):
        self.x,self.y,self.z = position
        self.yaw,self.pitch = rotation
    
    def update(self,world,key,dt):
        global fov
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
        if key[pygame.K_LEFT]: self.yaw -= dt
        if key[pygame.K_RIGHT]: self.yaw += dt
        if key[pygame.K_UP] and self.pitch < math.pi/2-.2:
            self.pitch += dt
        if key[pygame.K_DOWN] and self.pitch > -1*math.pi/2+.2:
            self.pitch -= dt
            
    def pos(self):
        return (self.x,self.y,self.z)
