#lab07.py
# Algorithm
# Answering questions about unauthorized immigration population

# importing csv to get access to data
import csv
from operator import itemgetter

# variable INDUSTRIES for largest number of unauthorized immigrants working
INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

# read file function to read file
def read_file(fp):
    
    # return list as empty list
    return_list = []  
    
    # reads csv file
    reader = csv.reader(fp) # attaches a reader to the file fp
    
    # skips the first 4 lines of the file
    next(reader,None)
    next(reader,None)
    next(reader,None)
    next(reader,None)
    
    temp_list = next(reader)
    return_list.append(temp_list)
    
    next(reader,None)
    
    # reads every line in the file
    for line in reader:
        # adds each line to empty list
        return_list.append(line)
   
    return return_list  

#get totals function to add up total and individual state populations
def get_totals(L):
    
    #initializing sum of us and sum of states to 0
    sum_of_US = 0
    sum_of_states = 0
    
    # convert to float and remove commas
    sum_of_US = float(L[0][1].replace(',', ''))
    
    # reads each line in file
    for row in L:
        # state population does not include U.S. population 
        if row[0] == "U.S.":
            continue
        temp_str = row[1].replace(',','')
        
        # for all states with <5000 population
        sum_of_states = sum_of_states + float(temp_str.strip('<'))
     
    # returns both populations
    return sum_of_US, sum_of_states  # temoprary return value so main runs

# function to calculate industry counts
def get_industry_counts(L):
    
    # empty list
    return_list = []
    
    # initializing all counts to 0
    agriculture_count = 0
    business_services_count = 0
    construction_count = 0
    leisure_count = 0
    manufacturing_count = 0
    
    # reads each line in file
    for row in L:
        # row 9 is row of interest
        temp_str = row[9]
        # not including U.S population in calculation
        if row[0] == "U.S.":
            continue
        # if statement to increase count by 1 when each is true
        if temp_str == INDUSTRIES[0]:
            agriculture_count += 1
        if temp_str == INDUSTRIES[1]:
            business_services_count += 1
        if temp_str == INDUSTRIES[2]:
            construction_count += 1
        if temp_str == INDUSTRIES[3]:
            leisure_count += 1
        if temp_str == INDUSTRIES[4]:
            manufacturing_count += 1
    
    # appending all data calculated to return list 
    return_list.append([INDUSTRIES[0],agriculture_count])
    return_list.append([INDUSTRIES[1],business_services_count])
    return_list.append([INDUSTRIES[2],construction_count])
    return_list.append([INDUSTRIES[3],leisure_count])
    return_list.append([INDUSTRIES[4],manufacturing_count])
    
    # sorts from increasing to decreasing order
    return_list.sort(key=itemgetter(1), reverse = True) 
    
    return return_list  # temoprary return value so main runs

# function to get largest unauthorized immigration population in states
def get_largest_states(L):
    
    # empty string
    return_list = []
    # converts to float and removes %
    us_percentage = float(L[0][2].replace('%', ''))
    
    # read each row in L
    for row in L:
        # converts to float and removes %
        temp_state_percentage = float(row[2].replace('%', ''))
        
        # if statement to add states with larger % than U.S to empty list
        if temp_state_percentage > us_percentage:
            return_list.append(row[0])
    
    # returns list in alphabetical order       
    return_list.sort()
    
    
    return return_list  # temoprary return value so main runs

# main function
def main(): 
    # opens file and reads the file
    fp = open("immigration.csv")
    L = read_file(fp)
    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        # prints U.S. and total population
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    # prints largest states where unauthorized immigration is largest
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    # prints out industry counts for largest industries
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
 
# calling main function       
if __name__ == "__main__":
    main()
    

    
    
        
    
        
        
    
    
    
    


