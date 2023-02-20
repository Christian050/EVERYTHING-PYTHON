course = 'Python for Beginners'

# Using the 'len' function for number of characters.

print(len(course))
# Output: 20


# Using the '.' methods

# .upper()

course.upper()
print(course.upper())
# Output: PYTHON FOR BEGINNERS


# .lower()

course.lower()
print(course.lower())
# Output: python for beginners


# .find()

course.find('P')
print(course.find('P'))
# Output: 0 (because the index of the first "P" in the string is 0 )

# .replace()

course.replace('Beginners', 'Absolute Beginners')
print(course.replace('Beginners', 'Absolute Beginners'))
# Output: Python for Absolute Beginners


# Using the 'in' operator.

print('Python' in course)
# Output: True


''' 
They are case sensitive.

Methods do not change/ modifies the original string,
instead it creates a new string and returns it.

The '.find()' method is used to find the sequence of a character/
string in a string. It returns the position of the string you're
serching for, ie. returns the first occurence of the string.
Returns indexes of negative characters.

In some cases you'll need to pass a character/string in methods.
Eg. course,find('P').

The .replace method and some other methods takes two arguments,
what you're replacing and what you'll replace with and are
seperated by a comma.

In situations where you'll need to find the existence of a character
or sequence of characters in a string, for that you'll need to use
the 'in' operator. It's usually in expression form and returns
boolean values (True or False).

'''