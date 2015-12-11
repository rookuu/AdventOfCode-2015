#!/usr/bin/env python

"""
Solution to Day X - Puzzle X of the Advent Of Code 2015 series of challenges.

--- Day 8: Matchsticks ---

Find the difference between the total number of characters used to code the string and the actual string length.
Taking into account escape characters and hex ASCII notation.
---------------------------

Author: Luke "rookuu" Roberts
"""

inputFile = open('input.txt')
dataFromFile = inputFile.read().splitlines()
noOfCodeChars = 0
noOfStrChars = 0

for line in dataFromFile:
    noOfCodeChars += len(line)
    noOfStrChars += len(eval(line))

print noOfCodeChars - noOfStrChars