class Cube:
    #TODO: texture
    def __init__(self,position):
        self.pos = position
        #north,east,south,west,up,down
        self.covered = [1,1,1,1,1,1]
        self.visible = [1,1,1,1,1,1]
        self.adjacent = [None]*6

    #hides faces of the cube the player can't see
    def relative_faces(self,pos):
        x = [self.pos[2]<pos[2],self.pos[0]<pos[0],self.pos[2]>pos[2],\
             self.pos[0]>pos[0],self.pos[1]<pos[1],self.pos[1]>pos[1]]
        self.visible = x

    #hides cube faces covered by other cubes
    def hide_faces(self):
        self.covered = [i != type(Cube) for i in self.adjacent]

    def expand(self,a):
        ptr = self
        new_cubes = []
        for i in range(0,a):
            x = (ptr.pos[0],ptr.pos[1],ptr.pos[2]+1)
            self.adjacent[0] = Cube(x)
            ptr = self.adjacent[0]
            new_cubes.append(ptr)
        return new_cubes

class chunk(self):
    def __init__(self):
        pass

class TerrainGenerator:
    def __init__(self):
        self.origin = Cube((0,0,0))
        self.cube_list = []

    #temporary structures
    def flat(self):
        self.cube_list += self.origin.expand(10)
        ptr = self.origin
        for i in range(0,10):
            ptr
    """
    def bumps(self):
        self.flat()
        height = len(self.map_data)
        self.map_data.append([])
        for i in range(0,10):
            self.map_data[height].append([])
            for j in range(0,10):
                if j%2:
                    self.map_data[height][i].append(Cube((i,height,j),(15,255,50)))
                    self.cube_list.append(self.map_data[height][i][j])
                else: self.map_data[height][i].append(None)
    #one cube(debug purposes)
    def one(self):
        self.map_data = [[[Cube((0,0,0),(15,255,50))]]]
        self.cube_list.append(self.map_data[0][0][0])
    #generates a tunnel made of cube objects
    def tunnel(self):
        for i in range(0,10):
            self.map_data.append([])
            for j in range(0,10):
                self.map_data[i].append([])
                for k in range(0,10):
                    if 0<i<9 and 0<j<9: self.map_data[i][j].append(None)
    """
    
