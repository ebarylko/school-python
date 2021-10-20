#Bubble Sort
#EItan
import random

import time



#def display_list():
#    rand_num = int(input("How many random numbers would you like: "))
#    rand_list = [random.randint(1,10000) for x in range(rand_num)]
#    start = time.time_ns()
#    sorted_list = bubble_sort(list(rand_list))
#    end = time.time_ns()
#    elapsed = ((end - start) / 1000000000)
#    print("How many random numbers would you like to sort? {0} \nUnsorted list: {1}\n Sorted list: {2}\n It took {3:.7f} seconds to do this".format(rand_num, rand_list, sorted_list, elapsed))
    
#def bubble_sort(nums):
#    length = len(nums) - 1
#    for j in range(length, -1, -1):
#        for i in range(j):
#            if nums[i] > nums[i + 1]:
#                nums[i], nums[i + 1] = nums[i + 1], nums[i]
#    return nums

rand_list = [random.randint(1, 10000) for x in range(5)]

#def find_largest_index(nums, j):
    # pre: a list of numbers in nums and j an number between 0 < j <= length(num)
    # post: an index largest where num[largest] >= num[n] where <= 0 n < j
#   largest = 0
#    for i in range(1, j):
#        # inv: num[largest] >= nums[n] for n where 0 <= n < i
#        if nums[i] > nums[largest]:
#            largest = i
#    return largest

#def insertion_sort(nums):
#    #pre: takes a random set of numbers from 1-10000
    #post: returns num sorted
#    length = len(nums)
#    for j in range(length, 0, -1):
        # inv: after j all the elements are sorted and all the elements are >= than the elements before j
#        largest = find_largest_index(nums, j)
#        nums[largest], nums[j-1] = nums[j-1], nums[largest]
#    return nums

#print(sorted(rand_list) == insertion_sort(rand_list))


def partition(nums, start, end):
    #pre: takes a random set of numbers from 1-10000
    #post: returns nums sorted
    #note: p is the last element in partition, numbers are checked up to p-1
    #invariant: everything to the left of the pivot is less than the pivot, and everything to the right of the pivot is greater than pivot.
    #invariant:everything to the left of i is smaller than i, numbers from i to j are greater than i
    #note:if j is less than p, inc i and swap nums[j] and nums[i]
    #note: if j = p, move p into nums[i + 1]
    #note: after moving p, quicksort the collection left of p, and right of p.
    pivot = end -1
    i = start - 1
    if end - start <= 1:
        return 
    for j in range(start, pivot):
        if nums[j] < nums[pivot]:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums.insert(i+ 1, nums[pivot])
    nums.pop()
    return i + 1 

def quick_sort(nums, start=0, end= None):
    #pre: takes a random set of numbers from 1-10000
    #post: returns set sorted
    end = end or  len(nums)
    p = partition(nums, start, end)
    quick_sort(nums, start, p)
    quick_sort(nums, p+1, end)

