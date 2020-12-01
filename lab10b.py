#########################################
# lab10b.py
# Algorithm
# Display each player's starting hand
# Create a card game "War" based on cards given
########################################

# importing cards class and random
import cards
#import random
#random.seed(100)

def deal_cards():
    ''' this function deals 5 cards to each player'''
# Create and shuffle the deck of cards
    the_deck = cards.Deck()
    #the_deck.shuffle()
    
    # each player has empty list of cards to begin with
    player_1 = []
    player_2 = []
    
    # each player gets dealt 5 cards
    for i in range(5):
        # deals the cards to each player
        player_1.append(the_deck.deal())
        player_2.append(the_deck.deal())

    return player_1, player_2

def main():
    ''' function will display stating hands and each battle won'''
    # calling deal cards functions
    player_1, player_2 = deal_cards()
    # display starting hand for each player
    print("Starting Hands")
    print("Hand1:", player_1)
    print("Hand2:", player_2)
    print()    
    
    
    
    # while loop to go through each round of game
    while True:
        # pops and displays first card in hand
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)
        
        player_1_rank = card_1.rank()
        player_2_rank = card_2.rank()
        
        # if statement to test for aces
        if player_1_rank == "A":
            player_1_rank = 100
        if player_2_rank == "A":
            player_2_rank = 100
        
        
        # compares the rank of cards
        if player_1_rank == player_2_rank:
            print("Battle was 1: {}, 2: {}. Battle was a draw.".format(card_1, card_2))
        elif player_1_rank > player_2_rank:
            print("Battle was 1: {}, 2: {}. Player 1 wins battle.".format(card_1, card_2))
        else:
            print("Battle was 1: {}, 2: {}. Player 2 wins battle.".format(card_1, card_2))
        
        # depending on player who wins, cards played will be added to winner's hand   
        if player_1_rank > player_2_rank:
            player_1.append(card_1)
            player_1.append(card_2)
        else:
            player_2.append(card_2)
            player_2.append(card_1)
            
        
        # print remaining cards in hand for both players
        print("hand1:", player_1)
        print("hand2:", player_2)
        
        if len(player_1) == 0:
            print("Player 2 wins!!!")
            break
        if len(player_2) == 0:
            print("Player 1 wins!!!")
            break
        # asks user to input to continue playing
        if input("Keep Going: (Nn) to stop:").lower() =="n":
        # if choice is no, the game ends
            if len(player_1) > len(player_2):
                print("Player 1 wins!!!")
            elif len(player_1) == len(player_2):
                print("Draw!!!")
            else:
                print("Player 2 wins!!!")
            break
main()    
    
    



