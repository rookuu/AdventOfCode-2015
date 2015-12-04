#!/usr/bin/env python

"""
Solution to Day 4 - Puzzle 1 of the Advent Of Code 2015 series of challenges.

--- Day 4: The Ideal Stocking Stuffer ---

Solution must generate sequences of MD5 Hashes in Hex, using the conjugation of a secret key (given in the puzzle) and
a number. The goal is to find the lowest number than generates a hash with 5 leading zeros.
-----------------------------------------

Author: Luke "rookuu" Roberts
"""
import hashlib

secretKey = "ckczppom" # Puzzle Input!
number = -1

# I want this to potentially run infinitely until it finds the solution, however it would probably be more elegant to
# just define a max value, but for completeness let's do it this way.

while True:
    number += 1
    hashedCode = hashlib.md5(secretKey + str(number)).hexdigest()

    if hashedCode[0:5] == "00000":
        print "The lowest number that generates a hash with 5 leading 0s is " + str(number) + ", with the hash '" + \
              str(hashedCode) + "'"
        break










