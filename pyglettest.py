import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet.graphics import vertex_list, vertex_list_indexed


class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(resizable=True)

        self.label = pyglet.text.Label("Hello World",
                                       font_name="Courier New",
                                       font_size=36,
                                       x=self.width//2, y=self.height//2,
                                       anchor_x="center", anchor_y="center")

        self.test_list = vertex_list_indexed(4, [0,1,2,0,2,3],
                                             ('v2i',(100,100,150,100,150,150,100,150)),
                                             ('c3B',(0,0,255, 0,0,255, 0,0,255, 0,0,255))
                                            )
    
    def on_draw(self):
        self.clear()
        
        self.test_list.draw(pyglet.gl.GL_QUADS_STRIP)
        self.label.draw()

    def on_mouse_press(self,x,y,button,modifiers):
        if button == mouse.LEFT:
            self.maximize()

#window.push_handlers(pyglet.window.event.WindowEventLogger()
window = HelloWorldWindow()
pyglet.app.run()

print("Hello World")