# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 11:01:39 2022

@author: mjenks
"""

def parse(puzzle_input):
    actions = {}
    start = []
    for line in puzzle_input:
        line = line.strip().split()
        if line[0] == 'bot':
            actor = ' '.join(line[:2])
            low = int(line[6])
            high = int(line[11])
            actions[actor] = low, high
        else:
            chip = int(line[1])
            bot = int(line[5])
            start.append((chip, bot))
    data = start, actions
    return data
    
def solve(puzzle_data):
    start, actions = puzzle_data
    #make a list of bots with a list of chips each has
    bots = [[] for i in range(len(actions))]
    unfound = True
    wanted = ''

    #set up by giving each bot chips it is assigned
    for inst in start:
        chip, bot = inst
        bots[bot].append(chip)
        
    #have bots act until a bot has chip 61 and 17
    while unfound:
        for i in range(len(bots)):
            if len(bots[i]) == 2:
                held = bots[i]
                name = 'bot ' + str(i)
                if 61 in held and 17 in held:
                    wanted = name
                    unfound = False
                held.sort()
                low, high = actions[name]
                bots[low].append(held[0])
                bots[high].append(held[1])
                bots[i] = []

    return wanted,0

puzzle_path = "input_day10.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)