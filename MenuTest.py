import pygame,sys
from Input import InputManager as im
pygame.init()

class button:
    def __init__(self,r,a,c = ((0,0,255),(10,10,255),(155,155,255))):
        self.rect = r
        self.action = a
        self.colors = c
        self.hover = False
    def update(self):
        for e in im.mousemotion():
            if self.rect.collidepoint(e.pos):
                self.hover = True
            else:
                self.hover = False
        for e in im.mbdown():
            if self.hover:
                print(dir(e))
                e.buttons
                self.action()
    def bg(self):
        if self.hover:
            return (10,10,255)
        else:
            return (0,0,255)
    
class __main__:
    
    def test_function():
        print("test")
    
    def __init__(self):
        im.__init__()
        
        window = pygame.display.set_mode((512,512))
        font = pygame.font.SysFont('Courier', 20)

        b1 = button(pygame.Rect(100,100,50,50),__main__.test_function)

        while True:
            im.manage_input()

            b1.update()
            window.fill((255,255,255))
            
            pygame.draw.rect(window,b1.bg(),b1.rect)
            
            fps = font.render("test",True,(0,255,0))
            window.blit(fps,(b1.rect.x,b1.rect.y))

            pygame.display.flip()
__main__()
