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
        elif isinstance(x,Point) and isinstance(y,Point):
            self.x = y.x - x.x
            self.y = y.y - x.y
        elif isinstance(x,Point):
            self.x = x.x
            self.y = x.y
    def __add__(self,other):
        newX = self.x + other.x
        newY = self.y + other.y
        return Vec2D(newX,newY)
    def __sub__(self,other):
        newX = self.x - other.x
        newY = self.y - other.y
        return Vec2D(newX,newY)
    def __mul__(self,other):
        if isinstance(self,Vec2D) and isinstance(other,Vec2D):
            dot_prod = (self.x * other.x) + (self.y * other.y)
            return dot_prod
        elif isinstance(other,Point):
            dot_prod = (self.x * other.x) + (self.y * other.y)
            return dot_prod
        elif isinstance(other,int):
            newX = self.x * other
            newY = self.y * other
            return Vec2D(newX,newY)
    def norm(self):
        magnitude = float(math.sqrt(self.x**2 + self.y**2))
        return magnitude
        
        
    pass


if __name__=='__main__':
    num2 = 3

