#!/usr/bin/env python

"""
Solution to Day 11 - Puzzle 1 and 2 of the Advent Of Code 2015 series of challenges.

--- Day 11: Corporate Policy ---

Increment a string until it fits various conditions

-----------------------------------------

Author: Luke "rookuu" Roberts
"""

puzzleInput = "hxbxwxba"


def increment_string(string, index):
    if ord(string[index]) != 122:
        if index == -1:
            return string[:index] + chr(ord(string[index]) + 1)
        else:
            return string[:index] + chr(ord(string[index]) + 1) + string[index + 1:]
    else:
        if index == -1:
            return increment_string(string[:index] + 'a', index - 1)
        else:
            return increment_string(string[:index] + 'a' + string[index + 1:], index - 1)


def convert_string_to_ordlist(string):
    list = []
    for char in string:
        list.append(ord(char))

    return list


def is_increasing_straight(string):
    ordList = convert_string_to_ordlist(string)

    for i in xrange(0,len(ordList) - 2):
        if ordList[i] == ordList[i+1] - 1 and ordList[i] == ordList[i+2] - 2:
            return True
    return False


def not_contain_iol(string):
    for letter in string:
        if letter == 'i' or letter == 'o' or letter == 'l':
            return False
    return True

def has_two_doubles(string):
    pairsFound = 0
    i = 0

    while i < len(string) - 1:
        if string[i] == string[i+1]:
            pairsFound += 1
            i += 2
        else:
            i += 1

    if pairsFound >= 2:
        return True
    else:
        return False


def check_conditions(string):
    if is_increasing_straight(string) is True and not_contain_iol(string) is True and has_two_doubles(string) is True:
        return True
    else:
        return False


def main(string):
    while check_conditions(string) is False:
        string = increment_string(string, -1)

    return string

newPassword = main(puzzleInput)

print "The next password that's in accordance with the new conditions is " + newPassword
print "The password after that will be " + main(increment_string(newPassword, -1))