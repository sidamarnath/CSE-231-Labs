# lab05.py
# algorithm
# taking data from a file and adding a new column related to given data(BMI)
#program will calculate the min, max, and avg of all columns

#opening files with designated modes 
infile = open("data.txt", "r")
outfile = open("output.txt", "w")

# will read the line in the string
str_row = infile.readline()

# printing all headings for columns using .format method
print("{:<12s}{:<12s}{:<12s}{:<12s}".format("Name", "Height(m)", "Weight(kg)", "BMI"), file = outfile)

# initializing max and total to 0
#initializing all min values to well above max value from data given
total_height = 0
minimum_height = 10e6
maximum_height = 0
total_weight = 0
minimum_weight = 10e6
maximum_weight = 0
total_BMI = 0
minimum_BMI = 10e6
maximum_BMI = 0
row_count = 0

#for loop to read each line in data.text file
for line in infile:
    row = line.split()
    
    # changing all rows 1,2, and 3 to floats
    height = float(row[1])
    # calculating total, max, and min values for height
    total_height += height
    if height < minimum_height:
        minimum_height = height
    if height > maximum_height:
        maximum_height = height
    
    # calculating total, max, and min values for weight
    weight = float(row[2])
    total_weight += weight
    if weight < minimum_weight:
        minimum_weight = weight
    if weight > maximum_weight:
        maximum_weight = weight
    
    row_count += 1
    # calculating total, max, and min values for BMI
    # formula for calculaing BMI
    BMI = weight / (height ** 2)
    total_BMI += BMI
    if BMI < minimum_BMI:
        minimum_BMI = BMI
    if BMI > maximum_BMI:
        maximum_BMI = BMI
    
    # append method to add BMI column with existing data
    row.append(BMI)
    
    print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format(row[0], height, weight, BMI), file = outfile)
    
# prints average, max, and min values for the number of rows in the file
print( file = outfile)

print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Average", total_height/row_count, total_weight/row_count, total_BMI/row_count), file = outfile) 
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Max", maximum_height, maximum_weight, maximum_BMI), file = outfile)
print("{:<12s}{:<12.2f}{:<12.2f}{:<12.2f}".format("Min", minimum_height, minimum_weight, minimum_BMI), file = outfile) 


# closes both files   
infile.close()
outfile.close()

