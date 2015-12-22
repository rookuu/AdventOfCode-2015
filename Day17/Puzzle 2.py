#!/usr/bin/env python

"""
Solution to Day 17 - Puzzle 2 of the Advent Of Code 2015 series of challenges.

--- Day 17: No Such Thing as Too Much ---

Find the minimum amount of numbers from a list that sum to 150; then return the amount of combinations.
-----------------------------------------

Author: Luke "rookuu" Roberts
"""

import itertools

containers = []
combinationsOfContainers = []
x = 0

with open("input.txt") as dataFile:
    for line in dataFile:
        containers.append(int(line.strip()))

while len(combinationsOfContainers) == 0:
    for combination in itertools.combinations(containers, x):
        if sum(combination) == 150:
            combinationsOfContainers.append(combination)
    x += 1

print len(combinationsOfContainers)