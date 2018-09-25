import pygame
from Input import InputManager as im
import Draw
pygame.init()

class button:
    def __init__(self,_rect,_action,_text,font,_colors = ((0,0,255),(50,50,255),(155,155,255))):
        self.rect = _rect
        self.action = _action
        self.colors = _colors
        self.hover = False
        
        self.text = _text
        self.label = font.render(_text,True,(0,0,0))
        self.text_pos = (self.rect.x+(self.rect.width-self.label.get_width())//2,\
                         self.rect.y+(self.rect.height-self.label.get_height())//2)
    
    def update(self):
        for e in im.mousemotion():
            self.hover = self.rect.collidepoint(e.pos)
        for e in im.mbup():
            if self.hover and e.button == 1:
                self.action()
    
    def draw(self,window=None):
        c = self.hover*(1+pygame.mouse.get_pressed()[0])
        pygame.draw.rect(window,self.colors[c],self.rect)
        window.blit(self.label,self.text_pos)
    
class __main__:
    
    def test_function(x="test"):
        print(x)
    
    def __init__(self):
        im.__init__()
        
        window = pygame.display.set_mode((512,512))
        font = pygame.font.SysFont('Courier', 20)

        b1 = button(pygame.Rect(100,100,120,50),__main__.test_function,"button 1",font)
        b2 = button(pygame.Rect(100,160,120,50),__main__.test_function,"button 2",font)
        b3 = button(pygame.Rect(230,100,120,50),__main__.test_function,"button 3",font)

        while True:
            im.manage_input()
            b1.update()
            b2.update()
            b3.update()
            
            window.fill((255,255,255))
            b1.draw(window)
            b2.draw(window)
            b3.draw(window)

            pygame.display.flip()
__main__()
