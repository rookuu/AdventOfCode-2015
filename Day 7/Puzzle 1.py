#!/usr/bin/env python

"""
Solution to Day X - Puzzle X of the Advent Of Code 2015 series of challenges.

--- Day 7: Some Assembly Required ---

We're given a list of instructions containing bitwise fucntions and a ton of inputs.
However the commands aren't in order and multiple itterations of the file must be made,
running only the commands that can be run with the inputs we already have.
-------------------------------------

Author: Luke "rookuu" Roberts
"""

inputFile = open('input.txt')
dataFromFile = inputFile.read().splitlines()
wires = []
temp = 0


def readFromWires(wirename):
    global temp

    for items in wires:
        if items[0] == wirename:
            temp = items
            return True

    wires.append([wirename,0])
    temp = [wirename,0]


def searchInWires(wirename):
    if isInt(wirename) is True:
        return int(wirename)
    else:
        for items in wires:
            if items[0] == wirename:
                return int(items[1])
    raise


def writeToWires():
    global temp

    for items in wires:
        if items[0] == temp[0]:
            items[1] = temp[1]


def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def itterateOverFile():
    for line in dataFromFile:
        splitLine = line.split(" ")

        try:
            if len(splitLine) == 3:
                readFromWires(splitLine[2])
                temp[1] = searchInWires(splitLine[0])
                writeToWires()
                dataFromFile.remove(line)

                print "Successfully applied assignment operation."
            elif len(splitLine) == 4:
                readFromWires(splitLine[3])
                temp[1] = 65536 + (~ searchInWires(splitLine[1]))
                writeToWires()
                dataFromFile.remove(line)

                print 'Successfully applied NOT operation.'
            elif len(splitLine) == 5:
                if splitLine[1] == "AND":
                    readFromWires(splitLine[4])
                    temp[1] = searchInWires(splitLine[0]) & searchInWires(splitLine[2])
                    writeToWires()
                    dataFromFile.remove(line)

                    print "Successfully applied AND operation."
                elif splitLine[1] == "OR":
                    readFromWires(splitLine[4])
                    temp[1] = searchInWires(splitLine[0]) | searchInWires(splitLine[2])
                    writeToWires()
                    dataFromFile.remove(line)
                elif splitLine[1] == "RSHIFT":
                    readFromWires(splitLine[4])
                    temp[1] = searchInWires(splitLine[0]) >> int(splitLine[2])
                    writeToWires()
                    dataFromFile.remove(line)

                    print "Successfully applied RSHIFT operation."
                elif splitLine[1] == "LSHIFT":
                    readFromWires(splitLine[4])
                    temp[1] = searchInWires(splitLine[0]) << int(splitLine[2])
                    writeToWires()
                    dataFromFile.remove(line)
                    print "Successfully applied LSHIFT operation."
        except:
            wires.pop()

    print wires
    print str(len(dataFromFile)) + " operations left."
    print "\n"

while len(dataFromFile) != 0:
        itterateOverFile()

print searchInWires("a")