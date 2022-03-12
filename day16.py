# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:31:16 2022

@author: mjenks
"""

def gendata(data):
    new_data = data[:]
    new_data.append(0)
    i = len(data)
    while i > 0:
        i -= 1
        new_data.append((data[i]+1)%2)
    return new_data
    
def solve(puzzle_data, disc_size):
    
    return 0, 0


#puzzle_input = 01111001100111011    
puzzle_data = [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1]
disc1 = 272
solution1 = solve(puzzle_data, disc1)
print(solution1)
#solution2 = solve(puzzle_data)
#print(solution2)