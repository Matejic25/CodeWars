# Where my anagrams at?
# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/python

# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters.
# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words.
# You should return an array of all the anagrams or an empty array if there are none.


# Sample input:
# 'abba', ['aabb', 'abcd', 'bbaa', 'dada']

# Sample output:
# ['aabb', 'bbaa']


def anagrams(word, words):
    return [sample for sample in words if
            {letter: word.count(letter) for letter in word} == {letter: sample.count(letter) for letter in sample}]


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
