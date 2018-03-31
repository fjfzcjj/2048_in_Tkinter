import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(3)  # initializing the choice, i.e. Python

languages = [
    ("Python"),
    ("Perl"),
    ("Java"),
    ("C++"),
    ("C")
]

def ShowChoice():
    print(v.get())

tk.Label(root,
         text="""Choose your favourite 
programming language:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root,
                  text=language,
                  padx = 20,
                  width = 20,
                  variable=v,
                  command=ShowChoice,
                  value=val,
                  indicatoron = 0).pack(anchor=tk.W)


root.mainloop()