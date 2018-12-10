import pyglet
from pyglet.gl import *


class Quad2:
    def __init__(self):
        self.indices = [0,1,2,3,0]
        self.points = [-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]
        self.colors = [1.0,0.0,0.0, 0.0,1.0,0.0, 0.0,0.0,1.0, 1,1,1]
        
        self.vertices = pyglet.graphics.vertex_list_indexed(\
            4, self.indices, ('v3f', self.points), ('c3f', self.colors)\
        )

class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.set_minimum_size(400,300)
        glClearColor(0.0, 0.0, 0.0, 1.0)

        self.quad2 = Quad2()

    def on_draw(self):
        self.clear()
        self.quad2.vertices.draw(GL_QUADS)

    def on_resize(self, width, height):
        glViewport(0,0, width,height)

window = MyWindow(1280, 720, "Hello Triangle", resizable = True)
pyglet.app.run()
