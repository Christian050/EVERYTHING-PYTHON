# Object Oriented Programming

# Methods, aside the '__init__' method don't need 'self.' --not sure--

# All methods start with a parameter called 'self'.		eg. def bark(self):


# Example 1 -> Using Classes.

class Dog:											# Class Dog

	def bark(self):									# Bark Method
		print('bark')


d = Dog()
d.bark()
print(type(d))

'''
Dog in brackets '()' refers to an instanciation '__main__' refers to the type of
module the classs was defined in. '__main__' is the default module.
'''





# Example 2 -> Adding Methods.

class Dog:										 	# Class Dog

	def bark(self):									# Bark Method
		print('bark')

	def add_one(self, x):						    # Add one Method
		return x + 1 

print(Dog().add_one(5))






# Example 3 -> Using the '__init__' method.

# It's called whenever the 'Dog()' (class) instance is written. eg. d = Dog()

# 'self' denotes the object itself.

'''
Instanciates the object right when it's created. ie. whenever 'Dog()' is written.
It also passes args(arguments) when given.
Eg
		from class below:
		d = Dog('Tim')

		'Tim' is passed into 'def __init__(self, name)'
'''
class Dog:

	def __init__(self, name, age):
		self.name = name  						# self.name = attribute of the class 'Dog' which is name
		self.age = age  						# self.age = attribute of the class 'Dog' which is age
		# print(name)
		# print(age)

		# Name in 'self.name' doesn't need to match, neither does age. Acts as a variable name.

	
	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def set_age(self, age):
		self.age = age
	
d = Dog('Tim', 34)

# or

print(d.name)

# or

# print(d.get_name())

print('Hello, I\'m ',d.get_name(), d.get_age(), 'years of age.')


d2 = Dog('Bill', 12)

# or

print(d2.name)

# or

# print(d.get_name())

print('Hello, I\'m ',d2.get_name(), d2.get_age(), 'years of age.')





# Example 4 -> Adding set_age

class Dog:

	def __init__(self, name, age):
		self.name = name  						# self.name = attribute of the class 'Dog' which is name
		self.age = age  						# self.age = attribute of the class 'Dog' which is age

	
	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def set_age(self, age):
		self.age = age


d = Dog('Tim', 34)
d.set_age(23)
print(d.get_age())								# Always add the brackets afer every class/ method called




# Example 7 -> Using Multiple Classes

class Student:

	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade   # 0 - 100

	def get_grade(self):
		return self.grade

class Course:

	def __init__(self, name, max_students):
		self.name = name
		self.max_students = max_students
		self.students = []

	def add_student(self, student):							# The student parameter is an instance of a student object
		if len(self.students) < self.max_students:
			self.students.append(student)
			return True
		return False

	def get_average_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()

		return value / len(self.students)

# Add students
s1 = Student('Christian', 19, 100)
s2 = Student('Bill', 19, 75)
s3 = student('Jill', 19, 65)

# Add Course
course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)
# print(course.students)		
print(course.student[0].name)