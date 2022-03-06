# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 22:17:17 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split(',')
        items = 0
        for item in line:
            item = item.split()
            if 'chip' in item[-1]:
                items += 1
            if 'generator' in item[-1]:
                items += 1
        data.append(items)
        
    return data

def solve(puzzle_data):
    steps = 0
    steps_part2 = 0
    #ignoring any conditions on what can go where to move items you take 2 up a floor then bring one down
    #repeating this pattern it will take 2n-3 steps to move n items up one floor

    #move everything from floor 1 to 2
    steps += 2*(puzzle_data[0]) - 3
    steps_part2 += 2*(puzzle_data[0]+4) - 3
    puzzle_data[1] += puzzle_data[0]
    #move everything from floor 2 to 3
    steps += 2*(puzzle_data[1]) - 3
    steps_part2 += 2*(puzzle_data[1]+4) - 3
    puzzle_data[2] += puzzle_data[1]
    #move everything to floor 4
    steps += 2*(puzzle_data[2]) - 3
    steps_part2 += 2*(puzzle_data[2]+4) - 3

    return steps, steps_part2
    
puzzle_path = "input_day11.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)


print(solution1)
print(solution2)