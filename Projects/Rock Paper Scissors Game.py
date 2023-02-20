import random


choices = ['Rock', 'Paper', 'Scissors']

user = input('Rock Paper Scissors?\t').title()

comp = random.choice(choices)


# Outcomes
user_rock_win = 'Rock crush Scissors, User wins!'
user_rock_lose = 'Paper covers Rock, Computer wins!.'

user_paper_win = 'Paper covers Rock, User wins!'
user_paper_lose = 'Scissors cuts Paper, Computer wins.'

user_scissors_win = 'Scissors cuts Paper, User wins!'
user_scissors_lose = 'Rock crush Scissors, Computer wins.'

# 
print(f'Comp: {comp}')
if user == comp:
	print("It's a tie!")
if user == 'Rock' and comp == 'Paper':
	print(user_rock_lose)
if user == 'Rock' and comp == 'Scissors':
	print(user_rock_win)
if user == 'Paper' and comp == 'Rock':
	print(user_paper_lose)
if user == 'Paper' and comp == 'Scissors':
	print(user_paper_lose)
if user == 'Scissors' and comp == 'Paper':
	print(user_scissors_win)
if user == 'Scissors' and comp == 'Rock':
	print(user_scissors_lose)
