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
def add_path(path, facing, distance):
    current_locations = set(path)
    current_path = []
    path_crossings = []
    for i in range(0,distance):
        x,y = path[-1]
        if facing == 0:
            current_path.append((x, y + 1 + i))
        elif facing == 1:
            current_path.append((x + 1 + i, y))
        elif facing == 2:
            current_path.append((x, y - 1 - i))
        elif facing == 3:
            current_path.append((x - 1 - i, y))
    
    for step in current_path: 
        j = len(current_locations)
        current_locations.add(step)
        if j == len(current_locations):
            path_crossings.append(step)
    
    if len(path_crossings) == 0:
        hq = 0
        intersect = False
    else:
        hq = path_crossings[0]
        intersect = True
        
    path = path + current_path
    
    return path, intersect, hq

#solve
def solve(puzzle_data):
    facing = 0 #compass North: 0 East:1 South:2 West: 3 
    position = (0,0)
    path = [(0,0)]
    intersect = False
    
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
            
        if not intersect:    
            path, intersect, hq = add_path(path, facing, distance)


    if hq == 0:
        print "no repeated location"
        bunny_hq = (0,0)
    else:
        bunny_hq = hq
        
        
            
    return abs(position[0]) + abs(position[1]), abs(bunny_hq[0]) + abs(bunny_hq[1])

#run and print solution 
puzzle_path = "input_day1.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)