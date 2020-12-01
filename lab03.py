#lab03.py
#Asks user for word until user enters "quit"
#If word begins with a vowel, program will print the word plus "way"
#If word begins with a consonant, program will append all consonants and "ay"


#declaring VOWELS variable set to all vowels
VOWELS = "aeiou"

#While loop to continue asking user for a word
while True:
    word = input("Enter a word ('quit' to quit): ").lower()
    
    #if user enters the word "quit", the loop will break
    if word == "quit":
        break 
    #if an empty string is entered, the program prints an error message
    elif word== "":
        print("Can't convert empty string.  Try again.")
        continue
    #checks to see if the first letter of the word is a vowel or not
    for i,ch in enumerate(word):
        if i == 0 and ch in VOWELS:
            print(word + "way")
            break
        elif ch not in VOWELS:
            if len(word) == 1: #handles single character inputs
                print(ch + "ay")
                break
            else:
                pass
        else:
            print(word[i:] + word[0:i] + "ay") #prints corresponding outputs
            break 
            #breaks after the first output if more than one vowel in word
            
        
    
    
            
                
        

    
    


    



