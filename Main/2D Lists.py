matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
print(matrix[2])


# Modifying 2D Lists
matrix[0] [1] = 20
print(matrix[0] [1])


# Iterating items using nested loops
for row in matrix:
	for item in row:
		print(item)


'''
A two dimensional list (2D list) is a lists
where each item in that list is another
list.

The variable in matrix is an example of
a python matrix

When printing a 2D list, the first index
is of the first list (Outside list).
Eg.
	example = [
		[1, 2, 3],
		[4, 5, 6]
	]

	print(example[0])

	Output: [1, 2, 3]


While
The second is of the list located inside
the list (Inside list).
Eg.
	example = [
		[1, 2, 3],
		[4, 5, 6]
	]

	print(example[0][2])

	Output: 3

'''