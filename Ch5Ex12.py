#Ch5 Ex12
#Eitan

student = {"name": "Sam Bouie", "Exercise 1.1": "88%", "Ecercise 2.3": "75%", "Exercise 3.7": "92%", "Exercise 4.6": "68%"}

def score_change(student, exercise, score):
    #pre:takes a dictionary of student's exercises and scores, an exercise to modify and the changed score
    #post: returns the dictionary modified with the new score for the exercise
    student[exercise] = score
