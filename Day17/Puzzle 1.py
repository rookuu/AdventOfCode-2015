#!/usr/bin/env python

"""
Solution to Day 17 - Puzzle 1 of the Advent Of Code 2015 series of challenges.

--- Day 17: No Such Thing as Too Much ---

Find the number of ways that combinations of numbers from a list sum to 150.
-----------------------------------------

Author: Luke "rookuu" Roberts
"""

import itertools

containers = []
combinationsOfContainers = []

with open("input.txt") as dataFile:
    for line in dataFile:
        containers.append(int(line.strip()))

for x in range(1,len(containers)):
    for combination in itertools.combinations(containers, x):
        if sum(combination) == 150:
             combinationsOfContainers.append(combination)

print len(combinationsOfContainers)