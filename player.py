class Player:
	"""Player Class"""

	def __init__(self, name, tile, score):
		"""initializes player class"""
		self.name = name
		self.tile = tile
		self.score = score

	def __str__(self):
		return f'{self.name}'
