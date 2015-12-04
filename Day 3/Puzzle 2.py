#!/usr/bin/env python

"""
Solution to Day 3 - Puzzle 2 of the Advent Of Code 2015 series of challenges.

--- Day 3: I Was Told There Would Be No Math ---

<^v> determines what coordinate the pointer moves to. Count the amount of houses that the pointer visits at least once.
Input needs to be split into 2 parts, so that there is 2 pointers working on the problem.
-----------------------------

Author: Luke "rookuu" Roberts
"""

coordinate = [0,0]
visitedCoords = set()
visitedCoords.add((coordinate[0],coordinate[1]))
inputFile = open('input.txt')
dataFromFile = inputFile.read()
separatedLists = ["",""]

for index,value in enumerate(dataFromFile):
    if index % 2 == 0:
        separatedLists[0] += value
    else:
        separatedLists[1] += value

for lists in separatedLists:
    for characters in lists:
        if characters == "<":
            coordinate[0] += -1
        elif characters == ">":
            coordinate[0] += 1
        elif characters == "^":
            coordinate[1] += 1
        elif characters == "v":
            coordinate[1] += -1

        visitedCoords.add((coordinate[0],coordinate[1]))

    coordinate = [0,0]

print "Unique houses visited by both Santa and Robo-Santa: " + str(len(visitedCoords))

