# Unique In Order
# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other and preserving the original order of elements.


# Sample input:
# ('AAAABBBCCDAABBB')

# Sample output
# ['A','B','C','D','A','B']


def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    else:
        niz = [iterable[0]]
        for i in range(len(iterable)):
            if iterable[i] != niz[-1]:
                niz.append(iterable[i])
        return niz

print(unique_in_order('AAAABBBCCDAABBB'))
