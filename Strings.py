# Python arrays start from 0 to 1 less than the number of the string.

# Negative Indexes are also used. Starts from the end of the string.

# Whitespaces are counted.

'''
In the case you need to extract a few characters ie. [0:3], it starts
from the beginning of the string (0) and moves, from left to right
(unless negative which is right to left) three letters/spaces and
prints out the numbers from 0 and ends at 2. It also works for 
negative numbers. Eg: [0:-9], [-3:4], [-4:-8].


If the end index is blank ie. [0:] or [3:], it prints out all characters
from the start index to the end of the string, from left to right
(including negative numbers).


When the start index isn't provided but the end index is, Eg: [:5] or
[:10], the python interpreter assumes 0 as the start index. [0:5],
[0:10](including negative numbers).

When the syntax is left blank, [:], it prints out / clones the string
(Default indexes).

'''

# Single Quote in Double Quotes.
course = "Python's Course for Beginners"

# This also works.
course = 'Python\'s Course for Beginners'

# Double Quotes in Single Quote.
course = 'Python for "Beginners"'


# Multi-line String.
course = '''
Hi John, 

Here is our first email to you.

Thank you, 
The support team

'''

# Using Arrays (Indexing).
course = 'Python for Beginners'
	    # 01234567
print(course[-2:])
# Output: rs


# Example
course = 'Python for Beginners'
another = course[:]
print(another)
# Output: Python for Beginners


''' 
With or without '[:]' it prints out the string
in course because it(the string) has been assigned
to course and merely assigned a variable name.

'''


# Example
name = 'Christian'
print(name[1:-1])
# Output: hristia