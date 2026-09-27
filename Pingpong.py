import curses
import random
import time
import shutil

_size = shutil.get_terminal_size()
paddle_x = 1
paddle_h = 4

h = max(8, min(20, _size.lines - 2))
w = max(20, min(40, _size.colums -1))

def main(stdscr):
    curses.curs.set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)

    ball_x = w//2
    ball_y = h//2
    dx = random.choice([-1, 1])
    dy = random.choice([-1,1])

    paddle_y = h//2 - paddle_h//2
    score = 0
    game_over = False

    def draw():
        stdscr.erase()
        for x in range(w):
            try:
                stdscr.addch(0, x, '#')
                stdscr.addch(h - 1, x, '#')
            except curses.error:
                pass
            for y in range(h):
                try:
                    stdscr.addch(y, 0, '#')
                    stdscr.addch(y, w - 1, '#')
                except curses.error:
                    pass
            for i in range(paddle_h):
                try:
                    stdscr.addch(paddle_y + i, paddle_x, '|')
                except curses.error:
                    pass
            try:
                stdscr.addch(ball_y, ball_x, 'O')
            except curses.error:
                pass
            try:
                stdscr.addstr(h + 1, 0, f"Счёт: {score} (W - up, S - down, Q - exit)")
            except curses.error:
                pass
            stdscr.refresh()

    def input():
        nonlocal paddle_y, game_over
        while True:
            c = stdscr.getch()
            if c == -1:
                break
            if c in (ord('w'), ord('W')):
                if paddle_y > 1:
                    paddle_y -= 1
            elif c in (ord('s') or ord('S')):
                if paddle_y + paddle_h < h - 1:
                    paddle_y += 1
            elif c in (ord('q') or ord('Q')):
                game_over = True
    
    





