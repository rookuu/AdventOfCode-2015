#!/usr/bin/env python

"""
Solution to Day 12 - Puzzle 1 of the Advent Of Code 2015 series of challenges.

--- Day 12: JSAbacusFramework.io ---

Regular expressions to find all numbers in a file and sum them!
------------------------------------

Author: Luke "rookuu" Roberts
"""

import re

inputData = open("input.txt").read()

print "The sum of all numbers in the JSON object: " + str(sum(map(int, re.findall("-?\d+", inputData))))