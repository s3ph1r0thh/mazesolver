from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.running = False
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(bg="white", height=height, width=width)
        self.__canvas.pack()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            time.sleep(0.01)
        print("window closed...")

    def close(self):
        self.running = False

def main():
    win = Window(800, 600)
    win.wait_for_close()