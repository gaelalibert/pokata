from poker_table import Table
from poker_player import Players 
from poker_cards import Cards
from poker_hand_values import HandValue
from utils import *

# We create the table
cg_table = Table(limit = 1)
STEP = "pre-flop"

#We create our players and add them to the table
robert = Players('Robert')
youri = Players('Youri')
zizou = Players('Zinedine')
dede = Players('Didier')
lilian = Players('Lilian')
titi = Players('Thierry')

cg_table.sit(robert, 50)
cg_table.sit(youri, 99)
cg_table.sit(zizou, 100)


# The dealer is chosen randomly (for this iteration)
cg_table.dealer = rd.choice(list(cg_table.spots_taken))
print("The seat %i is the Dealer" %cg_table.dealer)
dealer = cg_table.spot_name[cg_table.dealer]
print("The player %s is the Dealer" %dealer)

ordered_players = ordered_seats(cg_table)
print(seats_list_to_names_list(ordered_players, cg_table))

# We create the full deck
deck = deck_creation()

# We chose the 2 cards for all players
chosen_cards = [{'pseudo': 'Robert', 'card1': (14,3), 'card2': (14,2)},
				{'pseudo': 'Youri', 'card1': (13,3), 'card2': (13,2)},
				{'pseudo': 'Zinedine', 'card1': (12,3), 'card2': (12,2)}]

deck, cards_dealed = chosen_dealing(cg_table, deck, chosen_cards)

for i in show_cards_dealed(cg_table, cards_dealed):
	print(i)

for i in cg_table.players:
	i.show_info()

cg_table.show()

# The 5 board cards
#deck, board_cards = dealing_board(deck)
#print("The board cards are the following : ")
#show_deck(board_cards)

# The flop
deck, flop_cards = dealing_flop(deck)
STEP = "flop"
print("The flop cards are the following : ")
show_deck(flop_cards)
board_cards = flop_cards

# The turn
deck, turn_card = dealing_turn(deck)
STEP = "turn"
print("The turn card is the following : ")
show_deck(turn_card)
board_cards += turn_card

# The river
deck, river_card = dealing_turn(deck)
STEP = "river"
print("The river card is the following : ")
show_deck(river_card)
board_cards += river_card


# We select the best game among all players
hand_winner(cg_table, board_cards, cards_dealed)











#We want to sit on this table
#print(cg_table.sit())

#cg_hand = Cards(11,3)

#cg_hand.show()