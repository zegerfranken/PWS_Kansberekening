from card_functions import find_suit, find_level

def computer_bet(hand, trump_suit):
    bet = 0
    estimate = []
    level_list = []
    p = 2
    while len(level_list) < 13:
        level_list.append(p)
        p += 1

    for i in hand:  # rates the chance per card on being able to win a strike
        aboveInHand = 0
        for p in hand:
            if (find_suit(i) == find_suit(p)) and (find_level(i) <= find_level(
                p)): aboveInHand += 1  # finds cards that beat your card, which are already in your hand. includes the card itself
        print(aboveInHand)
        below = (find_level(i) - 2)
        above = 0
        if find_suit(
                i) == trump_suit:  # finds number of cards that can beat your card. cards in a suit - cards under card level - card itself and other same-suit cards in your hand + 14 trump cards (if card is not a trump)
            above = 14 - below - aboveInHand
        else:
            above = 14 - below + 14
    return bet
