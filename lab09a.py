#######################################
# lab09a.py
# Algorithm
# uses dictionary of lists
# program links continents to countries and cities where it is located
#######################################

# import itemgetter
from operator import itemgetter


def build_map( in_file1, in_file2 ):
    
    # reads each file and each line in each file
    in_file1.readline()
    in_file2.readline()
    
    # empty dictionary
    data_map = {}

    #READ EACH LINE FROM FILE 1
    for line in in_file1:
        
        # Split the line into two words
        continent_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        continent = continent_list[0].strip().title()
        country = continent_list[1].strip().title()
        
        # Ignore empty strings
        if continent != "":
            
            # If current continent not in map, insert it 
            if continent not in data_map:
                data_map[continent] = {}
            
            # If country is not empty insert (continent is guaranteed to be in map)
            if country not in data_map[continent]:
                
            
                # If current country not in map, insert it 
                data_map[continent][country] = []

     #READ EACH LINE FROM FILE 2
    for line in in_file2:  
        
        # Split the line into two words
        countries_list = line.strip().split()
        
        # Convert to Title case, discard whitespace
        country = countries_list[0].strip().title()
        city = countries_list[1].strip().title()
        
        # Ignore empty strings
        if country != "":
            
            # insert city (country is guaranteed to be in map)
            for continent in data_map:
                if country in data_map[continent]:
                    if city not in data_map[continent][country]:
                        data_map[continent][country].append(city)
    return data_map

def display_map( data_map ):
    
    # convert to list before program is able to sort data
    continents_list = list(data_map.keys())
    continents_list.sort() #sorted list of the continent keys
    
    # For each continent
    for continents in continents_list:
        print("{}:".format(continents)) #continents in continents_list
        countries_list = list(data_map[continents].keys())
        countries_list.sort() #sorted list of the countries keys in the continents
          
        # For each country
        for country in countries_list:
            
            # display formatting for results
            print("{:>10s} --> ".format(country),end = '') #countries in countries_list
            cities = data_map[continents][country]
            cities.sort() #sorted list of the cities
            # For each city 
            num_of_cities = 0
            for city in cities:
                num_of_cities += 1 
                #As long as not last city, add a comma and a space after the cities names
                if len(cities) > num_of_cities:
                    print('{}, '.format(city),end = '') # city in cities 
                # if it is the last, don't add a comma and a space.
                else:
                    print('{}'.format(city)) # city in cities

def open_file():
    # prompts user for both files
    try:
        filename = input("Enter file name: ")
        in_file = open( filename, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file

def main():

    data_map = {}
    in_file1 = open_file() #Continents with countries file: continents.txt
    in_file2 = open_file() #Countries with cities file: cities.txt

    if in_file1 != None and in_file2 != None:
        
        data_map = build_map( in_file1, in_file2 ) # data_map is a dictionary
        display_map(data_map)
        in_file1.close()
        in_file2.close()

if __name__ == "__main__":
    main()

