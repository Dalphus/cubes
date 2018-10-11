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
    def __init__(self,_level=0):
        self.octants = [None]*8
        self.level = _level
        
    def start(self):
        self.octants[0] = Cube((0,0,0)); self.octants[1] = Cube((1,0,0))
        self.octants[2] = Cube((0,0,1)); self.octants[3] = Cube((1,0,1))
        self.octants[4] = Cube((0,1,0)); self.octants[5] = Cube((1,1,0))
        self.octants[6] = Cube((0,1,1)); self.octants[7] = Cube((1,1,1))
        
    def raise_level(self):
        x = Octree(self.level+1)
        x.octants[0] = self
        return x

class TerrainGenerator:
    def __init__(self):
        self.map = Octree()
        self.map.start()
        
        self.cube_list = []

    def test(self):
        self.cube_list += self.map.octants
    
