# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:28:10 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        sides = []
        for side in line.strip().split():
            sides.append(int(side))
        sides.sort()
        data.append(sides)
    
    return data
    
def parse2(puzzle_input):
    data = []
    i = 1
    for line in puzzle_input:
        line = line.strip().split()
        if i == 1:
            tri1 = [int(line[0])]
            tri2 = [int(line[1])]
            tri3 = [int(line[2])]
        if i == 2:
            tri1.append(int(line[0]))
            tri2.append(int(line[1]))
            tri3.append(int(line[2]))
        if i == 3:
            tri1.append(int(line[0]))
            tri2.append(int(line[1]))
            tri3.append(int(line[2]))
            tri1.sort()
            tri2.sort()
            tri3.sort()
            data.append(tri1)
            data.append(tri2)
            data.append(tri3)
            i = 0
        i+=1
            
            
    return data
    
def solve(puzzle_data):
    possible = 0
    
    for triangle in puzzle_data:
        if triangle[0] + triangle[1] > triangle[2]:
            possible += 1
    
    return possible

puzzle_path = "input_day3.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
puzzle_data2 = parse2(puzzle_input)

solution1 = solve(puzzle_data)
solution2 = solve(puzzle_data2)

print(solution1)
print(solution2)