#!/usr/bin/env python

"""
Solution to Day 1 - Puzzle 1 of the Advent Of Code 2015 series of challenges.

--- Day 1: Not Quite Lisp ---

An opening parenthesis represents an increase in floor and a closing parenthesis represents a decrease in floor.
After taking a 7000 character long input string of assorted parenthesis, determine the resulting floor.

-----------------------------

Author: Luke "rookuu" Roberts
"""

inputData = raw_input("Puzzle Input: ")  # Copy and Paste in the input string, hint: use CTRL-A
floor = 0  # Holds the variable to decrement/increment depending on the flavor of parenthesis.

for char in inputData:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1

print "The floor Santa arrives at is... Floor " + str(floor)
