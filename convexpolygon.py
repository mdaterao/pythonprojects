
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

    ''' Convex Polygon class definition'''
    


    
    def __str__(self):

        nv = 'No. of Vertices: '+str(self.nverts)+'\n'
        vs = "Vertices "+" ".join([v.__str__() + ', ' for v in self.verts]) + '\n'
        es = "Edges "+ " ".join([e.__str__() + ', ' for e in self.edges]) 
        return nv + vs + es

    
    def __init__(self,points):
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
        for i in self.verts:
            i.x = i.x + other.x
            i.y = i.y + other.y
    
    def rotate(self, angle, point = None):
        x_sum = 0
        y_sum = 0
        for i in self.verts:
            x_sum += i.x
            y_sum += i.y
        cx = x_sum / self.nverts
        cy = y_sum / self.nverts
        
        centroid = Point(cx,cy)
        
        if point == None:
            point = centroid
        
        for i in self.verts:
            temp_x = i.x
            i.x = (math.cos(angle) * (i.x - point.x)) - (math.sin(angle) * (i.y - point.y)) + point.x
            i.y = (math.sin(angle) * (temp_x - point.x)) + (math.cos(angle) * (i.y - point.y)) + point.y
       
        new_edges = []
        for i in range(len(self.verts)-1):
            edge = self.verts[i+1] - self.verts[i]
            new_edges.append(edge)
        new_edges.append(self.verts[0] - self.verts[-1])
        self.edges = new_edges
        
    def scale(self, sx, sy):
        try:
            if sx < 0 or sy < 0:
                raise ValueError('scale must be positive')
            x_sum = 0
            y_sum = 0
            for i in self.verts:
                x_sum += i.x
                y_sum += i.y
            cx = x_sum / self.nverts
            cy = y_sum / self.nverts
            
            
            for i in self.verts:
                i.x = float(sx * (i.x - cx) + cx)
                i.y = float(sy * (i.y - cy) + cy)
            
            new_edges = []
            for i in range(len(self.verts)-1):
                edge = self.verts[i+1] - self.verts[i]
                new_edges.append(edge)
            new_edges.append(self.verts[0] - self.verts[-1])
            self.edges = new_edges
       
        except ValueError as excpt:
            print(excpt)
            print('scale must be positive')
    
    def __and__(self,other):
        E = []
        for i in self.edges:
            E.append(i)
        for i in other.edges:
            E.append(i)
        n = len(self.edges)
        m = len(other.edges)
        for i in range (n + m):
            edge = E[i]
            orthogonal = Vec2D(-edge.y,edge.x)
            proj_A = [Vec2D(vertex) * orthogonal for vertex in self.verts]
            proj_B= [Vec2D(vertex) * orthogonal for vertex in other.verts]
            minA = min(proj_A)
            maxA = max(proj_A)
            minB = min(proj_B)
            maxB = max(proj_B)
            if maxA < minB or maxB < minA:
                return False
        return True
            
            
        
    
if __name__=='__main__':
    pass
