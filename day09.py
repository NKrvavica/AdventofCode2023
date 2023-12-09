# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 08:11:54 2023

@author: Nino
"""

from aoc import *
import numpy as np


history = np.loadtxt('day09/input.txt', delimiter=' ')

# =============================================================================
# PART 1
# =============================================================================
part1 = 0
for line in history:
    diff = np.diff(line)
    last_num = [line[-1], diff[-1]]
    while (diff != 0).any():
        diff = np.diff(diff)
        last_num.append(diff[-1])
    part1 += sum(last_num)

print(part1)

# =============================================================================
# PART 2
# =============================================================================
part2 = 0
for line in history:
    diff = np.diff(line)
    last_num = [line[0], diff[0]]
    while (diff != 0).any():
        diff = np.diff(diff)
        last_num.append(diff[0])
    temp = 0
    for num in last_num[::-1][1:]:
        temp = num - temp
    part2 += temp
print(part2)
