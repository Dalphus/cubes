import pygame

class Test:
    
    def __init__(self,pos):
        self.a = pos[0]
        self.b = pos[1]
        self.c = pos[2]
    def __str__(self):
        return "Test "+str(self.a)+" "+str(self.b)+" "+str(self.c)

class __main__:
    def __init__(self):
        x = [Test((1,2,3)),Test((4,5,6))]
        y = []
        print("X: ",x)

        y += x
        print("Y: ",y)

        x[0] = 1
        print("X :",x)
        print("Y: ",y)

__main__()
