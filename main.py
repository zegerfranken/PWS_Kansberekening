from card_functions import generate_deck, deal, print_cards
from game_functions import add_players, round_start

playerHand = []
opponent1Hand = []
opponent2Hand = []
opponent3Hand = []
activePlayers = [playerHand, opponent1Hand]
cardPool = []
turnCount = 0 #turn counter. 0 = player, 1 = opponent1 etc

def main():

    mode = int(input("See all cards?\n  0: no\n  1: yes\n"))
    generate_deck(cardPool)
    rounds = int(input("Rounds? "))
    add_players(int(input("Players? ")),activePlayers,opponent2Hand,opponent3Hand)
    deal(rounds,activePlayers,cardPool)
    print_cards(1,activePlayers,playerHand)
    round_start(rounds,cardPool,activePlayers)

main()
