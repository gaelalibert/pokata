from .poker_cards import Cards

class Players(object):
	"""
	Creates the environment for the poker players
	Keeps the chips amount
	Keeps the seat number
	"""
	def __init__(self, pseudo):
		self.pseudo = pseudo
		self.seat = -1
		self.chips = 0
		self.hand = (Cards(-1, -1), Cards(-1, -1))

	def show_info(self):
		print("pseudo : " + self.pseudo)
		print("seat number " + str(self.seat))
		print("Stack : " + str(self.chips))
		print("player cards : " + self.hand[0].show() + " & " + self.hand[1].show())