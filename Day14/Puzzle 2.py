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
        reindeerInfo[name]["Points"] = 0


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


def calculate_points():
    maxDistance = 0
    distances = []
    leaders = []

    for deer in reindeerInfo:
        distances.append((deer,reindeerInfo[deer]["Distance"]))

        if reindeerInfo[deer]["Distance"] > maxDistance:
            maxDistance = reindeerInfo[deer]["Distance"]

    for deer in distances:
        if deer[1] == maxDistance:
            leaders.append(deer[0])

    return leaders

collect_information()

while time != endTime:
    for reindeer in reindeerInfo:
        update_position(reindeer)
    time += 1

    for reindeer in calculate_points():
        reindeerInfo[reindeer]["Points"] += 1

points = []

for reindeer in reindeerInfo:
    points.append(reindeerInfo[reindeer]["Points"])

print "The highest scoring reindeer has " + str(max(points)) + " points."



