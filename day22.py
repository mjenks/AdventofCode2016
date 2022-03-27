# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:15:38 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input[2:]:
        line = line.strip().split()
        data.append(line) #listed in order id, size, used, avail, use%
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day22.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)