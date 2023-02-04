import subprocess
import curses

def print_menu(stdscr):
    curses.curs_set(0)
    stdscr.addstr(0, 0, "Please select an option:")
    stdscr.addstr(1, 0, "1. Order")
    stdscr.addstr(2, 0, "2. Admin Console")
    stdscr.addstr(3, 0, "3. Exit")
    stdscr.refresh()

    key = stdscr.getkey()

    if key == "1":
        subprocess.Popen(["start", "cmd", "/c", "python", r"C:\Users\comic\Documents\GitHub\order\order.py"], cwd=r"C:\Users\comic\Documents\GitHub\order")
    elif key == "2":
        subprocess.Popen(["start", "cmd", "/c", "python", r"C:\Users\comic\Documents\GitHub\order\admin-console.py"], cwd=r"C:\Users\comic\Documents\GitHub\order")
    elif key == "3":
        curses.endwin()

curses.wrapper(print_menu)
