# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 07:57:47 2023

@author: Nino
"""

from aoc import *
import numpy as np

def count_ways_to_win(t, record):
    hold = np.arange(t+1).astype(np.longlong)
    distance = ((t - hold) * hold).astype(np.longlong)
    return (distance > record).sum()


races = read_input('day06/input')


# =============================================================================
# PART 1
# =============================================================================
times = integers(races[0])
records = integers(races[1])
part1 = 1
for t, record in zip(times, records):
    print(t, record)
    ways_to_win = count_ways_to_win(t, record)
    part1 *= ways_to_win
print(part1)


# =============================================================================
# PART 2
# =============================================================================
t = res = int("".join(map(str, times)))
record = res = int("".join(map(str, records)))
part2 = count_ways_to_win(t, record)
print(part2)


