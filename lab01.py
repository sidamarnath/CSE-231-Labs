import math

#Requesting input from user
a = float(input("\nEnter the coefficient A: "))
b = float(input("\nEnter the coefficient B: "))
c = float(input("\nEnter the coefficient C: "))
d = ((b**2) - (4*a*c))

print("\nThe coefficients of the equation:\n")

#Redisplaying coefficients entered by user
print("  Coefficient A = ", a)
print("  Coefficient B = ", b)
print("  Coefficient C = ", c)

#using quadratic function from math module
root_1 = (-b+math.sqrt(d))/(2*a)
root_2 = (-b-math.sqrt(d))/(2*a)
  
#displaying roots
  
print("\nThe roots of the equation:\n")
print(" Root #1 = ", round(root_1,3))
print(" Root #2 = ", round(root_2,3))



