# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 11:23:17 2022

@author: mjenks
"""

import hashlib
import itertools

def stretch_hash(val, stretch):
    val = hashlib.md5(str(val)).hexdigest()
    for x in range(stretch):
        val = hashlib.md5(str(val)).hexdigest()
    return val

def iskey(salt, i, stretch):
    key = False
    if stretch == 0:
        hash_val = stretch_hash(salt + str(i), stretch)
    else:
        if i in stretched_hashes.keys():
            hash_val = stretched_hashes[i]
        else:
            hash_val = stretch_hash(salt + str(i), stretch)
            stretched_hashes[i] = hash_val
              
    char = ''
    #check for a character repeated at least 3 times and store first instance
    for k, g in itertools.groupby(str(hash_val)):
        count = sum(1 for i in g)
        if count >= 3:
            char = k
            break
    #check next 1000 index's for that char repeated 5 times
    if len(char) > 0:
        if stretch == 0:
            for val in [stretch_hash(salt + str(j), stretch) for j in range(i+1,1001+i)]:
                if 5*char in str(val):
                    key = True
                    break
        else:
            hashes = []
            for x in range(i+1,1001+i):
                if x in stretched_hashes.keys():
                    hashes.append(stretched_hashes[x])
                else:
                    val = stretch_hash(salt + str(x), stretch)
                    hashes.append(val)
                    stretched_hashes[x] = val
            for val in hashes:
                if 5*char in str(val):
                    key = True
                    break                    
           
    return key
    
def solve(puzzle_data, stretch=0):
    key_num = 0
    i = 0
    while key_num < 64:
        if iskey(puzzle_data, i, stretch):
            key_num += 1
        i += 1
        
    return i-1

puzzle_input = 'ahsbgdzn'

#store found stretched hash values to avoid refinding them
stretched_hashes = {}
solution1 = solve(puzzle_input)
print(solution1)
solution2 = solve(puzzle_input, 2016)
print(solution2)