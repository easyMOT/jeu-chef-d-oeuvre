import curses
from settings import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self, key, game_map):
        new_x, new_y = self.x, self.y
        
        if key == curses.KEY_UP:
            new_y -= 1
        elif key == curses.KEY_DOWN:
            new_y += 1
        elif key == curses.KEY_LEFT:
            new_x -= 1
        elif key == curses.KEY_RIGHT:
            new_x += 1
            
        # Check collision with walls
        if not game_map.is_wall(new_x, new_y):
            self.x, self.y = new_x, new_y
            
    def draw(self, screen):
        screen.addch(self.y, self.x, PLAYER)