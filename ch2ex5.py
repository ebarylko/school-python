#ch2ex5.py
#Eitan

def cost_of_pizza(size):
    ilabour_cost = 4.5
    irent_cost = 1
    imaterials_cost = 0.05 * size ** 2
    ifinal_cost = ilabour_cost + irent_cost + imaterials_cost
    return ifinal_cost

size = int(input("What size pizza do you want?: "))

print(cost_of_pizza(size))


def find_odd(nbrs):
    count = 0
    for n in nbrs:
        if n % 2 == 1:
            count += 1

    print(count > 0)


def find_filter(nbrs):
    found = filter(lambda x: x % 2 == 1, nbrs)
    return next(found, None) != None

def find_odd_iter(nbrs):
    found = False
    end = len(nbrs)
    i = 0
    # guard: i < end and nbrs[i] % 2 == 0
    while i < end and nbrs[i] % 2 == 0:
        i += 1

    while i < end :
        if nbrs[i] % 2 == 1:
            break
        i += 1

    return i < end

    # scenario 1: no odd numbers
    # i = end

    # scenario 2: it has one odd number at j
    # i = j and nbrs[j] % 2 == 1

    # at the end of the loop, not guard has to be True
    # not guard -> i >= end or nbrs[i] % 2 == 1
    # a and b -> not a or not b
    # a or b -> not a and not b
    # a implies b -> not a or b
