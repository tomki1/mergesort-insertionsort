# insertsort.py
# name: Kimberly Tom
# CS325 Homework 1
# insertSort with help from https://www.geeksforgeeks.org/insertion-sort/

#open a file for reading and open a file for writing
data_file = open("data.txt", "r")
insert_file = open("insert.txt", "w")

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


# for each line in the data file
# with help from https://stackoverflow.com/questions/3122121/python-how-to-read-and-split-a-line-to-several-integers
for line in data_file:
    one_line = list(map(int, line.split()))
    # read from the second integer to the end of the line
    array = one_line[1:]
    insertSort(array)
    # for each number character in the array, write to merge file
    for number in array:
        insert_file.write(str(number) + " ")
    # create a new line for next array
    insert_file.write("\n")

data_file.close()
insert_file.close()