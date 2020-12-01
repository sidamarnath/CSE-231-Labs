#########################################
# lab10a.py
# Algorithm
# Display each player's starting hand
# Display certain cards given and compare them
########################################

#import cards class
import cards

# importing random 
import random
random.seed( 100 )

# Create a deck of cards
my_deck = cards.Deck()


# Shuffle the deck, then display it 
my_deck.shuffle()
print( "===== shuffled deck =====" )
my_deck.display()


# Deal five cards to each player (alternating)
print( "Dealt five cards to each player (alternating)" )
print()

# player 1 and 2 list set to empty list
player1_list=[]
player2_list=[]
# for loop to deal 5 cards to each player
for i in range(5):
    player1_list.append(my_deck.deal())
    player2_list.append(my_deck.deal())

# Display each player's cards and the cards still in the deck
print( "===== player #1 =====" )
print()
print( player1_list )
print()
print( "===== player #2 =====" )
print()
print( player2_list )
print()
print( "===== remaining cards in deck =====" )
my_deck.display()


# First card dealt to Player #1
player1_card = player1_list.pop( 0 )

print( "First card dealt to player #1:", player1_card )
print("Player #1 hand: ", player1_list)

# First card dealt to Player #2
player2_card = player2_list.pop( 0 )

print( "First card dealt to player #2:", player2_card )
print("Player #2 hand: ", player2_list)

# Compare the ranks of the two cards
print()
if player1_card.rank() == player2_card.rank():
    print( "Tie:", player1_card, "and", player2_card, "of equal rank" )
elif player1_card.rank() > player2_card.rank():
    print( "Player #1 wins:", player1_card, "of higher rank than", player2_card )
else:
    print( "Player #2 wins:", player2_card, "of higher rank than", player1_card )
print()    
player1_card2 = player1_list.pop(0)
player2_card2 = player2_list.pop(0)

# showing second card in each player's hand
print("Second card dealt to player #1: ", player1_card2)
print("Player #1 hand: ", player1_list)
print()

print("Second card dealt to player #2: ", player2_card2)
print("Player #2 hand: ", player2_list)
print()

player1_card5 = player1_list.pop(2)
player2_card5 = player2_list.pop(2)

# showing last card in each player's hand
print("Last card in hand of player #1: ", player1_card5)
print("Last card in hand of player #2: ", player2_card5)
print()
# compares last card
if player1_card5.rank() == player2_card5.rank():
    print( "Tie:", player1_card, "and", player2_card5, "of equal rank" )
elif player1_card5.rank() > player2_card5.rank():
    print(player1_card5, "of higher rank than", player2_card5)
else:
    print(player2_card5, "of higher rank than", player1_card5)
