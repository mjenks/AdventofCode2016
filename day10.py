# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 11:01:39 2022

@author: mjenks
"""

def parse(puzzle_input):
    actions = {}
    start = []
    for line in puzzle_input:
        line = line.strip().split()
        if line[0] == 'bot':
            actor = ' '.join(line[:2])
            low = int(line[6])
            high = int(line[11])
            actions[actor] = low, high
        else:
            chip = int(line[1])
            bot = int(line[5])
            start.append((chip, bot))
    data = start, actions
    return data
    
def solve(puzzle_data):
    return 0,0

puzzle_path = "input_day10.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)