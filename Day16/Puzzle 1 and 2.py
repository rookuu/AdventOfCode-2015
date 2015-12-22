#!/usr/bin/env python

"""
Solution to Day 16 - Puzzle 1 and 2 of the Advent Of Code 2015 series of challenges.

--- Day 16: Aunt Sue ---

Filter dictionary.
--------------------------------------

Author: Luke "rookuu" Roberts
"""

import re

regex = re.compile('([a-z]+): ([0-9]{1})')
knownData = { "children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3,
    "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3,
    "cars": 2, "perfumes": 1 }
sueNum = 1

with open("input.txt") as dataFile:
    for line in dataFile:
        data = re.findall(regex, line)
        sue = {x[0]: int(x[1]) for x in data}

        for key, value in sue.iteritems():
            if knownData[key] != value:
                break
        else:
            print "Puzzle 1: You should thank Sue #" + str(sueNum)

        for key, value in sue.iteritems():
            if key == "cats" or key == "trees":
                if not knownData[key] < value:
                    break
            elif key == "pomeranians" or key == "goldfish":
                if not knownData[key] > value:
                    break
            elif knownData[key] != value:
                break
        else:
            print "Puzzle 2: You should thank Sue #" + str(sueNum)

        sueNum += 1