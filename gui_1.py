import tkinter as tk
from tkinter import ttk
win = tk.Tk()

win.title('Python GUI')

aLabel = ttk.Label(win, text ="Enter Your name")
aLabel.grid(column = 0, row = 0)

def ClickMe():
    action.configure(text ="Hello"+name.get())
action = ttk.Button(win, text="Click Me!", command = ClickMe)
action.grid(column = 1, row = 1)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column = 0, row = 1)


win.mainloop()
