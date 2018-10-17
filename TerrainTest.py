import pygame
from Input import InputManager as im
import math
pygame.init()
im.__init__()

class Quadtree:
    def __init__(self):
        self.quadrants = [None]*4

    def draw(self):
        pass

class Square:
    def __init__(self,pos):
        self.x,self.y = pos
        
    def draw(self,window,offset):
        x,y = (self.x*50-offset[0],(-1-self.y)*50-offset[1])
        pygame.draw.polygon(window,(0,0,255),((x,y),(x+50,y),(x+50,y+50),(x,y+50)),3)

class Camera:
    def __init__(self):
        self.x = -100; self.y = 400
        self.keys = [pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d]
        self.pressed = [False]*4
    
    def update(self):
        for e in im.keydown():
            for i in range(0,4):
                if e.key == self.keys[i]: self.pressed[i] = True
        for e in im.keyup():
            for i in range(0,4):
                if e.key == self.keys[i]: self.pressed[i] = False
        if self.pressed[0]: self.y += 5
        if self.pressed[1]: self.y -= 5
        if self.pressed[2]: self.x -= 5
        if self.pressed[3]: self.x += 5

class Cursor:
    def __init__(self):
        self.x = 0; self.y = 0
    
    def update(self):
        for e in im.keydown():
            if e.key == pygame.K_UP: self.y += 1
            elif e.key == pygame.K_DOWN: self.y -= 1
            elif e.key == pygame.K_LEFT: self.x -= 1
            elif e.key == pygame.K_RIGHT: self.x += 1

    def draw(self,window,offset):
        x,y = (self.x*50-offset[0],(-1-self.y)*50-offset[1])
        pygame.draw.polygon(window,(0,0,0),((x,y),(x+50,y),(x+50,y+50),(x,y+50)),3)
        
class __main__:
    def __init__(self):
        window = pygame.display.set_mode((500,500))
        font = pygame.font.SysFont('Courier', 20)
        clock = pygame.time.Clock()
        cam = Camera()
        board = Square((0,0))
        square_list = [board]
        cursor = Cursor()
        
        while True:
            im.manage_input()
            cam.update()
            cursor.update()

            for e in im.keydown():
                if e.key == pygame.K_RETURN:
                    s = Square((cursor.x,cursor.y))
                    

                    
                    square_list.append(s)
            
            x,y = (cam.x,-cam.y)
            
            window.fill((255,255,255))
            for s in square_list: s.draw(window,(x,y))
            cursor.draw(window,(x,y))
            pygame.draw.line(window,(255,0,0),(-x,0),(-x,500))
            pygame.draw.line(window,(255,0,0),(0,-y),(500,-y))

            fps = font.render(('%.1f'%cursor.x)+", "+('%.1f'%cursor.y),True,(0,255,0))
            window.blit(fps,(20,20))
            
            pygame.display.flip()
            clock.tick(30)

__main__()
