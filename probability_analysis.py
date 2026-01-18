from card_functions import find_suit, find_level

def computer_bet(hand, top_card,active_players):
    bet = 0
    estimate = []

    for i in hand:  # rates the chance per card on being able to win a strike
        aboveInHand = 0
        for p in hand:
            if (find_suit(i) == find_suit(p)) and (find_level(i) <= find_level(p)):
                aboveInHand += 1  # finds cards that beat your card, which are already in your hand. includes the card itself
        below = (find_level(i) - 2)
        if find_suit(i) == find_suit(top_card):  # finds number of cards that can beat your card. cards in a suit - cards under card level - card itself and other same-suit cards in your hand + 12 cards from trump suit because one trump card is already dealt - trump cards in hand
            above = 13 - below - aboveInHand
            if find_level(i) < find_level(top_card): above -= 1
        else:
            trumpCardsInHand = 0
            for q in hand:
                if find_suit(q) == find_suit(top_card): trumpCardsInHand += 1
            above = 13 - below - aboveInHand + 12 - trumpCardsInHand
        estimate.append(round(float(((above/52)*len(hand))*(len(active_players)-1)),2)) #average number of cards in the opponents' hand that can beat that card
    win_percent = []
    for i in estimate:
        win_percent.append(str(round((1.00 - i)*100,1))+"%")
    estimate = [estimate,win_percent]
    return estimate
