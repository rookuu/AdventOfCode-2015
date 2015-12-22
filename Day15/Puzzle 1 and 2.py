#!/usr/bin/env python

"""
Solution to Day 15 - Puzzle 1 and 2 of the Advent Of Code 2015 series of challenges.

--- Day 15: Science for Hungry People ---

Calculate the exact amount of ingredients to produce the perfect cookie.
-----------------------------------------

Author: Luke "rookuu" Roberts
"""

import itertools
import re

regex = re.compile("([a-zA-Z]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)")
Ingredients = []
bestCookie = 0
bestCookieWithCalories = 0


class Ingredient(object):
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)

with open('input.txt') as dataFile:
    for line in dataFile:
        data = regex.match(line.strip())
        Ingredients.append(Ingredient(*data.groups()))

print "This may take a while..."

for combination in itertools.combinations_with_replacement(Ingredients, 100):
    cookieProperties = [0, 0, 0, 0, 0]
    score = 0

    for ingredient in combination:
        cookieProperties[0] += ingredient.capacity
        cookieProperties[1] += ingredient.durability
        cookieProperties[2] += ingredient.flavor
        cookieProperties[3] += ingredient.texture
        cookieProperties[4] += ingredient.calories

    for i, cookieProperty in enumerate(cookieProperties):
        if cookieProperty < 0:
            cookieProperties[i] = 0

    score = cookieProperties[0] * cookieProperties[1] * cookieProperties[2] * cookieProperties[3]

    if score > bestCookie:
        bestCookie = score

    if score > bestCookieWithCalories and cookieProperties[4] == 500:
        bestCookieWithCalories = score

print "The highest scoring cookie has a score of: " + str(bestCookie)
print "The highest scoring cookie that has exactly 500 calories has a score of: " + str(bestCookieWithCalories)


