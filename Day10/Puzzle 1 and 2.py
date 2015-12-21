#!/usr/bin/env python

"""
Solution to Day 10 - Puzzle 1 and 2 of the Advent Of Code 2015 series of challenges.

--- Day 10: Elves Look, Elves Say ---

Implement a look and say algorithm, then repeat it 40 times on a given string.

--- Part 2 ---

Repeat it 50 times.
-----------------------------------------

Author: Luke "rookuu" Roberts
"""
from itertools import groupby

inputString = "3113322113"
numberOfIterations = 40

def look_and_say(string):
    output = ''
    for k, g in groupby(string):
        output += str(len(list(g))) + k

    return output


def repeat_function(string, num):
    for i in range(num):
        string = look_and_say(string)
    return string

print "The number of digits after the " + str(numberOfIterations) + "th iteration is: " + str(len(repeat_function(inputString, numberOfIterations)))