#txtbkch3ex6.py
#Eitan

def grade(mark):
    ranks = [(75, 100, "First"),
             (70, 75, "Upper Second"),
             (60, 70, "Second"),
             (50, 60, "Third"),
             (45, 50, "F1 supp"),
             (40, 45, "F2")]

    found = [s for a, b, s in ranks if mark in range(a, b)]

    return mark, found[0] if found else "F3"

numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]

def grades():
    return [grade(x) for x in numbers]
