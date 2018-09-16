import pygame, math

#swanky arrays
verticies = [(0,0,0),(0,1,0),(1,0,0),(1,1,0),\
             (0,0,1),(0,1,1),(1,0,1),(1,1,1)]
#north,east,south,west,up,down
faces = [(4,5,7,6),(2,3,7,6),(0,1,3,2),(4,5,1,0),(1,5,7,3),(0,4,6,2)]
#green,pink,purple,blue,turquoise,yellow
colors = [(0,255,0),(255,192,203),(160,32,240),\
          (0,0,255),(64, 224, 208),(255,255,0)]

class Render:
    def rotate2D(pos,rad):
        x,y = pos
        s,c = math.sin(rad),math.cos(rad)
        return x*c-y*s, y*c+x*s

    def distance3D(pos1,pos2):
        x = math.hypot(pos1[0]-pos2[0],pos1[2]-pos2[2])
        return math.hypot(x,pos1[1]-pos2[1])**2
    
    def render(window,cubes,player):
        w,h = list(window.get_rect())[2:]
        w //= 2
        h //= 2
        draw_queue = []
        for cube in cubes:
            for face in range(0,len(faces)):
                if not cube.covered[face] or not cube.visible[face]: continue
                total_dist = 0
                points = []
                can_draw = 0
                for vertex in faces[face]:
                    x,y,z = cube.pos
                    x1,y1,z1 = verticies[vertex]
                    x+=x1;y+=y1;z+=z1
                    
                    total_dist += Render.distance3D((x,y,z),player.pos())
                    
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
                        points.append((w+int(x),h+int(y)))
                        can_draw += 1
                    else:
                        if x < 0: x = 0
                        elif x > 0: x = 2*w
                        if y < 0: y = 0
                        elif y > 0: y = 2*h
                        points.append((int(x),int(y)))
                        
                if can_draw > 0:
                    draw_queue.append((total_dist,points,colors[face]))

        #draws polygons
        draw_queue.sort(reverse=True)
        for i in range(0,len(draw_queue)):
            a,b,c = draw_queue[i]
            pygame.draw.polygon(window,c,b)
