# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 10:18:16 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day13.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)