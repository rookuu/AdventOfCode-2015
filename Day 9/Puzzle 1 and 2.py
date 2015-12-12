#!/usr/bin/env python

"""
Solution to Day X - Puzzle X of the Advent Of Code 2015 series of challenges.

--- Day X: Day X Title ---

Description of Puzzle
-----------------------------------------

Author: Luke "rookuu" Roberts
"""

from collections import defaultdict
from itertools import permutations

inputFile = open('input.txt')
dataFromFile = inputFile.read().splitlines()

places = set()
graph = defaultdict(dict)
distances = []

for line in dataFromFile:
    values = line.split(" ")

    places.add(values[0])
    places.add(values[2])

    graph[values[0]][values[2]] = int(values[4])
    graph[values[2]][values[0]] = int(values[4])

for perm in permutations(places):
    distance = 0
    for i, elem in enumerate(perm):
        if i != len(perm) - 1:
            distance += graph[perm[i]][perm[i+1]]
    distances.append(distance)

print "The minimum distance that Santa can take is: " + str(min(distances))
print "The maximum distance that Santa can take is: " + str(max(distances))