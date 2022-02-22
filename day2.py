# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 20:57:25 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        data.append(list(line.strip()))

    return data

def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day2.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)