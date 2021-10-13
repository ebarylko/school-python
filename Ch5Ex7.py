#Ch5 Ex7
#Eitan

import random

rand_list = [random.randint(1,10) for x in range(10)]

print(rand_list)

for x in rand_list:
    num = rand_list.count(x)
    if num > 1:
       rand_list.remove(x)
