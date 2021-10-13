#Ch5 Ex8

Scores = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]

print(Scores)

NewScore = int(input("Enter your new score: "))

LastScore = len(Scores) - 1

del Scores[LastScore]

Scores.append(NewScore)

Scores.sort(reverse = True)

print(Scores)
