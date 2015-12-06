#!/usr/bin/env python

"""
Solution to Day 6 - Puzzle 1 of the Advent Of Code 2015 series of challenges.

--- Day 6: Probably a Fire Hazard ---

Need to apply operations to a 1000x1000 grid of boolean switches.
-------------------------------------

Author: Luke "rookuu" Roberts
"""

grid = [[0 for x in range(1000)] for y in range(1000)]
inputFile = open('input.txt')
dataFromFile = inputFile.read().splitlines()
counter = 0

for lines in dataFromFile:
    string = lines.split(" ")
    fromCoord = string[1].split(",")
    toCoord = string[3].split(",")

    if string[0] == "on":
        for x in range(int(fromCoord[0]), int(toCoord[0])+1):
            for y in range(int(fromCoord[1]), int(toCoord[1])+1):
                grid[x][y] = 1
    elif string[0] == "off":
        for x in range(int(fromCoord[0]), int(toCoord[0])+1):
            for y in range(int(fromCoord[1]), int(toCoord[1])+1):
                grid[x][y] = 0
    elif string[0] == "toggle":
        for x in range(int(fromCoord[0]), int(toCoord[0])+1):
            for y in range(int(fromCoord[1]), int(toCoord[1])+1):
                if grid[x][y] == 0:
                    grid[x][y] = 1
                else:
                    grid[x][y] = 0

for x in range(0,1000):
    for y in range(0,1000):
        if grid[x][y] == 1:
            counter += 1

print "The number of christmas lights that are turned on: " + str(counter)
