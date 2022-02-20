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
    facing = 0 #compass North: 0 East:1 South:2 West: 3 
    position = (0,0)
    visited = []
    
    for direction in puzzle_data:
        x, y = position
        turn, distance = direction
        
        #left turn is the compass value +3 mod 4 (essentially -1 but avoids negative values)
        if turn == 'L':
            facing = (facing + 3) % 4
        #right turn in compass value +1 mod 4 (mod moves from west back to north)
        elif turn == 'R':
            facing = (facing + 1) % 4
        
        #Now move position based on the new facing
        if facing == 0:
            position = x, y + distance
        elif facing == 1:
            position = x + distance, y
        elif facing == 2:
            position = x, y - distance
        elif facing == 3:
            position = x - distance, y
            
        visited.append(position)
            
    return abs(position[0]) + abs(position[1]), visited

#run and print solution 
puzzle_path = "input_day1.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1 = solve(puzzle_data)
solution2 = solve(puzzle_data)
print(solution1)
print(solution2)