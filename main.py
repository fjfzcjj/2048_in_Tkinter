import fundamentals as fund

game = fund.GameWindow()

mat = fund.GameMatrix()
game.bind_label_variable()


mat.check_ava()
mat.drop_num()
mat.check_ava()
mat.drop_num()
game.matrix_sync(mat.scoremat)
game.variable_sync()
game.label_sync()

print(mat.print_mat())



game.mainloop()