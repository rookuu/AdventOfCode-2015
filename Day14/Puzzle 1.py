#!/usr/bin/env python

"""
Solution to Day X - Puzzle X of the Advent Of Code 2015 series of challenges.

--- Day X: Day X Title ---

Description of Puzzle
-----------------------------------------

Author: Luke "rookuu" Roberts
"""
from collections import defaultdict

reindeerInfo = defaultdict(dict)
time = 0
endTime = 2503

def collect_information():
    dataFile = open("input.txt").read().splitlines()

    for line in dataFile:
        name,_,_,speed,_,_,stamina,_,_,_,_,_,_,rest,_ = line.split(" ")
        reindeerInfo[name]["Speed"] = int(speed)
        reindeerInfo[name]["Stamina"] = int(stamina)
        reindeerInfo[name]["RestTime"] = int(rest)
        reindeerInfo[name]["Timer"] = 0
        reindeerInfo[name]["State"] = "Flying"
        reindeerInfo[name]["Distance"] = 0


def update_position(reindeer):
    if reindeerInfo[reindeer]["State"] == "Flying" and reindeerInfo[reindeer]["Timer"] != reindeerInfo[reindeer]["Stamina"]:
        reindeerInfo[reindeer]["Timer"] += 1
        reindeerInfo[reindeer]["Distance"] += reindeerInfo[reindeer]["Speed"]

    elif reindeerInfo[reindeer]["State"] == "Flying" and reindeerInfo[reindeer]["Timer"] == reindeerInfo[reindeer]["Stamina"]:
        reindeerInfo[reindeer]["Timer"] = 1
        reindeerInfo[reindeer]["State"] = "Resting"

    elif reindeerInfo[reindeer]["State"] == "Resting" and reindeerInfo[reindeer]["Timer"] != reindeerInfo[reindeer]["RestTime"]:
        reindeerInfo[reindeer]["Timer"] += 1

    elif reindeerInfo[reindeer]["State"] == "Resting" and reindeerInfo[reindeer]["Timer"] == reindeerInfo[reindeer]["RestTime"]:
        reindeerInfo[reindeer]["Timer"] = 1
        reindeerInfo[reindeer]["State"] = "Flying"
        reindeerInfo[reindeer]["Distance"] += reindeerInfo[reindeer]["Speed"]


collect_information()

while time != endTime:
    for reindeer in reindeerInfo:
        update_position(reindeer)
    time += 1

finalDistances = []

for reindeer in reindeerInfo:
    finalDistances.append(reindeerInfo[reindeer]["Distance"])

print "The maximum distance after " + str(endTime) + " seconds is: " + str(max(finalDistances))
print finalDistances
