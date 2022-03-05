# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 20:21:38 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split(',')
        first = line[0].split()
        floor = first[1]
        chips = []
        generators = []
        for item in line:
            item = item.split()
            if 'chip' in item[-1]:
                chips.append(item[-2][:-11])
            if 'generator' in item[-1]:
                generators.append(item[-2])
        data.append((floor, chips, generators))
        
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day11.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)