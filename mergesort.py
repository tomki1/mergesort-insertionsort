# mergesort.py
# name: Kimberly Tom
# CS325 Homework 1
# mergesort function with help from https://www.geeksforgeeks.org/merge-sort/

#open a file for reading and open a file for writing
data_file = open("data.txt", "r")
merge_file = open("merge.txt", "w")

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




# for each line in the data file
# with help from https://stackoverflow.com/questions/3122121/python-how-to-read-and-split-a-line-to-several-integers
for line in data_file:
    one_line = list(map(int, line.split()))
    # read from the second integer to the end of the line
    array = one_line[1:]
    mergeSort(array)
    # for each number character in the array, write to merge file
    for number in array:
        merge_file.write(str(number) + " ")
    # create a new line for next array
    merge_file.write("\n")

data_file.close()
merge_file.close()