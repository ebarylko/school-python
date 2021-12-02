#Hangman
#Eitan

import string, random, os, time, pygame, sys, math
from HMGraphics import *
#pygame, sys

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

"""
make a window
make event pump to keep screen up
prompt user to select a difficulty

"""


pygame.init()

#sets window

screen = pygame.display.set_mode((1024, 768))


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
		screen.blit(self.text, (self.x, self.y))



class Guess:
    """ represents the guess in the game"""
    def __init__(self, guess):
        #pre: takes a guess 
        #post: initializes the attributes
        self.guess = guess

    def is_letter_guess(self, secret_word):
        #pre: takes the word to guess for
        #post: returns true if guess is in secret_word, false otherwise
        return self.guess in secret_word

    def is_word_guess(self, secret_word):
        #pre: takes the word to guess for
        #post: returns true if guess is equal to word, false otherwise
        return self.guess == secret_word


letter = ""

while True:
    pygame.time.delay(50)
    
    screen.fill((125,125,125))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            letter +=  event.unicode
            if event.key == pygame.K_RETURN:
                guess = Guess(letter)
                print(guess.guess)

        guess = Guess().new_guess(event)        

    pygame.display.flip()
pygame.quit()
