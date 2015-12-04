#!/usr/bin/env python

"""
Solution to Day 3 - Puzzle 1 of the Advent Of Code 2015 series of challenges.

--- Day 3: I Was Told There Would Be No Math ---

<^v> determines what coordinate the pointer moves to. Count the amount of houses that the pointer visits at least once.
-----------------------------

Author: Luke "rookuu" Roberts
"""

housesVisited = 1
coordinate = [0,0]
listOfXCoords = [0]
listOfYCoords = [0]
listOfCoords = []
listOfUniqueCoords = []
counter = 1
isUnique = True

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

    listOfXCoords.append(coordinate[0])
    listOfYCoords.append(coordinate[1])

    listOfCoords.append([listOfXCoords[len(listOfXCoords)-1],listOfYCoords[len(listOfYCoords)-1]])

for items in listOfCoords:
    isUnique = True
    for items2 in listOfUniqueCoords:
        if items == items2:
            isUnique = False

    if isUnique is True:
        listOfUniqueCoords.append(items)

print len(listOfUniqueCoords)