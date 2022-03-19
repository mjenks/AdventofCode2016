# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 10:56:33 2022

True for safe tiles False for traps

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for symb in puzzle_input:
        if symb == '.':
            data.append(True)
        if symb == '^':
            data.append(False)
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day18.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)