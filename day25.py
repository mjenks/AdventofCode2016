# -*- coding: utf-8 -*-
"""
Created on Tue Apr 05 13:44:20 2022

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
    
def test(puzzle_data, a):
    reg = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    output = []
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
            x = inst[1]
            try:
                target = i + int(x)
            except:
                target = i + reg[x]
            i += 1
            try: 
                test = puzzle_data[target]
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
        elif inst[0] == 'out':
            x = inst[1]
            output.append(str(reg[x]))
            i += 1
                
        else:
            print "Unknown Command"
            break
        if len(output) > 20:
            break
    return ''.join(output)
    
def solve(puzzle_data):
    a = 0 
    out = ''
    while out[:10] != '0101010101':
        a += 1
        out = test(puzzle_data, a)
    print out
    return a

puzzle_path = "input_day25.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1 = solve(puzzle_data)


print(solution1)
