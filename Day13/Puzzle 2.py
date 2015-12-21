#!/usr/bin/env python

"""
Solution to Day 13 - Puzzle 2 of the Advent Of Code 2015 series of challenges.

--- Day 13: Knights of the Dinner Table ---

Similar to Day 9 with the same skills tested, we must calculate the optimal seating arrangements for a dinner party.
 -----------------------------------------

Author: Luke "rookuu" Roberts
"""

from pprint import pprint
from itertools import permutations
from collections import defaultdict

inputFile = open('input.txt')
dataFromFile = inputFile.read().splitlines()
condensedDataDict = defaultdict(dict)
guestList = set()
happinessList = []
numberOfGuests = 0
selfName = "Me"

for line in dataFromFile:
    name1,_,gainOrLoss,happinessChange,_,_,_,_,_,_,name2 = line.split(" ")
    if gainOrLoss == "gain":
        condensedDataDict[name1][name2[:-1]] = int(happinessChange)
    else:
        condensedDataDict[name1][name2[:-1]] = int(happinessChange) * -1

    guestList.add(name1)

for name in guestList:
    condensedDataDict[selfName][name] = 0
    condensedDataDict[name][selfName] = 0

guestList.add(selfName)
numberOfGuests = len(guestList)

for perm in permutations(guestList):
    happiness = 0

    for i, person in enumerate(perm):
        if i == 0:
            happiness += condensedDataDict[perm[i]][perm[i+1]]
            happiness += condensedDataDict[perm[i]][perm[numberOfGuests-1]]
        elif i == numberOfGuests -1:
            happiness += condensedDataDict[perm[i]][perm[0]]
            happiness += condensedDataDict[perm[i]][perm[i-1]]
        else:
            happiness += condensedDataDict[perm[i]][perm[i+1]]
            happiness += condensedDataDict[perm[i]][perm[i-1]]

    happinessList.append(happiness)

print "The optimal seating arrangement so that everyone is happy would have a happiness change of: " + str(max(happinessList))