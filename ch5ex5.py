#ch 5 ex 5
#Eitan

import random

def odd_even(num):
    #pre: takes a positive number
    #post: returns a string saying how many odd and even numbers were in a random collection of numbers of size num
    even = 0
    for number in range(num):
       if random.randrange(1, 100) % 2:
           even += 1
    return "in your list of {0} random numbers from 1 to 100 you had {1} odd numbers and {2} even numbers".format(num, num - even, even)
    

rand_list = [random.randrange(1, 100) for _ in range(20)]
even_list = list(filter(lambda x: x % 2 == 0, rand_list))
