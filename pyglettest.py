import pyglet
from pyglet.window import key
from pyglet.window import mouse

class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super(HelloWorldWindow,self).__init__()

        self.label = pyglet.text.Label("Hello World",
                                       font_name="Courier New",
                                       font_size=36,
                                       x=self.width//2, y=self.height//2,
                                       anchor_x="center", anchor_y="center")
    
    def on_draw(self):
        self.clear()
        self.label.draw()

    def on_mouse_press(self,x,y,button,modifiers):
        if button == mouse.LEFT:
            self.maximize()

#window.push_handlers(pyglet.window.event.WindowEventLogger()
window = HelloWorldWindow()
pyglet.app.run()

print("Hello World")