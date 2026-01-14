import random
import math

playerHand = []
opponentHand = []
cardPool = []


def main():
    generate_deck()
    rounds = int(input("How many Rounds will you play? "))
    deal(rounds,playerHand,opponentHand)
    print("Your hand: " + str(playerHand))

def generate_deck():
    card_suits = ["♤", "♡", "♢", "♧"]
    card_level = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for x in card_suits:
        for y in card_level:
            if y != "10":
                cardPool.append("[" + y + " of " + x + "]") #fixes spacing due to number ten having two digits
            else:
                cardPool.append("[" + y + "of " + x + "]")


def dealcards(player,deck):
    selected_card = random.randrange(0,len(deck)-1)
    player.append(deck[selected_card])
    deck.pop(selected_card)

def deal(num_rounds,player,opponent):
    while num_rounds != 0:
        dealcards(player,cardPool)
        dealcards(opponent,cardPool)
        num_rounds -= 1

def gamestart():
    print("Your cards are:\n")


main()

