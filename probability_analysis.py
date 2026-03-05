import global_vars as gv
from card_functions import find_suit, find_level
import math

def computer_bet(hand):
    bet = 0
    estimate = []

    for i in hand:  # rates the chance per card on being able to win a strike
        aboveInHand = 0
        for p in hand:
            if (find_suit(i) == find_suit(p)) and (find_level(i) <= find_level(p)):
                aboveInHand += 1  # finds cards that beat your card, which are already in your hand. includes the card itself
        below = (find_level(i) - 2)
        if find_suit(i) == find_suit(gv.topCard):  # finds number of cards that can beat your card. cards in a suit - cards under card level - card itself and other same-suit cards in your hand + 12 cards from trump suit because one trump card is already dealt - trump cards in hand
            above = 13 - below - aboveInHand
            if find_level(i) < find_level(gv.topCard): above -= 1
        else:
            trumpCardsInHand = 0 #
            for q in hand:
                if find_suit(q) == find_suit(gv.topCard): trumpCardsInHand += 1
            above = 13 - below - aboveInHand + 12 - trumpCardsInHand
        n = 52 - gv.rounds - 1
        k = gv.rounds
        p = (above*(52-gv.rounds-2))/math.comb(n,k)
        estimate.append(p)
    win_percent = []
    for i in estimate:
        win_percent.append(str(round((1.00 - i)*100,1))+"%")
    gv.estimate = [estimate,win_percent]
