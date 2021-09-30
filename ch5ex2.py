#ch5 ex2
#Eitan

def remove_letter(letter, s):
    #pre: takes a letter and a string
    #post: returns the string with all occurences of the letter removed
    return s.replace(letter, "")

def remove_letter2(letter, s):
    return "".join([w for w in s if w != letter])

def remove_letter3(letter, s):
    return "".join(filter(lambda x: x != letter, s))

def remove_letter4(letter, s):
    result = ""
    for l in s:
        if l != letter:
            result += l
    return result

