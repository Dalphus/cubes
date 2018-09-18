import pygame,sys

#making this class static would mean you don't have
#to pass it into other classe. @classmethod maybe?
class InputManager:
    def __init__(self):
        pygame.event.set_allowed([pygame.KEYDOWN,\
                                  pygame.KEYUP,\
                                  pygame.MOUSEMOTION,\
                                  pygame.QUIT])

    def manage_input(self):
        self.filtered_input = [[],[],[]]
        if pygame.event.peek(pygame.QUIT):
                pygame.display.quit();pygame.quit();sys.exit()
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                self.filtered_input[0].append(e)
            elif e.type == pygame.KEYUP:
                self.filtered_input[1].append(e)
            elif e.type == pygame.MOUSEMOTION:
                self.filtered_input[2].append(e)

    def keydown(self):
        return self.filtered_input[0]
    def keyup(self):
        return self.filtered_input[1]
    def mousemotion(self):
        return self.filtered_input[2]
