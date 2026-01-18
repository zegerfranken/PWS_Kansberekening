from card_functions import *
from computer_bet import computer_bet

playerHand = []
opponent1Hand = []
opponent2Hand = []
opponent3Hand = []
activePlayers = [playerHand, opponent1Hand]
cardPool = []
turnCount = 0 #turn counter. 0 = player, 1 = opponent1 etc

def main():
    generate_deck(cardPool)
    rounds = int(input("Rounds? "))
    add_players(int(input("Players? ")))
    deal(rounds,activePlayers)
    print_cards(0)
    round_start(rounds)


#end of main

def turn(actor):
    return


def computer_turn_dumb():
    return




def round_start(rounds):
    topCard = ""
    topCard = dealcards(topCard, cardPool)
    print("Trump card:      " + str(topCard))
    bid = input("How many strikes will you win out of {}?\n".format(rounds))
    computer_bet(opponent1Hand,find_suit(topCard))

def add_players(num):
    if num == 3: activePlayers.append(opponent2Hand)
    elif num == 4:
        activePlayers.append(opponent2Hand)
        activePlayers.append(opponent3Hand)
    elif num == 2: pass
    else: print("Invalid number of players, continuing with 2...")

main()
