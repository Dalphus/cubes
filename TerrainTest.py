import pygame
from Input import InputManager as im
import math
pygame.init()
im.__init__()

class Square:
    def __init__(self,_rect,_color):
        self.rect = rect
        self.color = color

    def draw(self,window):
        pygame.draw.rect(window,self.color,rect,5)

class Camera:
    def __init__(self):
        self.x = 0; self.y = 0
        self.keys = [pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d]
    def update(self):
        pressed = [False]*4
        
        for e in im.keydown():
            for i in range(0,4):
                pressed[i] = pressed[i] or e.key == self.keys[i]
        for e in im.keyup():
            for i in range(0,4):
                pressed[i] = not(pressed[i] or e.key == self.keys[i])
        if pressed[0]: self.y += .1
        if pressed[1]: self.y -= .1
        if pressed[2]: self.x -= .1
        if pressed[3]: self.x += .1
        
        
class __main__:
    def __init__(self):
        window = pygame.display.set_mode((500,500))
        font = pygame.font.SysFont('Courier', 20)
        clock = pygame.time.Clock()
        cam = Camera()
        
        while True
            cam.update()
            
            window.fill((255,255,255))
            pygame.draw.line(window,(155,155,155),())
            
            pygame.display.flip()
            clock.tick(30)
__main__()
