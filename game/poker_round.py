from .poker_table import Table
from .utils import *

class Round():
	"""
	"""
	def __init__(self, table):
		self.step = "pre-flop"
		self.table = table
		self.deck = deck_creation()
		self.board_cards = None
		self.cards_dealed = None
		self.pot = 0
		self.ordered_players = ordered_players(table)
		self.players_left = ordered_players(table)
		self.players_bets = {x: 0 for x in ordered_players(table)}
		self.players_allin = {x: False for x in ordered_players(table)}
		#self.bets =
		#self.cards = 

	def get_blinds(self):
		small_blind = get_recursive_player(self.table, self.ordered_players, 1)
		big_blind = get_recursive_player(self.table, self.ordered_players, 2)
		small_blind.chips += -(self.table.limit / 2)
		big_blind.chips += -(self.table.limit)
		self.pot += 1.5 * self.table.limit
		self.players_bets[small_blind] += self.table.limit / 2
		self.players_bets[big_blind] += self.table.limit

	def dealing_cards(self):
		# We deal 2 cards per players RANDOMLY
		self.deck, self.cards_dealed = dealing(self.table, self.deck)

	def preflop_bets(self, type='manual'):
		self.betting(type='manual')
		self.show_info()

	def play_flop(self):
		self.deck, flop_cards = dealing_flop(self.deck)
		self.step = "flop"
		print("The flop cards are the following : ")
		show_deck(flop_cards)
		self.board_cards = flop_cards

	def play_turn(self):
		self.deck, turn_card = dealing_turn(self.deck)
		self.step = "turn"
		print("The turn card is the following : ")
		show_deck(turn_card)
		self.board_cards += turn_card

	def play_river(self):
		self.deck, river_card = dealing_turn(self.deck)
		self.step = "river"
		print("The river card is the following : ")
		show_deck(river_card)
		self.board_cards += river_card

	def get_round_winner(self):
		hand_winner(self.table, self.board_cards, self.cards_dealed)

	def play_directly(self):
		self.dealing_cards()
		self.play_flop()
		self.play_turn()
		self.play_river()
		self.get_round_winner()

	def show_info(self):
		print('_____________________________________________________________________')
		print("Step : " + self.step)
		print("Players Left" + str([x.pseudo for x in self.players_left]))
		print("Players chips : " + str({x.pseudo: x.chips for x in self.players_left}))
		print("Board cards " + str(self.board_cards))
		print("Pot : " + str(self.pot))
		print("Players bets : " + str({key.pseudo: value for key, value in self.players_bets.items()}))
		print('_____________________________________________________________________')

	def player_bet(self, player, max_bet, cnt):
		self.show_info()
		good_entry = False
		while good_entry == False:
			print('++++++++ ' + player.pseudo + ' +++++++++++')
			action = input("What's your action ? FOLD or CHECK/CALL OR RAISE ?")
			if action == 'FOLD':
				good_entry = True
				self.players_left.remove(player)
			elif action in ('CHECK', 'CALL', 'CHECK/CALL'):
				## TODO call allin with less chips
				good_entry = True
				diff = max_bet - self.players_bets[player]
				self.pot += diff
				player.chips += -diff
				self.players_bets[player] = max_bet
			elif action == 'RAISE':
				if cnt == 3:
					print('You cannot raise anymore. Please call or fold.')
				else:
					try:
						raise_action = int(input("What's your raise ammount? (minimum double)"))
						if raise_action > player.chips:
							print("You don't have enough chips")
						else:
							if raise_action >= max(2 * max_bet, self.table.limit):
								good_entry = True
								diff = raise_action - self.players_bets[player]
								self.pot += diff
								player.chips += -diff
								self.players_bets[player] = raise_action
								max_bet = raise_action
							else:
								if raise_action == player.chips:
									good_entry = True
									diff = raise_action - self.players_bets[player]
									self.pot += diff
									player.chips += -diff #Should be equal to 0.
									self.players_bets[player] = raise_action
									self.players_allin[player] = True
									self.players_left.remove(player)
								else:
									print("You need to bet at least 2 times the initial stake.")
					except:
						print('Bad entry. Please enter an integer')
			else:
				print('Bad entry. Please choose between FOLD or CHECK/CALL or RAISE with capital letters.')
		return max_bet

	def betting(self, type='manual'):
		if self.step == "pre-flop":
			play_order = self.ordered_players
			if len(self.ordered_players) > 3:
				play_order = self.ordered_players[3:]+self.ordered_players[:3]
		else:
			play_order = self.ordered_players[1:]+self.ordered_players[0]
		print('icicicicicici')
		print([x.pseudo for x in play_order])

		max_bet = max(self.players_bets.values())
		if type == 'manual':
			betting_status = 'in progress'
			cnt = 1
			while betting_status == 'in progress':
				play_order = [x for x in play_order if x in self.players_left]
				for player in play_order:
					max_bet = max(self.players_bets.values())
					self.player_bet(player, max_bet, cnt)
					best_players_left = {key: value for key, value in self.players_bets.items() if key in self.players_left}
					if (len(set(best_players_left.values())) == 1) and (cnt > 1):
						betting_status = 'over'
						break
				if cnt == 3:
					betting_status = 'over'
				if len(set(best_players_left.values())) == 1:
					betting_status = 'over'
				cnt += 1







