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
    
def solve(puzzle_data, c):
    reg = {'a': 0, 'b': 0, 'c': c, 'd': 0}
    i = 0
    while i < len(puzzle_data):
        inst = puzzle_data[i]
        if inst[0] == 'cpy':
            x = inst[1]
            y = inst[2]
            try:
                reg[y] = int(x)
            except:
                reg[y] = reg[x]
            i += 1
        elif inst[0] == 'inc':
            x = inst[1]
            reg[x] += 1
            i += 1
        elif inst[0] == 'dec':
            x = inst[1]
            reg[x] -= 1
            i += 1
        elif inst[0] == 'jnz':
            x = inst[1]
            y = int(inst[2])
            try:
                test = int(x)
            except:
                test = reg[x]
            if test == 0:
                i += 1
            else:
                i += y
        else:
            print "Unknown Command"
            break
                
    return reg['a']
    
puzzle_path = "input_day12.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = solve(puzzle_data, 0)
solution2 = solve(puzzle_data, 1)

print(solution1)
print(solution2)