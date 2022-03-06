# -*- coding: utf-8 -*-
"""
Created on Sun Mar 06 13:13:41 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        com = line[0]
        x = line[1]
        if len(line) > 2:
            y = line[2]
            inst = com, x, y
        else:
            inst = com, x
        data.append(inst)
   
    return data
    
def solve(puzzle_data):
    reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    return 0, 0
    
puzzle_path = "input_day12.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)