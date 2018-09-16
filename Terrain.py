
class Cube:
    #texture yet to be implemented
    #nature is supposed to allow animated and non-cube 'Cube' objects... eventually
    def __init__(self,position,texture,nature = ''):
        self.color = texture
        self.pos = position
        #north,east,south,west,up,down
        self.covered = [1,1,1,1,1,1]
        self.visible = [1,1,1,1,1,1]
    def relative_faces(self,pos):
        x = [self.pos[2]<pos[2],self.pos[0]<pos[0],self.pos[2]>pos[2],self.pos[0]>pos[0],self.pos[1]<pos[1],self.pos[1]>pos[1]]
        self.visible = x

class TerrainGenerator:
    def __init__(self):
        self.map_data = []
        self.cube_list = []
    #generates flat plane of cube objects
    def flat(self):
        for i in range(0,1):
            self.map_data.append([])
            for j in range(0,21):
                self.map_data[i].append([])
                for k in range(0,21):
                    self.map_data[i][j].append(Cube((j,i,k),(15,255,50)))
                    self.cube_list.append(self.map_data[i][j][k])
    #adds ridges to a flat plane
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
                    else:
                        self.map_data[i][j].append(Cube((j,i,k),(15,255,50)))
                        self.cube_list.append(self.map_data[i][j][k])
    def pillars(self):
        self.flat()
        for i in range(1,12):
            self.map_data.append([])
            for j in range(0,21):
                self.map_data[i].append([])
                for k in range(0,21):
                    if not((j-1)%3 or (k-1)%3):
                        self.map_data[i][j].append(Cube((j,i,k),(15,255,50)))
                        self.cube_list.append(self.map_data[i][j][k])
                    else: self.map_data[i][j].append(None)

    #hides cube faces covered by other cubes
    def hideFaces(self):
        height = len(self.map_data)-1
        width = len(self.map_data[0])-1
        length = len(self.map_data[0][0])-1
        for a in range(0,height+1):
            for b in range(0,width+1):
                for c in range(0,length+1):
                    if type(self.map_data[a][b][c]) != Cube: continue
                    #x = [c==length,b==width,c==0,b==0,a==height,a==0]
                    x = [c+1>length or type(self.map_data[a][b][c+1]) != Cube,\
                         b+1>width or type(self.map_data[a][b+1][c]) != Cube,\
                         c-1<0 or type(self.map_data[a][b][c-1]) != Cube,\
                         b-1<0 or type(self.map_data[a][b-1][c]) != Cube,\
                         a+1>height or type(self.map_data[a+1][b][c]) != Cube,\
                         a-1<0 or type(self.map_data[a-1][b][c]) != Cube]
                    
                    self.map_data[a][b][c].covered = x
