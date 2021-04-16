# insertTime.py
# name: Kimberly Tom
# CS325 Homework 1
# insertSort with help from https://www.geeksforgeeks.org/insertion-sort/
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

def insertSort(integer_array):
    # for each number in the array
    for y in range(1, len(integer_array)):
        key = integer_array[y]

        # while the element is greater than the key, move one position forward
        x = y - 1
        while x >= 0 and key < integer_array[x]:
            integer_array[x + 1] = integer_array[x]
            x = x - 1
        integer_array[x + 1] = key


for number in arraySizes:
        array_rand = genRandNum(number)
        start_time = timeit.default_timer()
        insertSort(array_rand)
        print("array size: " + str(number) + ", running time: " + "%s seconds" % (timeit.default_timer() - start_time) + "\n")
