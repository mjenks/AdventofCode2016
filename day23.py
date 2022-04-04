# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 10:25:08 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        com = line[0]
        x = line[1]
        if len(line) > 2:
            y = line[2]
            inst = [com, x, y]
        else:
            inst = [com, x]
        data.append(inst)
    return data
    
def solve(puzzle_data, a):
    reg = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    while i < len(puzzle_data):
        inst = puzzle_data[i]
        if inst[0] == 'cpy':
            x = inst[1]
            y = inst[2]
            if y not in reg.keys():
                i += 1 
                continue
            try:
                reg[y] = int(x)
            except:
                reg[y] = reg[x]
            i += 1
        elif inst[0] == 'inc':
            x = inst[1]
            reg[x] += 1
            i += 1
        elif inst[0] == 'dec':
            x = inst[1]
            reg[x] -= 1
            i += 1
        elif inst[0] == 'jnz':
            x = inst[1]
            y = inst[2]
            try:
                test = int(x)
            except:
                test = reg[x]
            try:
                y = int(y)
            except:
                y = reg[y]
            if test == 0:
                i += 1
            else:
                i += y
        elif inst[0] == 'tgl': 
        #for part 2
        #the next time the code hits this a becomes a*b, b is decreased 1, c decreased 2, d=0
        #the code will stop returning here after toggling the instruction 2 away (c = 2 is the last time)
        #this could be used to signifantly speed up the solution
            x = inst[1]
            try:
                target = i + int(x)
            except:
                target = i + reg[x]
            i += 1
            try: 
                test = puzzle_data[target]
                print target, test
            except:
                continue
            if len(test) == 2:
                if test[0] == 'inc':
                    puzzle_data[target][0] = 'dec'
                else:
                    puzzle_data[target][0] = 'inc'
            else:
                if test[0] == 'jnz':
                    puzzle_data[target][0] = 'cpy'
                else:
                    puzzle_data[target][0] = 'jnz'
                
        else:
            print "Unknown Command"
            break
        
    return reg['a']

puzzle_path = "input_day23.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
#solution1 = solve(puzzle_data, 7)
#print solution1
solution2 = solve(puzzle_data, 12)
print solution2