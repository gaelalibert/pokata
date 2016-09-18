

class Cards(object):
	"""
	Creation of the cards
	"""
	def __init__(self, figure, color):
		if figure > 1 and figure < 15:
			self.figure = figure
		else:
			raise ValueError("Your card number should be between 2 and 14")
		if color > 0 and color < 5:
			self.color = color
		else: 
			raise ValueError("Your card color should be between 1 and 4")

	def show(self):
		switcher_figure = {
			14: "Ace",
			2: "2",
			3: "3",
			4: "4",
			5: "5",
			6: "6",
			7: "7",
			8: "8",
			9: "9",
			10: "10",
			11: "Jack",
			12: "Queen",
			13: "King"
		}
		switcher_color = {
			1: "Heart",
			2: "Diamond",
			3: "Clubs",
			4: "Spade"
		}
		return("%s of %s" % (switcher_figure.get(self.figure), switcher_color.get(self.color)))
