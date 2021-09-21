#Ch1ex5
#Eitan

import math

def circle_circumference(radius):
   return math.pi * radius ** 2 

print(circle_circumference(5)) 

def five_times_table(num):
    for x in range(num):
        print("five times", x, "is", 5 * x)
