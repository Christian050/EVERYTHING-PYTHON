import random

correct_number = random.randint(1, 10)
attempts = 0
guess_limit = 3

while attempts < guess_limit:

	guess = input('Guess a number between 1 and 10: ')
	user_attempt = int(guess)

	if user_attempt != correct_number:

		print('Wrong!')
		attempts = attempts + 1

	else:

		print('Correct number!')
		break
else:

	print("\nYou ran out of attempts.")



'''
While loops can also have else statements.

Breaks terminates the loop.

'''