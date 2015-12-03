#!/usr/bin/env python

"""
Solution to Day 1 - Puzzle 2 of the Advent Of Code 2015 series of challenges.

--- Day 1: Not Quite Lisp ---

An opening parenthesis represents an increase in floor and a closing parenthesis represents a decrease in floor.
After taking a 7000 character long input string of assorted parenthesis, determine the first time that Santa arrives
at a specified floor.

-----------------------------

Author: Luke "rookuu" Roberts
"""

inputData = raw_input("Puzzle Input: ")
floor = 0
index = 0
floorRequired = int(raw_input("What floor are we looking for? "))

# Used to check the length of the input string.
# print len(inputData)

for char in inputData:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1

    index += 1

    if floor == floorRequired:
        print "The first time Santa visits floor " + str(floorRequired) + " is on instruction number " + str(index)
        break

