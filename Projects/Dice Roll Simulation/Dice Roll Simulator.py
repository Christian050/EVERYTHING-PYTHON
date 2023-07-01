# Import Necessary Libraries
from tkinter import *
from PIL import Image, ImageTk
import random

# Create Class


class Dice(Tk):
    def __init__(self):
        super().__init__()
        # Configure Layout
        self.geometry('500x170')
        self.title('Dice Simulation')
        # self.dice = ['Images\Dice 1.png', 'Images\Dice 2.png', 'Images\Dice 3.png', 'Images\Dice 4.png', 'Images\Dice 5.png', 'Images\Dice 6.png']
        self.LeftDice = random.randrange(1, 6)
        self.RightDice = random.randrange(1, 6)

    # Create Labels Method
    def Labels(self):
        self.Left = Label(self, text=self.LeftDice, font=500)
        self.Left.place(x=40, y=100)

        self.Right = Label(self, text=self.RightDice, font=500)
        self.Right.place(x=400, y=100)

        self.total = Label(
            self, text=f'Total: {self.LeftDice + self.RightDice}')
        self.total.place(x=220, y=150)

    # Create Command for Button
    def RollDice(self):
        self.LeftDice = random.randrange(1, 7)
        self.Left.config(text=self.LeftDice)

        self.RightDice = random.randrange(1, 7)
        self.Right.config(text=self.RightDice)

        self.total.config(text=f'Total: {self.LeftDice + self.RightDice}')

    # Create Button Method

    def Buttons(self):
        Button(self, text='Roll Dice', command=self.RollDice).pack()


if __name__ == '__main__':
    root = Dice()
    root.Labels()
    root.Buttons()
    root.mainloop()


# from tkinter import *
# from PIL import Image, ImageTk
# import random

# class Dice(Tk):
#     def __init__(self):
#         super().__init__()
#         self.dice = [
#             'Dice 1.png', 'Dice 2.png', 'Dice 3.png',
#             'Dice 4.png', 'Dice 5.png', 'Dice 6.png'
#         ]
#         self.LeftDice = None
#         self.RightDice = None
#         self.configure_layout()
#         self.load_dice_images()

#     def configure_layout(self):
#         self.geometry('500x360')
#         self.title('Dice Simulation')

#     def load_dice_images(self):
#         try:
#             self.LeftDice = ImageTk.PhotoImage(Image.open(random.choice(self.dice)))
#             self.RightDice = ImageTk.PhotoImage(Image.open(random.choice(self.dice)))
#         except FileNotFoundError as e:
#             print(f"Error: {e}")
#             # self.quit()

#     def Labels(self):
#         self.Left = Label(self, image=self.LeftDice)
#         self.Left.place(x=40, y=100)

#         self.Right = Label(self, image=self.RightDice)
#         self.Right.place(x=300, y=100)

#     def RollDice(self):
#         self.load_dice_images()
#         self.Left.config(image=self.LeftDice)
#         self.Right.config(image=self.RightDice)

#     def Buttons(self):
#         Button(self, text='Roll Dice', command=self.RollDice).pack()

# if __name__ == '__main__':
#     root = Dice()
#     root.Labels()
#     root.Buttons()
#     root.mainloop()
