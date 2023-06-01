'''
Inheritance is a mechanism for reusing code.

'''

class Mammal: 
    def walk(self):
        print('Walking...')
        
class Dog(Mammal):
        def bark(self):
            print('Dog is barking...')
    
    
class Cat(Mammal):
    def meow(self):
        print('Cat is meowing...')


Dog().walk()
Dog().bark()

Cat().walk()
Cat().meow()