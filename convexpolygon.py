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
        self.edges.append(points[-1]-points[0])
        for i in points:
            self.nverts += 1
            self.verts.append(i)
        
    def translate(self,other):
        for i in self.verts:
            i.x = i.x + other.x
            i.y = i.y + other.y
    
    def rotate(self, angle, point=0):
        a_sum = 0
        for i in range(self.nverts-1):
            a_sum += (self.verts[i].x * self.verts[i+1].y) - (self.verts[i+1].x * self.verts[i].y)
            print(self.verts[i], self.verts[i+1], a_sum)
        a = (1/2) * a_sum
        
        cx_sum = 0
        for i in range(self.nverts-1):
            cx_sum += (self.verts[i].x + self.verts[i+1].x) * ((self.verts[i].x * self.verts[i+1].y) - (self.verts[i+1].x * self.verts[i].y))
        cx = (1 / (6 * a)) * cx_sum
        
        cy_sum = 0
        for i in range(self.nverts-1):
            cy_sum += (self.verts[i].y + self.verts[i+1].y) * ((self.verts[i].x * self.verts[i+1].y) - (self.verts[i+1].x * self.verts[i].y))
        cy = (1 / (6 * a)) * cy_sum
        
        centroid = Point(cx,cy)
        if point == 0:
            point = centroid
        
        for i in self.verts:
            i.x = round(((math.cos(angle) * (i.x - point.x)) - (math.sin(angle) * (i.y - point.y)) + point.x), 4)
            i.y = round(((math.sin(angle) * (i.x - point.x)) - (math.cos(angle) * (i.y - point.y)) + point.y), 4)
        
        
            
    
        
        
        
    
    
   
if __name__=='__main__':
    pass
