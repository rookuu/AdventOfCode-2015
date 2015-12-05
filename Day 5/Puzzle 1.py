#!/usr/bin/env python

"""
Solution to Day 5 - Puzzle 1 of the Advent Of Code 2015 series of challenges.

--- Day 5: Doesn't He Have Intern-Elves For This? ---


Needs to apply sets of conditions to series of strings to determine whether they're valid or not.
-----------------------------------------------------

Author: Luke "rookuu" Roberts
"""

vowels = "aeiou"
badStrings = ["ab", "cd", "pq", "xy"]
noOfGoodStrings = 0
inputFile = open('input.txt')
dataFromFile = inputFile.read().splitlines()

def checkvowels (string):
    counter = 0

    for c in string:
        for vowel in vowels:
            if vowel == c:
                counter += 1

        if counter == 3:
            return True

    return False

def checkbadstrings (string):
    for badstring in badStrings:
        if string.find(badstring) != -1:
            return False

    return True

def checkdoubles (string):
    for i in range(0,len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def checkconditions (string):
    if checkvowels(string) and checkbadstrings(string) and checkdoubles(string):
        return True
    else:
        return False

for lines in dataFromFile:
    if checkconditions(lines):
        noOfGoodStrings += 1

print "The number of strings that are deemed 'nice' are " + str(noOfGoodStrings)
