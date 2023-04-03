import math

class Point:
    def __init__(self, x=0, y=0):
        '''
        __init__ method of the point class that supports
        the creation of a Point object in two ways. Initializes
        Point objects

        Parameters
        ----------
        x : TYPE, integer/float
           x attribute. The default is 0.
        y : TYPE, integer/float
            y attribute The default is 0.

        Returns
        -------
        None.

        '''
        self.x = x
        self.y = y
    def __str__(self):
        '''
        when a Point object is passed into the built-in
        print function, it displays the x and y attributes,
        provides a user friendly string

        Returns
        -------
        str
            

        '''
        return (f'x: {self.x} y: {self.y}')
    def __add__(self, other):
        '''
        addition of two point objects yields a new point object,
        defines + operator

        Parameters
        ----------
        other : TYPE, Point object

        Returns
        -------
        TYPE, Point object

        '''
        newX = self.x + other.x
        newY = self.y + other.y
        return Point(newX, newY)
    def __sub__(self, other):
        '''
        subtraction of two point objects yields a new point object,
        defined - operator

        Parameters
        ----------
        other : TYPE, Point object

        Returns
        -------
        TYPE, Point object

        '''
        newX = self.x - other.x
        newY = self.y - other.y
        return Point(newX, newY)
    def __iadd__(self, other):
        '''
        defines += operator, yields a point object

        Parameters
        ----------
        other : TYPE, Point object

        Returns
        -------
        TYPE, Point object

        '''
        self.x = self.x + other.x
        self.y = self.y + other.y
        return Point(self.x, self.y)
    def __isub__(self, other):
        '''
        defines -= operator, yields a point object

        Parameters
        ----------
        other : TYPE, Point object


        Returns
        -------
        TYPE, Point object

        '''
        self.x = self.x - other.x
        self.y = self.y - other.y
        return Point(self.x, self.y)
        
    pass
    
class Vec2D(Point):
    def __init__(self,x=0,y=0):
        '''
        Initializes Vec2D objects in 4 ways. Can create 
        a vector with no arguments, by passing two 
        numbers, by passing two point arguments,
        or by passing one argument

        Parameters
        ----------
        x : TYPE, optional, int, Point object
            DESCRIPTION. The default is 0.
        y : TYPE, optional, int, Point object
            DESCRIPTION. The default is 0.

        Returns
        -------
        None.

        '''
        if isinstance(x,(int, float)) and isinstance(y,(int, float)):
            self.x = x
            self.y = y 
        elif isinstance(x,Point) and isinstance(y,Point):
            self.x = y.x - x.x
            self.y = y.y - x.y
        elif isinstance(x,Point):
            self.x = x.x
            self.y = x.y
    def __add__(self,other):
        '''
        Overload + operator
        Addition of two vectors, returns new vector

        Parameters
        ----------
        other : TYPE, Vec2D object
            DESCRIPTION.

        Returns
        -------
        TYPE, Vec2D object
            DESCRIPTION.

        '''
        newX = self.x + other.x
        newY = self.y + other.y
        return Vec2D(newX,newY)
    def __sub__(self,other):
        '''
        Overload - operator
        Subtraction of two vectors, returns new vector

        Parameters
        ----------
        other : TYPE, Vec2D object
            DESCRIPTION.

        Returns
        -------
        TYPE, Vec2D object
            DESCRIPTION.

        '''
        newX = self.x - other.x
        newY = self.y - other.y
        return Vec2D(newX,newY)
    def __mul__(self,other):
        '''
        Overload * operator
        This method allows the * operator to handle 3 cases
        
        If the operands on either side of the * operator are Vec2D 
        objects the result has to be the dot product of two vectors.
        
        If the operand on the right hand side of the * operator is 
        a Point object (xb, yb), the result is also a dot product
        
        If the operand on the right hand side of the * operator
        is a number c (int/float) then the vector is scaled by a 
        factor c

        Parameters
        ----------
        other : TYPE, Vec2D, Point, int, float
            DESCRIPTION.

        Returns
        -------
        TYPE, float, int, Vec2D
            DESCRIPTION.

        '''
        if isinstance(other,Vec2D):
            dot_prod = (self.x * other.x) + (self.y * other.y)
            return dot_prod
        elif isinstance(other,Point):
            dot_prod = (self.x * other.x) + (self.y * other.y)
            return dot_prod
        elif isinstance(other,(int,float)):
            newX = self.x * other
            newY = self.y * other
            return Vec2D(newX,newY)
    def norm(self):
        '''
        returns the magnitude of the vector

        Returns
        -------
        magnitude : TYPE, int
            DESCRIPTION.

        '''
        magnitude = float(math.sqrt(self.x**2 + self.y**2))
        return magnitude
        
        
    pass



if __name__=='__main__':
    pass