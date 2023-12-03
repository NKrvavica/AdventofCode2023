# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 09:52:04 2023

@author: Nino
"""

from aoc import *


def parse_numbers_and_positions(row, input_string):
    result = []
    current_number = None
    current_positions = []
    for i, char in enumerate(input_string):
        if char.isdigit():
            if current_number is None:
                current_number = int(char)
                current_positions = [i]
            else:
                current_number = current_number * 10 + int(char)
                current_positions.append(i)
        else:
            if current_number is not None:
                result.append((current_number, row, current_positions))
                current_number = None
            current_positions = []
    if current_number is not None:
        result.append((current_number, row, current_positions))
    return result


def parse_symbols_and_positions(row, input_string):
    result = set()
    gears = set()
    for i, char in enumerate(input_string):
        if not char.isdigit() and char != '.':
            result.add((row, i))
            if char == '*':
                gears.add((row, i))
    return result, gears


def generate_adjacent_coordinates(row, cols):
    adjecent_coord = set()
    for r in range(row - 1, row + 2):
        for c in range(min(cols) - 1, max(cols) + 2):
            adjecent_coord.add((r, c))
    return adjecent_coord


def collect_gears(numbers, gears):
    # coordinates of the gear symbol and adjecent numbers
    gear_dict = {}
    for number, row, cols in numbers:
        adjecent_coord = generate_adjacent_coordinates(row, cols)
        gear_coord = adjecent_coord & gears
        if len(gear_coord) > 0:
            coord = list(gear_coord)[0]
            if coord in gear_dict:
                gear_dict[coord].append(number)
            else:
                gear_dict[coord] = [number]
    return gear_dict




# =============================================================================
# PARSE NUMBERS AND SYMBOLS
# =============================================================================
engine = read_input('day03/input')
# search for numbers and symbols with their positions
numbers = []
symbols = set()
gears = set()
for row, line in enumerate(engine):
    # print(line)
    numbers += parse_numbers_and_positions(row, line)
    symb, gear = parse_symbols_and_positions(row, line)
    symbols.update(symb)
    gears.update(gear)


# =============================================================================
# PART 1
# =============================================================================
# find numbers that are adjecent to a symbol
part1 = 0
for number, row, cols in numbers:
    adjecent_coord = generate_adjacent_coordinates(row, cols)
    if len(adjecent_coord & symbols) > 0:
        part1 += number
print(part1)


# =============================================================================
# PART 2
# =============================================================================
# find all gears that have two numbers, multiply them and add to the sum
part2 = 0
gear_dict = collect_gears(numbers, gears)
for val in gear_dict.values():
    if len(val) == 2:
        part2 += val[0] * val[1]
print(part2)

