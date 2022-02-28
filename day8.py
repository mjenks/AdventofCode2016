# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:57:52 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        if line[0] == 'rect':
            opr = 'rect'
            sqr = line[1].split('x')
            a = int(sqr[0])
            b = int(sqr[1])
        elif line[1] == 'row':
            opr = 'row'
            a = int(line[2].split('=')[1])
            b = int(line[4])
        elif line[1] == 'column':
            opr = 'col'
            a = int(line[2].split('=')[1])
            b = int(line[4])
        else:
            print "Unrecognized instruction"
        data.append((opr, a, b))
    return data
    
def solve(puzzle_data):
    rows = 6
    cols = 50
    screen = [[0 for i in range(cols)] for j in range(rows)]

    for instr in puzzle_data:
        opr, a, b = instr
        if opr == 'rect':
            for i in range(b):
                for j in range(a):
                    screen[i][j] = 1
        if opr == 'row':
            row = []
            for i in range(cols):
                row.append(screen[a][i])
            for x in range(cols):
                screen[a][(x+b)%cols] = row[x]
        if opr == 'col':
            col = []
            for j in range(rows):
                col.append(screen[j][a])
            for y in range(rows):
                screen[(y+b)%rows][a] = col[y]

                
    lit = sum(sum(screen[x]) for x in range(rows))
    
    return lit, 0
    
puzzle_path = "input_day8.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)