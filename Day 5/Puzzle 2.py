#!/usr/bin/env python

"""
Solution to Day 5 - Puzzle 2 of the Advent Of Code 2015 series of challenges.

--- Day 5: Doesn't He Have Intern-Elves For This? ---


Needs to apply sets of conditions to series of strings to determine whether they're valid or not.
-----------------------------------------------------

Author: Luke "rookuu" Roberts
"""

noOfGoodStrings = 0
inputFile = open('input.txt')
dataFromFile = inputFile.read().splitlines()

def checkdoubles(string):
    doubles = []

    for i in range(0,len(string)-1):
        doubles.append([string[i],string[i+1]])

    for double in doubles:
        if string.count(double[0]+double[1]) > 1:
            return True

    return False

def checkpattern(string):
    for i in range(0,len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

def checkconditions(string):
    if checkdoubles(string) and checkpattern(string):
        return True
    else:
        return False

for lines in dataFromFile:
    if checkconditions(lines):
       noOfGoodStrings += 1

print "The number of strings that are deemed 'nice' are " + str(noOfGoodStrings)
