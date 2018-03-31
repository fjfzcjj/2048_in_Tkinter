import tkinter as tk
import tk_tools
import itertools
import random
import time
import matplotlib as mpl
import numpy as np


class GameWindow(tk.Tk):
    def __init__(self):
        self.FONT = ("Verdana", 40, "bold" )
        super().__init__()
        self.padding = 10
        self.windowsize = (self.winfo_screenheight(), self.winfo_screenheight())
        self.bg_dict = {0: '#9e948a', 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
                                 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
                                 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
        self.cell_dict ={0: "gray", 2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                            32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
                            512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}

        main_options ={ 'bg' : "#92877d",
                        'padx' : self.padding,
                        'pady' : self.padding}
        self.config(main_options)
        self.title('Game of 2048')
        self.resizable(width = False, height = False)
        self.variables = [tk.IntVar() for _ in range(16)]
        # Arranged in a left to right order from Top-left corner.
        self.matrix = None


        def makegrids():
            """Bg tiles stay in place. They will never ever move."""
            background_cells = \
                [tk.Frame(self, bg= self.bg_dict[0], height=self.windowsize[0] // 5, width=self.windowsize[1] // 5) for _ in
                 range(16)]

            for i, cell in enumerate(background_cells):
                cell.grid(row=i // 4, column=i % 4, padx=self.padding, pady=self.padding)
                # Place bg_cells into grids. [row][column]
        makegrids()

        def maketiles():
            self.fg_tiles =[tk.Frame(self, bg=self.bg_dict[0], height = self.windowsize[0] // 5,\
                                width = self.windowsize[1] // 5) for _ in range(16)]

            for i, tile in enumerate(self.fg_tiles):
                tile.grid(row=i // 4, column=i % 4, padx=self.padding, pady=self.padding)
                tile.pack_propagate(False)
        maketiles()

    def bind_label_variable(self):
        """Labels stay in spot."""
        self.labels = [tk.Label(master = self.fg_tiles[i]) for i in range(16)]
        for i, label in enumerate(self.labels):
            display = self.variables[i].get()
            label.config(text = display, font = self.FONT, fg = "black", justify = "center", bg = "gray")
            label.place(relx = 0.5, rely= 0.5, anchor = 'center')

    def matrix_sync(self, matrix):
        """
        Updates the matrix inside object 'GameWindow'. Because the original matrix manipulation doesn't run within
        this class.

        :param matrix: Obtained from class Game_Matrix
        """

        self.matrix = matrix

    def variable_sync(self):
        """Spot to spot synchronises matrix with label from Top left corner. """

        for i, var in enumerate(self.variables):
            var.set(self.matrix[i//4][i%4])

    def label_sync(self):
        for i, label in enumerate(self.labels):
            num = self.variables[i].get()
            if num == 0:
                label.config(text=num, fg=self.bg_dict[0], bg=self.bg_dict[0])
            else:
                label.config(text = num, fg = self.cell_dict[num], bg= self.bg_dict[num])



class GameMatrix():
    @staticmethod
    def matcreator(x = 4,y = 4):
        """Number matrix by default is using x as top level, y as second level.
        This is a staticmethod because we don't actually need it in the object.
        We can also define this inside __init__() since "if we only use it locally, why not define it locally?".
        """
        matrix = [[0 for _ in range(y)] for _ in range(x)]
        return matrix

    def __init__(self):

        created = self.matcreator()
        self.scoremat = [ a[:] for a in created]
        self.spacetile = []
        self.available = []

    def __str__(self):

        definition = \
        """Matrix manipulations part of the program.
        self.scoremat[1][3] stands for row 2 column 4.
        [0][0] is top-left corner. 
        """
        return definition

    # def tell_pos(self,tuple = None):
    #     if tuple == None:
    #         print("Tell me a set of [a][b].")
    #     else:
    #         a, b = tuple
    #         print("This tile sits at column: ", a , "\nRow: ", b)

    def check_ava(self):
        """
        Checks which tiles are empty.
        Automatically clean up previous stored values when called.

        :return: True or False, used to determinate the end of game.
        """
        
        availability = None
        del self.available[:]
        for a in range(4):
            for b in range(4):
                if self.scoremat[a][b] == 0:
                    availability = True
                    self.available.append((a, b))

        if availability == True:
            self.ava = True
            return True

        else:
            self.ava = False
            return False

    def drop_num(self):
        if self.ava == True:
            num = random.randint(1 , 100)
            choice = random.choice(self.available)
            a , b = choice
            if 0 < num <= 90:
                self.scoremat[a][b] = 2
                print("A 2 has been dropped.")
            elif 90 < num <= 100:
                self.scoremat[a][b] = 4
                print("A 4 has been dropped.")
            else:
                print("Something goes wrong at dropping 2 or 4.")

        else:
            self.game_end()

    def mash(self):
        """This functions defines mash movements in all directions.
        Logic is the most important part of this function.
        """
        pass

    def print_mat(self):
        print(repr(self.scoremat))

    def game_end(self):
        pass

class StatsWindow(tk.Tk):
    pass