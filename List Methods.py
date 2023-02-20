# 2:06:09

numbers = [5, 2, 1, 7, 4]


# Using the insert method
numbers.append(20)


# Using the insert method
numbers.insert(0, 10)
print(numbers)


# Using the remove method.
numbers.remove(5)
print(numbers)


# Using the clear method.
numbers.clear()
print(numbers)


# Using the pop method.
numbers.pop()
print(numbers)


# Using the index method.
print(numbers.index(5))


# Using the in operator.
print(50 in numbers)


# Using the count method.
print(numbers.count(5))


# Using the sort method.
numbers.sort()
print(numbers)


# Using the reverse method.
numbers.reverse()
print(numbers)


# Using the copy method.
numbers2 = numbers.copy()
print(numbers2)



'''
List functions/ methods are the operations
you can perform on a list.(takes one argument)

The append method (.append()) adds an item
to a list.(takes one argument)

The insert method (.insert()) takes two args,
the 'int index' for where the object should be
placed and the 'object' for what you're replacing.
(takes two arguments)

The remove method (.remove()) removes an object
in a list.(takes one argument)

The clear emthod (.clear()) removes all items
/objects in a list.(takes no arguments)

The pop method (.pop()) removes the last
number on a list.(takes one argument)

The index method (.index()) is used to check
the existence of an item in a list. It returns
the index of the first occurence of an item
and produces a value error if the index being
searched for is not in the list. (takes one argument)

The in operator (in) works just like the index method.
It's used to search for the existence of a character
or a sequence of characters in a list and returns a
boolean value.(takes one-to-many arguments)

The count method (.count()) is used to check for the
number of occurences of an item in a list.


The sort method is used to sort items in ascending
order in a list. It returns no other value than
'None' when printed. (takes no arguments)


The reverse method sorts items in desending order
in a given list.(takes no arguments)


The copy method (.copy()) copies the list
None object represents the absence of a value.
It does not modify an already copied list when
the original list has been updated.
(takes no arguments)

'''