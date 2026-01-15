import random
import math

playerHand = []
opponent1Hand = []
opponent2Hand = []
opponent3Hand = []
activePlayers = [playerHand, opponent1Hand]
cardPool = []

def main():
    generate_deck(cardPool)
    rounds = int(input("How many Rounds will you play? "))
    #players = input("How many players will be playing?")


    deal(rounds,activePlayers)
    for i in activePlayers:
        opponent_number = 1
        if activePlayers.index(i) == 0:
            print("Your hand: " + str(i))
        else:
            print("Opponent " + str(opponent_number) + " hand: " + str(i))
            opponent_number += 1

def dealcards(player, deck):
    selected_card = random.randrange(0, len(deck) - 1)
    player.append(deck[selected_card])
    deck.pop(selected_card)


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



def gamestart():
    print("Your cards are:\n")

main()
