import classes as clss

game = clss.GameWindow()

game.makegrids()
game.maketiles()
mat = clss.GameMatrix()

mat.check_ava()
mat.droptwoorfour()
mat.check_ava()
mat.droptwoorfour()
game.matrix_sync(mat.scoremat)
game.mat_varibales()
game.bind_label_variable()

game.mainloop()