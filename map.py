from settings import *

class Map:
    def __init__(self):
        self.map_data = [
            [WALL] * MAP_WIDTH,
            *[[WALL] + [EMPTY] * (MAP_WIDTH-2) + [WALL] for _ in range(MAP_HEIGHT-2)],
            [WALL] * MAP_WIDTH
        ]
        
        # Add some walls to make it more interesting
        for i in range(5, 15):
            self.map_data[7][i] = WALL
        for i in range(3, 8):
            self.map_data[i][5] = WALL
            
    def is_wall(self, x, y):
        if 0 <= y < len(self.map_data) and 0 <= x < len(self.map_data[0]):
            return self.map_data[y][x] == WALL
        return True
        
    def draw(self, screen):
        for y, row in enumerate(self.map_data):
            for x, cell in enumerate(row):
                screen.addch(y, x, cell)