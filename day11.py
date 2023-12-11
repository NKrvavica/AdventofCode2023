# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 08:56:13 2023

@author: Nino
"""

from aoc import *
import numpy as np
from itertools import combinations


def find_all(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


def find_distance(galaxy, N):
    res = 0
    for a, b in combinations(galaxy, 2):
        # print(a, b)
        man_dist = manhattan(a, b)
        add_rows = len(empty_rows[(empty_rows > min(a[0], b[0]))
                                  & (empty_rows < max(a[0], b[0]))])
        add_cols = len(empty_cols[(empty_cols > min(a[1], b[1]))
                                  & (empty_cols < max(a[1], b[1]))])
        res += man_dist + add_rows*(N-1) + add_cols*(N-1)
    return res


image = read_input('day11/input')

n, m = len(image), len(image[0])
array = np.zeros((n, m))

galaxy = []
for i, line in enumerate(image):
    idx = find_all(line, '#')
    for j in idx:
        array[i, j] = 1
        galaxy.append((i, j))

empty_cols = np.where((array==0).all(axis=0))[0]
empty_rows = np.where((array==0).all(axis=1))[0]

part1 = find_distance(galaxy, 2)
print(part1)
part2 = find_distance(galaxy, 1000000)
print(part2)
