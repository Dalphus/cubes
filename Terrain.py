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

class TerrainGenerator:
    def __init__(self):
        self.map = Octree()
        self.map.octants[0] = Cube((0,0,0))
        self.cube_list = [self.map.octants[0]]

    def test(self):
        c = Cube((1,0,0))
        self.define(c)

    def define(self,cube):
        level = []
        max_level = self.map.level
        for i in range(0,3):
            if cube.pos[i] != 0:
                max_level = max(max_level,int(math.log2(cube.pos[0])))
            
            level[i] = [int(i) for i in bin(cube.pos[i])[2:]]

        temp = self.map
        if self.map.level < max_level:
            self.map = Octree(max_level)
            self.map.octants[0] = temp
        
        for i in range(0,3):
            level[i] = [0 for i in range(len(level[i])-1,max_level)] + level[i]

        temp = self.map
        ctr = 0
        while temp.level > 0:
            index = level[0][ctr] + 2*level[1][ctr] + 4*level[2][ctr]
            if not isinstance(temp.octants[index],Octree):
                temp.octants[index] = Octree(max_level-ctr-1)
            temp = temp.quadrants[index]
            ctr += 1

        index = x1[max_level] + 2*y1[max_level]
        temp.quadrants[index] = s
        square_list.append(s)
