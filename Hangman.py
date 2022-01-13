# This Python file uses the following encoding: utf-8
# above comment is for mac

# Eitan
#python pygame version

import random
import sys
import pygame
pygame.init()

#difficulty levels constants

# matching constants
NO_MATCH = 1
PARTIAL_MATCH = 2
FULL_MATCH = 8
LOST_MATCH = 16


#sounds to use
bad_guess = pygame.mixer.Sound("sounds/klaxon.wav")
good_guess = pygame.mixer.Sound("sounds/gold.wav")
victory = pygame.mixer.Sound("sounds/Applause.mp3")
loss  = pygame.mixer.Sound("sounds/Boo.mp3")

#list of colors
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color("#EA5C1F")
BLUE = pygame.Color(0, 0, 255)
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
POWDER_BLUE = pygame.Color("#9AD4D6")
OXFORD_BLUE = pygame.Color("#101935")
CYBER_GRAPE = pygame.Color("#564787")
LANGUID_LAVENDER = pygame.Color("#DBCBD8")
AZURE_WHITE = pygame.Color("#F2FDFF")
RED_PIGMENT = pygame.Color("#FF002B")
RUSSIAN_GREEN = pygame.Color("#678D58")

#font specification
FONT_SIZE = 30

# surface details
WIN = pygame.display.set_mode((1200, 768))
pygame.display.set_caption("Colorful Hangman")


class Text:
    """represents the text on the screen"""

    last_message = ""

    def __init__(self, x, y, size = 40, color = WHITE, background = OXFORD_BLUE):
        """
        pre: takes x and y position, optional size and color
		post: initializes attributes of the text
        """
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.font = pygame.font.SysFont(None, self.size)
        self.background = background

    def render(self, message):
        """
        pre: takes a message
        post: displays the text on the screen and returns the y coordinate after the text
        """
        new_y = self.y
        for line in message.splitlines():
            text = self.font.render(line.strip(), True, self.color)
            WIN.blit(text, (self.x, new_y))
            new_y += 50

        self.last_message = message

        return new_y

    def clear_text(self):
        """
        Pre: (None)
        Post: Clears the text at the given x and y position
        """
        if self.last_message:
            width, height = self.font.size(self.last_message)
            WIN.fill(self.background, pygame.Rect(self.x, self.y, width, height))


class Button:
    """represents the button used in game"""
    def __init__(self, x_coord, y_coord, text, clicked = True):
        """
         pre: takes the x and y coordinates, text, optional  clicked value
        post: creates the button at position with given text
        """
        self.x = x_coord
        self.y = y_coord
        self.font = pygame.font.SysFont(None, 80)
        width, height = self.font.size(text)
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, width + 30, height + 30)
        self.draw_button()
        self.clicked = clicked

    def draw_button(self):
        """
         pre: (None)
        post: draws the button two different ways depending on cursor position
        """

        bkg = CYBER_GRAPE
        pos = pygame.mouse.get_pos()
        self.hover = self.rect.collidepoint(pos)
        if self.hover:
            bkg = LANGUID_LAVENDER

        text = self.font.render(self.text , True, AZURE_WHITE, bkg)
        WIN.blit(text, self.rect)


    def is_clicked(self):
        """
         pre: (None)
        post: returns true if the button is being clicked
        """

        pressed = pygame.mouse.get_pressed()[0] == 1
        return pressed and self.hover and self.clicked


class ButtonGroup:
    """
    Represents a collection of buttons to select an option
    """

    def __init__(self, x, y, **config):
        """
        pre: takes initial position for the first button, and the details for each button
        post: draws the  buttons one below the other
        """
        self.buttons = []

        for text, clicked in config.items():
            self.buttons.append(Button(x, y, text, clicked))
            y += 100


    def handle_event(self, _):
        """
        pre:takes an event
        post: returns the value of the button if clicked, or None
        """

        for b in self.buttons:
            b.draw_button()

        selected = [b.is_clicked() for b in self.buttons if b.is_clicked()]

        return selected and selected[0]

class Screen:
    """represents the base screen"""

    def __init__(self, background=POWDER_BLUE):
        """
        pre: takes a background color
        post:  fills the screen with the background color
        """
        pygame.mixer.stop()
        WIN.fill(background)

    def handle_event(self, event):
        """
        handles the event and returns the next screen if it changes
        pre: takes an event
        post: returns the screen to handle the next event
        """
        return self


class Difficulty:
    """
    represents the difficulty setting of the game
    """
    EASY = 1
    MEDIUM = 2
    HARD = 4

    dictionary_words = open("Dictionary.txt").read().strip(" ").split(" \n")

    difficulty_word = {
        EASY: range(9, 200),
        MEDIUM: range(6, 9),
        HARD: range(3, 6)
    }

    levels = {
        "Easy: 9+ letters": EASY,
        "Medium: 6-8 letters": MEDIUM,
        "Hard: 3-5 letters": HARD
    }

    def secret_word(self, level):
        """
        pre: takes a level
        post: returns the secret word for that level
        """
        rng = self.difficulty_word[level]
        choices = list(filter(lambda w: len(w) in rng, self.dictionary_words))
        return random.choice(choices)


class IntroScreen(Screen):
    """Represents the screen to start the game"""

    rules = """
        Welcome to colorful hangman
        we're going to give you a word, and you have to guess it letter by letter
        or if you're confident, grab it in one go
        you must choose the characters and then press enter for the guess to be registered
        if you press the delete button the last character entered will be removed
        for every letter error you make, a body part will be drawn.
        you have a limit of eight errors, and the ninth will make you lose
        furthermore, if you attempt to guess the word and it is wrong, you will also lose
        click the button to begin
        Good luck!
    """

    def __init__(self):
        """
        pre: (None)
        post: displays the intro screen
        """
        super().__init__()
        y = Text(100, 100, size=30, color=OXFORD_BLUE).render(self.rules)
        self.button = Button(100, y, "START")

    def handle_event(self, event):
        """
        pre: takes an event
        post: returns ConfigScreen if user wants to start playing,
        otherwise returns self
        """
        self.button.draw_button()
        if self.button.is_clicked():
            return ConfigScreen()

        return self


class ConfigScreen(Screen):
    """
    Represents the difficulty selection screen
    """
    difficulty = Difficulty()

    def __init__(self):
        """
        pre: (None)
        post: displays the ConfigScreen
        """
        super().__init__()
        Text(100, 70, color=OXFORD_BLUE).render("Select a difficulty please")
        self.btn_group = ButtonGroup(100, 100, **self.difficulty.levels)

    def handle_event(self, event):
        """
        Pre: Takes an event
        Post: Returns an instance of GameScreen if the user selects a difficulty,
        otherwise returns the same configuration screen
        """
        level = self.btn_group.handle_event(event)

        if level:
            return GameScreen(self.difficulty.secret_word(level))

        return self


class GameScreen(Screen):
    """
    Represents the game screen
    """

    def __init__(self, secret_word):
        """
        pre: Takes secret word
        post: Initializes the game screen components: Gallow, UserInput, UsedLetters and WordGuess
        """
        super().__init__(OXFORD_BLUE)

        self.error_count = 0
        self.gallow = Gallow()
        self.user_input = UserInput()
        self.used_list = UsedLetters()
        self.secret_word = secret_word
        self.word_guess = Word(self.secret_word)
        self.correct_letters  = ""
        self.error = Text(330, 620, color = RED)
        print(self.secret_word)

    def already_used_letter(self, letter):
        """
        Pre: Takes the letter that was already used
        Post: Renders the error message on the screen
        """
        self.error.render("You already used {0}, please use another letter".format(letter))


    def handle_event(self, event):
        """
        pre: takes an event
        post: returns the win screen if player won, lose screen if they lost, or the same game screen if they have not reached either point
        """
        guess = self.user_input.handle_event(event)

        if not guess:
            return self

        self.error.clear_text()

        match = guess.matches(self.secret_word, self.correct_letters)

        if match == LOST_MATCH:
            return LoseScreen(guess.guess, self.secret_word)

        if match == FULL_MATCH:
            return WinScreen(self.secret_word)

        if guess.guess in self.used_list.used_letters:
            self.already_used_letter(guess.guess)
            return self

        if match == PARTIAL_MATCH:
            pygame.mixer.stop()
            pygame.mixer.Sound.play(good_guess)
            self.correct_letters += guess.guess
            self.word_guess.update_word(guess.guess)
            self.used_list.update_list(guess.guess)
            return self

        if self.error_count == 8:
            return LoseScreen(guess.guess, self.secret_word)

        pygame.mixer.stop()
        pygame.mixer.Sound.play(bad_guess)
        self.used_list.update_list(guess.guess)
        self.error_count += 1
        self.gallow.draw_body()
        return self


class EndScreen(Screen):
    RESTART = 1
    QUIT = 2

    def __init__(self, background, message, sound=None):
        """
        pre: takes the background color and message
        post: displays the lose screen
        """
        super().__init__(background)
        if sound:
            pygame.mixer.Sound.play(sound)

        self.btn_group = ButtonGroup(
            100, 400,
            Restart=self.RESTART,
            Quit=self.QUIT
        )

        Text(100, 100, background=WHITE).render(message)


    def handle_event(self, event):
        """
        pre: takes an event
        post: returns user to difficulty screen if restart is clicked, returns none if quit is clicked, returns self otherwise
        """

        btn = self.btn_group.handle_event(event)


        if btn  == self.RESTART:
            return ConfigScreen()

        if btn == self.QUIT:
            return None

        return self


class LoseScreen(EndScreen):
    """
    represents the final screen if the player loses
    """

    wrong_word = """
        You Lose!
        You guessed  "{0}", but the secret word was "{1}"
        I hope you have better luck next time
        click the 'Restart' button if you want to play again, and 'Quit' to exit
    """

    too_many_errors = """
        You Lose!
        You haven't figured out the word so we will tell you,
            it was "{0}"
        I hope you have better luck next time
        click the 'Restart' button if you want to play again, and 'Quit' to exit
    """

    def __init__(self, guess, secret_word):
        """
        pre: takes the erroneous guess(letter/word) and the secret_word
        post: displays the lose screen
        """
        lose_message = self.too_many_errors.format(secret_word)

        if len(guess) > 1:
            lose_message = self.wrong_word.format(guess, secret_word)

        super().__init__(RED, lose_message, loss)




class WinScreen(EndScreen):
    """
    Represents the screen the player reaches when they win
    """

    win_text = """
        Congratulations!
        You correctly guessed the secret word "{0}"
        click the 'Restart' button if you want to play again, and 'Quit' to exit
    """

    def __init__(self, secret_word):
        """
        pre: takes the secret_word
        post: displays the win screen
        """
        win_message = self.win_text.format(secret_word)
        super().__init__(RUSSIAN_GREEN, win_message, victory)



class UsedLetters:
    """represents the letters user has entered throughout game"""

    def __init__(self, x = 420, y = 550):
        """
        pre: (none)
        post: draws the empty list of used letters
        """
        self.text = Text(x, y, size = 40, background = OXFORD_BLUE)
        self.used_letters = ""
        self.update_list("")


    def update_list(self, letter):
        """
        Pre: Takes a letter
        Post: Redraws the used letter list with new character
        """
        self.used_letters += letter
        self.text.render("Letters used: " + self.used_letters)


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
        pos = (self.x, self.y)
        WIN.fill(OXFORD_BLUE, pygame.Rect(self.x - 10, self.y - 10, self.width + 10, self.height + 10))
        with_spaces = "".join([c + ' ' for c in new_word])
        text = self.font.render(with_spaces, True, WHITE)
        WIN.blit(text, pos)


class UserInput:
    """represents the user input(letter, word) in the game"""
    user_input = ""
    char_selection = Text(600, 200)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def handle_event(self, event):
        """
        pre: takes an event
        post: returns a letter guess, word guess, or nothing
        """
        if event.type != pygame.KEYDOWN:
            return

        if event.unicode in self.alphabet:
            self.user_input += event.unicode
            self.char_selection.render(self.user_input)

        if event.key == pygame.K_BACKSPACE:
            self.user_input = self.user_input[0:-1]
            self.char_selection.clear_text()
            self.char_selection.render(self.user_input)
            return

        if event.key == pygame.K_RETURN:
            self.char_selection.clear_text()
            result = WordGuess(self.user_input) if len(self.user_input) > 1 else LetterGuess(self.user_input)
            self.user_input = ""
            return result


class Gallow:
    """represents the gallow in the game"""

    #body parts for hangman
    body_parts = [[pygame.draw.line, GREEN, (425, 95), (425, 200), 10],
                [pygame.draw.circle, WHITE, (425, 230), 30, 5],
                [pygame.draw.line, WHITE, (425, 260), (425, 305), 5],
                [pygame.draw.line, WHITE, (425, 260), (425, 350), 5],
                [pygame.draw.line,  WHITE, (425, 305), (365, 305), 5],
                [pygame.draw.line, WHITE, (425, 305), (485, 305), 5],
                [pygame.draw.line, WHITE, (425, 350), (365, 400), 5],
                [pygame.draw.line, WHITE, (425, 350), (485, 400), 5]]



    def __init__(self):
        """
        pre: (None)
        post: draws the empty gallow
        """
        pygame.draw.rect(WIN, WHITE, ((76, 500), (291, 106)), 0)
        pygame.draw.line(WIN, BLUE, (226, 553), (226, 100 ), 10)
        pygame.draw.line(WIN, RED, (222, 100), (430, 100), 10)
        self.error = 0

    def draw_body(self):
        """
        pre: (None)
        post: draws body part of hangman
        """
    
        fn, *args = self.body_parts[self.error]
        fn(WIN, *args)
        self.error += 1

    def hang(self):
        """
        pre: (None)
        post: draws the full body
        """
        for part in self.body_parts:
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
        
    def matches(self, secret_word, letters):
        """
        pre: takes the secret_word and the correct letters guessed so far
        post: returns PARTIAL_MATCH if guess in secret_word, FULL_MATCH if all the letters  were guessed
        """
        if self.guess not in secret_word:
            return NO_MATCH

        if set(letters + self.guess) == set(secret_word):
            return FULL_MATCH
        
        return PARTIAL_MATCH

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
        
    def matches(self, secret_word, _):
        """
        pre: takes the secret_word
        post: returns FULL_MATCH if guess is secret_word, LOST_MATCH otherwise
        """
        if self.guess == secret_word:
            return FULL_MATCH
        return LOST_MATCH


def event_loop(scr):
    """
    Pre: receives a screen to forward events
    Post: returns the screen after handing the events
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        scr = screen.handle_event(event)

    pygame.display.flip()

    return scr

screen = IntroScreen()

while screen:
    pygame.time.delay(50)

    # While the user is playing
    while not isinstance(screen, EndScreen):
        screen = event_loop(screen)

    # While the user is choosing to quit or retry
    while screen and isinstance(screen, EndScreen):
        screen = event_loop(screen)

pygame.quit()
