###############################
# lab08b.py
# Algorithm
# Prints out student scores alphabetically
# If name appears more than once in file, add scores together
###############################

# read file function to open and read file
# takes in dictionary and filename as argument
def read_file(dictionary, filename):
    
    # opens file and reads the lines
    fp = open(filename, "r")
    reader = fp.readlines()
    
    # ignores the first line of the file
    for line in reader[1:]:
        
        #splits line into list
        line_list = line.split()
        
        
        name = line_list[0]
        score = int(line_list[1])
        
        # checks for name in dictionary
        if name not in dictionary:
            dictionary[name] = score
        else:
            # find the dublicate name in dictionary and combine scores
            dictionary[name] += score
        
# display function displays results from read_file function
def display(dictionary):
    
    # set to an empty list
    display_list = list()
    
    # adds name and scores into display list
    for name, score in dictionary.items():
        display_list.append((name, score))
    
    # sorts list alphabetically
    # formats results
    display_list.sort()
    print("{:10s} {:<10s}".format("Name", "Total")) 
    
    for item in display_list:
        print( "{:10s} {:<10d}".format(item[0], item[1]))
        
    
def main():
    dictionary = {}
    read_file(dictionary, "data1.txt")
    read_file(dictionary, "data2.txt")    
    display(dictionary)    
    
main()        
    
