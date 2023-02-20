number = [5, 2, 5, 2, 2]

for x in number:
	x = 'xxxxx'
	for y in number:
		y = 'xx'
print(f'{x}\n{y}\n{x}\n{y}\n{y}')


# OR


numbers = [5, 2, 5, 2, 2]

for x in numbers:
	print('x' * x)


# OR


numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
	output = ''
	for count in range(x_count):
		output += 'x'
	print(output)


'''
Note:

The first one works but there's a lot of '\n' (new lines)
makes the code look...stuffy??

The second one works too but that's a lazy approach to
it.

The third one works, looks neat and overall the best way
to solve the problem.

Variable names can also be in the range function.
Eg.
	range(x_count)


'''