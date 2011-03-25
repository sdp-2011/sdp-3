import math
import copy

"""
This file is 'import *' safe.

Contains classes and functions for using vectors, maths and other geometry.
"""

class Vector(object):
    """
    This class represents a vector with variable dimension.
    All components are converted to floats.
    
    Vectors can be created as follows:
    
    x = Vector(1.2, 3.0)
    y = Vector(1.2, 3.5, 2.3)
    z = V( [1.0, 3.0]  )
    
    vectors are indexed with subscript []
    
    x[1] => 1.2
    
    All normal arithmetic functions work as standard.
    Can be iterated over, mapped too, etc.
    """
    
    def __init__(self, *args):
        """
        Builds a vector from the passed args. Can be built using a tuple, 
        list or simply from individual parameters.
        """
        if type(args[0]) == type([]):
            self.items = list( map(lambda x: float(x), args[0]))
        elif type(args[0]) == type(()):
            self.items = list( map(lambda x: float(x), args[0]))
        else:
            self.items = list( map(lambda x: float(x), args))
            
    def __str__(self):
        c = ""
        for i in self.items: c += str(i)+", "
        return "V("+c[:-2]+")"
    
    def __repr__(self):
        return str(self)
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self,key):
        return self.items[key]
    
    def __setitem__(self,key,value):
        self.items[key] = float(value)
    
    def __contains__(self,item):
        if item in self.items:
            return True
        else:
            return False
            
    def __iter__(self):
        return self.items

    def __eq__(self,v):
        if v is None:
            return False
        equal = True
        if len(v) != len(self.items):
            raise Exception("Vectors not of same length")
        for i in range(0,len(v)):
            if self.items[i] != v[i]: return False
        return equal
        
    def __ne__(self,v):
        return not(v == self)
        
    def __iadd__(self,v):
        if len(v) != len(self.items):
            raise Exception("Vectors not of same length")
        for i in range(0,len(v)):
            self.items[i] += v[i]
        return self
        
    def __add__(self,v):
        if len(v) != len(self.items):
            raise Exception("Vectors not of same length")
        r = copy.copy(self.items)
        for i in range(0,len(v)):
            r[i] += v[i]
        return Vector(*r)

    def __isub__(self,v):
        if len(v) != len(self.items):
            raise Exception("Vectors not of same length")
        for i in range(0,len(v)):
            self.items[i] -= v[i]
        return self	
        
    def __sub__(self,v):
        if len(v) != len(self.items):
            raise Exception("Vectors not of same length")
        r = copy.copy(self.items)
        for i in range(0,len(v)):
            r[i] -= v[i]
        return Vector(*r)
        
    def __mul__(self,v):
        return Vector(*map(lambda x: x*v,self.items))
        
    def __imul__(self,v):
        self.items = map(lambda x: x*v,self.items)
        return self
        
    def __div__(self,v):
        return Vector(*map(lambda x: x/v,self.items))
        
    def __idiv__(self,v):
        self.items = map(lambda x: x/v,self.items)
        return self
        
    def __abs__(self):
        return Vector(*map(lambda x: abs(x),self.items))

    def __neg__(self):
        return Vector(*map(lambda x: x*(-1),self.items))

    def __copy__(self):
        return Vector(copy.copy(self.items))

	def __lshift__(self, vec):
		return self - vec
		
	def __rshift__(self, vec):
		return vec - self
		
    def getw(self):
        if (len(self.items) == 4):
            return self.items[0]
        else:
            raise Exception("Only 4 dimensional vectors have a 'w' component")
    
    def setw(self, value):
        if (len(self.items) == 4):
            self.items[0] = float(value)
        else:
            raise Exception("Only 4 dimensional vectors have a 'w' component")
    
    w = property(getw, setw)

    def getx(self):
        if (len(self.items) == 4):
            return self.items[1]
        else:
            return self.items[0]

    def setx(self, value):
        if (len(self.items) == 4):
            self.items[1] = float(value)
        else:
            self.items[0] = float(value)

    x = property(getx, setx)
    
    def gety(self):
        if (len(self.items) == 4):
            return self.items[2]
        else:
            return self.items[1]

    def sety(self, value):
        if (len(self.items) == 4):
            self.items[2] = float(value)
        else:
            self.items[1] = float(value)
    
    y = property(gety, sety)
    
    def getz(self):
        if (len(self.items) == 4):
            return self.items[3]
        else:
            return self.items[2]

    def setz(self, value):
        if (len(self.items) == 4):
            self.items[3] = float(value)
        else:
            self.items[2] = float(value)

    z = property(getz, setz)

        
# Vectors can also be created just using the V() function

def V(*args): return Vector(*args)


class Polar:
    """
    This class represents a Polar coordinate.
    All components are converted to floats.

    
    Polars can be created as follows:
    
    x = Polar(target_coordinates, orgin_coordiantes)
    y = Polar(distance, angle, orgin_coordiantes)
   
    Polars are indexed with subscript []
    
    x[1] => distance
    x[2] => angle
    x[3] => orgin

    """
    
    def __init__(self, *args):
        """
        Builds a Polar from the passed args.
        """
        if (len(args) == 2):
            self.items = []
            angle = 0.0

            #distance
            self.items.append(distance(args[0], args[1]))

            # angle
            x = 0.0
            y = 0.0
            x = args[0].x - args[1].x
            y = args[0].y - args[1].y
            if x > 0:
                angle = math.atan(y/x)
            elif (x < 0) and (y >= 0):
                angle = math.atan(y/x) + math.pi
            elif (x < 0) and (y < 0):
                angle = math.atan(y/x) - math.pi
            elif (x == 0) and (y > 0):
                angle = 0.5 * math.pi
            elif (x == 0) and (y < 0):
                angle = (-0.5) * math.pi
            elif (x == 0) and (y == 0):            
                angle = 0

            if angle < 0:
                angle = math.pi + (math.pi + angle)

            self.items.append(angle)

            # orgin point
            self.items.append(args[1])
        elif (len(args) == 3):
            self.items = list( map(lambda x: float(x), args[:2]))
            self.items.append(args[2])
        else:
            raise Exception("Not valid constructor args. Constructor " + \
                    "arguments should be of form (Vector, Vector) or " + \
                    "((0,1), (2,3)) or (l[0,1],[2,3]) or (float, " + \
                    "float, Vector) or (1.0, 1.0, [0,1]) or (1.0, 1.0, (0,1)")
    
    def toCartesian(self):
        x = self.origin.x + (self.distance * (math.cos(self.angle)))
        y = self.origin.y + (self.distance * (math.sin(self.angle)))
        return V(x,y)

    def __str__(self):
        c = ""
        for i in self.items: c += str(i)+", "
        return "Polar("+c[:-2]+")"
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self,key):
        return self.items[key]
    
    def __setitem__(self,key,value):
        self.items[key] = float(value)
    
    def __contains__(self,item):
        if item in self.items:
            return True
        else:
            return False
            
    def __iter__(self):
        return self.items
        
    def __imul__(self,v):
        return Polar(self.distance * v, self.angle, self.orgin)   
        
    def __idiv__(self,v):
        return Polar((self.distance / v), self.angle, self.orgin)

    @property
    def distance(self):
        return self.items[0]
            
    @property
    def angle(self):
        return self.items[1]
            
    @property
    # The origin point of the polar plane as a cartesian
    def origin(self):
        return self.items[2]


# Vector Functions.
# TODO: Why is there a Polar class definition between these?

def clamp(vec, v1, v2):
    r = copy.copy(vec)
    if len(vec) != len(v1) or len(vec) != len(v2):
        raise Exception("Vectors not of same length")
    for i in range(0,len(r)):
        r[i] = max(vec[i], v1[i])
        r[i] = min(vec[i], v2[i])
    return r

def vectorFrom(v1, v2):
    return (v2 - v1)

def dot(v1, v2):
    if len(v1) != len(v2):
        raise Exception("Vectors not of same length")
    sum = 0
    for i in range(0,len(v1)):
        sum += (v1[i] * v2[i])
    return sum
    
def distanceSqrd(v1, v2):
    if len(v1) != len(v2):
        raise Exception("Vectors not of same length")
    sum = 0.0
    for i in range(0,len(v1)):
        sum += (v1[i] - v2[i])**2
    return sum
    
def distance(v1, v2):
    return math.sqrt(distanceSqrd(v1, v2))
    
def lengthSqrd(vec):
    sum = 0
    for i in range(0,len(vec)):
        sum += vec[i]**2
    return sum

def length(vec):
    return math.sqrt( lengthSqrd(vec) )

def IsZero(vec):
    if (length(vec) == 0):
        return True
    else:
        return False
    
def normalize(vec):
    if length(vec) == 0:
        raise Exception("Cannot normalize zero vector")
    else:
        return vec / length(vec)

def projectOnto(w, v):
    return v * d(w,v) / lengthSqrd(v)


def rotate2D(vec, angle):
    if len(vec) != 2:
        raise Exception("Cannot perform rotation on non-2D vector")
    else:
        x = vec.x * math.cos(angle) + vec.y * -math.sin(angle)
        y = vec.x * math.sin(angle) + vec.y * math.cos(angle)
        return V(x,y)
    
# Other maths Functions

def angleModulus(angle):
    # returns an angle between 0 and 2 pi
    while (angle < 0.0):
        angle = angle + (2 * math.pi)
    while (angle > (2 * math.pi)):
        angle = angle - (2 * math.pi)
    return angle

def angleBetweenPolar(polar_orgin, polar2):
    """
    Returns an angle between two polars.
    positive angle if polar2 lies to the left of polar_orgin, else a negative angle
    """
    return angleRotDiff(polar_orgin.angle, polar2.angle)

def diffAngles(angle1, angle2):
    """
    Returns an angle between two absolute angles that is always positive
    
    Calls angleRotDiff and converts the returned value to a positive value

    Note: Has only been tested with angles between 0 and 2 pi radians.
    """
    angle_between = angleRotDiff(angle1, angle2)
    if angle_between < 0:
        angle_between = (-1.0) * angle_between
    
    return angle_between

def angleRotDiff(angle_orgin, angle2):
    """
    Returns an angle between two absolute angles.
    positive angle if angle2 lies to the right of angle_orgin, else a negative angle

    Note: Has only been tested with angles between 0 and 2 pi radians.
    """
    angle = 0.0
    angle = angle2 - angle_orgin

    if (angle > math.pi):
        angle = -(2 * math.pi - angle)
    elif (angle < -math.pi):
        angle = 2 * math.pi + angle

    return angle



