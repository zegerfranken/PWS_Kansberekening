import global_vars as gv
from card_functions import find_suit, find_level
import math

from global_vars import player1_eval


def hypergeometric(N, K, n, k):
    return (math.comb(K, k)) * (math.comb((N - K), (n - k))) / (math.comb(N, n))


def eval_hand(player):
    for i in gv.players[player]:  # rates the chance per card on being able to win a strike
        aboveInHand = 0
        for p in gv.players[player]:
            if (find_suit(i) == find_suit(p)) and (find_level(i) <= find_level(p)):
                aboveInHand += 1  # finds cards that beat your card, which are already in your hand. includes the card itself
        below = (find_level(i) - 2)
        if find_suit(i) == find_suit(
                gv.topCard):  # finds number of cards that can beat your card. cards in a suit - cards under card level - card itself and other same-suit cards in your hand + 12 cards from trump suit because one trump card is already dealt - trump cards in hand
            above = 13 - below - aboveInHand
            if find_level(i) < find_level(gv.topCard): above -= 1
        else:
            trumpCardsInHand = 0  #
            for q in gv.players[player]:
                if find_suit(q) == find_suit(gv.topCard): trumpCardsInHand += 1
            above = 13 - below - aboveInHand + 12 - trumpCardsInHand
        N = 52 - gv.rounds - 1  #unseen cards in game
        K = above
        n = (len(gv.players) - 1) * gv.rounds
        k_upper_bound = n + 1  #added +1 due to pythons range not including the top value. for k in range 1 - 5, printing k returns 1 2 3 4, excluding 5. this bound checks for every single chance, up to the chance of each card an opponent drew being superior
        summed_probability_superior_cards = 0.0
        for k in range(1, k_upper_bound): summed_probability_superior_cards += hypergeometric(N, K, n, k)  #equivalent to summation in mathematics
        chance = (str(int(round((1-summed_probability_superior_cards), 2)*100))+"% ") #turns 0.6 (chance of losing) into 40% (chance of winning)
        weighted_average_superior_cards = n*(K/N)
        chance += str(round(weighted_average_superior_cards, 2))
