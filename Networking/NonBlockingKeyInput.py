import curses
import datetime

stdscr = curses.initscr()
curses.noecho()
stdscr.nodelay(1)
stdscr.addstr(0, 0, 'Press "p" to show count, "q" to exit...')

line = 1
try:
    while 1:
        c = stdscr.getch()
        if c == ord('p'):
            stdscr.addstr(line, 0, "Some text here")
            line += 1
        elif c == ord('q'):
            break
        elif c != -1:
            print(c)

        # Do more things

finally:
    curses.endwin()
