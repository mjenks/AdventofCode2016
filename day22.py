# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:15:38 2022

@author: mjenks

the node grid goes to 0 to 34 in x and  to 24 in y
"""

class Node:
    def __init__(self, info):
        self.name = info[0]
        self.size = int(info[1][:-1])
        self.used = int(info[2][:-1])
        self.avail = int(info[3][:-1])
        self.percent_used = int(info[4][:-1])
        loc = self.name.split('-')[1:]
        self.x = int(loc[0][1:])
        self.y = int(loc[1][1:])

def parse(puzzle_input):
    data = []
    for line in puzzle_input[2:]:
        line = line.strip().split() #listed in order id, size, used, avail, use%
        data.append(Node(line))
    return data
    
def solve(puzzle_data):
    pairs = 0
    for a in puzzle_data:
        if a.used == 0:
            continue
        for b in puzzle_data:
            if a == b:
                continue
            if a.used <= b.avail:
                pairs += 1
                
    #part 2 the goal is to move data from x34-y0 to x-y0
    
    return pairs, 0

puzzle_path = "input_day22.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)