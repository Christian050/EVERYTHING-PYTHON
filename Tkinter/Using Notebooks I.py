from tkinter import *
from tkinter import ttk


master = Tk()
master.geometry("150x150")

# Tabs
note = ttk.Notebook(master)
note.pack(pady=5)

# Frame
info_frame = Frame(note, width=140, height=140)
info_frame.pack(fill='both', expand=1)

# Create Tab
note.add(info_frame, text="Note Tab")

master.mainloop()


master = Tk()
master.title("Currency Convertor")
master.geometry("500x500")

# Tabs
nb = ttk.Notebook(master)
nb.pack(pady=5)

#Two frames
currency_frame = Frame(nb, width=480, height=480)
conversion_frame = Frame(nb, width=480, height=480)

currency_frame.pack(fill="both", expand=1)
conversion_frame.pack(fill="both", expand=1)

# Add Tabs
nb.add(currency_frame, text="Currency")
nb.add(conversion_frame, text="Convert")

# Disable 2nd Tab
nb.tab(1, state='disabled')

master.mainloop()