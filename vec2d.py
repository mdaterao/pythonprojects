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
    def __init__(self,x=0,y=0):
        if isinstance(x,int) and isinstance(y,int):
            self.x = x
            self.y = y
        else:
            num1 = Point(x)
            num2 = Point(y)
            self.x = int(num2.x) - int(num1.x)
            self.y = int(num2.y) - int(num1.y)
        
    pass

if __name__=='__main__':

    pass

