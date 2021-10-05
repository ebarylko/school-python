#ch5 ex6
#Eitan

def frequencies(acc, x):
    #pre: takes a dictionary and a number from one to ten
    #post: returns the same dictionary with the count increased for x
   acc[x] = acc.get(x, 0) + 1
   return acc


rand_list = [random.randrange(1, 11) for _ in range(1000)]

a = reduce(frequencies, rand_list, {})
print("your list of 1000 random numbers had:")

for k in sorted(a):
    print("{0:<4}{1:>4}\n".format(k, a[k]))


