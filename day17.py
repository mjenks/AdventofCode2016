# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:04:27 2022

@author: mjenks
"""

import hashlib

def opendoors(passcode, path):
    hashcode = hashlib.md5(passcode + ''.join(path)).hexdigest()
    good = {'b', 'c', 'd', 'e', 'f'}
    options = []
    #up
    if hashcode[0] in good:
        options.append('U')
    #down
    if hashcode[1] in good:
        options.append('D')
    #left
    if hashcode[2] in good:
        options.append('L')
    #right
    if hashcode[3] in good:
        options.append('R')
    return options
        
    
def solve(puzzle_data):
    path = []
    location = (1,1)
    
    return 0, 0


    
puzzle_data = 'njfxhljp'
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)