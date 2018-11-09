from entity import Entity
from random import randint

#Represents the apple to be eaten

class Apple:
	
	def __init__(self, char, colour, screen_width, screen_height):
		self.apple = Entity(0, 0, char, colour)
		self.width = screen_width
		self.height = screen_height
		self.move()
	
	#Move to a random location on the screen
	def move(self):
		self.apple.x = randint(0, self.width-1)
		self.apple.y = randint(0, self.height-1)
		