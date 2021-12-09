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



# set up the window

		# if errors == 0:
		# 	pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
		# if errors == 1:
		# 	pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
		# 	pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
		# if errors == 2:
		# 	pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
		# 	pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
		# 	pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
		# if errors == 3:
		# 	pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
		# 	pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
		# 	pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 260), (495, 305), 5)
		# if errors == 4:
		# 	pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
		# 	pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
		# 	pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 260), (495, 305), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 260), (495, 350), 5)
		# if errors == 5:
		# 	pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
		# 	pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
		# 	pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 260), (495, 305), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 260), (495, 350), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 305), (435, 305), 5)
		# if errors == 6:
		# 	pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
		# 	pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
		# 	pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 260), (495, 305), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 260), (495, 350), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 305), (435, 305), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 305), (555, 305), 5)
		# if errors == 7:
		# 	pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
		# 	pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
		# 	pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 260), (495, 305), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 260), (495, 350), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 305), (435, 305), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 305), (555, 305), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 350), (435, 400), 5)
		# if errors == 8:
		# 	pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0), pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10), pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
		# 	pygame.draw.line(WIN, GREEN, (495, 95), (495, 200), 10)
		# 	pygame.draw.circle(WIN, WHITE, (495, 230), 30, 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 260), (495, 305), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 260), (495, 350), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 305), (435, 305), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 305), (555, 305), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 350), (435, 400), 5)
		# 	pygame.draw.line(WIN, WHITE, (495, 350), (555, 400), 5)

body_parts = [[pygame.draw.line, GREEN, (495, 95), (495, 200), 10],
              [pygame.draw.circle, WHITE, (495, 230), 30, 5],
              [pygame.draw.line, WHITE, (495, 260), (495, 305), 5],
              [pygame.draw.line, WHITE, (495, 260), (495, 350), 5],
              [pygame.draw.line, WHITE, (495, 305), (435, 305), 5],
              [pygame.draw.line, WHITE, (495, 305), (555, 305), 5],
              [pygame.draw.line, WHITE, (495, 350), (435, 400), 5],
              [pygame.draw.line, WHITE, (495, 350), (555, 400), 5]
]


# class Label:
#     def __init__(self, message, x, y, size, color = (0, 0, 0)):
# 		self.x = x
# 		self.y = y
# 		self.colour = color
# 		self.size = size
# 		self.message = message
# 		self.font = pygame.font.SysFont('arial', self.size)


# 	def draw(self):
# 		self.text = self.font.render(self.message, True, (0, 0, 0))
# 		WIN.blit(self.text, (self.x, self.y))


class Gallow:
    """represents the gallow in the game"""
#     body_parts = [[pygame.draw.line, GREEN, (495, 95), (495, 200), 10],
#                   [pygame.draw.circle, WIN, WHITE, (495, 230), 30, 5],
#                   [pygame.draw.line, WIN, WHITE, (495, 260), (495, 305), 5],
#                   [pygame.draw.line, WIN, WHITE, (495, 260), (495, 350), 5],
#                   [pygame.draw.line, WIN, WHITE, (495, 305), (435, 305), 5],
#                   [pygame.draw.line, WIN, WHITE, (495, 305), (555, 305), 5],

# [pygame.draw.line, WIN, WHITE, (495, 350), (555, 400), 5]
#     ]

    def __init__(self):
        #pre: (None)
        #post: draws the empty gallow
        pygame.draw.rect(WIN, WHITE, ((146, 500), (291, 106)), 0)
        pygame.draw.line(WIN, BLUE, (296, 553), (296, 100 ), 10)
        pygame.draw.line(WIN, RED, (292, 100), (500, 100), 10)
        self.error = 0

    def draw_body(self):
        #pre: (None)
        #post: draws body part of hangman
        fn, *args = body_parts[self.error]
        fn(WIN, *args)
        self.error += 1

    def hang(self):
        #pre: (None)
        #post: draws the full body
        for part in body_parts:
            fn, *args = part
            fn(WIN, *args)



# class Word:
	# """represents the word being drawn on the screen"""
	# def __init__(self, word, letters_guessed):
		# #pre: takes the word and letters guessed fpr
		# #post: draws the word with each char being an underscore
		# #or the letter if player has guessed the letter



class Guess:
    MATCH = 1
    LOST = 4
    GOOD_GUESS = 8
    BAD_GUESS = 5
    error = 0
    guessed_letters = ""

    """ Represents the guess in the game"""
    def __init__(self, secret_word):
        #pre: takes a guess
        #post: initializes the attributes
        self.secret_word = secret_word

    def add(self, user_input):
        print(user_input)
        if len(user_input) > 1:
            if user_input == self.secret_word:
                return self.MATCH
            else:
                return self.LOST

        if user_input not in self.secret_word:
            if self.error == 8:
                return self.LOST
            self.error += 1
            return self.BAD_GUESS

        self.guessed_letters += user_input

        if len(self.guessed_letters) == len(self.secret_word):
            return self.MATCH
        return self.GOOD_GUESS



gallow = Gallow()
gallow.draw_body()
user_input = ""
error = 0
guess = Guess(secret_word)

while error < 9:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
        if event.type == pygame.KEYDOWN:
            if event.unicode in alphabet:
                user_input +=  event.unicode

            if event.key == pygame.K_RETURN:
                #print(letter)

                result = guess.add(user_input)
                user_input = ""
                
                if result == guess.MATCH:
                    print("You have won")

                elif result == guess.GOOD_GUESS:
                    print("good job, Keep guessing")

                elif result == guess.BAD_GUESS:
                    gallow.draw_body()
                    print("sorry, Keep guessing")

                else:
                    print("You have lost")
                    gallow.hang()


    pygame.display.flip()

pygame.quit()
