# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:41:41 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for room in puzzle_input:
        room = room.strip()
        name = room.split('-')[:-1]
        id_check = room.split('-')[-1]
        sector_id = id_check.split('[')[0]
        checksum = id_check.split('[')[1]
        checksum = checksum[:-1]
        data.append((name, sector_id, checksum))
    return data
   
def solve(puzzle_data):
    return 0,0

puzzle_path = "input_day4.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)
