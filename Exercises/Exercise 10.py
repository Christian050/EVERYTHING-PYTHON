'''
Person          # Class
    -name       # Attribute
    -talk()     # Method
    
'''

class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f'Hi, I am {self.name}')
        

Person('Christian').talk()
Person('John').talk()