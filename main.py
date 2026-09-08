from card_functions import generate_deck, deal, print_cards
from game_function import set_players, round_start
import global_vars as gv
from probability_analysis import hypergeometric


def main():
    mode = int(input("Display all cards?\n  0: no\n  1: yes\n"))
    generate_deck()
    gv.rounds = int(input("Rounds? "))
    set_players(int(input("Players? ")))
    deal()
    print_cards(mode)
    round_start()

main()

