# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:10:24 2023

@author: Nino
"""

import math
from aoc import *
from itertools import cycle
import re

pattern = r'\b\w+\b'

instructions, network = read_input('day08/input', sep='\n\n')
network = network.split('\n')

mapp = {}
for line in network:
    values = re.findall(pattern, line)
    mapp[values[0]] = (values[1:])


# =============================================================================
# PART 1
# =============================================================================
br = 0
start = 'AAA'
end = 'ZZZ'
for instruc in cycle(instructions):
    br += 1
    if instruc == 'L':
        next_el = mapp[start][0]
    else:
        next_el = mapp[start][1]
    if next_el == end:
        break
    else:
        start = next_el
print(br)



# =============================================================================
# PART 2
# =============================================================================
def lcm(numbers):
    res = numbers[0]
    for num in numbers[1:]:
        res = abs(res * num) // math.gcd(res, num)
    return res


starting = [node for node in mapp.keys() if node[-1] == 'A']
periods = []

for start in starting:
    br = 0
    for instruc in cycle(instructions):
        br += 1
        if instruc == 'L':
            next_el = mapp[start][0]
        else:
            next_el = mapp[start][1]
        if next_el[-1] == 'Z':
            break
        else:
            start = next_el
    periods.append(br)

print(lcm(periods))