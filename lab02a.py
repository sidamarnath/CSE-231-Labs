###########################################################
#lab02a.py
#Algorithm
#Prompts user for positive integer
#Continue asking for integers until user enters 0
#Calculates the odd count, even count, odd sum, even sum, and positive count
#Negative numbers entered will be ingored in calculations
 ###########################################################


#declaring variables to 0 to hold number counts and sums
odd_count = 0
even_count = 0
odd_sum = 0
even_sum = 0
positive_count = 0

#While loop to continue asking user for an integer
while True:
    number = int(input("Enter an integer: "))
    
    # program will ignore negative inputs and continue while loop
    if number < 0:
        print("Number is negative")
        continue
    
     #Once the user enters 0, the loop breaks    
    if (number == 0):
        break
    
    #Positive count increases by 1 when a positive integer is entered
    positive_count = positive_count + 1
    
    #Checks whether the integer entered is odd or even 
    if (number % 2 == 0):
        even_count = even_count + 1
        even_sum = even_sum + number
    else:
        odd_count = odd_count + 1
        odd_sum = odd_sum + number
        
#Displays all information processed by program 
print("The sum of odds is ", odd_sum)
print("The sum of evens is ", even_sum)
print("The odd count is ", odd_count)
print("The even count is ", even_count)
print("The positive integer count is ", positive_count)  
    
    
    

