# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 11:18:44 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        com = line[0]
        if com == 'swap':
            typ = line[1]
            x = line[2]
            y = line[-1]
            data.append((com, typ, x, y))
        elif com == 'rotate':
            typ = line[1]
            if typ == 'based':
                x = line[-1]
            else:
                x = line[2]
            data.append((com, typ, x))
        else:
            x = line[2]
            y = line[-1]
            data.append((com, x, y))

    return data
    
def swap(pwd, typ, x, y):
    if typ == 'position':
        new = list(pwd)
        x = int(x)
        y = int(y)
        new[x] = pwd[y]
        new[y] = pwd[x]
    elif typ == 'letter':
        new = []
        for char in pwd:
            if char == x:
                new.append(y)
            elif char == y:
                new.append(x)
            else:
                new.append(char)
    return ''.join(new)
    
def rotate(pwd, typ, x):
    if typ == 'based':
        i = pwd.index(x)
        x = 1+i
        if i >= 4:
            x += 1
        typ = 'right'
    x = int(x)
    new = list(pwd)
    for j in range(len(pwd)):
        if typ == 'right':
            new[j] = pwd[(j-x)%len(pwd)]
        elif typ == 'left':
            new[j] = pwd[(j+x)%len(pwd)]
    return ''.join(new)  
    
def reverse(pwd, x, y):
    x = int(x)
    y = int(y)
    new = list(pwd)
    for i in range(y-x+1):
        new[x+i] = pwd[y-i]
    return ''.join(new)
    
def move(pwd, x, y):
    x = int(x)
    y = int(y)
    new = []
    i = 0
    hold = pwd[x]
    for char in pwd:
        if i == y:
            new.append(hold)
            i += 1
        if i != x:
            new.append(char)
        i +=1
    return ''.join(new)
        
def solve(puzzle_data):
    pwd = 'abcdefgh'
    return 0, 0

puzzle_path = "input_day21.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)