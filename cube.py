import pygame, sys, math
pygame.init()

#swanky arrays
verticies = [(0,0,0),(0,1,0),(1,0,0),(1,1,0),\
             (0,0,1),(0,1,1),(1,0,1),(1,1,1)]
#north,east,south,west,up,down
faces = [(4,5,7,6),(2,3,7,6),(0,1,3,2),(4,5,1,0),(1,5,7,3),(0,4,6,2)]
#green,pink,purple,blue,turquoise,yellow
colors = [(0,255,0),(255,192,203),(160,32,240),\
          (0,0,255),(64, 224, 208),(255,255,0)]

#class that holds camera information
#could be used to have multiple players maybe
class Player:
    def __init__(self,position=(0,0,0),rotation=(0,0)):
        self.x,self.y,self.z = position
        self.yaw,self.pitch = rotation
    
    def update(self,key,dt):
        s,c = math.sin(self.yaw),math.cos(self.yaw)
        #wasd movement relative to camera angle
        if key[pygame.K_w]:
            self.z += dt*c
            self.x += dt*s
        if key[pygame.K_s]:
            self.z -= dt*c
            self.x -= dt*s
        if key[pygame.K_d]:
            self.z -= dt*s
            self.x += dt*c
        if key[pygame.K_a]:
            self.z += dt*s
            self.x -= dt*c
        #up/down
        if key[pygame.K_SPACE]: self.y -= dt
        if key[pygame.K_LSHIFT]: self.y += dt
        #looking around
        if key[pygame.K_LEFT]: self.yaw -= dt
        if key[pygame.K_RIGHT]: self.yaw += dt
        if key[pygame.K_UP] and self.pitch < math.pi/2-.2:
            self.pitch += dt
        if key[pygame.K_DOWN] and self.pitch > -1*math.pi/2+.2:
            self.pitch -= dt
            
    def pos(self):
        return (self.x,self.y,self.z)

#i have no clue wtf im doing
class TerrainGenerator:
    def __init__(self):
        self.map_data = []
        self.cube_list = []
    #generates flat plane of cube objects
    def flat(self):
        for i in range(0,2):
            self.map_data.append([])
            for j in range(0,10):
                self.map_data[i].append([])
                for k in range(0,10):
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
                    
                    self.map_data[a][b][c].face_visible = x

class Cube:
    #texture yet to be implemented
    #nature is supposed to allow animated and non-cube 'Cube' objects... eventually
    def __init__(self,position,texture,nature = ''):
        self.color = texture
        self.pos = position
        #north,east,south,west,up,down
        self.face_visible = [1,1,1,1,1,1]
        #is_covered
        #is_visible
    def relative_faces(self,pos):
        x = [self.pos[2]<pos[2],self.pos[0]<pos[0],self.pos[2]>pos[2],self.pos[0]>pos[0],-self.pos[1]>pos[1],-self.pos[1]<pos[1]]
        self.face_visible = x
        
#calculates and draws polygons
class Render:
    def rotate2D(pos,rad):
        x,y = pos
        s,c = math.sin(rad),math.cos(rad)
        return x*c-y*s, y*c+x*s

    def distance3D(pos1,pos2):
        x = math.hypot(pos1[0]-pos2[0],pos1[2]-pos2[2])
        return math.hypot(x,pos1[1]-pos2[1])**2
    
    def render(self,window,cubes,player):
        w,h = list(window.get_rect())[2:]
        w //= 2
        h //= 2
        draw_queue = []
        for cube in cubes:
            for face in range(0,len(faces)):
                if not cube.face_visible[face]: continue
                total_dist = 0
                points = []
                can_draw = True
                for vertex in faces[face]:
                    x,y,z = cube.pos
                    x1,y1,z1 = verticies[vertex]
                    x+=x1;y+=y1;z+=z1
                    y*=-1
                    total_dist += Render.distance3D((x,y,z),player.pos())
                    
                    #player position displacment
                    x -= player.x
                    y -= player.y
                    z -= player.z
                    #camera rotation
                    x,z = Render.rotate2D((x,z),player.yaw)
                    z,y = Render.rotate2D((z,y),player.pitch)
                    
                    #depth compensation
                    if z <= .01:
                        can_draw = False
                        break
                    f = 200/z
                    x *= f
                    y *= f
                
                    points.append((w+int(x),h+int(y)))
                if can_draw:
                    draw_queue.append((total_dist,points,colors[face]))

        #draws polygons
        draw_queue.sort(reverse=True)
        for i in range(0,len(draw_queue)):
            a,b,c = draw_queue[i]
            pygame.draw.polygon(window,c,b)

#shit gets real    
class __main__:
    
    def __init__(self):
        #screen variables
        w,h = 400,400

        #pygame shit
        window = pygame.display.set_mode((w,h))
        clock = pygame.time.Clock()

        #terrain generation maybe
        world = TerrainGenerator()
        world.tunnel()
        #world.hideFaces()

        #other shit idk
        draw_thingy = Render()
        Mae_Weller = Player((0,0,-5))
        font = pygame.font.SysFont('Courier', 20)
        
        #game loop
        while True:
            #time since last call, in millis maybe
            dt = clock.tick()/200
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); sys.exit()

            for a in world.cube_list:
                a.relative_faces(Mae_Weller.pos())
            
            #outsourcing graphics to Render object
            window.fill((255,255,255))
            draw_thingy.render(window,world.cube_list,Mae_Weller)

            #print out fps
            fps = font.render(str(int(clock.get_fps())),True,(0,255,0))
            window.blit(fps,(20,20))
    
            pygame.display.flip()
            Mae_Weller.update(pygame.key.get_pressed(),dt)
__main__()

