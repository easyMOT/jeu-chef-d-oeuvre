import curses
from player import Player
from map import Map
from settings import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.map = Map()
        self.player = Player(5, 5)
        
    def handle_input(self):
        key = self.screen.getch()
        if key == ord('q'):
            self.running = False
        elif key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            self.player.move(key, self.map)
            
    def draw(self):
        self.screen.clear()
        # Draw map
        self.map.draw(self.screen)
        # Draw player
        self.player.draw(self.screen)
        self.screen.refresh()
        
    def run(self):
        while self.running:
            self.draw()
            self.handle_input()