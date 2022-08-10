# Tribonacci Sequence
# https://www.codewars.com/kata/556deca17c58da83c00002db/python

# You need to create a fibonacci function that given a signature array/list,
# returns the first n elements - signature included of the so seeded sequence.
# Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0,
# then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)


# Sample input:
# ([3, 2, 1], 10)

# Sample output:
# [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]


def tribonacci(signature, n):
    if n <= len(signature):
        return signature[:n]
    else:
        while len(signature) < n:
            signature.append(
                signature[len(signature) - 1] + signature[len(signature) - 2] + signature[len(signature) - 3])
            return tribonacci(signature, n)
    return []


print(tribonacci([3, 2, 1], 10))
