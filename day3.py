# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:28:10 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        sides = []
        for side in line.strip().split():
            sides.append(int(side))
        sides.sort()
        data.append(sides)
    
    return data
    
def solve(puzzle_data):
    
    return 0,0

puzzle_path = "input_day3.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)

solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)