# lab04.py
# Algorithm
# Leap year funcion tests whether input year is a leap year
# Rotate function will take a string and an int and rotate the string by int
# Digit Count function will count the zero, even, and odd numbers in a number
# Float Check function will return true if string contains only digits

# Function for calculating leap year where a year is entered as a string
def leap_year(year_str):
    # Converting year from string to integer
    year_int = int(year_str)
    # If statement to calulate whether year entered is a leap year
    if year_int % 400 == 0 or (year_int % 4 == 0 and year_int % 100 != 0):
        # Returns true if year entered is a leap year and false if it is not
        return True
    else:
        return False
 
# Function for rotating characters in a string
def rotate(s,n):
    # Takes the length of the string entered and puts it in variable word
    word = len(s)
    # Rotates the word by the integer n that is input by user
    o = s[word - n:]
    # Calculates and returns the rotated string
    s = o + s[:word - n]
    return s

# Function digit count to count number of digits in a number
def digit_count(number):
    # Change number to a string
    number = str(number)
    # Initialize variables to 0
    zero_count = 0
    even_count = 0
    odd_count = 0
    # For loop for digits in number
    for digits in number:
        # If statement to account for decimals in input number
        if digits != ".":
            digits = int(digits)
            if digits == 0:
                zero_count += 1   
            # If digit is odd, odd count will increase by 1
            elif digits % 2 == 0:
                even_count = even_count + 1
            # Else, even count will increase by 1
            else:
                odd_count = odd_count + 1
        else:
            break
            
            #Returns even count, odd count, zero count and temp count zero
    return(even_count, odd_count, zero_count)
    
    
def float_check(number):
    return number.replace(".","",1).isdigit()
    
#print(leap_year("1900"))
#print(rotate("abcdefgh",3))
print(digit_count("123400.345"))
#print(float_check("34e46"))


