#txtbkch4ex9.py
#Eitan

def hours_in(secs):
    #pre:takes a number of seconds
    #post: returns the integer number of hours
    return secs // 3600

def mins_in(secs):
    #pre: takes a number of seconds
    #post: returns the integer number of minutes left after calculating the number of hours for secs
    mins_sec = secs % 3600
    return mins_sec // 60

def secs_in(secs):
    #pre: takes a positive number of seconds
    #post:returns the remaining seconds left after calculating the whole hour and minutes from secs
    assert secs >= 0 , "Wrong Input"
    return secs % 60
#figure out how to work with negative integers
