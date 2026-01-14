roundNo = 1
playerHand = []
opponentHand = []

cardSuits = ["♤", "♡", "♢", "♧"]
cardLevel = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
cardPool = []

for x in cardSuits:
    for y in cardLevel:
        cardPool.append(y + " of " + x)


def dealcards():
    print()

def gamestart():
    print("Your cards are:\n")
