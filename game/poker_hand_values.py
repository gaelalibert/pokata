from .poker_cards import Cards
from collections import Counter

class HandValue(object):
	""" 
	Computation of the value of a player hand
	"""
	def __init__(self, game):
		if len(game) == 7:
			self.figures = [x.figure for x in game]
			self.colors = [x.color for x in game]
			self.game = game
		else:
			raise ValueError("The game of a player should be composed of 7 cards")

	def pair(self):
		s = set()
		# Find the duplicated figures
		duplicates = list(set(x for x in self.figures if x in s or s.add(x)))
		if len(duplicates) > 0:
			other_cards = sorted([x for x in self.figures if x != sorted(duplicates, reverse = True)[0]], reverse = True)
			return(True, [sorted(duplicates, reverse = True)[0], other_cards[0], other_cards[1], other_cards[2]])
		else:
			return(False, 0)

	def double_pair(self):
		s = set()
		duplicates = list(set(x for x in self.figures if x in s or s.add(x)))
		if len(duplicates) > 1:
			other_cards = sorted([x for x in self.figures if x not in sorted(duplicates, reverse = True)[0:2]], reverse = True)
			return(True, [sorted(duplicates, reverse = True)[0], sorted(duplicates, reverse = True)[1], other_cards[0]])
		else:
			return(False, 0)

	def set_(self):
		count = Counter(self.figures)
		max_repetition = sorted(count.values(), reverse = True)
		if max_repetition[0] == 3:
			keys = [x for x,y in count.items() if y == 3]
			other_cards = sorted([x for x,y in count.items() if x != max(keys)], reverse = True)
			return(True, [max(keys), other_cards[0], other_cards[1]])
		else:
			return(False, 0)

	def square(self):
		count = Counter(self.figures)
		max_repetition = sorted(count.values(), reverse = True)
		if max_repetition[0] == 4:
			other_cards = sorted([x for x,y in count.items() if count.values() != 4], reverse = True)
			return(True, [max(count, key=count.get), other_cards[0]])
		else:
			return(False, 0)

	def full(self):
		count = Counter(self.figures)
		max_repetition = sorted(count.values(), reverse = True)
		if max_repetition[0] == 3:
			if max_repetition[1] == 2:
				keys = [x for x,y in count.items() if y == 2]
				return(True, [max(count, key=count.get), max(keys)])
			if max_repetition[1] == 3:
				keys = sorted([x for x,y in count.items() if y == 3], reverse = True)
				return(True, [keys[0], keys[1]])
			else:
				return(False, 0)
		else:
			return(False, 0)

	def straight(self):
		all_straights = []
		for i in range(2,12):
			all_straights.append(set(range(i, i+5)))
		player_figures = set(self.figures)
		min_straight = set([2,3,4,5,14])
		a = False
		b = 0
		for i in all_straights:
			if i.issubset(player_figures):
				a = True
				b = max(i)
		# Specific case where the Ace is also the lowest card:		
		if a == False:
			if min_straight.issubset(player_figures) == True:
				return(True, 5)
			else: return(False, 0)
		else:
			return(a, b)

	def color(self):
		count = Counter(self.colors)
		max_repetition = sorted(count.values(), reverse = True)
		if max_repetition[0] >= 5:
			good_color = max(count, key=count.get)
			figures_good_color = [x.figure for x in self.game if x.color == good_color]
			return(True, sorted(figures_good_color, reverse = True))
		else:
			return(False, 0)

	def flush(self):
		all_straights = []
		for i in range(2,12):
			all_straights.append(set(range(i, i+5)))
		a = False
		b = 0
		for color in self.colors:
			same_color_figures = [x.figure for x in self.game if x.color == color]
			if len(same_color_figures) >= 5:
				min_straight = set([2,3,4,5,14])
				for i in all_straights:
					if i.issubset(same_color_figures):
						a = True
						b = max(i)
				if a == False:
					if min_straight.issubset(same_color_figures) == True:
						a = True
						b = 5
		return(a, b)

	def highest_cards(self):
		return(sorted(self.figures, reverse = True)[0:5])


	def best_hand(self, verbose = False):
		if self.flush()[0] == True:
			if verbose == True:
				print("You have a flush with high %d" %self.flush()[1])
			return(8, [self.flush()[1]])
		elif self.square()[0] == True:
			if verbose == True:
				print("You have a square of %d" %self.square()[1][0])
			return(7, self.square()[1])
		elif self.full()[0] == True:
			if verbose == True:
				print("You have a full of %d by the %d" %(self.full()[1][0], self.full()[1][1]))
			return(6, self.full()[1])
		elif self.color()[0] == True:
			if verbose == True:
				print("You have a color with high %d" %self.color()[1][0])
			return(5, self.color()[1][0:5])
		elif self.straight()[0] == True:
			if verbose == True:
				print("You have a straight with high %d" %self.straight()[1])
			return(4, [self.straight()[1]])
		elif self.set_()[0] ==True:
			if verbose == True:
				print("You have a set of %d" %self.set_()[1][0])
			return(3, self.set_()[1])
		elif self.double_pair()[0] == True:
			if verbose == True:
			 print("You have a double pair of %d and %d" %(self.double_pair()[1][0], self.double_pair()[1][1]))
			return(2, self.double_pair()[1])
		elif self.pair()[0] == True:
			if verbose == True:
				print("You have a pair of %d" %self.pair()[1][0])
			return(1, self.pair()[1])
		else:
			if verbose == True:
				print("You have an high %d" %self.highest_cards()[0])
			return(0, self.highest_cards())










			










