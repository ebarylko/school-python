#txtbkch4ex7.py
#Eitan

def to_secs(hrs, mins, secs):
    #pre: takes three numbers which represents hours, minutes, and seconds
    #post: returns the total amount of seconds as an integer
    hr_sec = hrs * 3600
    min_sec = mins * 60
    total_sec = int(hr_sec + min_sec + secs)
    return total_sec
