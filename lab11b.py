######################################
# lab11b.py
# class Time
# Algorithm
# create a class Time to display time "hh:mm:ss"
######################################

class Time():
    # setting instance variables
    def __init__(self, hour = 0, mins = 0, secs = 0):
        ''' construct a 24 hr clock using 3 integers'''
        self.__hour = hour
        self.__mins = mins
        self.__secs = secs
        self.__valid = self.__validate()
        
    def __validate(self):
        # if statement to check for valid time
        flag = False
        if self.__hour >= 0 and self.__hour <= 24:
            
            if self.__mins >=0 and self.__mins <= 60:
            
                if self.__secs >=0 and self.__secs <= 60:
                    return True
            
        return flag

    
    def __repr__(self):
        ''' returns a string as formal representation of clock'''
        out_str = "Class Time: {:02d}:{:02d}:{:02d}".format(self.__hour, self.__mins, self.__secs)
        
        return out_str
    
    def __str__(self):
        ''' returns a string as formal representation of clock'''
        
        out_str = "{:02d}:{:02d}:{:02d}".format(self.__hour, self.__mins, self.__secs)
        
        return out_str
    
    def from_str(self, in_str):
        ''' takes in string of form hh:mm:ss and initializes self object'''
        hour, mins, secs = [int(n) for n in in_str.split(':')]
        self.__hour = hour
        self.__mins = mins
        self.__secs = secs
        self.__valid = self.__validate()
        
# from clockDemo.py       
A = Time( 12, 25, 30 )

print( A )
print( repr( A ) )
print( str( A ) )
print()

B = Time( 2, 25, 3 )

print( B )
print( repr( B ) )
print( str( B ) )
print()

C = Time( 2, 25 )

print( C )
print( repr( C ) )
print( str( C ) )
print()

D = Time()

print( D )
print( repr( D ) )
print( str( D ) )
print()

D.from_str( "03:09:19" )

print( D )
print( repr( D ) )
print( str( D ) )       
        
        
        
        
        
        

