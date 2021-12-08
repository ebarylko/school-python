#Eitan

import pygame, sys, random
pygame.init()
from pygame.locals import *
"""
requirements: 
Randomly select a word from that text file that is greater than 3 letters in length. In order to get an A on this assignment, you will need to have difficulty settings such that if they choose “easy mode” they get a word that is 3-5 letters, and “hard mode” will be 6+ letters.

4. Display “_” such that there is one underscore plus a space for every letter in the word selected.

5. Allow the player to enter single letters in as guesses and then your program will check for occurrences of the letter guessed in the actual word. For every correct letter you must replace the “_ “with the correctly guessed letter.

6. Display a list of “letters already used”

7. Also allow the player to enter in a guess if they want to guess the word.

8. Every wrong letter guessed results in another body part being added to the gallows.

9. Every wrong word guessed automatically results in a “hanging”.

10. Do not use an infinite loop to control your game. Instead, use the number of erroneous guesses as your loop control. Once they hit 9 errors, the game end
"""

#make the screen, 
#intro page, actual part of the game, win-screen, lose-screen, replay option
#intro page: greet user, display rules for game, clear away once clicked
#dictionary_words = open("Dictionary.txt").read().strip(" ").split(" \n")
secret_word = "hello"
print(secret_word)
#surface details
WIN = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Hangman")
alphabet = "abcdefghijklmnopqrstuvwxyz"

from pygame.locals import *
#hangman stand details
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)

hangman_stand = [pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)]
error_1 = pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
error_2 = pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
error_3 = pygame.draw.line(WIN, WHITE, (495, 260), (495, 305), 5)
error_4 = pygame.draw.line(WIN, WHITE, (495, 260), (495, 350), 5)
error_5 = pygame.draw.line(WIN, WHITE, (495, 305), (435, 305), 5)
error_6 = pygame.draw.line(WIN, WHITE, (495, 305), (555, 305), 5)
error_7 = pygame.draw.line(WIN, WHITE, (495, 350), (435, 400), 5)
error_8 = pygame.draw.line(WIN, WHITE, (495, 350), (555, 400), 5)
   
hangman = [error_1, error_2, error_3, error_4, error_5, error_6, error_7, error_8]    



# set up the window



class Label:
	def __init__(self, message, x, y, size, color = (0, 0, 0)):
		self.x = x
		self.y = y
		self.colour = color
		self.size = size
		self.message = message
		self.font = pygame.font.SysFont('arial', self.size)
		

	def draw(self):
		self.text = self.font.render(self.message, True, (0, 0, 0))
		WIN.blit(self.text, (self.x, self.y))


# class Gallow:
	# def __init__(self, errors):
		

# class Word:
	# """represents the word being drawn on the screen"""
	# def __init__(self, word, letters_guessed):
		# #pre: takes the word and letters guessed fpr
		# #post: draws the word with each char being an underscore
		# #or the letter if player has guessed the letter
		



class Guess:
	""" represents the guess in the game"""
	def __init__(self, guess, secret_word):
		#pre: takes a guess 
		#post: initializes the attributes
		self.guess = guess
		self.secret_word = secret_word
    
	def is_guess_multi_char(self):   
		#pre: (None)
		#post: returns true if guess is longer than one letter, flase otherwise
		#return False	
		return len(self.guess) > 1 
		

	def letter_guess(self):
		#pre: takes the word to guess for
		#post: returns true if guess is in secret_word, false otherwise
		return self.guess in secret_word

	def word_guess(self):
		#pre: takes the word to guess for
		#post: returns true if guess is equal to word, false otherwise
		return self.guess == secret_word

class Gallow:
	"""represents the gallow in the game"""
	def __init__(self, errors = 0):
		#pre: takes number of errors
		#post: draws the gallow corresponding with the number of errors
		if errors == 0:
			pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
		if errors == 1:
			pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
			pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
		if errors == 2:
			pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
			pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
			pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
		if errors == 3:
			pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
			pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
			pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
			pygame.draw.line(WIN, WHITE, (495, 260), (495, 305), 5)
		if errors == 4:
			pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
			pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
			pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
			pygame.draw.line(WIN, WHITE, (495, 260), (495, 305), 5)
			pygame.draw.line(WIN, WHITE, (495, 260), (495, 350), 5)
		if errors == 5:
			pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
			pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
			pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
			pygame.draw.line(WIN, WHITE, (495, 260), (495, 305), 5)
			pygame.draw.line(WIN, WHITE, (495, 260), (495, 350), 5)
			pygame.draw.line(WIN, WHITE, (495, 305), (435, 305), 5)
		if errors == 6:
			pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
			pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
			pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
			pygame.draw.line(WIN, WHITE, (495, 260), (495, 305), 5)
			pygame.draw.line(WIN, WHITE, (495, 260), (495, 350), 5)
			pygame.draw.line(WIN, WHITE, (495, 305), (435, 305), 5)
			pygame.draw.line(WIN, WHITE, (495, 305), (555, 305), 5)
		if errors == 7:
			pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
			pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
			pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
			pygame.draw.line(WIN, WHITE, (495, 260), (495, 305), 5)
			pygame.draw.line(WIN, WHITE, (495, 260), (495, 350), 5)
			pygame.draw.line(WIN, WHITE, (495, 305), (435, 305), 5)
			pygame.draw.line(WIN, WHITE, (495, 305), (555, 305), 5)
			pygame.draw.line(WIN, WHITE, (495, 350), (435, 400), 5)
		if errors == 8:							
			pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
			pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
			pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
			pygame.draw.line(WIN, WHITE, (495, 260), (495, 305), 5)
			pygame.draw.line(WIN, WHITE, (495, 260), (495, 350), 5)
			pygame.draw.line(WIN, WHITE, (495, 305), (435, 305), 5)
			pygame.draw.line(WIN, WHITE, (495, 305), (555, 305), 5)
			pygame.draw.line(WIN, WHITE, (495, 350), (435, 400), 5)
			pygame.draw.line(WIN, WHITE, (495, 350), (555, 400), 5)
  
			
letter = ""
error = 0
while error < 9:
	pygame.time.delay(50)

	WIN.fill((125,125,125))
	gallow = Gallow(error)
	gallow
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:    
			if event.unicode in alphabet:
				letter +=  event.unicode
			if event.key == pygame.K_RETURN:
				#print(letter)
				guess = Guess(letter, secret_word)
				print(len(guess.guess))
				if guess.is_guess_multi_char():
				#else:
					#error += 1	
				# if guess.is_guess_multi_char:
					# print("WHY")
					# print(guess.guess)
					
					# if guess.word_guess:
						# print("you win")
					# else: 
						# print("you lose")
				# elif not guess.is_guess_multi_char:			
					# if guess.letter_guess:
						# print(guess.guess)
					# else: 
						# print("letter not in word")	
						# error += 1		
				letter = ""
                #print(guess.is_valid_guess())
	
											
	pygame.display.flip()
pygame.quit()
