# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 08:24:20 2023

@author: Nino
"""

from aoc import *
import numpy as np


def matching_numbers(line):
    card, you = line.split(' | ')
    _, card_num = card.split(': ')
    card_num = set(integers(card_num))
    numbers = set(integers(you))
    winning = card_num.intersection(numbers)
    return len(winning)


cards = read_input('day04/input')

# =============================================================================
# PART 1
# =============================================================================
points = 0
for line in cards:
    n = matching_numbers(line)
    if n > 0:
        points += 2**(n-1)
print(points)


# =============================================================================
# PART 2
# =============================================================================
lines = len(cards)
copies = np.ones(lines, dtype=int)
for i, line in enumerate(cards):
    n = matching_numbers(line)
    copies[i+1: i+1+n] += copies[i]
print(copies.sum())
