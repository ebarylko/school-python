#ch5 ex1
#Eitan
from functools import reduce

def reverse(s):
    #pre:takes a string
    #post: returns the string backwards
    rng = range(len(s) - 1, -1, -1)
    return reduce(lambda acc, i: acc + s[i], rng, "")

def reverse1(s):
    result = ""
    rng = range(len(s) - 1, -1, -1)
    for i in rng:
        result += s[i]
    return result        

def reverse2(s):
    rng = range(len(s) - 1, -1, -1)
    return "".join([s[i] for i in rng])

