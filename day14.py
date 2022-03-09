# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 11:23:17 2022

@author: mjenks
"""

import hashlib
import itertools

def iskey(salt, i):
    key = False
    hash_val = hashlib.md5(salt + str(i)).hexdigest()
    char = ''
    #check for a character repeated at least 3 times and store first instance
    for k, g in itertools.groupby(str(hash_val)):
        count = sum(1 for i in g)
        if count >= 3:
            char = k
            break
    #check next 1000 index's for that char repeated 5 times
    if len(char) > 0:
        for val in [hashlib.md5(salt + str(j)).hexdigest() for j in range(i+1,1001+i)]:
            if 5*char in str(val):
                key = True
                break
           
    return key
    
def solve(puzzle_data):
    key_num = 0
    i = 0
    while key_num < 64:
        if iskey(puzzle_data, i):
            key_num += 1
        i += 1
        
    return i-1, 0

puzzle_input = 'ahsbgdzn'

solution1, solution2 = solve(puzzle_input)

print(solution1)
print(solution2)