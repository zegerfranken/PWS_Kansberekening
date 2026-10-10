from probability_analysis import eval_hand
from card_functions import *
import global_vars as gv

def turn():
    if gv.centerPile == "":
        print("Choose a card (1-{}):\n\n  ".format(len(gv.player1)) + str(gv.player1) +"\n")
        gv.centerPile = gv.player1[int(input())-1]
        gv.player1.remove(gv.centerPile)
    else:
        return

    gv.turnCount += 1

def round_start():
    dealcard(gv.trumpCard)
    print("Trump card:      " + str(gv.trumpCard))
    for i in gv.players:
        player = gv.players.index(i)
        eval_hand(player)
        print(gv.playerNames[player]+":")
        print(gv.player_evals[player])

    gv.player1_bid = input("\nHow many tricks will you win out of {}? ".format(gv.rounds))
    print("Player "+ str(gv.starting_player+1) +" starts the round:")
    turn()


def set_players(num):
    gv.players = [gv.player1]
    p = 0
    while num != 1:
        gv.players.append(gv.opponents[p])
        p += 1
        num -= 1