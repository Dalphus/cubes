
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

class Chunk:
    def __init__(self,position,height):
        self.pos = position
        self.block_map = []
        self.cube_list = []

        for i in range(0,32):
            self.block_map.append([])
            for j in range(0,16):
                self.block_map[i].append([])
                for k in range(0,height):
                    if i < 16:
                        self.block_data[i][j].append(Cube((j,i,k),(15,255,50)))
                        self.block_data.append(self.block_data[i][j][k])
                    else:
                        self.block_data[i][j].append(None)


class TerrainGenerator:
    def __init__(self):
        self.chunk_list = [[Chunk((0,0),16)]]

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
