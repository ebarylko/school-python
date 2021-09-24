#txtbkch4ex1.py
#EItan

def turn_clockwise(direction):
    #pre:takes a string of the first character of a cardinal direction
    #post:returns the first character of the cardinal direction turning clockwise
    return directions.get(direction) 

directions = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N"
}

