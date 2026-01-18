from probability_analysis import computer_bet
from card_functions import *

def turn(actor):
    return


def round_start(rounds,card_pool,active_players):
    topCard = ""
    topCard = dealcards(topCard, card_pool)
    print("Trump card:      " + str(topCard))
    bid = input("How many strikes will you win out of {}?\n".format(rounds))
    for i in active_players:
        print(computer_bet(active_players[active_players.index(i)],find_suit(topCard)))

def add_players(num,active_players,opponent2_hand,opponent3_hand):
    if num == 3: active_players.append(opponent2_hand)
    elif num == 4:
        active_players.append(opponent2_hand)
        active_players.append(opponent3_hand)
    elif num == 2: pass
    else: print("Invalid number of players, continuing with 2...")
