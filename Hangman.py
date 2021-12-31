# This Python file uses the following encoding: utf-8

#Eitan

import functools
import random
import sys

import pygame

pygame.init()

# requirements:
# Randomly select a word from that text file that is greater than 3 letters in length.
# In order to get an A on this assignment, you will need to have difficulty settings such that if they
# choose “easy mode” they get a word that is 3-5 letters, and “hard mode” will be 6+ letters.
# 4. Display “_” such that there is one underscore plus a space for every letter in the word selected.
# 5. Allow the player to enter single letters in as guesses and then your program will check for occurrences of the letter guessed in the actual word. For every correct letter you must replace the “_ “with the correctly guessed letter.
# 6. Display a list of “letters already used”
# 7. Also allow the player to enter in a guess if they want to guess the word.
# 8. Every wrong letter guessed results in another body part being added to the gallows.
# 9. Every wrong word guessed automatically results in a “hanging”.
# 10. Do not use an infinite loop to control your game. Instead, use the number of
# erroneous guesses as your loop control. Once they hit 9 errors, the game end

#difficulty levels constants
EASY = 1
MEDIUM = 2
HARD = 4

# matching constants
NO_MATCH = 1
PARTIAL_MATCH = 2
FULL_MATCH = 8
LOST_MATCH = 16


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

FONT = pygame.font.SysFont(None, 30)

# surface details
WIN = pygame.display.set_mode((1200, 768))
pygame.display.set_caption("Hangman")
alphabet = "abcdefghijklmnopqrstuvwxyz"

body_parts = [[pygame.draw.line, GREEN, (425, 95), (425, 200), 10],
              [pygame.draw.circle, WHITE, (425, 230), 30, 5],
              [pygame.draw.line, WHITE, (425, 260), (425, 305), 5],
              [pygame.draw.line, WHITE, (425, 260), (425, 350), 5],
              [pygame.draw.line,  WHITE, (425, 305), (365, 305), 5],
              [pygame.draw.line, WHITE, (425, 305), (485, 305), 5],
              [pygame.draw.line, WHITE, (425, 350), (365, 400), 5],
              [pygame.draw.line, WHITE, (425, 350), (485, 400), 5]]


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
        


def draw_error(x = 310, y = 610  ):
    #pre: takes x and y coordinates
    #post: draws error message on the screen    
    text = FONT.render(("You already used this letter, please use another"), True, WHITE)
    WIN.blit(text , (x, y))     


def clear_error(x= 310, y = 610):
    """
    pre: takes x and y coordinates
    post: clears the error message from the screen
    """
    WIN.fill(BLACK, (x - 10, y - 10, 730, 100))


class Screen:
    """represents the base screen"""
    def handle_event(self, event):
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
        if self.button.is_clicked():
            return ConfigScreen()

        return self


class ConfigScreen(Screen):
    """represents the difficulty selection screen"""
    def __init__(self):
        WIN.fill(POWDER_BLUE)
        self.easy = Button(100, 100, "Easy", EASY)
        self.medium = Button(100, 200, "Medium", MEDIUM)
        self.hard = Button(100, 300, "Hard", HARD)


    def handle_event(self, event):
        """
        pre: takes an event
        post: selects the difficulty
        """
        buttons = [self.easy, self.medium, self.hard]
        for b in buttons:
            b.draw_button()


        selected  = [b.is_clicked() for b in buttons if b.is_clicked()]


        if selected:
            return GameScreen(selected[0])

        return self 


class GameScreen(Screen):
    """
    Represents the game
    """

    dictionary_words = open("Dictionary.txt").read().strip(" ").split(" \n")

    easy_words = list(filter((lambda word: len(word) >= 9), dictionary_words))
    medium_words = list(filter((lambda word: len(word) >= 6 and len(word) <= 8), dictionary_words))
    hard_words = list(filter((lambda word: len(word) >= 3 and len(word) <= 5), dictionary_words))

    difficulty_word = {EASY: random.choice(easy_words), MEDIUM: random.choice(medium_words), HARD: random.choice(hard_words)}

    def __init__(self, difficulty):
        """
        pre: Takes difficulty selected
        post: Initializes the game screen components: Gallow, UserInput, UsedLetters and WordGuess
        """
        WIN.fill(BLACK)
        self.error_count = 0
        self.gallow = Gallow()
        self.user_input = UserInput()
        
        #self.word_guess = Text(420, 450)
        self.used_list = UsedLetters()
        # self.used_list = Text(420, 550)
        # self.used_list.used_letters()
        self.secret_word = self.difficulty_word[difficulty]
        self.word_guess = Word(self.secret_word)
        print(self.secret_word)
    def handle_event(self, event):
        """
        pre: takes an event
        post: decide
        """
        guess = self.user_input.handle_event(event)

        if not guess:
            return self

        clear_error()

        match = guess.matches(self.secret_word)

        if match == LOST_MATCH:
            return LoseScreen(guess.guess, self.secret_word)

        if match == FULL_MATCH:
            return WinScreen(self.secret_word)

        if guess.guess in self.used_list.used_letters:
            print("Duplicate")
            draw_error()
            return self


        if match == PARTIAL_MATCH:
            self.word_guess.update_word(guess.guess)
            self.used_list.update_list(guess.guess)

            return self

        if self.error_count == 8:
            return LoseScreen(guess.guess, self.secret_word)


        self.used_list.update_list(guess.guess)

        self.error_count += 1

        return self


class UsedLetters:
    """represents the letters user has entered throughout game"""

    def __init__(self, x = 420, y = 550):
        self.used_letters = ""

        """
        pre: (none)
        post: draws the empty list of used letters
        self.used_list = Text(420, 550)
        """
        self.x = x
        self.y = y
        text = FONT.render("Letters used: ", True, WHITE)
        WIN.blit(text, (self.x, self.y))

    def update_list(self, letter):

        """
        pre:takes a letter
        post: redraws the used letter list with new character
        """
        self.used_letters += letter
        text = FONT.render(("Letters used: " + self.used_letters), True, WHITE)
        WIN.fill(BLACK, (self.x - 10, self.y, 730, 100))
        WIN.blit(text, (self.x, self.y))


class Word:
    """
    Represents the word guessed for in the game
    """
    font = pygame.font.SysFont("spacemono", 40)

    def __init__(self, word, x = 420, y = 450 ):
        """
        Pre: takes the secret_word
        Post: draws the empty word on the screen
        """
        self.x = x
        self.y = y
        self.secret_word = word

        self.freq = {}
        for (i, c) in enumerate(word):
            self.freq[c] = self.freq.get(c, []) + [i]

        self.width, self.height = self.font.size(self.secret_word * 2)

        self.guess = ['_' for c in word]
        self.draw(self.guess)


    def update_word(self, new_guess):
        """
        pre: takes the guess
        post: updates the empty word with the guess at the appropriate spot
        """
        c_guess = new_guess[0]
        pos = self.freq[c_guess]
        for i in pos:
            self.guess[i] = c_guess

        self.draw(self.guess)

    def draw(self, new_word):
        """
        Pre: takes the word to draw
        Post: renders the new word on the screen
        """
        print("The new word", new_word)
        pos = (self.x, self.y)
        WIN.fill(BLACK, pygame.Rect(self.x - 10, self.y - 10, self.width + 10, self.height + 10))
        with_spaces = "".join([c + ' ' for c in new_word])
        text = self.font.render(with_spaces, True, WHITE)
        WIN.blit(text, pos)


class UserInput:
    """represents the user input(letter, word) in the game"""
    user_input = ""
    char_selection = Text(600, 200)
    def handle_event(self, event):
        """
        pre: takes an event
        post: returns a letter guess, word guess, or nothing
        """
        if event.type != pygame.KEYDOWN:
            return

        if event.unicode in alphabet:
            self.user_input += event.unicode
            self.char_selection.display_choice(self.user_input)

        if event.key == pygame.K_BACKSPACE:
            self.user_input = self.user_input[0:-1]
            self.char_selection.clear_text()
            self.char_selection.display_choice(self.user_input)
            return

        if event.key == pygame.K_RETURN:
            self.char_selection.clear_text()
            result = WordGuess(self.user_input) if len(self.user_input) > 1 else LetterGuess(self.user_input)
            self.user_input = ""
            return result


class Button:
    """represents the button used in game"""
    def __init__(self, x_coord, y_coord, text, clicked = True):
        #pre: takes the x and y coordinates, and text
        #post: creates the button at position with given text
        self.x = x_coord
        self.y = y_coord
        self.font = pygame.font.SysFont(None, 80)
        width, height = self.font.size(text)
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, width + 30, height + 30)
        self.draw_button()
        self.clicked = clicked

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
        pressed = pygame.mouse.get_pressed()[0] == 1
        return pressed and self.hover and self.clicked

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



class LetterGuess:
    """
    represents a guess of one letter
    """
    def __init__(self, guess):
        """
        pre: takes a guess
        post: stores the guess
        """
        self.guess = guess
        
    def matches(self, secret_word):
        """
        pre: takes the secret_word
        post: returns PARTIAL_MATCH if guess in secret_word
        """
        if self.guess in secret_word:
            return PARTIAL_MATCH
        return NO_MATCH


class WordGuess:
    """
    represents a guess for an entire word
    """
    def __init__(self, guess):
        """
        pre: takes a guess
        post: stores the guess
        """
        self.guess = guess
        
    def matches(self, secret_word):
        """
        pre: takes the secret_word
        post: returns FULL_MATCH if guess is secret_word, LOST_MATCH otherwise
        """
        if self.guess == secret_word:
            return FULL_MATCH
        return LOST_MATCH


screen = IntroScreen()

while True:
    pygame.time.delay(50)

    # start.draw_button()
    # if start.is_clicked():
    #     print("Hello")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        screen = screen.handle_event(event)    

    pygame.display.flip()

pygame.quit()
