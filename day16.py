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
    
def findchecksum(data):
    i = 0
    checksum = []
    while i+1 < len(data):
        if data[i] == data[i+1]:
            checksum.append(1)
        else:
            checksum.append(0)
        i += 2
    return checksum 
    
def solve(puzzle_data, disc_size):
    while len(puzzle_data) < disc_size:
        puzzle_data = gendata(puzzle_data)
    data = puzzle_data[:disc_size]
    checksum = findchecksum(data)
    while len(checksum)%2 == 0:
        checksum = findchecksum(checksum)
    
    return ''.join([str(num) for num in checksum])


#puzzle_input = 01111001100111011    
puzzle_data = [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1]
disc1 = 272
solution1 = solve(puzzle_data, disc1)
print(solution1)
#solution2 = solve(puzzle_data)
#print(solution2)