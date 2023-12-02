# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:12:37 2023

@author: Nino
"""

from aoc import *
import re


def find_all(seg, string):
    return [m.start() for m in re.finditer(string, seg)]


def extract_digits(input_string):
    return [c for c in input_string if c.isdigit()]


def extract_digits_and_strings(input_string):
    # Define a dictionary mapping number words to their numeric values
    wnumbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
                'eight', 'nine']
    numbers =  [str(x) for x in range(1,10)]
    number_mapping = {word : nr for word, nr in zip(wnumbers, numbers)}
    numbers += wnumbers

    # find all digits in int or str format and save its position in the string
    positions = []
    for number in numbers:
        position = find_all(input_string, number)
        positions += [(pos, number) for pos in position if pos >= 0]

    # Sort positions by the starting index
    sorted_numbers = sorted(positions, key=lambda x: x[0])

    # first digit
    _, first = sorted_numbers[0]
    if not first.isdigit():
        first = number_mapping.get(first)

    # last digit
    _, last = sorted_numbers[-1]
    if not last.isdigit():
        last = number_mapping.get(last)

    return first + last


code = read_input('day01/input')

part1, part2 = 0, 0

for line in code:

    ints = extract_digits(line)
    part1 += int(ints[0] + ints[-1])

    str_num = extract_digits_and_strings(line)
    part2 += int(str_num)

print(part1)
print(part2)

