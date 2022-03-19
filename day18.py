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
    
def isSafe(left, center, right):
    trap = False
    if right and not center and not left:
        trap = True
    if left and not center and not right:
        trap = True
    if center and left and not right:
        trap = True
    if center and right and not left:
        trap = True       
    return not trap
    
def newRow(row):
    new = []
    new.append(isSafe(True, row[0], row[1]))
    for i in range(1,len(row)-1):
        new.append(isSafe(row[i-1], row[i], row[i+1]))
    new.append(isSafe(row[-2], row[-1], True))
    return new
    
def solve(puzzle_data):
    current = puzzle_data
    safe_tiles = sum(current)
    row = 1
    while row < 400000:
        current = newRow(current)
        safe_tiles += sum(current)
        row += 1
        if row == 40:
            part1 = safe_tiles
        
    return part1, safe_tiles

puzzle_path = "input_day18.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)