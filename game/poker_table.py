
import random as rd

class Table(object):
	"""
	Creates the environment of the poker game
	Accept 0 to 10 players
	For now the spots around the table are randomly determined.
	"""
	def __init__(self, nb_players):
		if nb_players >= 0 and nb_players < 11:
			self.nb_players = nb_players
		else :
			raise ValueError("The number of players should be between 0 and 10")
		#Spots where the players are sitting over the 10 available spots	
		self.spots_taken = set(rd.sample(range(10), nb_players))
		self.free_spots = set(range(10)) - self.spots_taken
		print("Taken spots : ", self.spots_taken)
		print("Free spots : ", self.free_spots)

	def sit(self):
		""" 
		Adding a new player
		"""
		if self.nb_players < 10:
			## Increase the number of players
			self.nb_players += 1
			## Assign a spot to the new player
			spot = rd.sample(self.free_spots, 1)
			## Update the taken and free spots
			self.spots_taken.update(spot)
			self.free_spots = self.free_spots - set(spot)
			print("You can sit here. There are now %d players on this table." %self.nb_players)
		else: 
			print("This table is full, please come later")
		print("Taken spots : ", self.spots_taken)
		print("Free spots : ", self.free_spots)


	def leave(self, spot):
		"""
		Player leaving the table
		"""




