from vec2d import Point
from vec2d import Vec2D

import math


def orient2d(a, b, c):

    '''

    Note that you will need this function only if you plan
    to code up the optional question listed in section 2.4.2
    
    Parameters
    ----------
        a : Point object
        b : Point object
        c : Point object
        
    Returns
    --------
        Integer 1/1/0
        Returns 1 if points are oriented in the 
        counter clockwise direction -1 if clockwise
        and 0 if collinear
        
    '''

    # Signed area of triangle formed by a,b,c
    s_a = (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)
    
    # Orientation
    result = 1 if s_a > 0 else -1 if s_a < 0 else 0
    
    return result



class ConvexPolygon:

    ''' Convex Polygon class definition:
        
        Create and modify convex polygon objects
    
    '''
    


    
    def __str__(self):
        '''
        prints the number of vertices (self.nverts) attribute
        prints the vertices (self.verts) atribute 
        prints the edges (self.edges) attribute

        Returns
        -------
        TYPE, str
            DESCRIPTION.

        '''

        nv = 'No. of Vertices: '+str(self.nverts)+'\n'
        vs = "Vertices "+" ".join([v.__str__() + ', ' for v in self.verts]) + '\n'
        es = "Edges "+ " ".join([e.__str__() + ', ' for e in self.edges]) 
        return nv + vs + es

    
    def __init__(self,points):
        '''
        Initializes a polygon and its attributes: self.nverts,
        self.verts, and self.edges
        
        accepts a list of Point objects as an argument and initializes 
        a ConvexPolygon object

        Parameters
        ----------
        points : TYPE, list
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.nverts = 0
        self.verts = []
        self.edges = []
        for i in range(len(points)-1):
            self.edges.append(points[i+1] - points[i])
        self.edges.append(points[0]-points[-1])
        for i in points:
            self.nverts += 1
            self.verts.append(i)
        
    def translate(self,other):
        '''
        translates a polygon in the direction of a vector

        Parameters
        ----------
        other : TYPE, vec2D object
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        for i in self.verts:
            i.x = i.x + other.x
            i.y = i.y + other.y
    
    def centroid(self):
        '''
        determines the centroid of a polygon

        Returns
        -------
        centroid : TYPE, Point object
            DESCRIPTION.

        '''
        x_sum = 0
        y_sum = 0
        for i in self.verts:
            x_sum += i.x
            y_sum += i.y
        cx = x_sum / self.nverts
        cy = y_sum / self.nverts
        centroid = Point(cx,cy)
        return centroid
    
    def edges(self):
        '''
        updates the self.edges attribute when the vertices
        of a polygon have changed

        Returns
        -------
        None.

        '''
        new_edges = []
        for i in range(len(self.verts)-1):
            edge = self.verts[i+1] - self.verts[i]
            new_edges.append(edge)
        new_edges.append(self.verts[0] - self.verts[-1])
        self.edges = new_edges
    
    def rotate(self, angle, point = None):
        '''
        rotates a polygon in the counter-clockwise direction
        about a pivot point
        
        If the method is called without the (optional) pivot 
        point argument the centroid of the polygon must be set 
        as the pivot point
        
        The rotate method updates the edges and vertices of the 
        polygon upon rotation

        Parameters
        ----------
        angle : TYPE, float
            DESCRIPTION.
        point : TYPE, optional, Point object
            DESCRIPTION. The default is None.

        Returns
        -------
        None.

        '''
        centroid = ConvexPolygon.centroid(self)
        
        if point == None:
            point = centroid
        
        for i in self.verts:
            temp_x = i.x
            i.x = (math.cos(angle) * (i.x - point.x)) - (math.sin(angle) * (i.y - point.y)) + point.x
            i.y = (math.sin(angle) * (temp_x - point.x)) + (math.cos(angle) * (i.y - point.y)) + point.y
       
        ConvexPolygon.edges(self)
        
    def scale(self, sx, sy):
        '''
        rescales a polygon
        The method must accept two positive float objects
        to scale the polygon by scale factors sx and sy
        
        updates edges and vertices of the polygon after it
        is scaled

        Parameters
        ----------
        sx : TYPE, float
            DESCRIPTION.
        sy : TYPE, float
            DESCRIPTION.

        Raises
        ------
        ValueError
            DESCRIPTION.
            The scale factors must be positive floats

        Returns
        -------
        None.

        '''
        try:
            if sx < 0 or sy < 0:
                raise ValueError('scale factors must be positive')
            centroid = ConvexPolygon.centroid(self)
            
            for i in self.verts:
                i.x = float(sx * (i.x - centroid.x) + centroid.x)
                i.y = float(sy * (i.y - centroid.y) + centroid.y)
            
            ConvexPolygon.edges(self)
       
        except ValueError as excpt:
            print(excpt)
            print('scale must be positive')
    
    
    def __and__(self,other):
        '''
        checks overlaps between polygons
        returns the boolean object True if two polygons 
        overlap and False otherwise
        
        overloads the & operator

        Parameters
        ----------
        other : TYPE, ConvexPolygon object
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        '''
        E = []
        for i in self.edges:
            E.append(i)
        for i in other.edges:
            E.append(i)
        n = len(self.edges)
        m = len(other.edges)
        for i in range (n + m):
            edge = E[i]
            ortho = Vec2D(-edge.y,edge.x)
            proj_A = [Vec2D(vert) * ortho for vert in self.verts]
            proj_B= [Vec2D(vert) * ortho for vert in other.verts]
            minA = min(proj_A)
            maxA = max(proj_A)
            minB = min(proj_B)
            maxB = max(proj_B)
            if maxA < minB or maxB < minA:
                return False
        return True
            
            
        
    
if __name__=='__main__':
    pass
