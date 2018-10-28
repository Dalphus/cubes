from Input import InputManager as im
import pygame

class Cursor:

    @classmethod
    def __init__(cls,pos=(0,0,0)):
        cls.x,cls.y,cls.z = pos
    
    @classmethod
    def update(cls):
        for e in im.keydown():
            if e.key == pygame.K_LEFT: cls.x -= 1
            if e.key == pygame.K_RIGHT: cls.x += 1
            if e.key == pygame.K_UP: cls.z += 1
            if e.key == pygame.K_DOWN: cls.z -= 1
            if e.key == pygame.K_RSHIFT: cls.y += 1
            if e.key == pygame.K_RCTRL: cls.y -= 1
    
    @classmethod
    def pos(cls):
        return (cls.x,cls.y,cls.z)