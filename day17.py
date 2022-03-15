# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:04:27 2022

@author: mjenks
"""

import hashlib
passcode = 'njfxhljp'

def opendoors(path, location):
    global passcode
    hashcode = hashlib.md5(passcode + ''.join(path)).hexdigest()
    good = {'b', 'c', 'd', 'e', 'f'}
    options = []
    #up
    if hashcode[0] in good and location[1] != 1:
        options.append('U')
    #down
    if hashcode[1] in good and location[1] != 4:
        options.append('D')
    #left
    if hashcode[2] in good and location[0] != 1:
        options.append('L')
    #right
    if hashcode[3] in good and location[0] != 4:
        options.append('R')
    return options
         
    
def solve():
    #holds the path taken and current location of all options on each step
    current = [([], (1,1))]
    vault_reached = False
    steps = 0
    while not vault_reached:
        step = [] #hold all possible steps
        for path, location in current:
            if location == (4,4):
                vault_reached = True
                short_path = path
            options = opendoors(path, location)
            for direction in options:
                new = path[:]
                new.append(direction)
                x, y = location
                if direction == 'U':
                    y -= 1
                elif direction == 'D':
                    y += 1
                elif direction == 'L':
                    x -= 1
                elif direction == 'R':
                    x += 1
                step.append((new, (x,y)))
                
        current = step[:]
        steps += 1
                
    return ''.join(short_path), 0


    
solution1, solution2 = solve()

print(solution1)
print(solution2)