# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 15:31:40 2022

@author: mjenks
"""


#parse input
def parse(puzzle_input):
    data = []
    for direction in puzzle_input.strip().split(', '):
        turn = direction[0]
        distance = int(direction[1:])
        data.append((turn, distance))
    return data
    

#functions

#solve
def solve(puzzle_data):

        
    return 0

#run and print solution 
puzzle_path = "input_day1.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1 = solve(puzzle_data)
solution2 = solve(puzzle_data)
print(solution1)
print(solution2)