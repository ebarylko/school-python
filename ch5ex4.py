#ch5 ex4
#Eitan
import re
import string

text = """Pythons are constrictors, which means that they will 'squeeze' the life out of their prey. They coil themselves around their prey and with each breath the creature takes the snake will squeeze a little tighter until they stop breathing completely. Once the heart stops the prey is swallowed whole. The entire animal is digested in the snake's stomach except for fur or feathers. What do you think happens to the fur, feathers, beaks, and eggshells? The 'extra stuff' gets passed out as --- you guessed it --- snake POOP!"""

def no_punct(char):
    return char not in string.punctuation

def word_count(word, paragraph):
    #pre: takes a word and a paragraph
    #post: returns the number of times the word appears in the paragraph(ignoring punctuation)
    list_words = re.split('\W+', paragraph.lower())
    return list_words.count(word)
