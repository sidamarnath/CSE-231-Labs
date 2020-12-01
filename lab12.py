#########################################
# lab12.py
# ALgorithm
# Create a vector class
# Have program do calculations
#########################################

class Vector():
    
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        #self.__valid = self.__validate()
        
    def __str__(self):
        ''' returns a string as formal representation of vector'''
        
        out_str = "(" + str(round(self.__x ,2)) + "," + str(round(self.__y,2)) + ")"
        
        return out_str
    
    def __repr__(self):
        ''' returns representation of vector'''
        out_str = "({:02d},{:02d})".format(self.__x, self.__y)
        
        return out_str
    
    def __add__(self, v):
        ''' returns addition of vectors in Vector format'''
        return Vector(self.__x + v.__x, self.__y + v.__y)
    
    def __sub__(self, v):
        ''' returns subtraction of vectors in Vector format'''
        return Vector(self.__x - v.__x, self.__y - v.__y)
    
    def __mul__(self,v):
        ''' returns multiplication of vectors in Vector format'''
        return Vector(self.__x * v.__x, self.__y * v.__y)
    
    def magnitude(self):
        ''' returns magnitude of given vector'''
        from math import sqrt
        return sqrt(self.__x**2 + self.__y**2)
    
    def __eq__(self, v):
        ''' returns true/false if vectors are equal '''
        return self.__x == v.__x and self.__y == v.__y
    
    def __rmul__(self, v):
        ''' returns multiplication but not in Vector format'''
        return self.__x * v.__x + self.__y * v.__y
    
    def unit(self):
        ''' function returns ValueError if magnitude = 0'''
        result = self.magnitude()
        if result == 0:
            
            raise ValueError("Cannot convert zero vector to a unit vector")
        
    
    
        
def main():
    ''' function used for testing previous functions'''
    # testing __inti__ and __str__
    v1 = Vector(1,2)
    v2 = Vector(3,4)
    print(v1)
    print(v2)
    
    # testing __add__
    v_ret = v1.__add__(v2)
    print(v_ret)
    v3 = Vector(5,-2)
    v_ret = v1.__add__(v3)
    print(v_ret)
    v4 = Vector(-3,-3)
    v_ret = v1.__add__(v4)
    print(v_ret)
    
    # testing __sub__
    v_ret = v1.__sub__(v2)
    print(v_ret)
    v_ret = v1.__sub__(v4)
    print(v_ret)
    
    # testing __mul__
    v_ret = v1.__mul__(v4)
    print(v_ret)
    v_ret = v1.__mul__(v2)
    print(v_ret)
    
    # testing __rmul__
    v_ret = v1.__rmul__(v4)
    print(v_ret)
    
    # testing __eq__
    v5 = Vector(3,4)
    v_ret = v2.__eq__(v5)
    print(v_ret)
    
    v6 = Vector(0,0)
    v_ret = v1.unit()
    print(v_ret)
    # testing unit function
    v_ret = v6.unit()
    print(v_ret)
main()