# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 12:35:05 2022

@author: mjenks
"""

import hashlib

def solve(puzzle_data):
    code = []
    code_2 = ['_', '_', '_', '_', '_', '_', '_', '_']
    i = 0
    while '_' in code_2:
        hash_val = hashlib.md5(puzzle_data.encode('utf-8') + str(i).encode('utf-8')).hexdigest()
        if hash_val.startswith('00000'):
            if len(code) < 8:
                code.append(hash_val[5])
            j = int(hash_val[5], 16)
            if j < 8 and code_2[j] is '_':
                code_2[j] = hash_val[6]
                print ''.join(code_2)
                
                
        i += 1
            
    
    return ''.join(code), ''.join(code_2)


    
puzzle_data = "ffykfhsq"
solution1, solution2 = solve(puzzle_data)

print solution1, solution2