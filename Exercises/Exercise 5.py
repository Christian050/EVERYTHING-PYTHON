'''
If name is less than 3 characters long
	name must be at least three characters
otherwise if it's more than 50 characters long
	name can be a maximum of 50 characters
otherwise
	name looks good!

'''

name = input('What is your name: ')

if len(name) < 3:
	print('Name must be at least 3 characters long.')

elif len(name) > 50:
	print('Name can be a maximum of 50 characters long.')

else:
	print('Name looks good!')