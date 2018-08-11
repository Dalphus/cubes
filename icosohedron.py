
import pygame, sys
from math import sin,cos,pi,atan,hypot,sqrt

class Camera:
    def __init__(self,pos,rot):
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]

        self.yaw = rot[0]
        self.pitch = rot[1]
    def update(self,key,dt):
        if key[pygame.K_w]: cam.z += dt
        if key[pygame.K_s]: cam.z -= dt
        if key[pygame.K_a]: cam.x -= dt
        if key[pygame.K_d]: cam.x += dt
        if key[pygame.K_e]: cam.y -= dt
        if key[pygame.K_q]: cam.y += dt
        dt /= 2
        if key[pygame.K_RIGHT]:
            self.yaw += dt
            if self.yaw > pi*2: self.yaw = 0
        if key[pygame.K_LEFT]:
            self.yaw -= dt
            if self.yaw < 0: self.yaw = pi*2
        if key[pygame.K_UP]:
            self.pitch += dt
            if self.pitch > pi*2: self.pitch = 0
        if key[pygame.K_DOWN]:
            self.pitch -= dt
            if self.pitch < 0: self.pitch = pi*2

def sign(x):
    if x < 0: return -1
    else: return 1

#screen variables
w,h = 1024,512
cw,ch = w/2,h/2

#pygame shit
window = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

#cool arrays
a = .5*(sqrt(5)-1)
corners = [(0,1,a),(0,-1,-1*a),(a,0,1),(-1*a,0,-1),(1,a,0),(-1,-1*a,0),(0,1,-1*a),(0,-1,a),(-1*a,0,1),(a,0,-1),(1,-1*a,0),(-1,a,0)]
origin = (0.1,0.1,0.1)
edges = [(0,2),(0,4),(0,6),(0,8),(0,11),(1,3),(1,5),(1,7),(1,9),(1,10),(2,4),(2,7),(2,8),(2,10),(3,5),(3,6),\

         (3,9),(3,11),(4,6),(4,9),(4,10),(5,7),(5,8),(5,11),(6,9),(6,11),(7,8),(7,10),(8,11),(9,10)]

#other variables
#idk
cam = Camera((1,0,-5),(0,0))
log = 0
log1 = 1

while True:
    dt = clock.tick()/1000
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_i and log1:
                log = 1
                print("")
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_i:
                log1 = 1
    
    window.fill((255,255,255))
    for line in edges:
        points = []
        for x,y,z in (corners[line[0]],corners[line[1]]):
            
            #camera rotation
            x -= origin[0]
            y -= origin[1]
            z -= origin[2]
            
            c = 0 if x == 0 else atan(z/x)
            c += cam.yaw
            h = hypot(z,x)*sign(x)
            x = h*cos(c)
            z = h*sin(c)

            c = 0 if z == 0 else atan(y/z)
            c += cam.pitch
            h = hypot(y,z)*sign(z)
            z = h*cos(c)
            y = h*sin(c)
            
            if log : print(x,y,z)
            
            #player position displacment
            x -= cam.x
            y -= cam.y
            z -= cam.z
            
            #z compensation
            f = 900/z
            x *= f
            y *= f
            
            points.append((cw+int(x),ch+int(y)))
        pygame.draw.line(window,(0,0,0),points[0],points[1])
        
    log = 0
        
    clock.tick(60)
    pygame.display.flip()
    cam.update(pygame.key.get_pressed(),.1)
