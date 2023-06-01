import random


class Dice:
    def roll():
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(f'({x}, {y})')
    
    
Dice.roll()