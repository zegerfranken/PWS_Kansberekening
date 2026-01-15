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
    players = input("How many players will be playing?")


    deal(rounds,activePlayers)
    for i in activePlayers:
        opponent_number = 1
        if i == playerHand:
            print("Your hand: " + str(activePlayers))
        else:
            print("Opponent " + str(opponent_number) + " hand: " + str(activePlayers))

def generate_deck(deck):
    card_suits = ["♤", "♡", "♢", "♧"]
    card_level = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for x in card_suits:
        for y in card_level:
            if y != "10":
                deck.append("[" + y + " of " + x + "]") #fixes spacing due to number ten having two digits
            else:
                deck.append("[" + y + "of " + x + "]")


def dealcards(players,deck):
    for i in players:
        selected_card = random.randrange(0, len(deck) - 1)
        players[players.index(i)].append(deck[selected_card])
        deck.pop(selected_card)

def deal(num_rounds,players):
    while num_rounds != 0:
        dealcards(players,cardPool)
        num_rounds -= 1

def gamestart():
    print("Your cards are:\n")

main()
