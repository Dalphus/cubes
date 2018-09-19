import pygame,sys
pygame.init()

class Button:
    def __init__(self,pos,dim,colors,label,a):
        self.x,self.y = pos
        self.w,self.h = dim
        self.default_color,self.hover_color,self.press_color = colors
        self.name = label
        self.action = a

    def pos(self):
        return (self.x,self.y)

def test_function():
    print("You pressed the button")

window = pygame.display.set_mode((512,512))
b1 = Button((100,100),(200,50),((0,0,255),(0,50,255),(155,155,155)),"Button",test_function)
font = pygame.font.SysFont('Courier', 20)

while True:
    if pygame.event.peek(pygame.QUIT):
        pygame.quit(),sys.exit()

    window.fill((255,255,255))
    fps = font.render(b1.name,True,(0,255,0))
    window.blit(fps,(100,100))

    pygame.display.flip()
