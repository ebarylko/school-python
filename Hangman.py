#This Python file uses the following encoding: utf-8

#Eitan

import pygame, sys, random
from pygame.locals import *
pygame.init()
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
# dictionary_words = open("Dictionary.txt").read().strip(" ").split(" \n")

# easy_words = list(filter((lambda word: len(word) >= 9), dictionary_words))
# medium_words = list(filter((lambda word: len(word) >= 6 and len(word) <= 8), dictionary_words))
# hard_words = list(filter((lambda word: len(word) >= 3 and len(word) <= 5), dictionary_words))


# secret_word = random.choice(easy_words)
secret_word = "magnificent"
print(secret_word)
#surface details
WIN = pygame.display.set_mode((1200, 768))
pygame.display.set_caption("Hangman")
alphabet = "abcdefghijklmnopqrstuvwxyz"

from pygame.locals import *
#hangman stand details
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
POWDER_BLUE = pygame.Color("#9AD4D6")
OXFORD_BLUE = pygame.Color("#101935")
CYBER_GRAPE = pygame.Color("#564787")
LANGUID_LAVENDER = pygame.Color("#DBCBD8")
AZURE_WHITE = pygame.Color("#F2FDFF")
# set up the window

	

body_parts = [[pygame.draw.line, GREEN, (425, 95), (425, 200), 10],
              [pygame.draw.circle, WHITE, (425, 230), 30, 5],
              [pygame.draw.line, WHITE, (425, 260), (425, 305), 5],
              [pygame.draw.line, WHITE, (425, 260), (425, 350), 5],
              [pygame.draw.line,  WHITE, (425, 305), (365, 305), 5],
              [pygame.draw.line, WHITE, (425, 305), (485, 305), 5],
              [pygame.draw.line, WHITE, (425, 350), (365, 400), 5],
              [pygame.draw.line, WHITE, (425, 350), (485, 400), 5]]


#intro screen idea:
# welcome to colorful hangman
#explain rules: we're going to give you a word, and you have to guess it letter by letter or if you're confident, grab it in one go.
#you must choose the characters and then press enter for the guess to be registered
# for every letter error you make, a body part will be drawn. you will have a limit of eight errors, and when you reach nine you will lose
# furthermore, if you attempt to guess the word and it is wrong, you will also lose. good luck!
#start option below all that

FONT = pygame.font.SysFont('arial', 20)

class Screen:
    """represents the base screen"""
    def handle_event(event):
        """
        handles the event and returns the next screen if it changes
        pre: event
        post: returns the screen to handle the next event
        """
        return self


class IntroScreen(Screen):
    """Represents the screen to start the game"""

    rules =  """
    Welcome to colorful hangman
     we're going to give you a word, and you have to guess it letter by letter
     or if you're confident , grab it in one go 
     you must choose the characters and then press enter for the guess to be registered
     for every letter error you make, a body part will be drawn.
      you have a limit of eight errors, and the ninth will make you lose 
     furthermore, if you attempt to guess the word and it is wrong, you will also lose
     Good luck!"""



    def __init__(self):
        WIN.fill(POWDER_BLUE)
        x, y = 100, 100
        for line in self.rules.splitlines():
            text = FONT.render(line.strip(), True, OXFORD_BLUE)
            WIN.blit(text, (x, y))
            y += 50
        self.button = Button(100, y, "START")

    def handle_event(self, event):
       self.button.draw_button()
       return self


class Button:
    """represents the button used in game"""
    def __init__(self, x, y, text):
        #pre: takes the x and y coordinates, and text
        #post: creates the button at position with given text
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(None, 80)
        width, height = self.font.size(text)
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, width + 30, height + 30)
        self.draw_button()

    def draw_button(self):
        #pre: (None)
        #post: draws the button two different ways depending on cursor position
        bkg = CYBER_GRAPE
        pos = pygame.mouse.get_pos()
        self.hover = self.rect.collidepoint(pos)
        if self.hover:
            bkg = LANGUID_LAVENDER

        text = self.font.render(self.text , True, AZURE_WHITE, bkg)
        WIN.blit(text, self.rect)
            

    def is_clicked(self):
        #pre: (None)
        #post: returns true if the button is being clicked
        clicked = pygame.mouse.get_pressed()[0] == 1
        return clicked and self.hover

def letters_in_word(word, letters):
	check = []
	for char in word:
		check.append(char in letters)
	return all(check)


class Gallow:
    """represents the gallow in the game"""

    def __init__(self):
        #pre: (None)
        #post: draws the empty gallow
        pygame.draw.rect(WIN, WHITE, ((76, 500), (291, 106)), 0)
        pygame.draw.line(WIN, BLUE, (226, 553), (226, 100 ), 10)
        pygame.draw.line(WIN, RED, (222, 100), (430, 100), 10)
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

#make a text class?
# in text class i have word, letters used, and error, letters_picked
#initialilze it requires color, x, y, and size.


class Text:
	"""represents the text on the screen"""
	def __init__(self, x, y, size = 40, color = WHITE):
		#pre: takes x and y position, optional size and color
		#post: initializes attributes of the text
		self.x = x
		self.y = y
		self.color = color
		self.size = size
		self.font = pygame.font.SysFont(None, self.size)
		
	def draw_word(self, word):
		#pre: takes the word to guess for
		#post: draws the empty word on the screen
		self.word = word
		empty_word = "_ " * len(self.word)
		text = self.font.render(empty_word, True, self.color)

		WIN.blit(text, (self.x, self.y))
         
	def update_word(self, word, correct_letters):
		#pre: takes letters guessed and word
		#post: updates the word filling in the spots with correct letters
		new_word = ""
		for char in word:
			if char in correct_letters:
				new_word += char + " "
			else:
				new_word += "_ "
		#clear_text(self.x, self.y)
		self.text = self.font.render(new_word, True, self.color)
		WIN.blit(self.text, (self.x, self.y))
		
	def display_choice(self, choice):
		#pre: takes the characters chosen
		#post: draws the choice on the side of the screen
		self.text = self.font.render(choice, True, self.color)
		WIN.blit(self.text, (self.x, self.y))	
        
	def clear_text(self):
		#pre: (None)
		#post: clears the text at the given x and y position
		WIN.fill(BLACK, (self.x - 10, self.y, 730, 100))
		  
	def used_letters(self):
		#pre: (None)
		#post: draws the empty used letters on the screen	  
		self.text = self.font.render("Letters used: ", True, self.color)
		WIN.blit(self.text, (self.x, self.y))
        
	def update_letters(self, guessed_letters):
		#pre: takes guessed letters
		#post: updates the guessed letter list
		self.text = self.font.render(("Letters used: " + guessed_letters), True, self.color)
		WIN.blit(self.text, (self.x, self.y))
        
        
	def draw_error(self):
		#pre: (None)
		#post: draws error message on the screen    
		self.text = self.font.render(("You already used this letter, use another"), True, self.color)
		WIN.blit(self.text, (self.x, self.y))     
        
        
# class Word:
    # """represents the word being drawn on the screen"""
    # def __init__(self, word, x, y, size = 40,  color = WHITE):
        # #pre: takes the word to guess for, x and y coordinates, optional coordinates for size and color
        # #post: draws the empty word on the screen, initializes attributes of word
        # self.word = word
        # self.x = x
        # self.y = y
        # self.color = color
        # self.size = size
        # empty_word = "_ " * len(self.word)
        # self.font = pygame.font.SysFont('arial', self.size)
        # self.text = self.font.render(empty_word, True, self.color)
        # WIN.blit(self.text, (self.x, self.y))


    # def update_word(self, correct_letters):
        # #pre: takes letters guessed
        # #post: updates the word filling in the spots with correct letters
        # new_word = ""
        # for char in self.word:
            # if char in correct_letters:
                # new_word += char + " "
            # else:
                # new_word += "_ "
        # WIN.fill(BLACK, (420, 450, 730, 100))
        # self.text = self.font.render(new_word, True, self.color)
        # WIN.blit(self.text, (self.x, self.y))


# class Used_Letters:
    # """represents the used_letters drawn on the screen"""
    # def __init__(self, x, y, size = 40,  color = WHITE):
        # #pre: takes the x and y coordinate, size, and color
        # #post: draws the empty list of letters used
        # self.base = "Letters used: "
        # self.x = x
        # self.y = y
        # self.color = color
        # self.size = size
        # self.font = pygame.font.SysFont('arial', self.size)
        # self.text = self.font.render(self.base, True, self.color)
        # WIN.blit(self.text, (self.x, self.y))

    # def update_letters(self, used_letters):
        # #pre: takes letters guessed
        # #post: updates the list with guessed letters
        
        # WIN.fill(BLACK, (420, 500, 730, 50))
        # self.text = self.font.render((self.base + used_letters), True, self.color)
        # WIN.blit(self.text, (self.x, self.y))






class Guess:
	MATCH = 1
	LOST = 4
	GOOD_GUESS = 8
	BAD_GUESS = 5
	ERROR_LIMIT = 9
	DUPLICATE = 12
	
	error = 0
	guessed_letters = ""
	correct_letters = ""

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
		
		if user_input in self.guessed_letters:
			return self.DUPLICATE
			
		self.guessed_letters += user_input
		
		if user_input not in self.secret_word:
			self.error += 1
			if self.error == (self.ERROR_LIMIT - 1):
				return self.LOST
			return self.BAD_GUESS

		self.correct_letters += user_input


		if letters_in_word(self.secret_word, self.correct_letters):
			return self.MATCH
		#self.correct_letters += user_input
		#self.guessed_letters += user_input
		return self.GOOD_GUESS



WIN.fill(BLACK)
gallow = Gallow()
gallow.draw_body()

user_input = ""
error = 0
guess = Guess(secret_word)
#word = Word(secret_word, 420, 450)	
word = Text(420, 450)#.draw_word(secret_word)
word.draw_word(secret_word)
#used_list = Used_Letters(420, 550)
used_list = Text(420, 550)#.used_letters()
used_list.used_letters()
char_selection = Text(600, 200)

screen = IntroScreen()
while error < 9:
    pygame.time.delay(50)

    # start.draw_button()
    # if start.is_clicked():
    #     print("Hello")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen = screen.handle_event(event)    

        # if event.type == pygame.KEYDOWN:
        #     if event.unicode in alphabet:
        #         user_input += event.unicode
        #     if event.key == pygame.K_BACKSPACE:
        #         user_input = user_input[0:-1]
        #         char_selection.clear_text()		
        #         char_selection.display_choice(user_input)

        #     if event.key == pygame.K_RETURN:
        #         char_selection.clear_text()
        #         Text(310, 610).clear_text()
        #         result = guess.add(user_input)
        #         user_input = ""

        #         if result == guess.MATCH:
        #             word.clear_text()
        #             word.update_word(secret_word, secret_word)
        #             print("You have won")
                    
				
        #         elif result == guess.DUPLICATE:
        #             Text(300, 610).draw_error()
        #             print("You already used this letter, use another")
                 
				
        #         elif result == guess.GOOD_GUESS:
        #             word.clear_text()
        #             used_list.clear_text()
        #             word.update_word(secret_word, guess.correct_letters)
        #             used_list.update_letters(guess.guessed_letters)
        #             print("good job, Keep guessing")

        #         elif result == guess.BAD_GUESS:
        #             gallow.draw_body()
        #             used_list.clear_text()
        #             used_list.update_letters(guess.guessed_letters)
        #             print("sorry, Keep guessing")

        #         else:
        #             print("You have lost")
        #             gallow.hang()
                    


    pygame.display.flip()

pygame.quit()
