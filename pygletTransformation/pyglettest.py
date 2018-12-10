#Get to draw one cube (without vertex lists)
#Change over to vertex lists (not indexed)
#Use batches?
#Do input stuff, probably get rid of InputManager
#Back to original functionality
#???
#Profit

import pyglet
from pyglet.gl import *
from pyglet.window import key
import math

class Model:

    def get_texture(self,file):
        texture = pyglet.image.load(file).texture
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        return pyglet.graphics.TextureGroup(texture)

    def __init__(self):

        self.side = self.get_texture('default.png')

        self.batch = pyglet.graphics.Batch()

        tex_coords = ('t2f',(0,0, 1,0, 1,1, 0,1 ))

        x,y,z = 0,0,-1
        X,Y,Z = x+1,y+1,z+1

        self.batch.add(4,GL_QUADS,self.side,('v3f',(x,y,z, X,y,z, X,Y,z, x,Y,z )),tex_coords)#front
        self.batch.add(4,GL_QUADS,self.side,('v3f',(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z )),tex_coords)#back
        self.batch.add(4,GL_QUADS,self.side,('v3f',(x,y,z, X,y,z, X,y,Z, x,y,Z )),tex_coords)#bottom
        self.batch.add(4,GL_QUADS,self.side,('v3f',(x,Y,z, X,Y,z, X,Y,Z, x,Y,Z )),tex_coords)#top
        self.batch.add(4,GL_QUADS,self.side,('v3f',(x,y,z, x,Y,z, x,Y,Z, x,y,Z )),tex_coords)#left
        self.batch.add(4,GL_QUADS,self.side,('v3f',(X,y,z, X,Y,z, X,Y,Z, X,y,Z )),tex_coords)#right
        #self.batch.add(2,GL_LINES,('c3f',(0,0,0, 0,0,0)),('v3f',(X,Y,Z, 2*X,Y,Z)))

    def draw(self):
        self.batch.draw()

class Player:
    def __init__(self):
        self.pos = [0,0,0]
        self.rot = [0,0]

    def mouse_motion(self,dx,dy):
        dx /= 8; dy /= 8
        self.rot[0] += dy; self.rot[1] -= dx
        if self.rot[0] > 90: self.rot[0] = 90
        elif self.rot[0] < -90: self.rot[0] = -90
                
    def update(self,dt,keys):
        s = dt*2
        rotY = -self.rot[1]/180*math.pi
        dx,dz = s*math.sin(rotY),s*math.cos(rotY)
        
        if keys[key.W]: self.pos[0] += dx; self.pos[2] -= dz
        if keys[key.S]: self.pos[0] -= dx; self.pos[2] += dz
        if keys[key.A]: self.pos[0] -= dz; self.pos[2] -= dx
        if keys[key.D]: self.pos[0] += dz; self.pos[2] += dx

        if keys[key.SPACE]: self.pos[1] += s
        if keys[key.LSHIFT]: self.pos[1] -= s

class Window(pyglet.window.Window):
    def push(self,pos,rot):
        glPushMatrix()
        glRotatef(-rot[0],1,0,0)
        glRotatef(-rot[1],0,1,0)
        glTranslatef(-pos[0],-pos[1],-pos[2])
    
    def Projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
    def Model(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    def set3D(self):
        self.Projection()
        gluPerspective(60,self.width/self.height,0.05,1000)
        self.Model()

    def setLock(self,state):
        self.lock = state
        self.set_exclusive_mouse(state)
    lock = False
    mouse_lock = property(lambda self:self.lock,setLock)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_minimum_size(200,200)
        
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule(self.update)
        
        self.model = Model()
        self.player = Player()

    def on_mouse_motion(self,x,y,dx,dy):
        if self.mouse_lock: self.player.mouse_motion(dx,dy)

    def on_key_press(self,KEY,MOD):
        if KEY == key.ESCAPE:
            self.close()
        elif KEY == key.E:
            self.mouse_lock = not self.mouse_lock

    def update(self,dt):
        self.player.update(dt,self.keys)
    
    def on_draw(self):
        self.clear()
        self.set3D()
        self.push(self.player.pos,self.player.rot)
        self.model.draw()
        glPopMatrix()

window = Window(width=1000,height=800,caption="cubes",resizable=True)
glClearColor(0.5,0.7,0.7,1)
glEnable(GL_DEPTH_TEST)

pyglet.app.run()
