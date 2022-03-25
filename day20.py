# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 10:34:19 2022

@author: mjenks

valid ips are from 0 to 4294967295 inclusive
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split('-')
        start = int(line[0])
        end = int(line[1])
        data.append((start,end))
    return data

def solve(puzzle_data):
    puzzle_data.sort(key=lambda y: y[0])
    allowed = []
    test = 0
    for start, end in puzzle_data:
        while test < start:
            allowed.append(test)
            test += 1
        if end > test:
            test = end + 1
    
    
    return allowed[0], 0

puzzle_path = "input_day20.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)