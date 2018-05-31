from .poker_cards import Cards 
from .poker_table import Table
from .poker_hand_values import HandValue
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

def dealing(players_left : list, deck : list):
	cards_dealed = []
	for player in players_left:
		card_idx = rd.sample(deck, 2)
		deck = set(deck) - set(card_idx)
		card1 = Cards(card_idx[0][0], card_idx[0][1])
		cards_dealed.append([player, card1])
		card2 = Cards(card_idx[1][0], card_idx[1][1])
		cards_dealed.append([player, card2])
		player.hand = (card1, card2)
	return(deck, cards_dealed)

def chosen_dealing(table : Table, deck : list, chosen_cards : list):
	cards_dealed = []
	if len(chosen_cards) != table.nb_players:
		raise ValueError("There is not the same number of players on the table as the decided cards")
	cards_list = [x['card1'] for x in chosen_cards] + [x['card2'] for x in chosen_cards]
	if len(cards_list) > len(set(cards_list)):
		raise ValueError("There are some duplicated cards in your choice")
	for idx, player in enumerate(table.spots_taken_list):
		player_entry = [x for x in chosen_cards if table.spot_name[player] == x['pseudo']][0]
		card1 = Cards(player_entry['card1'][0], player_entry['card1'][1])
		cards_dealed.append([player, card1])
		card2 = Cards(player_entry['card2'][0], player_entry['card2'][1])
		cards_dealed.append([player, card2])
		table.players[idx].hand = (card1, card2)
	deck = set(deck) - set(cards_list)
	return(deck, cards_dealed)

def dealing_board(deck : list):
	board_cards = rd.sample(deck, 5)
	deck = set(deck) - set(board_cards)
	return(deck, board_cards)

def dealing_flop(deck : list):
	flop_cards = rd.sample(deck, 3)
	deck = set(deck) - set(flop_cards)
	return(deck, flop_cards)

def dealing_turn(deck : list):
	turn_card = rd.sample(deck, 1)
	deck = set(deck) - set(turn_card)
	return(deck, turn_card)

def dealing_river(deck : list):
	river_card = rd.sample(deck, 1)
	deck = set(deck) - set(river_card)
	return(deck, river_card)


def player_game(spot, board_cards, cards_dealed):
	player_cards = [x[1] for x in cards_dealed if x[0] == spot]
	for cards in board_cards:
		player_cards.append(Cards(cards[0], cards[1]))
	return(player_cards)

## TO DO : change the table relation to a Round relation
def hand_winner(players_left, board_cards, cards_dealed, verbose = True):
	winner = -1
	winner_tie = []
	winner_hand = [0,[0, 0, 0, 0, 0]]
	for player in players_left:
		a = player_game(player, board_cards, cards_dealed)
		value = HandValue(a)
		print(player.pseudo + ' : ' + str(value.best_hand()))
		if verbose == True:
			value.best_hand(verbose = True)
		if value.best_hand()[0] > winner_hand[0]:
			winner = player
			winner_tie = []
			winner_hand = [value.best_hand()[0], value.best_hand()[1]]
		elif value.best_hand()[0] == winner_hand[0]:
			if value.best_hand()[1] == winner_hand[1]:
				winner_tie.append(player)
			for idx, top_card in enumerate(value.best_hand()[1]):
				if top_card > winner_hand[1][idx]:
					winner = player
					winner_tie = []
					winner_hand = [value.best_hand()[0], value.best_hand()[1]]
	winner_value = HandValue(player_game(winner, board_cards, cards_dealed))
	winner_tie.append(winner)
	winner_names = [x.pseudo for x in winner_tie]
	print("The player(s) %a win(s) the hand" %winner_names)
	winner_value.best_hand(verbose = True)
	return(winner_tie)


def ordered_players(table : Table):
	all_seats = sorted(list(table.spots_taken))
	seats_before_blinds = [x for x in all_seats if x < table.dealer]
	seats_blinds_and_after = [x for x in all_seats if x >= table.dealer]
	tmp = seats_blinds_and_after+seats_before_blinds
	return [table.spot_player[x] for x in tmp]

def get_recursive_player(table, ordered_players, additional_pos):
	len_seats = len(ordered_players)
	if additional_pos >= len_seats:
		while additional_pos >= len_seats:
			additional_pos += -len_seats
	return ordered_players[additional_pos]


def seats_list_to_names_list(l : list, table : Table):
	return([table.spot_name[i] for i in l])


#print(rd.sample(deck_creation(), 1))
	


