# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 11:04:13 2022

@author: mjenks
"""

import itertools

points = {}

def get_key(val):
    for key, value in points.items():
         if val == value:
             return key

def parse(puzzle_input):
    data = []
    j = 0
    for line in puzzle_input:
        line = line.strip()
        row = [] #store 0 for open and 1 for wall
        i = 0
        for char in line:
            if char == '#':
                row.append(1)
            elif char == '.':
                row.append(0)
            else:
                row.append(0)
                points[int(char)] = (i,j)
            i += 1
        data.append(row)
        j += 1            
        
    return data
    
def isopen(x,y):
    global puzzle_data
    if puzzle_data[y][x] == 0:
        return True
    else:
        return False
    
def move(current, visited):
    options = []
    for point in current:
        x, y = point
        if isopen(x+1,y) and (x+1,y) not in visited:
            spot = x+1, y
            visited.add(spot)
            options.append(spot)
        if isopen(x,y+1) and (x,y+1) not in visited:
            spot = x, y+1
            visited.add(spot)
            options.append(spot)
        if isopen(x-1, y) and (x-1,y) not in visited:
            spot = x-1, y
            visited.add(spot)
            options.append(spot)
        if isopen(x, y-1) and (x,y-1) not in visited:
            spot = x, y-1
            visited.add(spot)
            options.append(spot)
    return options, visited
    
def findPaths(p):
    location = [points[p]]
    steps = 0
    shortest_routes = [0 for a in range(len(points))]
    visited = set()
    visited.add(location[0])
    while (shortest_routes.count(0) != 1):
        steps += 1
        location, visited = move(location, visited)
        for spot in location:
            if spot in points.values():
                index = get_key(spot)
                if shortest_routes[index] == 0:
                    shortest_routes[index] = steps
    
    return shortest_routes
    
def solve():
    pair_routes = []
    shortest = 1000
    shortest_loop = 1000
    for i in range(len(points)):
        pair_routes.append(findPaths(i))
    for path in itertools.permutations(range(1,len(points))):
        length = pair_routes[0][path[0]]
        for i in range(6):
            length += pair_routes[path[i]][path[i+1]]
        shortest = min(length, shortest)
        #add the distance back to 0
        length += pair_routes[path[-1]][0]
        shortest_loop = min(length, shortest_loop)
    
    return shortest, shortest_loop

puzzle_path = "input_day24.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve()

print(solution1)
print(solution2)