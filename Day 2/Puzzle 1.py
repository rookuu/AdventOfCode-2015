#!/usr/bin/env python

"""
Solution to Day 2 - Puzzle 1 of the Advent Of Code 2015 series of challenges.

--- Day 2: I Was Told There Would Be No Math ---

Take in a list of dimensions representing presents (boxes), calculates the total amount of wrapping paper needed,
plus a little extra determined by the smallest side of each box.
-----------------------------

Author: Luke "rookuu" Roberts
"""

inputFile = open('input.txt')
dataFromFile = inputFile.read().splitlines()
totalAmount = 0
totalAmount2 = 0

for elements in dataFromFile:
    dimensions = elements.split("x")
    l, w, h = int(dimensions[0]), int(dimensions[1]), int(dimensions[2])
    totalAmount += 2*l*w + 2*w*h + 2*h*l

    totalAmount += min(l*w, w*h, h*l)

print "The total amount of wrapping paper needed is " + str(totalAmount) + " feet."
