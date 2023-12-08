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
    lcm_result = numbers[0]
    for num in numbers[1:]:
        lcm_result = abs(lcm_result * num) // math.gcd(lcm_result, num)
    return lcm_result


starting = []
for node in mapp.keys():
    if node[-1] == 'A':
        starting.append(node)


periods = [0] * len(starting)
for n, node in enumerate(starting):
    br = 0
    start = node
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
    periods[n] = br

print(lcm(periods))