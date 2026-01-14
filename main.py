import random
import math

rounds = 3
playerHand = []
opponentHand = []
cardPool = []


def main():
    generate_deck()
    print(len(cardPool))
    deal_rounds(rounds,playerHand,opponentHand)
    print(playerHand)
    print(opponentHand)

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
    player.append(deck[random.randrange(0,len(deck)-1)])

def deal_rounds(num_rounds,player,opponent):
    while num_rounds != 0:
        dealcards(player,cardPool)
        dealcards(opponent,cardPool)
        num_rounds -= 1

def gamestart():
    print("Your cards are:\n")


main()

