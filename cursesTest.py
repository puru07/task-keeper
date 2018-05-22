from curses import wrapper
import curses
import time


def main1(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    stdscr.addstr(1, 0, 'Counter is above')
    for i in range(0, 10):
        stdscr.addstr(0, 0, '#' * i)
        stdscr.addstr(0, i, '>')
        if i == 9:
            stdscr.addstr(2, 0, 'Counter has finished')
        stdscr.refresh()
        time.sleep(0.1)
        #stdscr.getkey()

    stdscr.getkey()


def main(stdscr):
    # Make stdscr.getch non-blocking
    stdscr.nodelay(True)
    stdscr.clear()
    width = 4
    count = 0
    direction = 1
    while True:
        c = stdscr.getch()
        # Clear out anything else the user has typed in
        curses.flushinp()
        stdscr.clear()
        # If the user presses p, increase the width of the springy bar
        if c == ord('p'):
            width += 1
        # Draw a springy bar
        stdscr.addstr("#" * count)
        count += direction
        if count == width:
            direction = -1
        elif count == 0:
            direction = 1
        # Wait 1/10 of a second. Read below to learn about how to avoid
        # problems with using time.sleep with getch!
        time.sleep(0.1)


wrapper(main1)
