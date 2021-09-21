#ch1ex9.py
#EItan


def mins_to_hrs(mins):
    hrs = mins // 60
    ten_min = str((mins % 60) // 10)
    one_mins = str((mins % 10) // 1)
    ten_mins = ten_min + one_mins
    return  {hrs:ten_mins}
