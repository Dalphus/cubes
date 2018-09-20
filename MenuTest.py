import pygame,sys
pygame.init()

class button:
    def __init__(self):
        self.rect = Rect(100,100,50,50)
        self.action = test_function
        self.hover = False
    def mouse_input(self,fi):
        for e in fi[0]:
            if self.rect.collidepoint(e.pos):
                self.hover = True
            else
                self.hover = False
        for e in fi[1]:
            if e.button
    

def test_function():
    print("You pressed the button")

window = pygame.display.set_mode((512,512))
font = pygame.font.SysFont('Courier', 20)

b1 = pygame.Rect(100,100,200,200)

while True:
    if pygame.event.peek(pygame.QUIT):
        pygame.quit(),sys.exit()

    filtered_input = [[],[],[]]
    for e in pygame.event.get():
        if e.type == pygame.MOUSEMOTION:
            filtered_input[0].append(e)
        elif e.type == pygame.MOUSEBUTTONDOWN:
            filtered_input[1].append(e)
        elif e.type == pygame.MOUSEBUTTONUP:
            filtered_input[2].append(e)

    button.mouse_input(filtered_input)

    window.fill((255,255,255))
    fps = font.render(b1.name,True,(0,255,0))
    window.blit(fps,(100,100))

    pygame.display.flip()
