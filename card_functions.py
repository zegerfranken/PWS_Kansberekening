import re
import random
import global_vars as gv

def find_suit(card):
    suit = ""
    if card.find("♡") != -1: suit = "hearts"
    elif card.find("♤") != -1: suit = "spades"
    elif card.find("♢") != -1: suit = "diamonds"
    elif card.find("♧") != -1: suit = "clubs"
    return suit


def find_level(card):
    level = re.sub(r"\D", "", card)    #regex from stack overflow
    if level == "":
        level = card[1].replace("J","11").replace("Q","12").replace("K","13").replace("A","14")
    return int(level)


def print_cards(value):
    if value == 1:
        opponent_number = 1
        for i in gv.players:
            if gv.players.index(i) == 0:
                print("\nYour hand:       " + str(i)[1:-1].replace("'",""))
            else:
                print("Opponent " + str(opponent_number) + " hand: " + str(i)[1:-1].replace("'",""))
                opponent_number += 1
    else: print("Your hand:       " + str(gv.player1)[1:-1].replace("'", ""))


def dealcards(player):
    if isinstance(player, list):
        if len(gv.cardPool) != 1:
            selected_card = random.randrange(0, len(gv.cardPool) - 1)
            player.append(gv.cardPool[selected_card])
            gv.cardPool.pop(selected_card)
        else:
            player.append(gv.cardPool[0])
            gv.cardPool.pop(0)
    elif isinstance(player, str):
        if len(gv.cardPool) != 1:
            selected_card = random.randrange(0, len(gv.cardPool) - 1)
            player = gv.cardPool[selected_card]
            gv.topCard = player
            gv.cardPool.pop(selected_card)
        else:
            gv.topCard = gv.cardPool[0]
            gv.cardPool.pop(0)
    return 0


def deal():
    num_rounds = gv.rounds
    while num_rounds != 0:
        for i in gv.players:
            dealcards(gv.players[gv.players.index(i)])
        num_rounds -= 1


def generate_deck():
    card_suits = ["♤", "♡", "♢", "♧"]
    card_level = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for x in card_suits:
        for y in card_level:
            if y != "10": gv.cardPool.append("[" + y + " of " + x + "]") #fixes spacing due to number ten having two digits
            else: gv.cardPool.append("[" + y + "of " + x + "]")
