import pygame
from Input import InputManager as im
import math
pygame.init()
im.__init__()
zoom = 10

class Quadtree:
    def __init__(self,_level=0):
        self.quadrants = [None]*4
        self.level = _level

    def draw(self,window,offset,pos=(0,0),width=1):
        x,y = pos[0]*zoom-offset[0],pos[1]*zoom-offset[1]
        scale = (2**(self.level+1))*zoom
        pygame.draw.polygon(window,(0,255,0),((x,y),(x+scale,y),(x+scale,y+scale),(x,y+scale)),width)

        bonus = 2**self.level
        for i in range(0,4):
            if isinstance(self.quadrants[i],Quadtree):
                self.quadrants[i].draw(window,offset,(pos[0]+(i%2)*bonus,pos[1]+(i>1)*bonus),width+1)
        pass

class Square:
    def __init__(self,pos):
        self.x,self.y = pos
        
    def draw(self,window,offset):
        x,y = self.x*zoom-offset[0],self.y*zoom-offset[1]
        pygame.draw.polygon(window,(0,0,255),((x,y),(x+zoom,y),(x+zoom,y+zoom),(x,y+zoom)),3)

class Camera:
    def __init__(self):
        self.x = -100; self.y = -100
        self.keys = [pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d]
        self.pressed = [False]*4
    
    def update(self):
        for e in im.keydown():
            for i in range(0,4):
                if e.key == self.keys[i]: self.pressed[i] = True
        for e in im.keyup():
            for i in range(0,4):
                if e.key == self.keys[i]: self.pressed[i] = False
        if self.pressed[0]: self.y += 15
        if self.pressed[1]: self.y -= 15
        if self.pressed[2]: self.x -= 15
        if self.pressed[3]: self.x += 15
        pass
        
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
        x,y = self.x*zoom-offset[0],self.y*zoom-offset[1]
        pygame.draw.polygon(window,(0,0,0),((x,y),(x+zoom,y),(x+zoom,y+zoom),(x,y+zoom)),3)
        
class __main__:
    def define(self,s):
        x1 = 0 if s.x == 0 else int(math.log2(s.x))
        y1 = 0 if s.y == 0 else int(math.log2(s.y))
        max_level = max(x1,y1)

        x1 = [int(i) for i in bin(s.x)[2:]]
        y1 = [int(i) for i in bin(s.y)[2:]]

        temp = self.board
        if self.board.level < max_level:
            self.board = Quadtree(max_level)
            self.board.quadrants[0] = temp
        max_level = self.board.level

        x1 = [0 for i in range(len(x1)-1,max_level)] + x1
        y1 = [0 for i in range(len(y1)-1,max_level)] + y1
                    
        temp = self.board
        ctr = 0
        while temp.level > 0:
            index = x1[ctr] + 2*y1[ctr]
            if not isinstance(temp.quadrants[index],Quadtree) or temp.quadrants[index].level != max_level-ctr-1:
                temp2 = temp.quadrants[index]
                temp.quadrants[index] = Quadtree(max_level-ctr-1)
                temp.quadrants[index].quadrants[0] = temp2
            temp = temp.quadrants[index]
            ctr += 1

        index = x1[max_level] + 2*y1[max_level]
        temp.quadrants[index] = s
        self.square_list.append(s)
        print(max_level)

    def __init__(self):
        #pygame variables
        screen = pygame.display.set_mode((600,600))
        window = pygame.Surface((600,600))
        font = pygame.font.SysFont('Courier', 20)
        clock = pygame.time.Clock()
        
        #UI variables
        cam = Camera()
        cursor = Cursor()
        
        #Data structure variables
        self.board = Quadtree()
        self.board.quadrants[0] = Square((0,0))
        self.square_list = [self.board.quadrants[0]]
        
        while True:
            #updating input
            im.manage_input()
            cam.update()
            cursor.update()

            #special case input
            for e in im.keydown():
                if e.key == pygame.K_RETURN:
                    s = Square((cursor.x,cursor.y))
                    self.define(s)

            x,y = cam.x,cam.y
            #graphics
            window.fill((255,255,255))
            pygame.draw.line(window,(255,0,0),(-x,0),(-x,600))
            pygame.draw.line(window,(255,0,0),(0,-y),(600,-y))
            self.board.draw(window,(x,y))
            for s in self.square_list: s.draw(window,(x,y))
            cursor.draw(window,(x,y))
            #flip dispaly, because 0y is the top of the screen
            window = pygame.transform.flip(window,0,1)

            fps = font.render(str((cursor.x,cursor.y)),True,(0,255,0))
            window.blit(fps,(20,20))
            
            screen.blit(window,(0,0))
            pygame.display.flip()
            clock.tick(30)

__main__()
