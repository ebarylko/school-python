#ch1ex8
#Eitan

from functools import reduce

COINS = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

def coin_change(acc, coin):
    """Pre: takes a pair of cents and result and a coin to get change
    Post: returns a pair of the cents amount minus how many times the coin can fit and the result with how many times it can fit"""
    cents, result = acc
    q = cents // coin # how many times coin fits
    result[COINS[coin]] = q
    return cents - q * coin, result


def change_reduce(cents):
    _, result = reduce(
        coin_change,
        list(COINS),
        (cents, {})
    )
    return result

def change_iter(cents):
    result = {}
    for coin in list(COINS):
        fit = cents // coin
        cents -= fit * coin
        result[coin] = fit
    return result    



def change(cents):
    q = cents // 25
    cents -= 25 * q
    d = cents // 10
    cents -= 10 * d
    n = cents // 5
    cents -= 5 * n
    p = cents // 1
    return {"quarters": q, "dimes": d, "nickels": n, "pennies": p}

print(change(70))
