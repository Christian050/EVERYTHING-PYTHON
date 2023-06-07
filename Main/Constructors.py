'''
A constructor is a function called when creating an object.

'''


class Point:
    def __init__(self, x, y):           # Constructor
        self.x = x
        self.y = y

    def move(self):
        print('Move')
        
    def draw(self):
        print('Draw')
        
        
point = Point(10, 20)
point.x = 11
print(point.x)