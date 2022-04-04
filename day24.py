# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 11:04:13 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    points = []
    j = 0
    for line in puzzle_input:
        line = line.strip()
        row = [] #store 0 for open and 1 for wall
        i = 0
        for char in line:
            if char == '#':
                row.append(1)
            elif char == '.':
                row.append(0)
            elif char == '0':
                row.append(0)
                start = (i,j)
            else:
                row.append(0)
                points.append((i,j))
            i += 1
        data.append(row)
        j += 1            
        
    return start, points, data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day24.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)