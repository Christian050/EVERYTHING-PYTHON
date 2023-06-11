# Write a program to:
# 1, Accept output from a user and remove the first character of the string and return the result
# 2, In a given string,"Thereisn'tmuchtodoaboutnothing!!" -count all the characters
# 3, Create a txt file with your favorite nursery rhyme
#    write a python function to count all the characters and return the result.
# 4, Write a simple program to handle a Formula Error and print the current date and time
# 5, Illustrate with a simple program, python inheritance

# 1
word = input('enter a word\n')
def remove_character(word, para):
    x = word[para:]
    return x
print(remove_character(word, 1))


# 2
word = "Thereisn'tmuchtodoaboutnothing!!"
size = len(word)
print(size)


# 3
Poem = open('Text Files/Hope.txt')
print(len(Poem.read()))


# 4
import datetime as datetime
class FormulaError(Exception):
    pass
x = float(input("Enter first number:    "))
y = float(input("Enter second number:   "))
product = x * y
try:
    if (x == 0) or (y == 0):
     raise FormulaError
    else:
        print(product)
except:
    print('Invalid, You entered 0')
datetime = datetime.datetime.now()
print(datetime)


# 5 (1)
class Person:
  def __init__(self, name, age):
    self.Name = name
    self.Age = int(age)

  def print(self):
    print(self.Name, self.Age)

x = Person('Christian', 19)
x.print()