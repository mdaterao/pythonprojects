import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return (f'x: {self.x} y: {self.y}')
    def __add__(self, other):
        newX = self.x + other.x
        newY = self.y + other.y
        return Point(newX, newY)
    def __sub__(self, other):
        newX = self.x - other.x
        newY = self.y - other.y
        return Point(newX, newY)
    def __iadd__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return Point(self.x, self.y)
    def __isub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        return Point(self.x, self.y)
        
    pass
    
class Vec2D(Point):
    def __init__(self,obj1 = Point(), obj2 = Point()):
        Point.__init__(self, x=0, y=0)
        num1= obj1
        num2 = obj2
        self.x = num2.x - num1.x
        self.y = num2.y - num1.y
        
    pass

if __name__=='__main__':

    pass

