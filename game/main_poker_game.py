from poker_table import Table
from poker_player import Players 
from poker_cards import Cards
from poker_hand_values import HandValue
from utils import *

# We create the table
cg_table = Table(limit = 1)

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

for i in cg_table.players:
	i.show_info()

# The dealer is chosen randomly (for this iteration)
cg_table.dealer = rd.choice(list(cg_table.spots_taken))
print("The seat %i is the Dealer" %cg_table.dealer)
dealer = cg_table.spot_name[cg_table.dealer]
print("The player %s is the Dealer" %dealer)

# We create the full deck
deck = deck_creation()

# We deal 2 cards per players
deck, cards_dealed = dealing(cg_table, deck)

for i in cards_dealed:
	print([i[0], i[1].show()])

# The 5 board cards
deck, board_cards = dealing_board(deck)

print("The board cards are the following : ")
show_deck(board_cards)

# We select the best game among all players
hand_winner(cg_table, board_cards, cards_dealed)











#We want to sit on this table
#print(cg_table.sit())

#cg_hand = Cards(11,3)

#cg_hand.show()