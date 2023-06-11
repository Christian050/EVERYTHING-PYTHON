import tkinter as tk
import sys
from tkinter import *
from tkinter.ttk import Combobox


# show entry fields
# set font style + size
fs = ('Calibri Light', 20, 'italic')
fs1 = ('Calibri Light', 11, 'italic')
n = "New User"
e = "Existing User"


def show_entry_fields():
    print('First Name =>\t %s\nLast Name => \t %s \nI.D => \t %s' %
          (e1.get(), e2.get(), e3.get()))  # print fields and get entries


def Btn_Click(event):
    print('Double Click, Terminate')
    sys.exit()

# Set master and Label


master = tk.Tk()
# window = Tk()
tk.Label(master, text='First Name', bg='Yellow', width=10).grid(row=0, pady=10)
tk.Label(master, text='Last Name', bg='Yellow').grid(row=2, pady=10)
tk.Label(master, text='I.D', bg='Yellow').grid(row=4, pady=10)
master.config(bg="Yellow")
master.title("SIM Reg Popup")
master.geometry("355x195")
master.resizable(0, 0)

# Set entry (name from show_entry_fields)
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

# Set stringvar for combobox
var = StringVar()
var.set('one')
var.data = (n, e)
cb = Combobox(master, values=var.data, background='Yellow', foreground='Black')
cb.place(x=210, y=10)

# Set listbox
lb = Listbox(master, height=5, bg='Yellow', selectmode='single',
             selectbackground='Yellow', selectforeground='Black')
lb.data = ('MTN', 'AirtelTigo', 'Vodafone', 'Glo', 'Other')
for num in lb.data:
    lb.insert(END, num)
    lb.place(x=218, y=50)

# Set Radiobutton
v0 = IntVar()
v0.set(1)
Rad1 = Radiobutton(master, text='Male', bg='Yellow', variable=v0, value=1)
Rad1.place(x=30, y=128)
Rad2 = Radiobutton(master, text='Female', bg='Yellow', variable=v0, value=2)
Rad2.place(x=100, y=127)

# Set grid
e1.grid(row=0, column=1, columnspan=2)
e2.grid(row=2, column=1, columnspan=2)
e3.grid(row=4, column=1, columnspan=2)

# Set buttons, commands and grid
tk.Button(master, text='Quit', font=fs1, command=master.quit).place(y=163)
tk.Button(master, text='Show', font=fs1, command=show_entry_fields).place(
    x=310, y=163)   # .grid(row=6, column=100, sticky=tk.E)
tk.mainloop()
