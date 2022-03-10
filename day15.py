# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:25:01 2022

@author: mjenks
"""

#input is parsed into a dictionary with the disc number as the key
#storing the number of positions and start position as a tuple
def parse(puzzle_input):
    data = {}
    for line in puzzle_input:
        line = line.strip().split()
        data[int(line[1][1])] = (int(line[3]), int(line[11][:-1]))
    return data
    
def escape(discs, time):
    escaped = True
    for disc in discs.keys():
        pos, start = discs[disc]
        if (time + disc + start)%pos != 0:
            escaped = False
    return escaped

def solve(puzzle_data):
    time = -1
    escaped = False
    while not escaped:
        time += 1
        escaped = escape(puzzle_data, time)
        
    return time, 0

puzzle_path = "input_day15.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)