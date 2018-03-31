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
        self.padding = 5
        self.windowsize = (self.winfo_screenheight(), self.winfo_screenheight())
        self.bg_dict = {None: "f5f5f5", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
                                 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
                                 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
        self.cell_dict = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                           32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
                           512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}
        main_options = {"height" : self.windowsize[0],
                        "width" : self.windowsize[1],
                        'bg' : "white",
                        'padx' : self.padding,
                        'pady' : self.padding
        }
        self.config(main_options)
        self.title('Game of 2048')
        self.resizable(width=False, height=False)
        self.variables = [tk.IntVar() for _ in range(16)]
        # Arranged in a left to right order from Top-left corner.
        self.matrix = None

    def makegrids(self):
        background_cells = \
        [tk.Frame(self, bg = "gray", height = self.windowsize[0]//5, width = self.windowsize[1]//5) for _ in range(16)]
        for i , cell in enumerate(background_cells):
            cell.grid(row = i//4, column = i % 4, padx= self.padding, pady=self.padding)

    def maketiles(self):
        fg_tiles_options = {'bg' : "black",
                            'height' : self.windowsize[0]//5,
                            'width' : self.windowsize[1]//5
        }

        self.foreground_tiles = \
        [tk.Frame(self, **fg_tiles_options) for _ in range(16)]

        for i, tile in enumerate(self.foreground_tiles):
            tile.grid(row = i //4, column = i % 4 , padx = self.padding, pady = self.padding)

    def matrix_sync(self, matrix):
        self.matrix = matrix


    def mat_varibales(self):
        """Spot to spot synchronises matrix with label from Top left corner. """
        for i, var in enumerate(self.variables):
            var.set(self.matrix[i//4][i%4])


    def bind_label_variable(self):
        """Labels stay in spot."""
        self.labels = [tk.Label(self.foreground_tiles[i]) for i in range(16)]
        for i, label in enumerate(self.labels):
            display = self.variables[i].get()
            print(display)
            label.config(text = display, font = self.FONT, fg = "black", justify = "center", bg = "gray")
            label.pack()

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
"""This module makes up the matrix part of the game. It doesn't have anything to do with the interface but it
 does do the most important job in the program, namely, the calculation part.
 The default coordinate system of matrix here is that [0][0] represents the top left corner of the tiles 
 since ordinarily in programming, (x,y) starts at the top left corner."""
        return definition

    def _tell_pos(self,tuple = None):
        if tuple == None:
            print("Tell me a set of [a][b].")
        else:
            a,b = tuple
            print("This tile sits at column: ", a , "\nRow: ", b)

    def check_ava(self):
        availability = None
        del self.available[:]
        for a in range(4):
            for b in range(4):
                if self.scoremat[a][b] == 0:
                    availability = True
                    self.available.append((a,b))

        if availability == True:
            self.ava_bool = True
            return True

        else:
            self.ava_bool = False
            return False

    def droptwoorfour(self):

        if self.ava_bool == True:
            chance = random.randint(1,100)
            choice = random.choice(self.available)
            a,b = choice
            if 0 < chance <= 90:
                self.scoremat[a][b] = 2
                print("A 2 has been dropped.")
            elif 90 < chance <= 100:
                self.scoremat[a][b] = 4
                print("A 4 has been dropped.")
            else:
                print("Something goes wrong at dropping 2 or 4.")

        else:
            self.gameend()

    def mash(self):
        """This functions defines mash movements in all directions."""
        pass




    def print_mat(self):
        print(repr(self.scoremat))

    def game_end(self):
        pass

class StatsWindow(tk.Tk):
    pass