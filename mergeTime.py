# mergeTime.py
# name: Kimberly Tom
# CS325 Homework 1
# mergesort function with help from https://www.geeksforgeeks.org/merge-sort/
# random integer generation with help from https://www.pythoncentral.io/how-to-generate-a-random-number-in-python/
# run time with help from https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
# and https://docs.python.org/2/library/timeit.html

import random
import timeit

arraySizes = {1000, 3000, 5000, 7000, 9000, 11000, 13000, 15000, 17000, 19000}

def genRandNum(n):
    array_nums = []
    for x in range(n):
        array_nums.append(random.randint(0,10001))
    return array_nums


def mergeSort(integer_array):
    if len(integer_array) > 1:
        # get middle index of the array
        middle = len(integer_array)//2
        # create array of the left side
        left_side = integer_array[:middle]
        # create array of the right side
        right_side = integer_array[middle:]

        mergeSort(left_side)
        mergeSort(right_side)

        a = b = c = 0

        while a < len(left_side) and b < len(right_side):
            if left_side[a] < right_side[b]:
                integer_array[c] = left_side[a]
                a = a + 1
            else:
                integer_array[c] = right_side[b]
                b = b + 1
            c = c + 1

        while a < len(left_side):
            integer_array[c] = left_side[a]
            a = a + 1
            c = c + 1

        while b < len(right_side):
            integer_array[c] = right_side[b]
            b = b + 1
            c = c + 1

for number in arraySizes:
        array_rand = genRandNum(number)
        start_time = timeit.default_timer()
        mergeSort(array_rand)
        print("array size: " + str(number) + ", running time: " + "%s seconds" % (timeit.default_timer() - start_time) + "\n")
