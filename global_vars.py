player1 = []
player1_eval = []
player1_bid = 0
player2 = []
player2_bid = 0
player2_eval = []
player3 = []
player3_bid = 0
player3_eval = []
player4 = []
player4_bid = 0
player4_eval = []
opponents = [player2, player3, player4]
players = []
player_evals = [player1_eval, player2_eval, player3_eval, player4_eval]
player_bids = [player1_bid, player2_bid , player3_bid, player4_bid]
playerNames = ["Player 1", "Player 2", "Player 3", "Player 4"]
cardPool = []
trumpCard = ""
turnCount = 1
rounds = 0
centerPile = [] #where players play cards
starting_player = 0

def dump_vars():
    return