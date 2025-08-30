from kivy.app import App
from game import Game
from config import WINDOW_WIDTH, WINDOW_HEIGHT
from kivy.core.window import Window

Window.size = (WINDOW_WIDTH, WINDOW_HEIGHT)

class MyGameApp(App):
    def build(self):
        return Game()

if __name__ == '__main__':
    MyGameApp().run()
