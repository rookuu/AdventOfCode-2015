#!/usr/bin/env python

"""
Solution to Day X - Puzzle X of the Advent Of Code 2015 series of challenges.

--- Day 8: Matchsticks ---

Find the difference between the total number of characters used to code the string and the actual string length.
Taking into account escape characters and hex ASCII notation.

--- Part 2 ---

Re-encode the strings using the same rules.
---------------------------

Author: Luke "rookuu" Roberts
"""

inputFile = open('input.txt')
dataFromFile = inputFile.read().splitlines()
noOfCodeChars = 0
noOfNewChars = 0

for line in dataFromFile:
    noOfCodeChars += len(line)
    noOfNewChars += len(line) + line.count("\"") + line.count("\\") + 2

print noOfNewChars - noOfCodeChars