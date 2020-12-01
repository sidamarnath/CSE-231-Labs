###############################
# lab08a.py
# Algorithm
# Finds unique words and prints count of them for specified data file
# Prints from most frequent to least frequent
# If words have same count, print those words alphabetically
###############################


import string
from operator import itemgetter


def add_word(word_map, word):
    ''' Adding the word into the dictionary and increasing count by 1 if 
    the word is found in the dictionary'''
    
    if word:
        # checks to see if word is in map, if not then count remains at 0
        if word not in word_map:
            word_map[ word ] = 0

        # if word is found in map, increase count by 1
        word_map[ word ] += 1


def build_map( in_file, word_map ):
    ''' This function reads each line in a file and removes any punctuation
    in the file and adds them to the dictionary'''

    for line in in_file:

        # splits each line by space and creates list
        word_list = line.split()

        for word in word_list:

            # removing all punctuation marks in string
            # changing all words to lowercase so captilization and lowercase
            # are counted as the same
            word = word.strip().strip(string.punctuation)
            word = word.lower()
            add_word(word_map, word)
        

def display_map( word_map ):
    ''' This function displays the words in the dictionary and the count of
    each word from most to least frequent. If the count for words is the same
    the program will list them alphabetically'''

    word_list = list()

    # adding word and count tuple to the word list
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # sorting list by largest count to smallest count
    # sorting words alphabetically for equal count
    word_list.sort()
    freq_list = sorted( word_list, key=itemgetter(1), reverse = True )

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():
    ''' This function is used to open the desired file and return the fp'''
    try:
        file_name = input("Enter file name: ")
        in_file = open( file_name, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()

