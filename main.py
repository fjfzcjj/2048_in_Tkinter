import fundamentals as fund

game = fund.GameWindow()

mat = fund.GameMatrix()

mat.check_ava()
mat.drop_num()
mat.check_ava()
mat.drop_num()
game.matrix_sync(mat.scoremat)
game.variable_sync()
game.bind_label_variable()

print(mat.print_mat())



game.mainloop()