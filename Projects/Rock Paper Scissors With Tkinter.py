import random
import tkinter as tk
from tkinter import *

# Root Configuration
root = tk.Tk()
root.resizable(0, 0)
root.title('Rock Paper Scissors Game')
root.config(bg='white')

# Command line


def game(e):
    if ent.get():
        choices = ['Rock', 'Paper', 'Scissors']

        Player = ent.get().title()

        comp = random.choice(choices)

        # Outcomes
        Player_rock_win = 'Rock crush Scissors, Player wins!'
        Player_rock_lose = 'Paper covers Rock, Computer wins!.'

        Player_paper_win = 'Paper covers Rock, Player wins!'
        Player_paper_lose = 'Scissors cuts Paper, Computer wins.'

        Player_scissors_win = 'Scissors cuts Paper, Player wins!'
        Player_scissors_lose = 'Rock crush Scissors, Computer wins.'

        # Choices
        ent.delete(0, END)
        if Player == comp:
            ent.insert(0, f"It's a tie!")
        if Player == 'Rock' and comp == 'Paper':
            ent.insert(0, f'{Player_rock_lose}')
        if Player == 'Rock' and comp == 'Scissors':
            ent.insert(0, f'{Player_rock_win}')
        if Player == 'Paper' and comp == 'Rock':
            ent.insert(0, f'{Player_paper_lose}')
        if Player == 'Paper' and comp == 'Scissors':
            ent.insert(0, f'{Player_paper_lose}')
        if Player == 'Scissors' and comp == 'Paper':
            ent.insert(0, f'{Player_scissors_win}')
        if Player == 'Scissors' and comp == 'Rock':
            ent.insert(0, f'{Player_scissors_lose}')
        ent.config(state='readonly')

        cs.config(state='normal')
        cs.insert(0, f'Computer Select: {comp}')
        cs.config(state='readonly')


def clear(x):
    ent.config(state='normal')
    cs.config(state='normal')
    ent.delete(0, END)
    cs.delete(0, END)
    cs.config(state='readonly')


# Label frame
fr = Label(root, text='Rock Paper Scissors',
           bg='white', justify=CENTER, fg='red', bd=0)
fr.pack()

# Entry points
ent = Entry(root, width=35, justify='center', bg='systembuttonface', fg='red')
ent.pack()

# Computer Selection
cs = Entry(root, width=23, justify='center', fg='red', state='readonly', bd=0)
cs.pack()

# # Button
# btn = Button(root, text='Shoot!', command=game, bg='white', fg='red')
# btn.pack()

# Bind esc key to clear
root.bind('<Escape>', lambda x: clear(x))

# Bind enter key to continue
root.bind('<Return>', lambda e: game(e))

# Lambda function
# They can only perform one expression.
# It’s not possible to have multiple independent operations in one lambda function.

# Run
root.mainloop()
