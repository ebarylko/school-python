#txtbkch4ex2-5.py
#Eitan

#ex2

def day_name(num):
    #pre: takes a number
    #post: returns a string of the day that corresponds to that number, otherwise none
    return num_day.get(num)

num_day = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

#ex3

def day_num(day):
    #pre: takes a string of a day
    #post: returns the number corresponding to that day, otherwise none
    return week.get(day)

week = {
     "Sunday": 0,
     "Monday": 1,
     "Tuesday": 2,
     "Wednesday": 3,
     "Thursday": 4,
     "Friday": 5,
     "Saturday": 6
}
    
#ex4

def day_add(day, add_days):
    #pre: takes a name of a day and a number
    #post: returns the name of the day add_days later if day is valid, otherwise none.
    if not day_num(day):
        return
    new_day = (day_num(day) + add_days) % 7
    return day_name(new_day)

#ex5
#test to see if day_add works with negative numbers
