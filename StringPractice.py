#String Practice
#EItan
#1
#sStringEntered = input("Please enter a string")

#print(len(sStringEntered))
#2
#print(sStringEntered.count("a", 3, 7))

#3
def password_check(password):
    return password == "k0Di@k$"
#4
def swap_characters(s):
    #pre: takes a string
    #post: returns the string with the last two characters in place of the first two and vice-versa if there are at least four characters, otherwise return the same string
    if len(s) < 4:
        return s
    first_2_char = s[0:2]
    last_2_char = s[(len(s) - 2):]
    new_string = s[2:(len(s) -2)]
    return last_2_char + new_string + first_2_char



string = "hello"
print(string[-1])
