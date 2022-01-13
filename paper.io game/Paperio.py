
#Paperio
#Eitan

import random, sys, math, pygame

WIN = pygame.display.set_mode((850, 850))
clock = pygame.time.Clock()

RIGHT = 1
LEFT = 2
UP = 4
DOWN = 8

# paper io basic concept:
"""
parts of game:

 need rectangle which can move across the screen,
  leaves a line wherever it goes
  if it collides with its own line the user dies
  """


class Player:
	"""
	represents the player on the screen
	"""
	
	def __init__(self):
	
		"""
		pre: (None)
		post: initializes the player attributes
		"""
	
		self.color = (255, 0, 0)
		self.border_color = (255, 255, 255)
		self.id = 1
		self.w = 10
		
		self.h = 10
		self.x = 85
		self.y = 85
		self.direction = "Right"
		self.safe = True
		self.next_pos = ()
		self.pointlist = [(self.x, self.y)]
		
	
	def draw(self):
	
		"""
		pre: (None)
		post: draws the player on the screen
		"""
		rect = pygame.Rect = (self. x -5, self.y - 5, self.w, self.h)
		pygame.draw.rect(WIN, self.color, rect, 0)
		pygame.draw.rect(WIN, self.border_color, rect, 2)
	
	def move(self):
		
		"""
		pre: (None)
		post: changes movement direction if player presses arrow key
		"""
		
		if (self.direction == "Right"):
			self.x += 10
			self.next_pos = (self.x , self.y)
			print("RIGHT")
		elif (self.direction == "Left"):
			self.x -= 10
			self.next_pos = (self.x, self.y)
			print("LEFT")
		elif (self.direction == "Up"):
			self.y -= 10
			self.next_pos = (self.x, self.y)
			print("UP")
		elif (self.direction == "Down"):
			self.y += 10
			self.next_pos = (self.x , self.y)
			print("Down")
		self.pointlist.append((self.next_pos))
	
	
	def crash(self):
		"""
		pre: (None)
		post: returns end if player crashes
		"""
		if self.next_pos in self.pointlist:
			print("End")
		else:
			self.pointlist.append(self.next_pos)	
	
	def line(self):
		"""
		pre: (None)
		post: draws the line from point 1 to point 2
		"""
		
		for point in range(len(self.pointlist) - 1):
					pygame.draw.line(WIN, self.color, self.pointlist[point], self.pointlist[point + 1], 1)
					

class GameScreen:
	"""
	represents the screen the player is on
	"""
	
	def __init__(self):
		"""
		pre: (None)
		post: initializes attributes of screen
		"""
		self.colums = 82
		self.rows = 82
		self.wall_color = (0, 0, 0)
		self.board = []
		text_file = open("gameboard.txt", "r+")
		for line in text_file.readlines():
			self.board.append(list(line))
			
	def draw(self):
		
		"""
		pre:(None)
		post: renders the screen
		"""
		
		for row in range(self.rows):
			for col in range(self.colums):
				color = self.wall_color
				
				if (self.board[row][col] == " "):
						color = (255, 255, 255)
				elif (self.board[row][col] == "1"):
						color = p1.color			
			
				pygame.draw.rect(WIN, color, (row * 10, col * 10, 10, 10), 0)
		
board = GameScreen()		
p1 = Player()

rungame = True

while rungame:
	
	WIN.fill((255, 255, 255))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			rungame = False
			
		if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					p1.direction = "Right"
				elif event.key == pygame.K_LEFT:
					p1.direction = "Left"
				elif event.key == pygame.K_DOWN:
					p1.direction = "Down"
				elif event.key == pygame.K_UP:
					p1.direction = "Up"
					
	
	board.draw()
	p1.move()				
	p1.draw()
	p1.line()
	p1.crash()				
					
	pygame.display.update()
	clock.tick(10)		
					
pygame.quit()


