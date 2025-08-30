from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from random import randint

from entities.player import Player
from entities.enemy import Enemy
from entities.platform import Platform
from entities.collectible import Collectible
from hud import HUD
from config import *

class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.level = 1
        self.player = None
        self.enemies = []
        self.platforms = []
        self.collectibles = []
        self.hud = None

        # Background
        with self.canvas.before:
            Color(0.8, 0.8, 0.8, 1)
            self.bg = Rectangle(size=(WINDOW_WIDTH, WINDOW_HEIGHT), pos=(0, 0))

        self.setup_world()
        Window.bind(on_key_down=self.on_key_down)
        Clock.schedule_interval(self.update, 1 / 30)

    def setup_world(self):
        floor = Platform(size=(WINDOW_WIDTH, FLOOR_HEIGHT), pos=(0, 0))
        block1 = Platform(size=(200, 20), pos=(200, 200))
        block2 = Platform(size=(150, 20), pos=(500, 350))
        self.platforms += [floor, block1, block2]

        for p in self.platforms:
            self.add_widget(p)

        self.player = Player(size=PLAYER_SIZE, pos=PLAYER_START_POS)
        self.add_widget(self.player)

        self.hud = HUD(pos=(10, WINDOW_HEIGHT - 40))
        self.add_widget(self.hud)

        self.spawn_enemies(3)
        self.spawn_collectibles(3)

    def spawn_enemies(self, count):
        for _ in range(count):
            enemy = Enemy(size=ENEMY_SIZE, pos=(randint(200, WINDOW_WIDTH-100), 40))
            self.enemies.append(enemy)
            self.add_widget(enemy)

    def spawn_collectibles(self, count):
        for _ in range(count):
            coin = Collectible(size=COIN_SIZE,
                               pos=(randint(100, WINDOW_WIDTH-100), randint(100, 400)))
            self.collectibles.append(coin)
            self.add_widget(coin)

    def on_key_down(self, instance, key, scancode, codepoint, modifier):
        if key == 276:  # Left
            self.player.x -= 20
        elif key == 275:  # Right
            self.player.x += 20
        elif key == 273:  # Up
            self.player.jump()

    def update(self, dt):
        self.player.move(self.platforms)

        # Enemy movement + collisions
        for enemy in self.enemies[:]:
            enemy.move()
            if self.player.collide_widget(enemy):
                if self.player.velocity_y < 0 and self.player.y > enemy.y + enemy.height / 2:
                    self.remove_widget(enemy)
                    self.enemies.remove(enemy)
                    self.player.score += 1
                    self.player.velocity_y = self.player.jump_power // 2
                else:
                    self.player.lives -= 1
                    self.player.pos = PLAYER_START_POS
                    if self.player.lives <= 0:
                        self.end_game("GAME OVER", (1, 0, 0, 1))
                        return

        # Collectibles
        for coin in self.collectibles[:]:
            if self.player.collide_widget(coin):
                self.remove_widget(coin)
                self.collectibles.remove(coin)
                self.player.score += 5

        # Level progression
        if len(self.enemies) == 0:
            if self.level == 1:
                self.next_level()
            else:
                self.end_game("YOU WIN 🎉", (0, 1, 0, 1))

        self.hud.update(self.player, self.level)

    def next_level(self):
        self.level = 2
        self.player.jump_power = LEVEL2_JUMP_POWER
        self.spawn_enemies(6)
        self.spawn_collectibles(5)

    def end_game(self, message, color):
        from kivy.uix.label import Label
        self.clear_widgets()
        self.add_widget(Label(text=message, font_size=50,
                              center=self.center, color=color))
