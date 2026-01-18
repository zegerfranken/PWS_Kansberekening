from probability_analysis import computer_bet
from card_functions import *
import global_vars as gv

def turn(actor):
    return


def round_start():
    dealcards(gv.topCard)
    print("Trump card:      " + str(gv.topCard))
    bid = input("\nHow many strikes will you win out of {}? ".format(gv.rounds))
    for i in gv.players:
        print(computer_bet(gv.players[gv.players.index(i)]))

def set_players(num):
    gv.players = [gv.player1]
    p = 0
    while num != 1:
        gv.players.append(gv.opponents[p])
        p += 1
        num -= 1