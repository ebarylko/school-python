#ch5 ex 3
#Eitan
import re

def remove_1(r, s):
    #pre: takes a substring and a string
    #post: returns the result of removing the first occurence of the substring from the string
    return s.replace(r, "", 1)

def remove_all(r, s):
    #pre: takes a substring and a string
    #post: returns the string with all occurences of the substring removed
    return s.replace(r, "")
    
