import math
import random

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
    computer_bet_dumb_confident(rounds,opponent1Hand)

#end of main

def turn(actor):
    return


def computer_turn_dumb():
    return


def computer_bet_dumb_confident(rounds,hand,trump):
    bet = math.floor(rounds/len(activePlayers))
    highCards = []
    for i in hand:
        if (i.find("J") or i.find("Q") or i.find("K") or i.find("A") != -1) and bet < rounds/2:
            highCards.append(i)
    bet += math.ceil(len(highCards)/2)
    return bet


def round_start(rounds):
    topCard = ""
    dealcards(topCard, cardPool)
    print("Trump card:      " + str(topCard))
    bid = input("How many strikes will you win out of {}?\n".format(rounds))


def add_players(num):
    if num == 3: activePlayers.append(opponent2Hand)
    elif num == 4:
        activePlayers.append(opponent2Hand)
        activePlayers.append(opponent3Hand)
    elif num == 2: pass
    else: print("Invalid number of players, continuing with 2...")


def print_cards(value):
    if value == 1:
        opponent_number = 1
        for i in activePlayers:
            if activePlayers.index(i) == 0:
                print("Your hand:       " + str(i)[1:-1].replace("'",""))
            else:
                print("Opponent " + str(opponent_number) + " hand: " + str(i)[1:-1].replace("'",""))
                opponent_number += 1
    else: print("Your hand:       " + str(playerHand)[1:-1].replace("'",""))


def dealcards(player, deck):
    if len(deck) != 1:
        selected_card = random.randrange(0, len(deck) - 1)
        player.append(deck[selected_card])
        deck.pop(selected_card)
    else:
        player.append(deck[0])
        deck.pop(0)


def deal(num_rounds, players):
    while num_rounds != 0:
        for i in players:
            dealcards(players[players.index(i)], cardPool)
        num_rounds -= 1


def generate_deck(deck):
    card_suits = ["♤", "♡", "♢", "♧"]
    card_level = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for x in card_suits:
        for y in card_level:
            if y != "10":
                deck.append("[" + y + " of " + x + "]") #fixes spacing due to number ten having two digits
            else:
                deck.append("[" + y + "of " + x + "]")


main()
