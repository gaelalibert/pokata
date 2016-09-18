from poker_cards import Cards 
from poker_table import Table
import random as rd

def deck_creation():
	deck = []
	for i in range(2,15):
		for j in range(1,5):
			deck.append((i,j))
	return(deck)

def show_deck(deck : list):
	for item in deck:
		card = Cards(item[0], item[1])
		print(card.show())

def dealing(table : Table, deck : list):
	cards_dealed = []
	for player in table.spots_taken:
		card_idx = rd.sample(deck, 2)
		deck = set(deck) - set(card_idx)
		card1 = Cards(card_idx[0][0], card_idx[0][1])
		cards_dealed.append([player, card1])
		card2 = Cards(card_idx[1][0], card_idx[1][1])
		cards_dealed.append([player, card2])
	return(deck, cards_dealed)


def dealing_board(deck : list):
	board_cards = rd.sample(deck, 5)
	deck = set(deck) - set(board_cards)
	return(deck, board_cards)

def player_game(spot, board_cards, cards_dealed):
	player_cards = [x[1] for x in cards_dealed if x[0] == spot]
	for cards in board_cards:
		player_cards.append(Cards(cards[0], cards[1]))
	return(player_cards)






#print(rd.sample(deck_creation(), 1))
	


