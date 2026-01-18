import re
import random

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


def print_cards(value,active_players,player_hand):
    if value == 1:
        opponent_number = 1
        for i in active_players:
            if active_players.index(i) == 0:
                print("Your hand:       " + str(i)[1:-1].replace("'",""))
            else:
                print("Opponent " + str(opponent_number) + " hand: " + str(i)[1:-1].replace("'",""))
                opponent_number += 1
    else: print("Your hand:       " + str(player_hand)[1:-1].replace("'",""))


def dealcards(player, deck):
    if isinstance(player, list):
        if len(deck) != 1:
            selected_card = random.randrange(0, len(deck) - 1)
            player.append(deck[selected_card])
            deck.pop(selected_card)
            return 0
        else:
            player.append(deck[0])
            deck.pop(0)
            return 0
    elif isinstance(player, str):
        if len(deck) != 1:
            selected_card = random.randrange(0, len(deck) - 1)
            player = deck[selected_card]
            deck.pop(selected_card)
            return player
        else:
            player = deck[0]
            deck.pop(0)
            return player
    return 0

def deal(num_rounds, players,cardPool):
    while num_rounds != 0:
        for i in players:
            dealcards(players[players.index(i)], cardPool)
        num_rounds -= 1


def generate_deck(deck):
    card_suits = ["♤", "♡", "♢", "♧"]
    card_level = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for x in card_suits:
        for y in card_level:
            if y != "10": deck.append("[" + y + " of " + x + "]") #fixes spacing due to number ten having two digits
            else: deck.append("[" + y + "of " + x + "]")
