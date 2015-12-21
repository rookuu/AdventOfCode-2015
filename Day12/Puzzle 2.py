#!/usr/bin/env python

"""
Solution to Day 12 - Puzzle 2 of the Advent Of Code 2015 series of challenges.

--- Day 12: JSAbacusFramework.io ---

Same as before, however now we don't want to sum any dictionarys with red in the values.
-----------------------------------------

Author: Luke "rookuu" Roberts
"""
import json

data = json.loads(open('input.txt').read())


def sum_numbers_not_red(data):
    if type(data) == type(dict()):
        if "red" in data.values():
            return 0

        return sum(map(sum_numbers_not_red, data.values()))

    if type(data) == type(list()):
        return sum(map(sum_numbers_not_red, data))

    if type(data) == type(0):
        return data

    return 0

print sum_numbers_not_red(data)