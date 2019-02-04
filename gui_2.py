import tkinter as tk
from tkinter  import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title('Python Gui')
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = 'Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = 'Tab 2')
tabControl.pack(expand = 1, fill = 'both')

mighty = ttk.LabelFrame(tab1, text = 'Mighty Python')
mighty.grid(column = 0, row = 0, padx = 8, pady = 4)

aLabel = ttk.Label(mighty, text ="Enter Your name")
aLabel.grid(column = 0, row = 0)

def ClickMe():
    action.configure(text ="Hello"+name.get()+" "+number.get())
action = ttk.Button(mighty, text="Click Me!", command = ClickMe)
action.grid(column = 2, row = 1)

name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column = 0, row = 1)

ttk.Label(mighty, text = 'Choose number:').grid(column = 1, row = 0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width = 12, textvariable=number)
number_chosen['value'] = (1,2,4,42,100)
number_chosen.grid(column = 1, row = 1)
number_chosen.current(0)

name_entered.focus() #place cursor into text box

scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(mighty, width = scrolW, height = scrolH, wrap = tk.WORD)
scr.grid(column = 0, columnspan = 3)


mighty2 = ttk.LabelFrame(tab2, text = 'Mighty Python')
mighty2.grid(column = 0, row = 0, padx = 8, pady = 4)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text = 'Disabled', variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column = 0, row = 4, sticky = tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text = 'Unchecked', variable = chVarUn)
check2.deselect()
check2.grid(column = 1, row = 4, sticky = tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text = 'Enabled', variable = chVarEn)
check3.select()
check3.grid(column = 2, row = 4, sticky = tk.W)

COLOR1 = 'Blue'
COLOR2 = 'Yellow'
COLOR3 = 'Red'

def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background = COLOR1)
    elif radSel == 2:
        win.configure(background = COLOR2)
    else :
        win.configure(background = COLOR3)

radVar = tk.IntVar()
rad1 = tk.Radiobutton(mighty2, text=COLOR1, variable = radVar, value=1, command = radCall)
rad1.grid(column = 0, row = 5,sticky = tk.W, columnspan = 3)
rad2 = tk.Radiobutton(mighty2, text=COLOR2, variable = radVar, value=2, command = radCall)
rad2.grid(column = 1, row = 5,sticky = tk.W, columnspan = 3)
rad3 = tk.Radiobutton(mighty2, text=COLOR3, variable = radVar, value=3, command = radCall)
rad3.grid(column = 2, row = 5,sticky = tk.W, columnspan = 3)

win.mainloop()