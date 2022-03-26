# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 11:18:44 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        com = line[0]
        if com == 'swap':
            typ = line[1]
            x = line[2]
            y = line[-1]
            data.append((com, typ, x, y))
        elif com == 'rotate':
            typ = line[1]
            if typ == 'based':
                x = line[-1]
            else:
                x = line[2]
            data.append((com, typ, x))
        else:
            x = line[2]
            y = line[-1]
            data.append((com, x, y))

    return data
    
def solve(puzzle_data):
    pwd = 'abcdefgh'
    return 0, 0

puzzle_path = "input_day21.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)