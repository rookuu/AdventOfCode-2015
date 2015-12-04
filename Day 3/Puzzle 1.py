#!/usr/bin/env python

"""
Solution to Day 3 - Puzzle 1 of the Advent Of Code 2015 series of challenges.

--- Day 3: I Was Told There Would Be No Math ---

<^v> determines what coordinate the pointer moves to. Count the amount of houses that the pointer visits at least once.
-----------------------------

Author: Luke "rookuu" Roberts
"""

coordinate = [0,0]
visitedCoords = set()
visitedCoords.add((coordinate[0],coordinate[1]))
inputFile = open('input.txt')
dataFromFile = inputFile.read()

for characters in dataFromFile:
    if characters == "<":
        coordinate[0] += -1
    elif characters == ">":
        coordinate[0] += 1
    elif characters == "^":
        coordinate[1] += 1
    elif characters == "v":
        coordinate[1] += -1

    visitedCoords.add((coordinate[0],coordinate[1]))

print "The number of unique houses visited is: " + str(len(visitedCoords))