#Ch5 Ex11
#Eitan

#write a script that will report best and worst scores

student = {"name": "Sam Bouie", "Exercise 1.1": "88%", "Ecercise 2.3": "75%", "Exercise 3.7": "92%", "Exercise 4.6": "68%"}

grades = []

for k in student:
    if len(student[k]) == 3:
        grades.append(int(student[k][0:2]))

scores = "Best Score:{0}%, Worst score:{1}%".format(max(grades), min(grades))
