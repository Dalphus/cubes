import pygame
from Input import InputManager as im
from GUI import *
pygame.init()
    
class __main__:
    
    def test_function(x="test"):
        print(x)
    
    def __init__(self):
        im.__init__()
        
        window = pygame.display.set_mode((512,512))
        font = pygame.font.SysFont('Courier', 20)

        menu = Menu()
        b1 = Button(pygame.Rect(100,100,120,50),__main__.test_function,"button 1",font)
        b2 = Button(pygame.Rect(100,160,120,50),__main__.test_function,"button 2",font)
        b3 = Button(pygame.Rect(230,100,120,50),__main__.test_function,"button 3",font)
        menu.add_buttons([b1,b2,b3])

        while True:
            im.manage_input()
            menu.update()
            
            window.fill((255,255,255))
            window.blit(menu.menu_surface,(0,0))

            pygame.display.flip()
__main__()
