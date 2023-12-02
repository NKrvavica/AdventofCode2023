# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 08:46:21 2023

@author: Nino
"""

from aoc import *
import numpy as np


games = read_input('day02/input')


# part 1
initial = {'red': 12, 'green': 13, 'blue': 14}
impossible = []
for line in games:
    game, data = line.split(': ')
    _, game_nr = game.split(' ')
    sets = data.split('; ')
    for sett in sets:
        cubes = sett.split(', ')
        drawn = {'red': 0, 'green': 0, 'blue': 0}
        for cube in cubes:
            nr, color = cube.split(' ')
            drawn[color] = int(nr)
        if (drawn['red'] > initial['red'] or
            drawn['green'] > initial['green'] or
            drawn['blue'] > initial['blue']):
            impossible.append(int(game_nr))
            break

n = int(game_nr)
total_sum = n * (n + 1) // 2

print(total_sum - np.array(impossible).sum())


# part 2
minimum = []
for line in games:
    initial = {'red': 0, 'green': 0, 'blue': 0}
    game, data = line.split(': ')
    _, game_nr = game.split(' ')
    sets = data.split('; ')
    for sett in sets:
        cubes = sett.split(', ')
        drawn = {'red': 0, 'green': 0, 'blue': 0}
        for cube in cubes:
            nr, color = cube.split(' ')
            drawn[color] = int(nr)
        if drawn['red'] > initial['red']:
            initial['red'] = drawn['red']
        if drawn['green'] > initial['green']:
            initial['green'] = drawn['green']
        if drawn['blue'] > initial['blue']:
            initial['blue'] = drawn['blue']
    minimum.append(initial['red'] * initial['green'] * initial['blue'])


print(np.array(minimum).sum())
