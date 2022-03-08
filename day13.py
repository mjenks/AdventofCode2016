# -*- coding: utf-8 -*-
"""
Created on Mon Mar 07 10:18:16 2022

@author: mjenks
"""

def isopen(x, y):
    if x < 0 or y < 0:
        return False
    global puzzle_input
    number = x*x + 3*x + 2*x*y + y + y*y + puzzle_input
    binary = [] #hold the 1's and 0's of the binary in reverse order
    while number != 0:
        binary.append(number%2)
        number = number//2
    count = sum(binary)
    if count%2 == 0:
        return True
    else:
        return False
        
def move(current):
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
    return options
    
def solve():
    location = [(1,1)]
    steps = 0
    while (31,39) not in visited:
        steps += 1
        location = move(location)
    
    return steps, 0

visited = set()
puzzle_input = 1364

solution1, solution2 = solve()

print(solution1)
print(solution2)