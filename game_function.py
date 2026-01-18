from probability_analysis import computer_bet
from card_functions import *
import global_vars as gv

def turn():
    if gv.centerPile == "":
        print("Choose a card (1-{}):\n\n  ".format(len(gv.player1)) + str(gv.player1) +"\n")
        gv.centerPile = gv.player1[int(input())-1]
        gv.player1.remove(gv.centerPile)
    gv.turnCount += 1

def round_start():
    dealcards(gv.topCard)
    print("Trump card:      " + str(gv.topCard))
    turn()
    for i in gv.players:
        computer_bet(gv.players[gv.players.index(i)])
        print(gv.playerNames[gv.players.index(i)]+":")
        print("  avg # of cards < these cards:   " + str(gv.estimate[0]) + "\n  win % chance:                   " + str(gv.estimate[1]))

    gv.bid = input("\nHow many strikes will you win out of {}? ".format(gv.rounds))

def set_players(num):
    gv.players = [gv.player1]
    p = 0
    while num != 1:
        gv.players.append(gv.opponents[p])
        p += 1
        num -= 1