#Eitan
#Final exam prep
from functools import reduce
from math import sqrt, floor, ceil
from itertools import count, groupby
"""
question 3: allow the user to enter a number from 1000 to
9999, create an algorithm that isolates each digit 
"""

def digits(num):
    """
    pre: takes an integer from 1000 to 9999
    post: returns each digit from the number starting from the 1000s place
    """
    digits = []
    for place in [1000, 100, 10, 1]:
        digits.append("{0}: {1}".format(place, num // place))
        num = num % place
    return digits    

"""
problem 5: if you had a thousand doors from 2-2000, with intervals of 2 for every door number, and you only opened the doors divisible by three, how many would be open?
"""

def door_count():
    """
    pre: (None)
    post: returns the number of doors divisible by 3
    """
    doors = range(2, 2001, 2)
    open_doors = 0
    for door in doors:
        if door % 3 == 0:
            open_doors  += 1
    return open_doors        


"""
problem 3:  calculate how many 4 letter combinations you can make using a, b, c, d, e, and f
"""

def factorial(num):
    """
    pre: takes a number
    post: returns the factorial of the number
    """
    if num < 0:
        return "Use a positive number"
    if num == 0:
        return 1
    nums = range(num, 0, -1)
    return reduce(lambda x, y: x * y, nums)  

def combinations(num, quantity):
    """
    pre: takes a number of elements and the combination limit
    post: returns the number of possible combinations of quantity in the number of elements
    """
    if num <=  0:
        return "Use  a positive number"
    if  quantity > num:
        return "select a quantity less or equal to num"
    q,p,r =  [factorial(x) for x in [num, quantity, num - quantity]]
    return q// (p * r)

"""
problem 2: find the smallest number divisible by the numbers 1-20
"""



def is_prime(num):
    """
    pre: takes a number
    post: returns true if num is prime, false otherwise
    """
    return num == 1 or len(prime_factors(num)) == 1


def prime_factors(num):
    """
    pre: takes a number
    post: returns the prime factors of the number
    """
    factors = []
    while num != 1:
        factor = next(x for x in primes() if x <= num and num % x == 0)
        if factor:
            factors.append(factor)
            num //= factor
        else:
            num = 1

    return factors        


# lcm(12, 30)

# 12 => {3: 1, 2: 2} => (3, 1) (2, 2)
# 30 => {3: 1, 2: 1, 5: 1} (3, 1), (2, 1) (5, 1)

# group-by first, then sort by second decreasing

# 3: [(3, 1), (3, 1)]
# 2: [(2, 2) (2, 1)]
# 5: [(5, 1)]

# 3 * 1 * 2 * 2 * 5 * 1 = lcm

def frequencies(elements):
    """
    pre: takes a collection of elements
    post: returns the number of times the each specific element appears in the collection as a dictionary
    """
    result = {}
    for elem in elements:
        freq = result.get(elem, 0)
        result[elem] = freq + 1

    return result



def lcm(*nums):
    """
    pre: takes a list of nums
    post: returns the lowest common multiple of those numbers
    """
    factors = []
    for n in nums:
        factors += list(frequencies(prime_factors(n)).items())

    fst = lambda x: x[0]
    grouped = groupby(sorted(factors, key=fst), fst)

    snd = lambda x: x[1]
    total = 1
    for _, pairs in grouped:
        x, y = max(pairs, key=snd)
        total *= x ** y

    return total

def find_next_prime(primes_so_far):
    """
    pre: takes a list of primes in consecutive order
    post: returns the next prime after the last one in the list
    """
    last_prime = primes_so_far[-1]
    return next(x for x in count(last_prime + 2, 2 )
                if not any(x % y == 0 for y in primes_so_far))

def primes():
    """
    pre: (None)
    post: returns a lazy sequence of prime numbers
    """
    yield 2
    yield 3
    primes_so_far= [3]
    while True:
        next_prime =  find_next_prime(primes_so_far)
        yield next_prime
        primes_so_far.append(next_prime)
