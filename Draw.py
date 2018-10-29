import pygame, math
import numpy as np
from Terrain import Octree

#swanky arrays
verticies = [(0,0,0),(0,1,0),(1,0,0),(1,1,0),\
             (0,0,1),(0,1,1),(1,0,1),(1,1,1)]
edges = [(0,1),(0,2),(1,3),(2,3),\
         (4,5),(4,6),(5,7),(6,7),\
         (0,4),(1,5),(2,6),(3,7)]
#north,east,south,west,up,down
faces = [(4,5,7,6),(2,3,7,6),(0,1,3,2),(4,5,1,0),(1,5,7,3),(0,4,6,2)]
#green,pink,purple,blue,turquoise,yellow
colors = [(0,255,0),(255,192,203),(160,32,240),\
          (0,0,255),(64, 224, 208),(255,255,0)]

class Render:
    @classmethod
    def __init__(cls,size=(512,512)):
        cls.world_surface = pygame.Surface(size)
        cls.w = size[0]//2
        cls.h = size[1]//2

        cls.line_queue = []
        cls.cursor_queue = []
    
    def rotate2D(pos,rad):
        x,y = pos
        s,c = math.sin(rad),math.cos(rad)
        return x*c-y*s, y*c+x*s

    def distance3D(pos1,pos2):
        x = math.hypot(pos1[0]-pos2[0],pos1[2]-pos2[2])
        return math.hypot(x,pos1[1]-pos2[1])

    @classmethod
    def translate_point(cls,point,player):
        x,y,z = point
        #player position displacment
        x -= player.x
        y -= player.y
        z -= player.z
        y*= -1

        #camera rotation
        x,z = Render.rotate2D((x,z),player.yaw)
        z,y = Render.rotate2D((z,y),player.pitch)

        #depth compensation
        if z > .01:
            f = 200/z
            x *= f
            y *= f
            return (cls.w+int(x),cls.h+int(y),1)
        else:
            if x < 0: x = 0
            elif x > 0: x = 2*cls.w
            if y < 0: y = 0
            elif y > 0: y = 2*cls.h
            return (int(x),int(y),0)

    @classmethod
    def cubes(cls,cubes,player):
        cls.cube_queue = []
        for cube in cubes:
            for face in range(0,6):
                if not cube.covered[face] or not cube.visible[face]: continue
                total_dist = 0
                points = []
                can_draw = 0

                for vertex in faces[face]:
                    x,y,z = cube.pos
                    x1,y1,z1 = verticies[vertex]
                    x+=x1;y+=y1;z+=z1
                    
                    total_dist += Render.distance3D((x,y,z),player.pos())**2
                    x,y,z = cls.translate_point((x,y,z),player)
                    points.append((x,y))
                    can_draw += z
                        
                if can_draw != 0:
                    cls.cube_queue.append((total_dist,points,colors[face]))
    pass

    @classmethod
    def octree(cls,ot,player,pos=(0,0,0)):
        scale = (2**(ot.level+1))
        for edge in edges:
            points = []
            can_draw = 0

            for vertex in edge:
                x,y,z = pos
                x1,y1,z1 = verticies[vertex]
                x+=x1*scale;y+=y1*scale;z+=z1*scale

                x,y,z = cls.translate_point((x,y,z),player)
                points.append((x,y))
                can_draw += z

            if can_draw != 0:
                cls.line_queue.append((points,(0,255,75)))
        
        bonus = 2**(ot.level)
        for i in range(0,8):
            if isinstance(ot.octants[i],Octree):
                cls.octree(ot.octants[i],player,(pos[0]+(i%2)*bonus,pos[1]+(i%4>1)*bonus,pos[2]+int(i/4)*bonus))
    pass
    
    @classmethod
    def cursor(cls,cursor,player):
        for edge in edges:
            points = []
            can_draw = 0

            for vertex in edge:
                x,y,z = cursor.pos()
                x1,y1,z1 = verticies[vertex]
                x+=x1;y+=y1;z+=z1

                x,y,z = cls.translate_point((x,y,z),player)
                points.append((x,y))
                can_draw += z

            if can_draw != 0:
                cls.cursor_queue.append((points,(0,0,0)))
    
    @classmethod
    def draw(cls):
        #draws polygons
        cls.cube_queue.sort(reverse=True)
        cls.world_surface.fill((255,255,255))
        
        for i in range(0,len(cls.cube_queue)):
            a,b,c = cls.cube_queue[i]
            pygame.draw.polygon(cls.world_surface,c,b)

        for i in range(0,len(cls.line_queue)):
            b,c = cls.line_queue[i]
            pygame.draw.line(cls.world_surface,c,b[0],b[1],5)
        cls.line_queue = []

        for i in range(0,len(cls.cursor_queue)):
            b,c = cls.cursor_queue[i]
            pygame.draw.line(cls.world_surface,c,b[0],b[1],1)
        cls.cursor_queue = []