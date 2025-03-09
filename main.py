from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, height, width):
        self.__root = Tk()
        self.__root.title("Maze Solver") 
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack()
        self.is_running = False
