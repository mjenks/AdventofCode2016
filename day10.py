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
            #assign outputs negative values and bots positive and output 0 set as -900
            if line[5] == 'bot':
                low = int(line[6])
            else:
                if int(line[6]) == 0:
                    low = -900
                else:
                    low = -1*int(line[6])
            if line[10] == 'bot':
                high = int(line[11])
            else:
                if int(line[11]) == 0:
                    high = -900
                else:
                    high = -1*int(line[11])
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
    outputs = [-1,-1,-1]

    #set up by giving each bot chips it is assigned
    for inst in start:
        chip, bot = inst
        bots[bot].append(chip)
        
    #have bots act until a bot has chip 61 and 17
    while unfound or -1 in outputs:
        for i in range(len(bots)):
            if len(bots[i]) == 2:
                held = bots[i]
                name = 'bot ' + str(i)
                if 61 in held and 17 in held:
                    wanted = name
                    unfound = False
                held.sort()
                low, high = actions[name]
                if low < 0:
                    if low == -900:
                        out = 0
                    else:
                        out = -1*low
                    if out < 3:
                        outputs[out] = held[0]
                else:
                    bots[low].append(held[0])
                if high < 0:
                    if high == -900:
                        out = 0
                    else:
                        out = -1*high
                    if out < 3:
                        outputs[out] = held[1]
                else:
                    bots[high].append(held[1])
                bots[i] = []
    product = outputs[0]*outputs[1]*outputs[2]

    return wanted, product

puzzle_path = "input_day10.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)