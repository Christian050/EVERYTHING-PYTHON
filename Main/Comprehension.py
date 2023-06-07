fruits  = [
    'Apple', 
    'Banana',
    'Tomato', 
    'Pineapples', 
    'Pawpaw'
]

# List Comprehension
length = [len(fruit) for fruit in fruits]

print(length)


# Dictionary Comprehension
length_of_fruits = {fruit:len(fruit) for fruit in fruits}

print(length_of_fruits)
