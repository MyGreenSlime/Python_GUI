import tkinter as tk
from tkinter import ttk
win = tk.Tk()

win.title('Python GUI')

aLabel = ttk.Label(win, text ="Enter Your name")
aLabel.grid(column = 0, row = 0)

def ClickMe():
    action.configure(text ="Hello"+name.get()+" "+number.get())
action = ttk.Button(win, text="Click Me!", command = ClickMe)
action.grid(column = 2, row = 1)

name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column = 0, row = 1)

ttk.Label(win, text = 'Choose number:').grid(column = 1, row = 0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width = 12, textvariable=number)
number_chosen['value'] = (1,2,4,42,100)
number_chosen.grid(column = 1, row = 1)
number_chosen.current(0)

name_entered.focus() #place cursor into text box

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text = 'Disabled', variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column = 0, row = 4, sticky = tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text = 'Unchecked', variable = chVarUn)
check2.deselect()
check2.grid(column = 1, row = 4, sticky = tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text = 'Enabled', variable = chVarEn)
check3.select()
check3.grid(column = 2, row = 4, sticky = tk.W)


win.mainloop()
