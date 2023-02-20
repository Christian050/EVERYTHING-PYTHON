# 1:41:55

# Using Strings
for item in 'Python':
	print(item)


# Using lists '[]' (Names)
for item in ['Christian', 'John', 'Sarah']:
	print(item)


# Using lists '[]' (Numbers)
for item in [1, 2, 3, 4]:
	print(item)


# Using range() function (One Number)
for item in range(10):
	print(item)


# Using range() function (Range)
for item in range(5, 10):
	print(item)


# Using range() function (Steps)
for item in range(5, 10, 2):
	print(item)



'''
For loops are used to iterate over items of a collection.
Eg.
Strings


Item is also called a loop variable.
Each iteration holds one item.

Range function 'range()' creates an object we can iterate over.
It's index(ing) starts from zero to one less than the given number.
In a given range, ie. range(5, 10), 5 becomes the starting point
and 10 becomes the end point.

When using steps in range functions ie range(5, 10, 2), it is
important to note that the last digit (2) determines what should
be printed out and cannot be greater than the end point.
in other words it determines what/how many items should be skipped.
Eg.

for item in range(5, 10, 2):
	print(item)
Output: 5
		7
		9

'''