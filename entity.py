class Entity:
	
	#Represents a generic game entity
	
	def __init__(self, x, y, char, colour):
		self.x = x
		self.y = y
		self.char = char
		self.colour = colour
		
	def move(self, x, y):
		self.x += x
		self.y += y
		