from poker_table import Table
from poker_cards import Cards
from poker_hand_values import HandValue
from utils import *

# We create the table
cg_table = Table(6)

toto = False
while toto == False:
	# We create the full deck
	deck = deck_creation()

	# e deal 2 cards per players
	deck, cards_dealed = dealing(cg_table, deck)

	for i in cards_dealed:
		print([i[0], i[1].show()])

	# The 5 board cards
	deck, board_cards = dealing_board(deck)

	print("The board cards are the following : ")
	show_deck(board_cards)

	# Final game for all players
	for player in cg_table.spots_taken:
		print("Game of player %d : " %player)
		a = player_game(player, board_cards, cards_dealed)
		value = HandValue(a)
		print(value.best_hand())
		if value.double_pair()[0] == True:
			toto =True








#We want to sit on this table
#print(cg_table.sit())

#cg_hand = Cards(11,3)

#cg_hand.show()