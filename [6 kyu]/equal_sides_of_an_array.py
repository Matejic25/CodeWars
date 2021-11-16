# Equal Sides Of An Array
# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

# You are going to be given an array of integers.
# Your job is to take that array and find an index N,
# where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.
# If there is no index that would make this happen, return -1.

# Note:
# If you are given an array with multiple answers, return the lowest correct index.


# Sample input:
# [1, 100, 50, -51, 1, 1]

# Sample output
# 1


def find_even_index(arr):
    if len(arr) == 0:
        return 0
    else:
        list_of_correct = []
        for i in range(len(arr)):
            pointer = i
            half_1 = arr[:pointer]
            half_2 = arr[pointer + 1:]
            if sum(half_1) == sum(half_2):
                list_of_correct.append(pointer)
            else:
                pass
    if len(list_of_correct) > 0:
        return list_of_correct[0]
    return -1


print(find_even_index([1, 100, 50, -51, 1, 1]))
