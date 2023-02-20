print('''
		Car Game
 Welcome to the car game.
Type 'help' for instructions.
	''')

command = ""
started = False

while True:	
	command = input('> ').lower()

	if command == 'help':
		print('''
	start - to start the car
	stop - to stop the car
	quit - to exit
			''')

	if command == 'start':

		if started:
			print('Car has already started.')

		else:
			started = True
			print('Car started...Ready to go!')

	if command == 'stop':

		if not started:
			print('Car has already stopped.')

		else:
			started = False
			print('Car has stopped.')

	elif command == 'quit':
		break

else:
	print("Sorry, I don't understand that! ")


'''
'while True' means that the code will run till it breaks/terminates.

Using Started 101


Command 'start'.


Started == False
∴ Code won't run

So,

if Started (which is false):
	print('Car has already started')	Which won't run because started == False
else:
	Started == True
	print('Car has started, ready to go')


What Happens When The User Types 'start' (When car hasn't started).

The if statement won't run because conditions aren't met (Started isn't True) so
the else statement will run. In the else statement, Started == True and 'Car has started'
is printed out since it didn't meet the if condition.


What Happens When The User Types 'start' (When car has already started).

The code is re-run and the if conditions are met (Started == True) so it prints
'Car has already started'.



Command 'stop'.

Started == False

if not started:
	print('Car has already stopped.')
else:
	started == False
	print('Car has stopped')


What Happens When The User Inputs 'stop' (When car hasn't started).

The if conditions are met (Started is False) therefore it prints out
'Car has already stopped' on the asumption that the car hasn't started
(Started == False) or 'stop' has already been typed.


What Happens When The User Types 'stop' (When car has started).

When 'start' has been typed and the else statement is run, the if conditions
aren't met (Started == True) so the else statement is run, started == False and
prints 'Car has stopped.'

'''