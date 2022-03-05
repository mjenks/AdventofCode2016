# -*- coding: utf-8 -*-
"""
Created on Fri Mar 04 20:21:38 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split(',')
        floor = {}
        floor["chip"] = []
        floor["RTG"] = []
        for item in line:
            item = item.split()
            if 'chip' in item[-1]:
                floor["chip"].append(item[-2][:-11])
            if 'generator' in item[-1]:
                floor["RTG"].append(item[-2])
        data.append(floor)
        
    return data
    
def check(floor):
    fried = False
    if len(floor["RTG"]) != 0:
        for chip in floor["chip"]:
            if chip not in floor["RTG"]:
                fried = True
    return fried
    
def solve(puzzle_data):
    elevator = 1
    
    return 0, 0

puzzle_path = "input_day11.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)