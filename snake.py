from entity import Entity
import libtcodpy as libtcod

#Represents the snake - dealing with movement, wraparound and collision
class Snake:
	
	def __init__(self, x, y, char, colour, dir, framerate, apple, screen_width, screen_height):
		self.char = char
		self.head_char = '@'
		self.tail_char = 'T'
		
		self.colour = colour
		self.dead_colour = libtcod.Color(50, 50, 50)
		self.dead_headcolour = libtcod.Color(150, 10, 10)
		
		self.dir = dir
		self.next_dir = dir
		self.interval = int(framerate/4.5)
		self.mininterval = 8
		self.timer = 0
		
		self.initialise_entities(x, y)
		self.alive = True
		self.apple = apple
		self.width = screen_width
		self.height = screen_height
	
	#Place the four entities representing the initial snake body
	def initialise_entities(self, x, y):
		self.entities = [Entity(x-3, y, self.char, self.colour), Entity(x-2, y, self.char, self.colour), Entity(x-1, y, self.char, self.colour), Entity(x, y, self.char, self.colour)]
	
	#Prepares the next direction to move in for the next movement update
	def set_next_dir(self, dir):
		self.next_dir = dir
		
	#Set the direction of movement for the snake, but don't allow a change to the opposite direction
	def set_dir(self, dir):
		if not(self.dir == 4 and dir == 2) and not(self.dir == 2 and dir == 4) and not(self.dir == 1 and dir == 3) and not(self.dir == 3 and dir == 1):
			self.dir = dir
	
	#Delay the automatic snake movement based on the current interval
	def update(self):
		self.timer += 1
		
		if self.timer == self.interval:
			self.timer = 0
			self.move()
	
	#"Move"" the snake in the current direction. Achieved by deleting the entity at the back of the snake and adding a new one in front.
	def move(self):
		self.set_dir(self.next_dir)
		self.entities.remove(self.entities[0])
		self.entities[0].char = self.tail_char
		self.entities[len(self.entities)-1].char = self.char
		
		if self.dir == 4:
			self.entities.append(Entity(self.entities[len(self.entities)-1].x, self.entities[len(self.entities)-1].y-1, self.head_char, self.colour))
		
		elif self.dir == 1:
			self.entities.append(Entity(self.entities[len(self.entities)-1].x+1, self.entities[len(self.entities)-1].y, self.head_char, self.colour))
			
		elif self.dir == 2:
			self.entities.append(Entity(self.entities[len(self.entities)-1].x, self.entities[len(self.entities)-1].y+1, self.head_char, self.colour))
			
		elif self.dir == 3:
			self.entities.append(Entity(self.entities[len(self.entities)-1].x-1, self.entities[len(self.entities)-1].y, self.head_char, self.colour))
		
		self.wraparound()
		self.check_overlap()
		self.check_apple()
	
	#Wraps the new snake head around the screen edges if necessary.
	def wraparound(self):
		if self.entities[len(self.entities)-1].x == self.width:
			self.entities[len(self.entities)-1].x = 0
			
		if self.entities[len(self.entities)-1].x == -1:
			self.entities[len(self.entities)-1].x = self.width - 1
			
		if self.entities[len(self.entities)-1].y == self.height:
			self.entities[len(self.entities)-1].y = 0
			
		if self.entities[len(self.entities)-1].y == -1:
			self.entities[len(self.entities)-1].y = self.height - 1
	
	#Checks if the snake is overlapping with itself and kills it if it is.
	def check_overlap(self):
		for e in self.entities:
			for e2 in self. entities:
				if e != e2 and (e.x == e2.x and e.y == e2.y):
					self.die()
					
	#Kills off the snake and updates the snake entities visually to show death
	def die(self):
		self.alive = False
		
		for e in self.entities:
			e.colour = self.dead_colour
		
		self.entities[len(self.entities)-1].colour = self.dead_headcolour
		
	#Checks if the snake head is overlapping with the apple and grows the snake, reduces movement interval, and moves the apple if it is.
	def check_apple(self):
		if self.entities[len(self.entities)-1].x == self.apple.apple.x and self.entities[len(self.entities)-1].y == self.apple.apple.y:
			self.entities.insert(0, Entity(self.entities[0].x, self.entities[0].y, self.char, self.colour))
			self.apple.move()
			
			if self.interval > self.mininterval:
				self.interval -= 1