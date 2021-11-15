# Find Outlier in Array
# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/python

# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers
# or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.


# Sample input:
# [2, 4, 0, 100, 4, 11, 2602, 36]

# Sample output:
# 11


def find_outlier(integers):
    even = None
    for i in range(2):
        for j in range(i+1, 3):
            if integers[i] % 2 == 0 and integers[j] % 2 == 0:
                even = True
            elif integers[i] % 2 != 0 and integers[j] % 2 != 0:
                even = False
    if even:
        for i in range(len(integers)):
            if integers[i] % 2 != 0:
                return integers[i]
    else:
        for i in range(len(integers)):
            if integers[i] % 2 == 0:
                return integers[i]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
