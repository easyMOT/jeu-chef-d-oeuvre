import curses
import time
from game import Game

def main():
    # Initialize curses
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    curses.curs_set(0)
    
    try:
        game = Game(screen)
        game.run()
    finally:
        # Clean up curses
        curses.nocbreak()
        screen.keypad(False)
        curses.echo()
        curses.endwin()

if __name__ == "__main__":
    main()