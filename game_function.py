from probability_analysis import eval_hand
from card_functions import *
import global_vars as gv

def crossout(text): #from stack overflow
    return ''.join(c + '\u0336' for c in text)


def turn(playerNum):
    if not gv.centerPile[0]:
        print(gv.playerNames[playerNum])
        print("Choose a card (1-{}):\n\n  ".format(len(gv.players[playerNum])) + str(gv.players[playerNum]) +"\n")
        gv.centerPile.append(gv.players[playerNum][int(input())-1])
        gv.players[playerNum].remove(gv.centerPile[0])
    else:
        print("Cards on Pile: " + gv.centerPile + "\n")
        requiredSuit = find_suit(gv.centerPile[0])
        for i in gv.players[playerNum]:
            if find_suit(i) != requiredSuit or find_suit(gv.trumpCard): print(crossout(i))
            else: print(i)
        choice = int(input("Select a valid card: ") - 1)
        while find_suit(gv.players[playerNum][choice]) != requiredSuit or find_suit(gv.trumpCard):
            choice = input("Invalid choice. Select a valid card.")


def round_start():
    dealcard(gv.trumpCard)
    print("Trump card:      " + str(gv.trumpCard))
    for i in gv.players:
        player = gv.players.index(i)
        eval_hand(player)
        print(gv.playerNames[player]+":")
        print(gv.player_evals[player])

    gv.player1_bid = input("\nHow many tricks will you win out of {}? ".format(gv.rounds))
    gv.starting_player = int(input("\nWho starts the Round? ")) - 1
    print("Player "+ str(gv.starting_player+1) +" starts the round:")

    while gv.turnCount != len(gv.players):
        local_count = 0
        turn(gv.starting_player + local_count)
        gv.turnCount += 1
        local_count += 1
        if (gv.starting_player + local_count) == len(gv.players - 1):
            gv.starting_player = 0
            local_count = 0 

    if gv.turnCount == len(gv.players):
        pass



def set_players(num):
    gv.players = [gv.player1]
    p = 0
    while num != 1:
        gv.players.append(gv.opponents[p])
        p += 1
        num -= 1