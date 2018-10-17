import math

class Cube:
    #TODO: texture
    def __init__(self,position):
        self.pos = position
        #north,east,south,west,up,down
        self.covered = [1,1,1,1,1,1]
        self.visible = [1,1,1,1,1,1]

    #hides faces of the cube the player can't see
    def relative_faces(self,pos):
        x = [self.pos[2]<pos[2],self.pos[0]<pos[0],self.pos[2]>pos[2],\
             self.pos[0]>pos[0],self.pos[1]<pos[1],self.pos[1]>pos[1]]
        self.visible = x

    #hides cube faces covered by other cubes
    def hide_faces(self):
        #self.covered = [i != type(Cube) for i in self.adjacent]
        pass

class Octree:
    def __init__(self,_pos=None,_level=0):
        self.octants = [None]*8
        self.pos = pos
        self.level = _level

    def define(self,cube):
        x,y,z = cube.pos
        x1,y1,z1 = (0,0,0)
        x2,y2,z2 = (0,0,0)
        
        if self.level = 0:
            x1,y1,z1 = self.pos
            x2,y2,z2 = (2**x1-1+x,2**y1-1+y,2**z1-1+z)

            if x2<x<x2-1 or y2<y<y2-1 or z2<z<z2-1:
                sup = Octree(None,self.level+1)
                sup.octants[0] = self
                sup.octants[1] = Octree((1,0,0))
                sup.octants[1].octants[0] = cube
                return sup
        else:
            pass

        if type(self.octants[quad]) == Cube:
            temp = self.octants[quad]
            self.octants[quad] = Octree()
            self.octants[quad].octants[0] = temp
            self.octants[quad].octants[1] = cube
        

class TerrainGenerator:
    def __init__(self):
        self.map = Octree((0,0,0))
        self.start()
        
        self.cube_list = []
        self.cube_list.append(self.map.octants[0])
        self.cube_list.append(self.map.octants[1])
        
    def start(self):
        self.map.octants[0] = Cube((0,0,0)); self.map.octants[1] = Cube((1,0,0))
        self.map.octants[2] = Cube((0,0,1)); self.map.octants[3] = Cube((1,0,1))
        self.map.octants[4] = Cube((0,1,0)); self.map.octants[5] = Cube((1,1,0))
        self.map.octants[6] = Cube((0,1,1)); self.map.octants[7] = Cube((1,1,1))

    def test(self):
        c = Cube((2,0,0))
        self.map.define(c)
        #self.cube_list.append(c)
